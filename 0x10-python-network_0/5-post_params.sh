#!/bin/bash
# sends a POST request to the URL, and display the response body
curl -s -X "POST" -d "email=test@gmail.com&subject=I will be here for PLD" "$1"
