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


def check_block(block_number):
    if not isinstance(block_number, (int, float)):
        raise Exception("block_number must be int or float, not %s" % type(block_number))

    if block_number < 0:
        raise Exception("Block must be greater than 0, is %s" % block_number)


# Load the json
tokens = json.loads(open("tokens.json").read())

# Check start and end of all entries
for token in tokens:
    if "startTime" in token and "startBlock" in token:
        raise Exception("Only startTime or startBlock can be specified, not both")
    if "endTime" in token and "endBlock" in token:
        raise Exception("Only endTime or endBlock can be specified, not both")

    if "startTime" in token:
        check_datetime(token["startTime"])
    if "endTime" in token:
        check_datetime(token["endTime"])
    if "startBlock" in token:
        check_block(token["startBlock"])
    if "endBlock" in token:
        check_block(token["endBlock"])
