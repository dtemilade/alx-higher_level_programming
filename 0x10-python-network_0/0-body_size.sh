#!/bin/bash
# Bash script for URL to send REQUEST and display RESPONSE

if [ -z "$1" ]; then
	exit 1
fi

URL=$1

RETVAL=$(curl -sI "$URL" | awk '/Content-Length/ {print $2}' | tr -d '\r')

echo "${RETVAL}"
