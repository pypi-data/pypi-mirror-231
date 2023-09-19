# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetSubvolumeResult',
    'AwaitableGetSubvolumeResult',
    'get_subvolume',
    'get_subvolume_output',
]

@pulumi.output_type
class GetSubvolumeResult:
    """
    Subvolume Information properties
    """
    def __init__(__self__, id=None, name=None, parent_path=None, path=None, provisioning_state=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parent_path and not isinstance(parent_path, str):
            raise TypeError("Expected argument 'parent_path' to be a str")
        pulumi.set(__self__, "parent_path", parent_path)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
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
    @pulumi.getter(name="parentPath")
    def parent_path(self) -> Optional[str]:
        """
        parent path to the subvolume
        """
        return pulumi.get(self, "parent_path")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        Path to the subvolume
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

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


class AwaitableGetSubvolumeResult(GetSubvolumeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubvolumeResult(
            id=self.id,
            name=self.name,
            parent_path=self.parent_path,
            path=self.path,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_subvolume(account_name: Optional[str] = None,
                  pool_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  subvolume_name: Optional[str] = None,
                  volume_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubvolumeResult:
    """
    Returns the path associated with the subvolumeName provided
    Azure REST API version: 2022-11-01.


    :param str account_name: The name of the NetApp account
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str subvolume_name: The name of the subvolume.
    :param str volume_name: The name of the volume
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['poolName'] = pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['subvolumeName'] = subvolume_name
    __args__['volumeName'] = volume_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:netapp:getSubvolume', __args__, opts=opts, typ=GetSubvolumeResult).value

    return AwaitableGetSubvolumeResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        parent_path=pulumi.get(__ret__, 'parent_path'),
        path=pulumi.get(__ret__, 'path'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_subvolume)
def get_subvolume_output(account_name: Optional[pulumi.Input[str]] = None,
                         pool_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         subvolume_name: Optional[pulumi.Input[str]] = None,
                         volume_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSubvolumeResult]:
    """
    Returns the path associated with the subvolumeName provided
    Azure REST API version: 2022-11-01.


    :param str account_name: The name of the NetApp account
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str subvolume_name: The name of the subvolume.
    :param str volume_name: The name of the volume
    """
    ...
