#!/bin/bash
# Bash script for URL to send REQUEST and display RESPONSE

if [ -z "$1" ]; then
	exit 1
fi

URL=$0

RESPONSE=$(curl -s "$URL" | awk '/Content-Length/ {print $2}' | tr -d '\r')
RETVAL=$(echo -n "$RESPONSE" | wc -c)

echo $RETVAL
