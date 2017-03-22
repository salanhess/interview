#Difference for PowerVM KVM VMware ESX Server

> refer to [Overview](https://www.ibm.com/developerworks/cn/cloud/library/cl-hypervisorcompare/)

## PowerVM( For IBM POWER server series) ##

arch refer ![to](https://www.ibm.com/developerworks/cn/cloud/library/cl-hypervisorcompare-powervm/figure3.gif)

Runs based on OS
> * . Active Memory Sharing: Easy to balance memory 
> * . Live Partition Mobility:Running process will not stop during tansfer
> * . Create 10 LPARs to share 1 CPU(But NOT suggest,just image CPU execute failed situtaion
[More info](https://www.ibm.com/developerworks/cn/cloud/library/cl-hypervisorcompare-powervm/)

## VMware ESX Server(Can Integrated with Bear metal sever directly) ##

> Not rely on server OS
arch refer ![to](https://www.ibm.com/developerworks/cn/cloud/library/cl-hypervisorcompare-vmwareesx/figure4.gif)


  ESX Server 是一种操作系统，它的功能类似于虚拟机管理程序，直接在系统硬件上运行。
  ESX Server 在系统硬件与虚拟机之间插入一个虚拟化层，将系统硬件转换为一个逻辑计算资源池，
  ESX Server 可将其中的资源动态地分配给任何操作系统或应用程序。
  在虚拟机中运行的 Guest 操作系统与虚拟资源交互，就好象它们是物理资源一样。
  上图显示了一个运行虚拟机的 ESX Server 系统。ESX Server 运行一个具有服务控制台的虚拟机和 3 个额外的虚拟机。
  每个额外的虚拟机与其他虚拟机都独自运行一个操作系统和应用程序，同时共享相同的物理资源。 
  
> * . Work together with  *VMware VirtualCenter*,will support more functions like PowerVM features.

> * . Client is *VMware vSphere* : Snapshot , Add Hardware, config CPU/Memory

[More info](https://www.ibm.com/developerworks/cn/cloud/library/cl-hypervisorcompare-vmwareesx/)

## KVM(Based on linux kernel virtual tech,now support  Linux、BSD、Solaris、Windows) ##

Arch refer ![to](https://www.ibm.com/developerworks/cn/cloud/library/cl-hypervisorcompare-kvm/figure6.gif)

> KVM 本身不执行任何模拟，一个用户空间程序会使用 /dev/kvm 接口设置一个 Guest 虚拟服务器的地址空间，
向它提供模拟的 I/O，并将它的视频显示映射回宿主的显示屏。

> 在 KVM 架构中，虚拟机实现为常规的 Linux 进程，由标准 Linux 调度程序进行调度。
事实上，每个虚拟 CPU 显示为一个常规的 Linux 进程。这使 KVM 能够享受 Linux 内核的所有功能。

> 管理和部署可以使用Kimchi(An HTML5 based management tool for KVM) [Kimchi参考](https://github.com/kimchi-project/kimchi)

[More info](https://www.ibm.com/developerworks/cn/cloud/library/cl-hypervisorcompare-kvm/index.html)

## z/VM (IBM latest virtual tech for Z series,support thousands virtual machines) ##

> * . Same IBM server/Storage/Network systems administation
> * . Virtualbility of CPU Memory I/O etc
> * . Max blance resoure between each VM


[More info](https://www.ibm.com/developerworks/cn/cloud/library/cl-hypervisorcompare-zvm/index.html)



