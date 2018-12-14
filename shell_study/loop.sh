#!/bin/bash

filename=/nfs/data.file
x=1
#while true
for k in $( seq 1 10 )
do
    echo "====$x times loop,currenttime `date`:====="
    dd if=/dev/urandom bs=1M count=1 oflag=direct count=10 of=${filename} && ls -lh ${filename}
    x=$(($x + 1))
    sleep 3s
done

~~~~~~~~

#!/bin/bash
ip1=116.196.92.101
ip2=116.196.93.163
ip3=118.184.216.183
ip4=118.184.217.97

array=( $ip1 $ip2 $ip3 $ip4 )
for ip in "${array[@]}"
do
    echo "[Cheking ip:] $ip..."
    #scp -i disk_auto/utils/id_rsa disk_auto/utils/auto_fdisk.sh ${ip}:/tmp/
    ssh -i disk_auto/utils/id_rsa ${ip} "ls -l /tmp/auto_fdisk.sh"
    sleep 1s
done

~~~~~~~~~~~~~~~

#!/bin/bash
ip_port=192.168.241.101:9698
logpath=log/operation.log
echo `date "+%Y-%m-%d-%H:%M:%S"`, start check quota |tee -ai $logpath
hd101sql="华东101 -h192.168.241.101 -uzbs_global -pzbs_global -P3306 zbs_global "
sq2ndsql="宿迁2期 -h10.226.134.236  -uzbs_global_zbs5 -pzbs_global_zbs5 -P3306 zbs_global_zbs5 "
sq1stsql="宿迁1期 -h192.168.241.132 -uzbs_global_zbs5 -pzbs_global_zbs5 -P3306 zbs_global_zbs5 "
array=( "${hd101sql}" "${sq2ndsql}" "${sq1stsql}" )
for sqlstr in "${array[@]}"
do
    tenvname=${sqlstr:0:5}
    tenvip=${sqlstr:7:16}
    tenvsqlstr=${sqlstr:5:100}
    #echo -e "$tenvname \n $tenvip \n $tenvsqlstr \n"
    echo "[$tenvname $tenvip]=======current Cluster_white list:========="
    #mysql $tenvsqlstr -e"select * from cluster_whitelist"
    mysql $tenvsqlstr -e"select * from quota where tenant_id=any (select tenant_id from cluster_whitelist)"
    echo -e "\n\n\n"
done

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#! /bin/bash
function pause(){
        read -n 1 -p "$*" INP
        if [ $INP != '' ] ; then
                echo -ne '\b \n'
        fi
}
 
