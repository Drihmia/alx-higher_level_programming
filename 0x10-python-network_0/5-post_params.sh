#!/bin/bash
# a Bash script that takes in a URL as an argument, sends a POST request to
# the URL, and displays the body of the response.
# A variable 'email' will be sent with the value "test@gmail.com"
# A variable 'subject' will be sent with the value "I will always be here for PLD"

curl -X "POST" -d "email: test@gmail.com" -d "subject: I will always be here for PLD" "$1"
