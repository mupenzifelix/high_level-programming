#!/bin/bash
# This script sends a DELETE request to a URL passed as an argument, and displays the body of the response.
curl -sX DELETE "$1"
