#!/usr/bin/env python3

import logging
logging.basicConfig(level=logging.DEBUG)


import pymonetdb

# classic behavior: paramstyle pyformat
assert pymonetdb.paramstyle == 'pyformat'

with pymonetdb.connect('demo') as conn, conn.cursor() as cursor:
    parameters = dict(number=42, fruit="ban'ana")
    cursor.execute("SELECT %(number)s, %(fruit)s", parameters)
    assert cursor.fetchone() == (42, "ban'ana")

# enable named parameters
pymonetdb.paramstyle = 'named'

with pymonetdb.connect('demo') as conn, conn.cursor() as cursor:
    parameters = dict(number=42, fruit="ban'ana")
    cursor.execute("SELECT :number, :fruit", parameters)
    assert cursor.fetchone() == (42, "ban'ana")
