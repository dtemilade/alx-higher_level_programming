#!/bin/bash
# Bash script for URL to send POST-request and display RESPONSE
curl -s $1 -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
