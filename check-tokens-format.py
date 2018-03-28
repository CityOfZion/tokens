#!/usr/bin/env python
"""
Check tokens.json for validity

Requires python-dateutil: https://pypi.python.org/pypi/python-dateutil/2.6.0
"""
import json
import dateutil.parser

# Load the json
obj = json.loads(open("tokens.json").read())

def check_datetime(dt):
    try:
        dateutil.parser.parse(dt)
    except:
        print("Error parsing datetime '%s'" % dt)
        raise

# Check start and end of all entries
for entry in obj:
    check_datetime(entry["start"])
    check_datetime(entry["end"])
