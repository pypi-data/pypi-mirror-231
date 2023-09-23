#!/usr/bin/env python3

import argparse
import logging
import ssl
import sys

from pymonetdb.exceptions import DatabaseError

logging.basicConfig(level=logging.DEBUG)


import pymonetdb
print(pymonetdb.__path__)


argparser = argparse.ArgumentParser()
argparser.add_argument('url')
argparser.add_argument('-c', '--cert')
args = argparser.parse_args()

print(f"CONNECT {args.url}")
try:
    with pymonetdb.connect(args.url, server_cert=args.cert) as conn, conn.cursor() as c:
        print()
        c.execute("SELECT VALUE FROM environment WHERE name = 'merovingian_uri'")
        row = c.fetchone()
        print(row)
except (ConnectionRefusedError,DatabaseError,ssl.SSLError) as e:
    sys.exit(str(e))

