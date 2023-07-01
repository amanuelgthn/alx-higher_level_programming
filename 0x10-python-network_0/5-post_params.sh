#!/bin/bash
#Bash script that takes URL sends a POST request to the passed URL and displays the response, a variable email must be sent with the value test@gmail.com,a variable subject with a value of I will always be here for PLD
curl -s -X POST -d "email="test@gmail.com"&subject="I will always be here for PLD" "$1"
