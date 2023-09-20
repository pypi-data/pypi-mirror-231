#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse
import csv
import json
import shutil
import uuid
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path
from stat import S_ISDIR, S_ISREG
from urllib.parse import unquote

import requests
import validators
from bs4 import BeautifulSoup
from happy_python import HappyLog, dict_to_pretty_json
from happy_python.happy_log import HappyLogLevel

hlog = HappyLog.get_instance()


class HttpMethod(Enum):
    POST = 'POST'
    GET = 'GET'


class EnumJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, HttpMethod):
            return obj.value

        return json.JSONEncoder.default(self, obj)


@dataclass
class CsvRow:
    request_id: int
    http_method: HttpMethod
    uri: str
    http_status: int
    payload: Path
    html_keywords: list[str]


class Application:
    def __init__(self, root: Path):
        self.instance_id = str(uuid.uuid4())
        self.cookies = {}
        self.url = ''
        self.charset = ''
        self.rules: list[CsvRow] = []

        self.payload_dir = root / 'payload'
        self.report_dir = root / 'report'
        self.cookie_file = root / 'cookie'
        self.rule_file = root / 'rule.csv'
        self.url_file = root / 'url'
        self.charset_file = root / 'charset'

        self.__check()
        self.__load()

    def __check(self):
        config_paths = [self.payload_dir, self.report_dir, self.cookie_file, self.rule_file, self.url_file, self.charset_file]
        config_type_checkers = [S_ISDIR, S_ISDIR, S_ISREG, S_ISREG, S_ISREG, S_ISREG]

        for i in range(0, len(config_paths)):
            config_path = config_paths[i]
            config_type_checker = config_type_checkers[i]
            config_type_txt = '目录' if config_type_checker == S_ISDIR else '文件'

            if not config_path.exists():
                hlog.error('%s（"%s"）不存在' % (config_type_txt, config_path))
                exit(1)

            if not config_type_checker(config_path.stat().st_mode):
                hlog.error('"%s"必须是%s' % (config_path, config_type_txt))
                exit(2)

    def __load_cookies(self):
        with open(self.cookie_file, mode='r', encoding='utf-8') as f:
            content = f.read()

            for item in content.split(';'):
                item = item.strip()
                index = item.find('=')
                key = item[:index]
                value = item[index + 1:]
                self.cookies[key] = value

    def __load_url(self):
        with open(self.url_file, mode='r', encoding='utf-8') as f:
            content = f.readlines()

            if len(content) == 0:
                hlog.error('"%s" 文件中没有URL字符串' % self.url_file)
                exit(3)
            elif len(content) != 1:
                hlog.warning('"%s" 文件中有多个URL字符串，忽略多余URL字符串' % self.url_file)
                exit(3)
            else:
                pass

            url = content[0]

            if not validators.url(url):
                hlog.error('"%s" 文件中指定的URL字符串（"%s"）无效' % (self.url_file, url))
                exit(4)

            self.url = url[:len(url) - 1] if url.endswith('/') else url
            hlog.var('self.url', self.url)

    def __load_rule(self):
        with open(self.rule_file, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)

            # 跳过标题行
            next(reader, None)

            for line_no, http_method, uri, http_status, payload, html_keywords in csv.reader(f):
                self.rules.append(CsvRow(request_id=int(line_no),
                                         http_method=HttpMethod[http_method],
                                         uri=uri,
                                         http_status=int(http_status),
                                         payload=Path(payload),
                                         html_keywords=html_keywords.split('|'),),)

            hlog.var('self.rule', self.rules)

    def __load(self):
        self.__load_cookies()
        self.__load_url()
        self.__load_charset()
        self.__load_rule()

    def __load_charset(self):
        self.charset = open(self.charset_file).read()


@dataclass
class HttpResponse:
    request_id: int
    url: str
    uri: str
    method: HttpMethod
    request_headers: dict
    request_body: str
    request_body_text: str
    expected_status: int
    status: int
    response_time: float
    response_headers: dict
    response_body: str

    def asdict(self) -> dict:
        return asdict(self)

    def __str__(self) -> str:
        return json.dumps(self.asdict(), cls=EnumJSONEncoder)


