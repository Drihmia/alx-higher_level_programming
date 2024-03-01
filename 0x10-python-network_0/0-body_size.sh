#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL,
curl "$1" -sI | grep "Content-Length" | cut -d ":" -f 2
