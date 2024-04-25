#!/bin/bash

# Script that takes in a URL, sends a request to that URL
# and displays the size of the body of response in bytes

size=$(curl -s -o /dev/null -w "%{size_download}" "$@")
echo "$size"
