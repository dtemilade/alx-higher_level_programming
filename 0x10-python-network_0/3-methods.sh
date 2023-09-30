#!/bin/bash
# Bash script for URL to displays all HTTP methods.
curl -siL -X OPTIONS $1 | grep Allow | cut -d" " -f2-
