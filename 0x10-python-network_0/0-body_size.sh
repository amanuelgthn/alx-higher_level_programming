#!/usr/bin/env bash
#Bash script that takes a URL,sends a request to that URL and displays the size of the body of the response
response=$(curl -s "$1")
echo "$response" | grep -i 'content-length'
