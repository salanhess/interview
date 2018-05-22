#!/bin/bash
echo "http://www.freeproxylists.net/zh/?pr=HTTP&u=94&s=u"
echo "Note:add proxy according above link"

sampleproxy=169.60.8.122:3128
echo [case1]
sh download.sh
echo [case2]
sh download.sh www.baidu.com
echo [case3]
echo sh download.sh www.baidu.com $sampleproxy
sh download.sh www.baidu.com $sampleproxy
