#!/bin/bash
#send a get request with header variable X-School-User-Id: 98
curl -s -H "X-School-User-Id : 98" "$1"
