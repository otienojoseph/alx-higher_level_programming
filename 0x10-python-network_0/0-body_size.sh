#!/usr/bin/env bash

# Script that takes in a URL, sends a request to that URL
# and displays the size of the body of response

size=$(curl -s -o /dev/null -w "%{size_download}" "$@")
echo "${size}"
