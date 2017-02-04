# -*- coding: utf-8 -*-

import sys

import msgpack
import requests as req


class MsfRpc(object):
    headers = {'Content-Type': 'binary/message-pack'}

    def __init__(self, host='127.0.0.1', port=55552, ssl=False, user='msf', passwd='msf'):
        self.token = None
        self.authenticated = False
        self.uri = '{}://{}:{}/api/'.format('https' if ssl else 'http', host, port)
        self.auth(user, passwd)

    def call(self, method, options=None):
        options = options or []
        if method != 'auth.login':
            options = [self.token] + options
        options = [method] + options
        options = msgpack.packb(options)
        resp = req.post(self.uri, data=options, headers=self.headers, stream=True)
        data = msgpack.unpack(resp.raw)
        return data

    def auth(self, user, passwd):
        resp = self.call('auth.login', [user, passwd])
        if resp.get('result') == 'success':
            self.token = resp['token']
            self.authenticated = True


def rpc_connect(host, port, ssl, user, passwd):
    print("[+] Connecting to the RPC server")
    rpc = MsfRpc(
        host=host, port=port, ssl=ssl,
        user=user, passwd=passwd
    )
    if not rpc.authenticated:
        print("[!] Login failed")
        sys.exit()
    return rpc
