#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL and displays the response, Displays only body of a 200 status code response
if [[ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == 200 ]]; then curl -sL "$1"; fi
