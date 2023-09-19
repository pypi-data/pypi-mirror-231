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
    'GetSyncSetResult',
    'AwaitableGetSyncSetResult',
    'get_sync_set',
    'get_sync_set_output',
]

@pulumi.output_type
class GetSyncSetResult:
    """
    SyncSet represents a SyncSet for an Azure Red Hat OpenShift Cluster.
    """
    def __init__(__self__, id=None, name=None, resources=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resources and not isinstance(resources, str):
            raise TypeError("Expected argument 'resources' to be a str")
        pulumi.set(__self__, "resources", resources)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def resources(self) -> Optional[str]:
        """
        Resources represents the SyncSets configuration.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetSyncSetResult(GetSyncSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSyncSetResult(
            id=self.id,
            name=self.name,
            resources=self.resources,
            system_data=self.system_data,
            type=self.type)


def get_sync_set(child_resource_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 resource_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSyncSetResult:
    """
    The operation returns properties of a SyncSet.


    :param str child_resource_name: The name of the SyncSet resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the OpenShift cluster resource.
    """
    __args__ = dict()
    __args__['childResourceName'] = child_resource_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:redhatopenshift/v20230701preview:getSyncSet', __args__, opts=opts, typ=GetSyncSetResult).value

    return AwaitableGetSyncSetResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        resources=pulumi.get(__ret__, 'resources'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_sync_set)
def get_sync_set_output(child_resource_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        resource_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSyncSetResult]:
    """
    The operation returns properties of a SyncSet.


    :param str child_resource_name: The name of the SyncSet resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the OpenShift cluster resource.
    """
    ...
