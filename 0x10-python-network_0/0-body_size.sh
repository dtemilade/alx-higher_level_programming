#!/bin/bash
# Bash script for URL to send REQUEST and display RESPONSE

curl -Is $1 | awk '/Content-Length/{print $2}'
