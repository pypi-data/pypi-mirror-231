# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetAccessPolicyResult',
    'AwaitableGetAccessPolicyResult',
    'get_access_policy',
    'get_access_policy_output',
]

@pulumi.output_type
class GetAccessPolicyResult:
    """
    Response to get/put access policy.
    """
    def __init__(__self__, id=None, name=None, permissions=None, provisioning_state=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions and not isinstance(permissions, str):
            raise TypeError("Expected argument 'permissions' to be a str")
        pulumi.set(__self__, "permissions", permissions)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
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
    def permissions(self) -> str:
        """
        Permissions for the access policy. Learn how to configure permissions at https://aka.ms/redis/AADPreRequisites
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of access policy
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAccessPolicyResult(GetAccessPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessPolicyResult(
            id=self.id,
            name=self.name,
            permissions=self.permissions,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_access_policy(access_policy_name: Optional[str] = None,
                      cache_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessPolicyResult:
    """
    Gets the detailed information about an access policy of a redis cache


    :param str access_policy_name: The name of the access policy that is being added to the Redis cache.
    :param str cache_name: The name of the Redis cache.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accessPolicyName'] = access_policy_name
    __args__['cacheName'] = cache_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cache/v20230501preview:getAccessPolicy', __args__, opts=opts, typ=GetAccessPolicyResult).value

    return AwaitableGetAccessPolicyResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        permissions=pulumi.get(__ret__, 'permissions'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_access_policy)
def get_access_policy_output(access_policy_name: Optional[pulumi.Input[str]] = None,
                             cache_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessPolicyResult]:
    """
    Gets the detailed information about an access policy of a redis cache


    :param str access_policy_name: The name of the access policy that is being added to the Redis cache.
    :param str cache_name: The name of the Redis cache.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
