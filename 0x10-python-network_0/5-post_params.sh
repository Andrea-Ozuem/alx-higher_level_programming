#!/bin/bash
#sends a POST request to url
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
