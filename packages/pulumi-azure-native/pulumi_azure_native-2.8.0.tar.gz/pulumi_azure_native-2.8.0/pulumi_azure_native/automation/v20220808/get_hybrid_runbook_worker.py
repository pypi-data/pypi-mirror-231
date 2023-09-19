# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetHybridRunbookWorkerResult',
    'AwaitableGetHybridRunbookWorkerResult',
    'get_hybrid_runbook_worker',
    'get_hybrid_runbook_worker_output',
]

@pulumi.output_type
class GetHybridRunbookWorkerResult:
    """
    Definition of hybrid runbook worker.
    """
    def __init__(__self__, id=None, ip=None, last_seen_date_time=None, name=None, registered_date_time=None, system_data=None, type=None, vm_resource_id=None, worker_name=None, worker_type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip and not isinstance(ip, str):
            raise TypeError("Expected argument 'ip' to be a str")
        pulumi.set(__self__, "ip", ip)
        if last_seen_date_time and not isinstance(last_seen_date_time, str):
            raise TypeError("Expected argument 'last_seen_date_time' to be a str")
        pulumi.set(__self__, "last_seen_date_time", last_seen_date_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if registered_date_time and not isinstance(registered_date_time, str):
            raise TypeError("Expected argument 'registered_date_time' to be a str")
        pulumi.set(__self__, "registered_date_time", registered_date_time)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vm_resource_id and not isinstance(vm_resource_id, str):
            raise TypeError("Expected argument 'vm_resource_id' to be a str")
        pulumi.set(__self__, "vm_resource_id", vm_resource_id)
        if worker_name and not isinstance(worker_name, str):
            raise TypeError("Expected argument 'worker_name' to be a str")
        pulumi.set(__self__, "worker_name", worker_name)
        if worker_type and not isinstance(worker_type, str):
            raise TypeError("Expected argument 'worker_type' to be a str")
        pulumi.set(__self__, "worker_type", worker_type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ip(self) -> Optional[str]:
        """
        Gets or sets the assigned machine IP address.
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter(name="lastSeenDateTime")
    def last_seen_date_time(self) -> Optional[str]:
        """
        Last Heartbeat from the Worker
        """
        return pulumi.get(self, "last_seen_date_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="registeredDateTime")
    def registered_date_time(self) -> Optional[str]:
        """
        Gets or sets the registration time of the worker machine.
        """
        return pulumi.get(self, "registered_date_time")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Resource system metadata.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmResourceId")
    def vm_resource_id(self) -> Optional[str]:
        """
        Azure Resource Manager Id for a virtual machine.
        """
        return pulumi.get(self, "vm_resource_id")

    @property
    @pulumi.getter(name="workerName")
    def worker_name(self) -> Optional[str]:
        """
        Name of the HybridWorker.
        """
        return pulumi.get(self, "worker_name")

    @property
    @pulumi.getter(name="workerType")
    def worker_type(self) -> Optional[str]:
        """
        Type of the HybridWorker.
        """
        return pulumi.get(self, "worker_type")


class AwaitableGetHybridRunbookWorkerResult(GetHybridRunbookWorkerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHybridRunbookWorkerResult(
            id=self.id,
            ip=self.ip,
            last_seen_date_time=self.last_seen_date_time,
            name=self.name,
            registered_date_time=self.registered_date_time,
            system_data=self.system_data,
            type=self.type,
            vm_resource_id=self.vm_resource_id,
            worker_name=self.worker_name,
            worker_type=self.worker_type)


def get_hybrid_runbook_worker(automation_account_name: Optional[str] = None,
                              hybrid_runbook_worker_group_name: Optional[str] = None,
                              hybrid_runbook_worker_id: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHybridRunbookWorkerResult:
    """
    Retrieve a hybrid runbook worker.


    :param str automation_account_name: The name of the automation account.
    :param str hybrid_runbook_worker_group_name: The hybrid runbook worker group name
    :param str hybrid_runbook_worker_id: The hybrid runbook worker id
    :param str resource_group_name: Name of an Azure Resource group.
    """
    __args__ = dict()
    __args__['automationAccountName'] = automation_account_name
    __args__['hybridRunbookWorkerGroupName'] = hybrid_runbook_worker_group_name
    __args__['hybridRunbookWorkerId'] = hybrid_runbook_worker_id
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:automation/v20220808:getHybridRunbookWorker', __args__, opts=opts, typ=GetHybridRunbookWorkerResult).value

    return AwaitableGetHybridRunbookWorkerResult(
        id=pulumi.get(__ret__, 'id'),
        ip=pulumi.get(__ret__, 'ip'),
        last_seen_date_time=pulumi.get(__ret__, 'last_seen_date_time'),
        name=pulumi.get(__ret__, 'name'),
        registered_date_time=pulumi.get(__ret__, 'registered_date_time'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        vm_resource_id=pulumi.get(__ret__, 'vm_resource_id'),
        worker_name=pulumi.get(__ret__, 'worker_name'),
        worker_type=pulumi.get(__ret__, 'worker_type'))


@_utilities.lift_output_func(get_hybrid_runbook_worker)
def get_hybrid_runbook_worker_output(automation_account_name: Optional[pulumi.Input[str]] = None,
                                     hybrid_runbook_worker_group_name: Optional[pulumi.Input[str]] = None,
                                     hybrid_runbook_worker_id: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHybridRunbookWorkerResult]:
    """
    Retrieve a hybrid runbook worker.


    :param str automation_account_name: The name of the automation account.
    :param str hybrid_runbook_worker_group_name: The hybrid runbook worker group name
    :param str hybrid_runbook_worker_id: The hybrid runbook worker id
    :param str resource_group_name: Name of an Azure Resource group.
    """
    ...