#使用时：
pause 'Press any key to continue...'
~~~~~~~~~~~~`
if false; then

....

fi
~~~~~~~~~~~~~
[root@A04-R08-I53-236 zbs-scheduler]# cat restart.sh
#!/bin/bash
#set -e
processname=/etc/zbs-scheduler1/zbs_scheduler.cfg
echo before restart $processname:
ps aux |grep -v grep|grep $processname
set -x
ps aux |grep -v grep|grep $processname |awk '{print $2}' |xargs kill -9
set +x

env_num=1
current_date=`eval date "+%Y_%m_%d_%H_%M_%S"`

nohup_out="zbs-scheduler_${current_date}.out"
rm -f /var/run/zbs/scheduler.lock
nohup ./zbs-scheduler -c /etc/zbs-scheduler${env_num}/zbs_scheduler.cfg > /export/log/zbs${env_num}/zbs-scheduler/${nohup_out} 2>&1 &

echo after restart $processname:
ps aux |grep -v grep|grep $processname

~~~~~~~~~~~~~~~~~~~~~~~~~~
function remote_rsa_ssh(){
    local rsa_name="${1}"
    local ssh_ip="${2}"
    local cmdshell="${3}"
    set -x
    local cmd_result=`ssh -i "${rsa_name}"  -t root@"${ssh_ip}" "$cmdshell"`
    set +x
    echo $cmd_result
    sleep "${wait_time}"
}

~~~~~~~~~~~~~~~~~~~~
if [[ "${filename}x" = "x" ]]; then echo "no target object" && exit -1; fi

if [[ ! -e /tmp/auto_fdisk.sh ]]; then echo 'target file not exist,copying...' &&  ; fi && 


if [ ! -e /tmp/auto_fdisk.sh ];then
	echo 'target file not exist,copying...'
fi
~~~~~~~~~~~~~~~~~~~~~~~
case "${ossenv}" in
	([yY][fF])
		ak=9593CF13DF84F8AAFC578F58B42F38F5
		sk=B6809CC9736CCD2ED80AC930058434F4
		bucketname=pre-test-bucket
		s3host=s3.cn-stag-1.jcloudcs.com;;
	([hH][dD])
		ak=85B6358FACFBA460D7C0E4A6598F29C5
		sk=8EA45CF83E9A128CD2766D02AF7CDD1E
		bucketname=zbs-test1
		s3host=s3.cn-test-1.jcloudcs.com;;
        (*)
        echo wrong ${method};;
esac
~~~~~~~~~~~~~~~~~
#!/bin/sh
for i in `ll /export/baihao/jcloud-zbs/src/jd.com/zbs/zbs-test/ci/playbooks/inventories/zbs_test_env/group_vars/zbs-* |awk '{print $9}'`
do
    fname=$i
    echo "=========checking ${fname}=================="
    #sed -i "4i oss_url: http://storage.jd.com/iaas-disk/zbs-test" ${fname}
    sleep 1s
done


#!/bin/sh
for i in `ps aux |grep -v grep|grep zbs-client |awk -F "domconf/" '{print $2}' |awk -F "." '{print $1}'`
do
    volname=$i
    echo "=========checking ${volname}=================="
    ps aux |grep -v grep|grep ${volname}
    #ps aux |grep -v grep|grep ${volname} |awk '{print $2}' |xargs kill -9
    sleep 1s
done

#!/bin/sh
x=1
while true
#for k in $( seq 1 10 )
do
	echo "$x times loop,currenttime `date`:"
	eval $1
	x=$(($x + 1))
	sleep 3s
done

echo ~~~concurrent ~~~~~~~~~~~~~~~~~
#!/bin/sh
x=1
#while true
for k in $( seq 1 2 )
do
	echo "$x times loop,currenttime `date`:"
	nohup go test -v > p_${x}.out 2>&1 &
    x=$(($x + 1))
done

#!/bin/bash

echo ~~~loop file ~~~~~~~~~~~~~~~~~
echo " cat file whiel read line"
cat vollist.txt |while read line
do
  echo sh del_volid.sh $line
  sh del_volid.sh $line
done

echo ~~~~compare~~~~~~~
flag=0
flag=`zbs-cli volume-create bh 10 ssd az1 -v |grep maintenance |wc -l`
if [[ $flag -eq 2  ]];then echo volume-create check success && flag=0; else echo volume-create Failed && exit; fi

echo ~~~~loop all the input parameters~~~~~~~
#!/bin/bash
for var in "$@"
do
    echo " ${var}"
done

echo ~~~~loop all the parameters~~~~~~~
#!/bin/bash

#Loop array
size=$1
array=( nbd0 nbd1 nbd2 nbd3 nbd4 nbd5 nbd6 nbd7 nbd8 nbd9 nbd10)
for i in "${array[@]}"
do
    hdname=$i
    echo "Start write to nbd"
    echo dd if=/dev/zero of=/dev/$hdname bs=1M count=$size oflag=direct
    dd if=/dev/zero of=/dev/$hdname bs=1M count=$size oflag=direct
    echo "Start read from nbd"
    echo dd if=/dev/$hdname of=/dev/null bs=1M count=$size iflag=direct
    dd if=/dev/$hdname of=/dev/null bs=1M count=$size iflag=direct
done

sleep 2
lsblk |grep nbd



#!/bin/bash
zbspath=/export/App/zbs1
cd $zbspath
array=( zbs-agent zbs-gateway zbs-scheduler zbs-server zbs-worker )
for i in "${array[@]}"
do
    modulename=$i
    echo "=========checking ${modulename}=================="
    cd ${modulename} && ./${modulename} -v && cd ..
    sleep 1s
done
