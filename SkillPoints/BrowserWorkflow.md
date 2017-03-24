refer to [http://t.im/1c3d6](http://t.im/1c3d6)

#browser工作原理#

web浏览器与web服务器之间通过HTTP协议进行通信的过程。所以，web C/S之间握手的协议就是HTTP协议。
![原理图](https://qaseven.github.io/image/front_end_performance_test.png)

##页面的请求过程##

###请求阶段###
![过程1](https://qaseven.github.io/image/LSBAWS_HTTP_request_response.png)

* > . browser send url request

* > . 递归寻找DNS server (refer to [link](http://www.cnblogs.com/xrq730/p/4931418.html))
    * > 1. [本地]先查找浏览器的缓存，然后查找Host文件（/etc/hosts）
    * > 2. 查找本地DNS解析服务器(LDNS)（/etc/resolv.conf）
    * > 3. 在Root Server进行解析
    * > 4. 根域名服务器返回给本地域名服务器一个所查询的主域名服务器（gTLD Server）地址。gTLD是国际顶级域名服务器，如.com、.cn、.org等，全球只有13台左右
    * > 5. 本地域名服务器(LDNS)再向上一步返回的gTLD服务器发送请求
    * > 6. 本地域名服务器LDNS再向上一步返回的gTLD服务器发送请求
    * > 7. 接受请求的gTLD服务器查找并返回此域名对应的Name Server域名服务器的地址，这个Name Server通常就是用户注册的域名服务器，例如用户在某个域名服务提供商申请的域名，那么这个域名解析任务就由这个域名提供商的服务器来完成
    * > 8. Name Server域名服务器会查询存储的域名和IP的映射关系表，在正常情况下都根据域名得到目标IP地址，连同一个TTL值返回给DNS Server域名服务器
    * > 9. 返回该域名对应的IP和TTL值，LDNS会缓存这个域名和IP的对应关系，缓存时间由TTL值控制
    * > 10. 把解析的结果返回给用户，用户根据TTL值缓存在本地系统缓存中，域名解析过程结束
   
   自己的理解：DNS的解析除了本地的2步，其余主要包含五个部分： User LocalDNS RootDNS gTLDservers(Top13) NameServer 
   * > . 其中User只和LocalDNS交互
   * > . LocalDNS依次和RootDNS  gTLDServer NameServer 交互最后拿到ip以及TTL(Time-To-Live)域名解析记录的存留时间，然后将ip回传给user
   
![flow](http://images2015.cnblogs.com/blog/801753/201511/801753-20151102204944102-1846720088.png)

    注：在实际的DNS解析过程中，可能还不止这10步，如Name Server可能有很多级，或者有一个GTM来负载均衡控制，这都有可能会影响域名解析过程。
    
* > . 连接目标IP并建立TCP连接

* > . 向目标服务器发送http请求

* > . web服务器接收请求后处理

* > . web服务器返回相应的结果【无效、重定向、正确页面等】

* > . 浏览器接收返回的http内容

![过程2](https://qaseven.github.io/image/dns.jpg)