class HttpRequest:
    def __init__(self, config: Application, rule: CsvRow):
        self.config = config
        self.rule = rule
        self.headers = {'User-Agent': 'GeekWebMan/1.0'}

    def send(self) -> HttpResponse:
        url = self.config.url + self.rule.uri

        with open(self.config.payload_dir / self.rule.payload, mode='r', encoding='UTF-8') as f:
            payload = json.load(f)

            if self.rule.http_method == HttpMethod.GET:
                r = requests.get(url, cookies=self.config.cookies, headers=self.headers)
            elif self.rule.http_method == HttpMethod.POST:
                r = requests.post(url, cookies=self.config.cookies, headers=self.headers, data=payload)
            else:
                hlog.error('不支持的HTTP请求方法：%s' % self.rule.http_method)
                exit(5)

            r.encoding = self.config.charset

            request_body = r.request.body

            if r.status_code != self.rule.http_status:
                hlog.error('%s->HTTP代码不匹配（%s != %s）' % (self.rule.uri, r.status_code, self.rule.http_status))
                exit(5)

            for keyword in self.rule.html_keywords:
                if r.text.find(keyword) == -1:
                    hlog.error('%s->响应HTML内容中没找到关键字（"%s"）' % (self.rule.uri, keyword))
                    exit(5)

            if isinstance(request_body, bytes):
                request_body = request_body.decode(encoding=self.config.charset)

            request_body_text = unquote(request_body) if request_body else ''

            return HttpResponse(request_id=self.rule.request_id,
                                url=url,
                                uri=self.rule.uri,
                                method=self.rule.http_method,
                                request_headers=dict(r.request.headers),
                                request_body=request_body,
                                request_body_text=request_body_text,
                                expected_status=self.rule.http_status,
                                status=r.status_code,
                                response_time=round(r.elapsed.total_seconds(), 2),
                                response_headers=dict(r.headers),
                                response_body=r.text)


class ReportSummary:
    def __init__(self):
        self.request_total_num: int = 0
        self.request_success_num: int = 0
        self.request_failed_num: int = 0
        self.execution_time: float = 0.0
        self.request_avg_time: float = 0.0


def build_uri(file_path: Path):
    return '/'.join(file_path.parts[-2:])


