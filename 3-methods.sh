#!/bin/bash
# This script shows all http methods the server will accept.
curl -sI "$1" | awk '/Allow: / {$1=""; print substr($0, 2)}'
