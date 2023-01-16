#!/bin/bash
# This scirpt takes in a URL and displays all HTTP methods the server will accept
curl -X OPTIONS "$1"
