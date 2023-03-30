#!/bin/bash
#displays all HTTP methods the server will accept
curl -sI "$1" | grep -i "Allow" | sed 's/Allow: //'
