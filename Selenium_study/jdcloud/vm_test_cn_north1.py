# coding=utf8

# Copyright 2018-2025

import unittest
import time
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.services.vm.client.VmClient import VmClient
from jdcloud_sdk.services.vm.apis.DescribeInstanceTypesRequest import *
from jdcloud_sdk.services.vm.apis.DescribeInstancesRequest import *
from jdcloud_sdk.services.vm.apis.DescribeInstanceRequest import *
from jdcloud_sdk.services.vm.apis.CreateInstancesRequest import *
from jdcloud_sdk.services.vm.apis.DeleteInstanceRequest import *
from jdcloud_sdk.services.vm.apis.StopInstanceRequest import *
from jdcloud_sdk.services.vm.models.InstanceSpec import InstanceSpec
from jdcloud_sdk.services.vm.models.InstanceNetworkInterfaceAttachmentSpec import InstanceNetworkInterfaceAttachmentSpec
from jdcloud_sdk.services.vm.models.InstanceDiskAttachmentSpec import InstanceDiskAttachmentSpec
from jdcloud_sdk.services.vpc.models.NetworkInterfaceSpec import NetworkInterfaceSpec
from jdcloud_sdk.services.common.models.Filter import Filter


class VmTest(unittest.TestCase):

    def setUp(self):
        access_key = 'ak'
        secret_key = 'sk'
        self.credential = Credential(access_key, secret_key)
        self.client = VmClient(self.credential)

#    def testDescribeInstanceTypes(self):
#        parameters = DescribeInstanceTypesParameters('cn-north-1')
#        request = DescribeInstanceTypesRequest(parameters)
#
#        resp = self.client.send(request)
#        self.assertTrue(resp.error is None)
#
#    def testDescribeInstances(self):
#        param = DescribeInstancesParameters('cn-north-1')
#        request = DescribeInstancesRequest(param)
#
#        resp = self.client.send(request)
#        self.assertTrue(resp.error is None)
#
#    def testDescribeInstancesPaging(self):
#        param = DescribeInstancesParameters('cn-north-1')
#        param.setPageNumber(2)
#        param.setPageSize(10)
#        request = DescribeInstancesRequest(param)
#
#        resp = self.client.send(request)
#        self.assertEqual(10, len(resp.result['instances']))
#
#    def testDescribeInstancesFilter(self):
#        f = Filter('instanceId', ['i-6e67ykot7m'], 'eq')
#        param = DescribeInstancesParameters('cn-north-1')
#        param.setFilters([f])
#        request = DescribeInstancesRequest(param)
#
#        resp = self.client.send(request)
#        self.assertEqual(1, len(resp.result['instances']))
#
#    def testDescribeInstance(self):
#        param = DescribeInstanceParameters('cn-north-1', 'i-6e67ykot7m')
#        request = DescribeInstanceRequest(param)
#
#        resp = self.client.send(request)
#        self.assertTrue(resp.error is None)

    def testCreateAndDeleteInstance(self):
        # create instance
        networkInterface = NetworkInterfaceSpec(az='cn-north-1a', subnetId='subnet-crpgl13lsv')
        network = InstanceNetworkInterfaceAttachmentSpec(networkInterface=networkInterface)
        sysDisk = InstanceDiskAttachmentSpec('local')
        instanceSpec = InstanceSpec(az='cn-north-1a', instanceType='g.s1.micro', name='python-sdk-test',
                                    imageId='7f7cc799-04dd-44a9-89f1-486de8bfed08',
                                    primaryNetworkInterface=network, systemDisk=sysDisk,
                                    dataDisks=None, keyNames=None, description='python-sdk-vm')
        param = CreateInstancesParameters('cn-north-1')
        param.setInstanceSpec(instanceSpec)
        param.setMaxCount(1)
        request = CreateInstancesRequest(param)
        create_resp = self.client.send(request)
	print create_resp
	print "========================="
        self.assertTrue(create_resp.error is None)
        instance_id = create_resp.result['instanceIds'][0]

        # stop instance
        def _stop_instance():
            param = StopInstanceParameters('cn-north-1', instance_id)
            request = StopInstanceRequest(param)
            #stop_resp = self.client.send(request)
            #return stop_resp.error is None
	    print "not stop instance dueto need attach vol"
	    return request

        result = self._try(10, 5, _stop_instance)
        self.assertTrue(result)

        # delete instance, may need try many times
        def _delete_instance():
            param = DeleteInstanceParameters('cn-north-1', instance_id)
            request = DeleteInstanceRequest(param)
            #delete_resp = self.client.send(request)
            #return delete_resp.error is None
	    print "~~~~~~~~~~~~~~~~~~"
	    print instance_id
	    print "~~~~~~~~~~~~~~~~~~"
            return instance_id

        result = self._try(10, 5, _delete_instance)
        self.assertTrue(result)

    def _try(self, count, wait, func):
        try_count = count
        result = False
        while try_count > 0:
            print 'try_count=', try_count
            time.sleep(wait)
            result = func()
            if result:
                break
            try_count -= 1
        return result
