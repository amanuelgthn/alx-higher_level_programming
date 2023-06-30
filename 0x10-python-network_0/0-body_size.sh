#!/usr/bin/env bash
#Bash script that takes a URL,sends a request to that URL and displays the size of the body of the response
#Size displayed in bytes
Arg=$1
response=$(curl -s "$Arg")
parse_response=$(echo "$response" | jq '.content-length')
echo "$parse_response"
