#!/bin/bash
# Bash script for URL to send REQUEST and display RESPONSE

if [ -z "$1" ]; then
	exit 1
fi

URL=$1

BODY_SIZE=$(curl -s "$URL" | wc -c)
#RESPONSE=$(curl -s "$URL" | awk '/Content-Length/ {print $2}' | tr -d '\r')
#RETVAL=$(echo -n "$RESPONSE" | wc -c)
#RETVAL=$(curl -sI "$URL" | awk '/Content-Length/ {print $2}' | tr -d '\r')

echo "${BODY_SIZE}"
