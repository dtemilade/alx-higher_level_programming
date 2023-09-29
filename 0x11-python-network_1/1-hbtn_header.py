#!/usr/bin/python3
"""Python script that fetches url"""


import urllib.request
import sys


if __name__ == "__main__":
	url = sys.argv[1]

	retval = urllib.request.Request(url)
	with urllib.request.urlopen(retval) as response:
		ret_resp = response.info()
		print(ret_resp.get('X-Request-Id'))
