#!/usr/bin/env python
# coding: utf-8
# @File Name: simple_server.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-05-07 14:05:18
# @Last Modified: 2018-05-07 15:05:58
# @Description:

import os
from http.server import BaseHTTPRequestHandler, HTTPServer

bolturis = ["192.168.9.14", "192.168.9.18"]
cur_graph = 0

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        api, params = self._parse_api()
        if api == "/reset":
            pass
        elif api == "/sync":
            if 0 == cur_graph:
                cmd = "scp data/gdl_u_p.csv.tar.gz hadoop018:~/program/miao-graph-transfer/data/"
                os.system(cmd)
                os.system("curl hadoop018:8899/sync")
        print(api)
        print(params)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        return

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        return

    def _parse_api(self):
        api_params = self.path.split("?")
        api = ""
        params = {}
        if len(api_params) == 2:
            api = api_params[0]
            tmp_params = api_params[1].split("&")
            for param in tmp_params:
                param = param.split("=")
                params[param[0]] = param[1]
        return api, params


def run():
    port = 8877
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print("starting server on port: %d" % port)
    httpd.serve_forever()


if __name__ == "__main__":
    run()

