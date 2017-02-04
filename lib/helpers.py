# -*- coding: utf-8 -*-


def add_rpc_parser(main_parser):
    rpc_parser = main_parser.add_argument_group('MSFRPC connection')
    rpc_parser.add_argument(
        '--rpc-host',
        metavar='HOST',
        help='MSFRPC host (default: 127.0.0.1)',
        default='127.0.0.1'
    )
    rpc_parser.add_argument(
        '--rpc-port',
        metavar='PORT',
        help='MSFRPC port (default: 55552)',
        default=55552,
        type=int
    )
    rpc_parser.add_argument(
        '--rpc-user',
        metavar='USER',
        help='user to use to connect to MSFRPC (default: msf)',
        default='msf'
    )
    rpc_parser.add_argument(
        '--rpc-passwd',
        metavar='PASSWD',
        help='password to use to connect to MSFRPC (default: msf)',
        default='msf'
    )
    rpc_parser.add_argument(
        '--rpc-ssl',
        help='use SSL to connect to MSFRPC (default: False)',
        action='store_true',
        default=False
    )


def explode_ranges(ranges):
    for r in ranges.split(','):
        if '-' in r:
            start, end = r.split('-')
            for item in range(int(start), int(end)+1):
                yield item
        else:
            yield int(r)
