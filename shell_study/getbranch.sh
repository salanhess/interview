#!/bin/bash
zbs_servercommit=8c12db
zbs_clientcommit=16923e
zbs_schedulercommit=aec44b
zbs_commoncommit=33c9fb50
zbs_gatewaycommit=4cda12b
zbs_storagecommit=29c220d
zbs_workercommit=84e55a9

check(){
    if [ ! -d "$1"  ]; then
          # Control will enter here if $DIRECTORY doesn't exist.
          git clone git@git.xx.com:xxx/${1}.git
    fi
    echo =======check $1 version=======
    cd $1
    git reset --hard
    git fetch
    git pull
    git branch -a --contain $2
    cd ..
}
check zbs-server $zbs_servercommit
check zbs-client $zbs_clientcommit
check zbs-scheduler $zbs_schedulercommit
check zbs-common $zbs_commoncommit
check zbs-gateway $zbs_gatewaycommit
check zbs-storage $zbs_storagecommit
check zbs-worker $zbs_workercommit
