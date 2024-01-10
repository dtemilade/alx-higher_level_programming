#!/usr/bin/python3
""" Python script that takes 2 arguments in order to solve this challenge."""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    x = 0
    login = requests.get(url)
    retval = login.json()
    for i in retval:
        commit = i["commit"]["author"]
        print("{}: {}".format(i["sha"], commit["name"]))
        x += 1
        if x == 10:
            break
