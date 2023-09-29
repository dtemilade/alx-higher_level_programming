#!/usr/bin/python3
"""Python script that fetches url"""


import urllib.request


if __name__ == "__main__":
	retval = urllib.request.Request('https://intranet.hbtn.io/status')
	with urllib.request.urlopen(retval) as response:
		resp = response.read()
		full_resp = resp.decode('utf-8')
		print("Body response:")
		print("\t- type: {}".format(type(resp)))
		print("\t- full_resp: {}".format(resp))
		print("\t- utf8 full_resp: {}".format(full_resp))

