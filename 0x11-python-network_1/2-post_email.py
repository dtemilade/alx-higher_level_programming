#!/usr/bin/python3
"""Python script that fetches url"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {}
    values['email'] = sys.argv[2]
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')

    r = urllib.request.Request(url, data)
    with urllib.request.urlopen(r) as response:
        ret_resp = response.read().decode('utf-8')
        print(ret_resp)
