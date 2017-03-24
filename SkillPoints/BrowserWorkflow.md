refer to [http://t.im/1c3d6](http://t.im/1c3d6)

# Browser工作原理 #

web浏览器与web服务器之间通过HTTP协议进行通信的过程。所以，web C/S之间握手的协议就是HTTP协议。
![原理图](https://qaseven.github.io/image/front_end_performance_test.png)

## 页面的请求过程 ##

### 请求阶段 ###

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
    
    如何查看和操作：   #nslookup <IP>
    
    hbaitekiMacBook-Air:~ hbai$ nslookup news.163.com
      Server:		8.8.8.8
      Address:	8.8.8.8#53

      Non-authoritative answer:
      news.163.com	canonical name = web.163.com.lxdns.com.
      web.163.com.lxdns.com	canonical name = 163.xdwscache.ourglb0.com.
      Name:	163.xdwscache.ourglb0.com
      Address: 211.144.7.85
      Name:	163.xdwscache.ourglb0.com
      Address: 111.161.120.199
      Name:	163.xdwscache.ourglb0.com
      Address: 60.28.100.38

      hbaitekiMacBook-Air:~ hbai$ dig +trace www.baidu.com

      ; <<>> DiG 9.8.3-P1 <<>> +trace www.baidu.com
      ;; global options: +cmd
      .			200209	IN	NS	a.root-servers.net.
      .			200209	IN	NS	b.root-servers.net.
      .			200209	IN	NS	c.root-servers.net.
      .			200209	IN	NS	d.root-servers.net.
      .			200209	IN	NS	e.root-servers.net.
      .			200209	IN	NS	f.root-servers.net.
      .			200209	IN	NS	g.root-servers.net.
      .			200209	IN	NS	h.root-servers.net.
      .			200209	IN	NS	i.root-servers.net.
      .			200209	IN	NS	j.root-servers.net.
      .			200209	IN	NS	k.root-servers.net.
      .			200209	IN	NS	l.root-servers.net.
      .			200209	IN	NS	m.root-servers.net.
      ;; Received 228 bytes from 8.8.8.8#53(8.8.8.8) in 34001 ms

      com.			172800	IN	NS	a.gtld-servers.net.
      com.			172800	IN	NS	b.gtld-servers.net.
      com.			172800	IN	NS	c.gtld-servers.net.
      com.			172800	IN	NS	d.gtld-servers.net.
      com.			172800	IN	NS	e.gtld-servers.net.
      com.			172800	IN	NS	f.gtld-servers.net.
      com.			172800	IN	NS	g.gtld-servers.net.
      com.			172800	IN	NS	h.gtld-servers.net.
      com.			172800	IN	NS	i.gtld-servers.net.
      com.			172800	IN	NS	j.gtld-servers.net.
      com.			172800	IN	NS	k.gtld-servers.net.
      com.			172800	IN	NS	l.gtld-servers.net.
      com.			172800	IN	NS	m.gtld-servers.net.
      ;; Received 491 bytes from 199.7.83.42#53(199.7.83.42) in 24977 ms

      baidu.com.		172800	IN	NS	dns.baidu.com.
      baidu.com.		172800	IN	NS	ns2.baidu.com.
      baidu.com.		172800	IN	NS	ns3.baidu.com.
      baidu.com.		172800	IN	NS	ns4.baidu.com.
      baidu.com.		172800	IN	NS	ns7.baidu.com.
      ;; Received 201 bytes from 192.42.93.30#53(192.42.93.30) in 3571 ms

      www.baidu.com.		1200	IN	CNAME	www.a.shifen.com.
      a.shifen.com.		1200	IN	NS	ns1.a.shifen.com.
      a.shifen.com.		1200	IN	NS	ns4.a.shifen.com.
      a.shifen.com.		1200	IN	NS	ns5.a.shifen.com.
      a.shifen.com.		1200	IN	NS	ns3.a.shifen.com.
      a.shifen.com.		1200	IN	NS	ns2.a.shifen.com.
      ;; Received 228 bytes from 202.108.22.220#53(202.108.22.220) in 11 ms



* > . 连接目标IP并建立TCP连接
   
   refer to [http://t.im/1c3lw](http://t.im/1c3lw)
   传输层的协议包括TCP协议和UDP协议，TCP协议系统内核会给其分配一个发送缓冲区和接收缓冲区，当应用层连续执行多次操作时，TCP先将这些数据写入TCP发送缓冲区中，当TCP模块真正开始发送数据时，发送缓冲区中这些等待发送的数据可能被封装成一个或多个TCP数据报文段发出，所以，TCP模块发出的TCP报文段的个数和应用程序执行的写操作次之间没有固定的联系。
   
 TCP的建立是三次握手
 
![如图](https://leanote.com/api/file/getImage?fileId=57c92e44ab644135ea06c6bd)

TCP协议的头部构造

![图](https://leanote.com/api/file/getImage?fileId=57c92e44ab644135ea06c6be)
 
   * > . 客户端的TCP进程也首先创建传输控制模块TCB，然后向服务端发出连接请求报文段，该报文段首部中的SYN=1，ACK=0，同时选择一个初始序号seq=i。TCP规定，SYN=1的报文段不能携带数据，但要消耗掉一个序号。这时，TCP客户进程进入SYN—SENT（同步已发送）状态，这是 TCP连接的第一次握手。
   
   * > . 服务端收到客户端发来的请求报文后，如果同意建立连接，则向客户端发送确认。确认报文中的SYN=1，ACK=1，确认号ack=i+1，同时为自己选择一个初始序号seq=j。同样该报文段也是SYN=1的报文段，不能携带数据，但同样要消耗掉一个序号。这时，TCP服务端进入SYN—RCVD（同 步收到）状态，这是TCP连接的第二次握手。
   
   * > . TCP客户端进程收到服务端进程的确认后，还要向服务端给出确认。确认报文段的ACK=1，确认号ack=j+1，而自己的序号为seq=i+1。TCP的标准规定，ACK报文段可以携带数据，但如果不携带数据则不消耗序号，因此，如果不携带数据，则下一个报文段的序号仍为seq=i+1。这时，TCP连接已经建立，客户端进入ESTABLISHED（已建立连接）状态。这是TCP连接的第三次握手，可以看出第三次握手客户端已经可以发送携带 数据的报文段了。 
   
   当服务端收到确认后，也进入ESTABLISHED（已建立连接）状态。

![连接](https://leanote.com/api/file/getImage?fileId=57c97450ab644135ea06cade)

* > . 向目标服务器发送http请求

* > . web服务器接收请求后处理

* > . web服务器返回相应的结果【无效、重定向、正确页面等】

* > . 浏览器接收返回的http内容

![过程2](https://qaseven.github.io/image/dns.jpg)

## 前端解析阶段 ## 

refer to [http://t.im/1c3ol](http://t.im/1c3ol)
   
   * > . 处理 HTML 标记并构建 DOM 树。
   * > . 处理 CSS 标记并构建 CSSOM 树。
   * > . 将 DOM 与 CSSOM 合并成一个渲染树。
   * > . 根据渲染树来布局，以计算每个节点的几何信息。
   * > . 将各个节点绘制到屏幕上。

![图](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/images/render-tree-construction.png?hl=zh-cn)

浏览器的架构图 

![参考](http://hi.csdn.net/attachment/201106/8/2143330_1307526705wVJ1.png)  
