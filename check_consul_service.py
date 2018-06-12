#!/usr/bin/python3
"""Icinga plugin for Comnsul service health."""
import sys
import argparse
from itertools import groupby

import consulate


def parse_arguments():
    """Parse command line argument."""
    parser = argparse.ArgumentParser(
        description='Check a consul service health'
    )
    parser.add_argument('-t', '--token', default=None)
    parser.add_argument('service')
    parser.add_argument('-H', '--host', default='localhost')
    parser.add_argument('-p', '--port', default=8500, type=int)
    parser.add_argument('-d', '--datacenter', default=None)
    parser.add_argument('-s', '--tls', default=False, action='store_true')
    return parser.parse_args()


def get_service_checks(args):
    """Request service checks on Consul API."""
    consul = consulate.Consul(
        token=args.token, port=args.port,
        host=args.host, datacenter=args.datacenter,
        scheme='https' if args.tls else 'http'
    )
    return consul.health.checks(args.service)


def groupby_status(checks):
    """Group check by Status."""
    return groupby(checks, lambda x: x.get('Status', None))


def format_failing_checks(checks):
    """Format check for output."""
    for check in checks:
        yield "%s: %s" % (check['Name'], check['Output'])


def print_checks(grouped_checks):
    """Print the highest severity status."""
    final_message = 'Unknown: no check for this service'
    final_exit_code = 3
    for status, gen_checks in grouped_checks:
        checks = list(gen_checks)
        if status == 'critical':
            final_exit_code = 2
            final_message = "Critical: %d checks with critical status\n%s" % (
                len(checks), "".join(format_failing_checks(checks))
            )
        elif status == 'warning' and final_exit_code in [0, 3]:
            final_exit_code = 1
            final_message = "Warning: %d checks with warning status\n%s" % (
                len(checks), "".join(format_failing_checks(checks))
            )
        elif status == 'passing' and final_exit_code == 3:
            final_exit_code = 0
            final_message = "OK: %d checks with passing status" % len(checks)
    print(final_message)
    sys.exit(final_exit_code)


def main():
    """Start the script."""
    args = parse_arguments()
    checks = get_service_checks(args)
    grouped_checks = groupby_status(checks)
    print_checks(grouped_checks)


if __name__ == "__main__":
    main()
