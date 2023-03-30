#!/bin/bash
#send a get request with header variable X-School-User-Id: 98
curl -sH "X-School-User-Id: 98" -X GET "$1"
