#!/bin/bash
#displays all HTTP methods the server will accept
curl -sI -X "OPTION" "$1" | grep "Allow" | sed 's/Allow: //'
