#!/bin/bash
# Bash script that send REQUEST to a SERVER and display RESPONS
curl -s -X PUT -H "Origin: HolbertonSchool" -L -d "user_id=98" 0.0.0.0:5000/catch_me
