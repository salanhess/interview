#!/bin/bash
WAIT_TIME=3s
set -e
#set -x

zbs_prject_path=/jcloud-zbs/src/xx.com/zbs
zbs_modules_commit_id_file=zbs_modules_commit_id.log
#BRANCH_common=openapi_master
BRANCH_common=master
BRANCH_gateway=master
BRANCH_server=master
BRANCH_client=master
BRANCH_storage=master
BRANCH_scheduler=master
BRANCH_worker=master
#BRANCH_worker=zbs-worker-ebs
BRANCH_openapi=master

cd ${zbs_prject_path}
echo start to update
current_zbs_path=`pwd`
echo "[INFO] Current path is ${current_zbs_path}"

if [ `cat /etc/hosts.allow |grep SSHD |wc -l` -eq 0 ] ; then
    echo "[Info]Modify /etc/hosts.allow ing...."
    echo 'SSHD: ALL' >> /etc/hosts.allow
fi

gitmodule() {
    modulename=$1
    branchname=$2
    if [ ! -d $modulename  ]; then
        echo "[INFO] git clone -b ${branchname} git@git.xx.com:xxx/${modulename}.git"
        git clone -b ${branchname} git@git.xx.com:xxx/${modulename}.git
    fi
    sleep ${WAIT_TIME}
    cd ${modulename}
    git reset --hard
    git checkout ${branchname}
    git fetch && git pull
    echo $modulename $branchname commitid: `git rev-parse --short HEAD`
    cd ..
}

cleanmodule () {
    if [ -d $1 ]; then
        echo "[INFO] clean up $1 before build"
        rm -rf $1
    fi
}

gitmodule zbs-common $BRANCH_common
gitmodule zbs-gateway $BRANCH_gateway
gitmodule zbs-storage $BRANCH_storage
gitmodule zbs-scheduler $BRANCH_scheduler
gitmodule zbs-server $BRANCH_server
gitmodule zbs-client $BRANCH_client
gitmodule zbs-worker $BRANCH_worker
gitmodule zbs-openapi $BRANCH_openapi

echo [Info]service is $1
case $1 in
    zbs-client)
    cleanmodule zbs-scheduler
    cleanmodule zbs-storage
    cleanmodule zbs-worker
    cleanmodule zbs-openapi
    sleep 3s && cd zbs-client && make clean && make && sleep 3s && ./zbs-client -v
    ;;
    zbs-openapi)
    cleanmodule zbs-scheduler
    cleanmodule zbs-gateway
    cleanmodule zbs-client
    cleanmodule zbs-storage
    cleanmodule zbs-worker
    sleep 3s && cd zbs-openapi && make clean && make && sleep 3s && ./zbs-openapi -v
    ;;
    zbs-gateway)
    cleanmodule zbs-client
    cleanmodule zbs-storage
    cleanmodule zbs-openapi
    sleep 3s && cd zbs-gateway && make clean && make && sleep 3s && ./zbs-gateway -v
    ;;
    zbs-scheduler)
    cleanmodule zbs-storage
    cleanmodule zbs-openapi
    sleep 3s && cd zbs-scheduler && make clean && make && sleep 3s && ./zbs-scheduler -v
    ;;
    zbs-server)
    cleanmodule zbs-storage
    cleanmodule zbs-client
    cleanmodule zbs-scheduler
    cleanmodule zbs-openapi
    sleep 3s && cd zbs-server && make clean && make && sleep 3s && ./zbs-server -v
    ;;
    zbs-storage)
    cleanmodule zbs-server
    cleanmodule zbs-client
    cleanmodule zbs-scheduler
    cleanmodule zbs-openapi
    cleanmodule zbs-worker
    sleep 3s && cd zbs-storage && make clean && make && sleep 3s && ./zbs-storage -v
    ;;
    zbs-worker)
    cleanmodule zbs-openapi
    cleanmodule zbs-storage
    sleep 3s && cd zbs-worker && make clean && make && sleep 3s && ./zbs-worker -v
    ;;
    *)
    echo xxxxx module NOT support
    ;;
esac
