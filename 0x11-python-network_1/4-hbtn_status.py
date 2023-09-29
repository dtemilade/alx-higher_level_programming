#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""


import requests

if __name__ == "__main__":
	retval = requests.get('https://intranet.hbtn.io/status')

	print("Body response:")
	print("\t- type: {}".format(type(retval.text)))
	print("\t- content: {}".format(retval.text))
