#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body response
curl -sL '0.0.0.0:5000/catch_me'
