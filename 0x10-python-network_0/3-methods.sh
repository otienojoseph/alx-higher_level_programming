#!/bin/bash
# sends a GET request to the URL, and display the response body
curl -s -I -X "OPTIONS" "$1" | grep "Allow:" | cut -f2- -d " "
