#!/bin/bash

getmodule() {
    if [ -d $1 ]; then
       cd $1
       echo "$1: `git branch |grep \*` : `git rev-parse --short HEAD`"
       cd ..
    fi
}
getmodule zbs-common
getmodule zbs-server
getmodule zbs-gateway
getmodule zbs-client
getmodule zbs-storage
getmodule zbs-scheduler
getmodule zbs-worker
getmodule zbs-openapi
