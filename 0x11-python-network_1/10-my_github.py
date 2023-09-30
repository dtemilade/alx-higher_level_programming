#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/?search=' + sys.argv[1]
    r = requests.get(url)
    json_obj = r.json()
    results = json_obj.get('results')
    print("Number of results: {}".format(json_obj.get('count')))
    for people in results:
        print(people.get('name'))
