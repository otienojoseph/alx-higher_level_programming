#!/bin/bash
# sends a GET request to the URL, and display the response body
response_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [[ "$response_code" -eq 200 ]]; then
	curl -s "$1"
fi
