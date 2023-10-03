#!/bin/bash
# Bash script that send REQUEST to a SERVER and display RESPONSE
curl -sd 'user_id=98' -X PUT -H 'Origin: School' -L 0.0.0.0:5000/catch_me
