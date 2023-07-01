#!/bin/bash
#Bash script that takes in a URL as an argument, sends GET requests to the URL and displays the body of the response, Header variable X-School_User-Id must be sent with the value 98
curl -s -H "X-School_User-Id:98" "$1"