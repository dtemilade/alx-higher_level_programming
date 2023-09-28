#!/bin/bash
# Bash script for URL to send GET-request and display RESPONSE

#curl -sL $1
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

curl_response=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

if [ "$curl_response" -eq 200 ]; then
  echo "Response body for $URL (HTTP 200 OK):"

  curl -s "$URL"
else
  echo "$curl_response"
fi
