##PCM VM_Support Openstack ##
> Install openstack component and do some preparation for PCM when install PCM 

> * . Provision KVM hypervisor host and join it to OpenStack cluster
> * . Discover and monitor KVM hypervisor hosts in OpenStack cluster
> * . Auto-discover existing VMs in OpenStack Nova compute
> * . Monitor a VM's state/performance
> * . Perform operations on a VM(e.g Power On /Off/Reboot
> * . Single GUI to manage OpenStack objects(e.g OpenStack VM images )
> * . Manage OpenStack VM networks

###Background###
> * 1 Install minimal openstack packages on PCM MN

> The controller node(PCM management node) runs Identity service(Keystone), Image service(Glance),Rabbit message queue, and Openstack Network service(Neuron), and Compute Service(Nova).

> * 2 Config the openstack to make sure that it can work

> Install rabbit message queue on the controller node

> * 3 Integrate the current postgresql DB into Openstack.

> Postgresql DB will be created for each openstack service(keystone/nova/neutron/glance)

> * 4 Provide Flat network for VMs

> The typical openstack network requires one management network, one tenant network, and one external network

> But for the typical PCM, we need management network(PCM provision network) and tenant network, the external network(public network) is optional.

> * 5 Support KVM hypervisor

> OOB build-in image profile “XX-kvm-openstack-compute” will be installed,used to install nova-compute on the KVM hypervisor. 


### Workflow ###

> * 1	Precondition:Lic file/Prepare openstack KVM image
> * 2	Network plan:NIC/bmc 
> * 3	Install PCM with VM support enable	
> * 4	Create PM network and network profile	
> * 5	Import KVM Node
> * 6	Modify KVM Cluster template	
> * 7	Create KVM Cluster	
> * 8	Modify VM Cluster template	
> * 9	Provision VM	
> * 10 VM operation	





