#!/bin/bash
# ends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -X post -d "$2" "$1"
