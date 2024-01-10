#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    headers = {'Authorization': 'token ' + argv[2]}
    login = requests.get('https://api.github.com/user', headers=headers)
    retval = login.json()
    if 'id' in retval:
        print(retval['id'])
    else:
        print(None)
