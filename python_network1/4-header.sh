#!/bin/bash
# Sends GET request with a custom header variable X-HolbertonSchool-User-Id: 98, and displays the body of the response.
curl -sH "X-School-User-Id: 98" "$1"