class Report:
    def __init__(self, config: Application):
        self.__start_time = None
        self.__stop_time = None
        self.__config = config
        self.responses: list[HttpResponse] = []

    def count_response_summary(self) -> ReportSummary:
        summary = ReportSummary()
        summary.request_total_num = len(self.responses)

        for response in self.responses:
            summary.execution_time += response.response_time

            if response.status == response.expected_status:
                summary.request_success_num += 1
            else:
                summary.request_failed_num += 1

        summary.execution_time = round(summary.execution_time, 2)
        summary.request_avg_time = round(summary.execution_time / summary.request_total_num, 2)

        return summary

    def dump(self):
        summary = self.count_response_summary()

        instance_report_dir = (self.__config.report_dir /
                               self.__config.url.replace(':', '_').replace('/', '_') /
                               self.__config.instance_id)

        if instance_report_dir.exists():
            hlog.error('目录（%s）已经存在' % instance_report_dir)
            exit(6)
        else:
            instance_report_dir.mkdir(parents=True)

        backup_rule_file = instance_report_dir / (self.__config.rule_file.name + '.txt')
        shutil.copyfile(self.__config.rule_file, backup_rule_file)

        html = '''<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <title>Geek Web Man</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            background-color: #f2f2f2;
        }

        h1 {
            text-align: center;
        }

        table {
            border-collapse: collapse;
            margin: 0 auto;
            background-color: #fff;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        }

        th,
        td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: center;
        }

        th {
            background-color: #f2f2f2;
        }

        tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        tr:hover {
            background-color: #f5f5f5;
        }

        td:first-child {
            font-weight: bold;
        }
    </style>
</head>

<body>
    <h1>Geek Web Man</h1>
    <table id="summary">
        <tr>
            <th>URL</th>
            <th>规则文件</th>
            <th>运行ID</th>
            <th>请求总数</th>
            <th>成功请求</th>
            <th>失败请求</th>
            <th>平均时间 (秒)</th>
            <th>时间总计 (秒)</th>
        </tr>
        <tr>
            <td><a href="%s">%s</a></td>
            <td><a href="%s">%s</a></td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
    </table>
    <br>
    <table id="details">
        <tr>
            <th>ID</th>
            <th>URL</th>
            <th>请求方法</th>
            <th>请求标头</th>
            <th>请求载荷</th>
            <th>响应代码</th>
            <th>响应时间</th>
            <th>响应标头</th>
            <th>响应内容</th>
        </tr>
''' % (self.__config.url,
       self.__config.url,
       backup_rule_file.name,
       backup_rule_file.name,
       self.__config.instance_id,
       summary.request_total_num,
       summary.request_success_num,
       summary.request_failed_num,
       summary.request_avg_time,
       summary.execution_time)

        for response in self.responses:
            request_id_dir = instance_report_dir / str(response.request_id)
            request_id_dir.mkdir(exist_ok=True)

            request_headers_file = request_id_dir / 'request_headers.json'
            request_body_file = request_id_dir / 'request_body.txt'
            response_headers_file = request_id_dir / 'response_headers.json'
            response_body_file = request_id_dir / 'response_body.txt'

            with open(request_headers_file, mode='w', encoding='UTF-8') as f:
                f.write(dict_to_pretty_json(response.request_headers))

            with open(request_body_file, mode='w', encoding='UTF-8') as f:
                f.write(response.request_body)
                f.write('\n\n')
                f.write(response.request_body_text)

            with open(response_headers_file, mode='w', encoding='UTF-8') as f:
                f.write(dict_to_pretty_json(response.response_headers))

            with open(response_body_file, mode='w', encoding='UTF-8') as f:
                f.write(response.response_body)

            html += '''
        <tr>
            <td>%s</td>
            <td>
                <a href="%s">%s</a>
            </td>
            <td>%s</td>
            <td>
                <a href="%s">请求标头</a>
            </td>
            <td>
                <a href="%s">请求载荷</a>
            </td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a href="%s">响应标头</a>
            </td>
            <td>
                <a href="%s">响应内容</a>
            </td>
        </tr>
''' % (response.request_id,
       response.url,
       response.uri,
       response.method.value,
       build_uri(request_headers_file),
       build_uri(request_body_file),
       response.status,
       response.response_time,
       build_uri(response_headers_file),
       build_uri(response_body_file))

        html += '''
            </table>
        </body>

        </html>
'''
        index_html = instance_report_dir / 'index.html'
        with open(index_html, mode='w', encoding='UTF-8') as f:
            bs = BeautifulSoup(html, features="lxml")
            f.write(bs.prettify())

        hlog.info('运行日志已经保存->\n\t%s' % index_html)


def main():
    parser = argparse.ArgumentParser(prog='geek_web_man',
                                     description='',
                                     usage='%(prog)s [-l level] -d root_dir')

    parser.add_argument('-d',
                        '--root',
                        help='启动目录',
                        required=True,
                        action='store',
                        dest='root')

    parser.add_argument('-l',
                        '--log-level',
                        help='日志级别，CRITICAL|ERROR|WARNING|INFO|DEBUG|TRACE，默认等级3（INFO）',
                        type=int,
                        choices=HappyLogLevel.get_list(),
                        default=HappyLogLevel.INFO.value,
                        required=False,
                        dest='log_level')

    args = parser.parse_args()

    hlog.set_level(args.log_level)

    config = Application(Path(args.root))

    hlog.info('运行实例：%s' % config.instance_id)

    report = Report(config)

    for rule in config.rules:
        request = HttpRequest(config, rule)
        response = request.send()

        report.responses.append(response)

    report.dump()


if __name__ == '__main__':
    main()
