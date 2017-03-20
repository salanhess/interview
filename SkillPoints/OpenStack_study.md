> https://docs.openstack.org/project-install-guide/ocata/

# Install #
> https://docs.openstack.org/ocata/install-guide-ubuntu/

1. Read [Overview](https://docs.openstack.org/ocata/install-guide-ubuntu/overview.html)

![arch](https://docs.openstack.org/ocata/install-guide-ubuntu/_images/hwreqs.png)


### Controller ###

The controller node runs the Identity service, Image service, management portions of Compute, management portion of Networking, various Networking agents, and the Dashboard. It also includes supporting services such as an SQL database, message queue, and NTP.
Optionally, the controller node runs portions of the Block Storage, Object Storage, Orchestration, and Telemetry services.
The controller node requires a minimum of two network interfaces.

### Compute ###

The compute node runs the hypervisor portion of Compute that operates instances. By default, Compute uses the KVM hypervisor. The compute node also runs a Networking service agent that connects instances to virtual networks and provides firewalling services to instances via security groups.
You can deploy more than one compute node. Each node requires a minimum of two network interfaces.

> hypervisor:Software that arbitrates and controls VM access to the actual underlying hardware.

> kernel-based VM:An OpenStack-supported hypervisor. KVM is a full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V), ARM, IBM Power, and IBM zSeries. It consists of a loadable kernel module, that provides the core virtualization infrastructure and a processor specific module.
    
### Block Storage ###

The optional Block Storage node contains the disks that the Block Storage and Shared File System services provision for instances.

For simplicity, service traffic between compute nodes and this node uses the management network. Production environments should implement a separate storage network to increase performance and security.

You can deploy more than one block storage node. Each node requires a minimum of one network interface.

### Object Storage ###

The optional Object Storage node contain the disks that the Object Storage service uses for storing accounts, containers, and objects.

For simplicity, service traffic between compute nodes and this node uses the management network. Production environments should implement a separate storage network to increase performance and security.

This service requires two nodes. Each node requires a minimum of one network interface. You can deploy more than two object storage nodes.

### Networking Option 1: Provider networks ###

The provider networks option deploys the OpenStack Networking service in the simplest way possible with primarily layer-2 (bridging/switching) services and VLAN segmentation of networks. Essentially, it bridges virtual networks to physical networks and relies on physical network infrastructure for layer-3 (routing) services. Additionally, a DHCP service provides IP address information to instances.

![arch](https://docs.openstack.org/ocata/install-guide-ubuntu/_images/network1-services.png)

### Networking Option 2: Self-service networks ###

The self-service networks option augments the provider networks option with layer-3 (routing) services that enable self-service networks using overlay segmentation methods such as VXLAN. Essentially, it routes virtual networks to physical networks using NAT. Additionally, this option provides the foundation for advanced services such as LBaaS and FWaaS.

![arch](https://docs.openstack.org/ocata/install-guide-ubuntu/_images/network2-services.png)
