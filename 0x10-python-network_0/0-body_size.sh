#!/bin/bash
#takes in a URL, sends a request to that URL, and displays size of the body
curl -s -w  "%{size_download}" -o /dev/null "$1"
