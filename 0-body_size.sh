#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sI "$1" | awk '/Content-Length/ {print $2}'
