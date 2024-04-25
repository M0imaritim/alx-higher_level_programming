#!/bin/bash
# ends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -X post -d "$(cat "$2")" -H "Content-Type: application/json" "$1"
