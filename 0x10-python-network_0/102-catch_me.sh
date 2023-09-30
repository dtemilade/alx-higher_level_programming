#!/bin/bash
# Bash script that send REQUEST to a SERVER and display RESPONSE
curl -s 0.0.0.0:5000/catch_me -X POST -d "You got me!" #url -s http://0.0.0.0:5000/catch_me > response.txt less response.txt
