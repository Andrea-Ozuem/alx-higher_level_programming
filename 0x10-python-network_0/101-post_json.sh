#!/bin/bash
#displays only the status code of the response
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
