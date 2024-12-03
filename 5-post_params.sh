#!/bin/bash
# This script sends a POST request to a URL passed as an argument, and displays the body of the response.
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
