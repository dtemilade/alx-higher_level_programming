#!/bin/bash
#  Bash script to send request of URL passed as an argument, and displays status code.

curl -s $1 -o /dev/null -w '%{http_code}'
