#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        value = sys.argv[1]
    else:
        value = ""
        r = requests.post(url, data={'q': value})
        try:
            json_obj = r.json()
            if not json_obj:
                print("No result")
            else:
                print("[{}] {}"
                      .format(json_obj.get('id'), json_obj.get('name')))
        except ValueError:
            print("Not a valid JSON")
