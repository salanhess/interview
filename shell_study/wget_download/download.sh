#!/bin/bash
maxtry=3
testurl=www.bing.com
noproxy=''

url=${1:-$testurl}   # Defaults to testurl
proxy="-e use_proxy=yes -e http_proxy="${2:-$noproxy}           # Default no proxy

#proxycfg="-e use_proxy=yes -e http_proxy=183.88.195.231:8080"
rm -f index.html
echo "\n===============start to download at `date`===============" >> his.log
echo "===============start to download at `date`==============="
echo wget ${url} ${proxy} to  his.log
nohup wget ${url} ${proxy} >> his.log 2>&1 &

count=1
while [[ `tail -2 his.log` != *"MB/s"* && $count -le $maxtry ]]
do
   sleep 3s
   try=${try}.
   echo "trying..."${try}
   (( count++ ))
done
if [ $count -eq 4 ];then ps aux |grep wget |grep "$url" |awk '{print $2}'|xargs kill -9 && echo "===============[Fail]download ${url} at `date` and killed wget related backend test thread===============" >> his.log;fi
if [ $count -lt 4 ];then echo "===============[Pass]download ${url} at `date`===============" >> his.log;fi
#cat his.log |grep MB/s
tail -3 his.log
