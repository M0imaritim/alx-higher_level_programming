#!/bin/bash
#  script that sends a DELETE request to the URL passed as the first argument
curl -sL -X DELETE "$1"
