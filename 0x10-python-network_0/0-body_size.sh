#!/bin/bash
# Bash script for URL to send REQUEST and display RESPONSE

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

URL=$1

RETVAL=$(curl -sI "$URL" | awk '/Content-Length/ {print $2}')
echo $RETVAL
