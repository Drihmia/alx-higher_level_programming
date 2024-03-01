#!/bin/bash
# a Bash script that takes in a URL as an argument, sends a GET request to
# the URL, and displays the body of the response.
# A header variable X-School-User-Id will be sent with the value 98

curl -H "X-School-User-Id: 98" "$1"
