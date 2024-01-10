#!/usr/bin/python3
"""Python script that fetches url"""


import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        resp = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(resp)))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(resp.decode("utf-8")))
