#!/usr/bin/env python
"""
Check tokens.json for validity

Requires python-dateutil: https://pypi.python.org/pypi/python-dateutil/2.6.0
"""
import json
import dateutil.parser


def check_datetime(dt):
    try:
        dateutil.parser.parse(dt)
    except:
        print("Error parsing datetime '%s'" % dt)
        raise


# Load the json
tokens = json.loads(open("tokens.json").read())

# Check start and end of all entries
for entry in tokens:
    if "start" in entry:
        check_datetime(entry["start"])
    if "end" in entry:
        check_datetime(entry["end"])
