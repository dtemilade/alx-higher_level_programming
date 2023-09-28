#!/bin/bash
# Bash script that send REQUEST to a SERVER and display RESPONSE

url -s http://0.0.0.0:5000/catch_me > response.txt
less response.txt
