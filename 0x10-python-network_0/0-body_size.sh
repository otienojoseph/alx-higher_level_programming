#!/bin/bash
# Takes URL,sends a request to that URL and prints size of response
echo "$(curl -s -o /dev/null -w "%{size_download}" "$@")"
