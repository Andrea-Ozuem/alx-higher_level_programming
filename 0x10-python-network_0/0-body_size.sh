#!/usr/bin/env bash
#sends a request to a URL, displays the size of the body of the response
curl -sI "$1" | grep -iF "content-length" | grep -Eo "[0-9]+"
