#!/bin/bash
# Bash script that send REQUEST to a SERVER and display RESPONSE
curl -sXL PUT -H "Origin:School" -d "user_id=98" "0.0.0.0:5000/catch_me"
