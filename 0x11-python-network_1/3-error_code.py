#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
from urllib import request, error
import sys


if __name__ == "__main__":
	try:
		with request.urlopen(sys.argv[1]) as response:
			ret_resp = response.read()
			print(ret_resp.decode('utf-8'))
	except error.HTTPError as e:
		print("Error code: {}".format(e.code))
