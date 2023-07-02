#!/bin/bash
#Bash script that sends a JSON POST request to a URL passed as the 1st argument, and displays the body of the response
curl -s "$1" --data "@$2" -X POST -H "Content-Type: application/json"
