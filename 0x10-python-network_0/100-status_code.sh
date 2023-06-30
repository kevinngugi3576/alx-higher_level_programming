#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Please provide a URL as an argument"
  exit 1
fi

# Send the request and retrieve the response headers
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Display the status code
echo "$response"

