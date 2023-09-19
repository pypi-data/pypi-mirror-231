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
    'GetPolicyResult',
    'AwaitableGetPolicyResult',
    'get_policy',
    'get_policy_output',
]

@pulumi.output_type
class GetPolicyResult:
    """
    Policy Contract details.
    """
    def __init__(__self__, format=None, id=None, name=None, type=None, value=None):
        if format and not isinstance(format, str):
            raise TypeError("Expected argument 'format' to be a str")
        pulumi.set(__self__, "format", format)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[str]:
        """
        Format of the policyContent.
        """
        return pulumi.get(self, "format")

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
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Contents of the Policy as defined by the format.
        """
        return pulumi.get(self, "value")


class AwaitableGetPolicyResult(GetPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyResult(
            format=self.format,
            id=self.id,
            name=self.name,
            type=self.type,
            value=self.value)


def get_policy(format: Optional[str] = None,
               policy_id: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               service_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyResult:
    """
    Get the Global policy definition of the Api Management service.


    :param str format: Policy Export Format.
    :param str policy_id: The identifier of the Policy.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['format'] = format
    __args__['policyId'] = policy_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230301preview:getPolicy', __args__, opts=opts, typ=GetPolicyResult).value

    return AwaitableGetPolicyResult(
        format=pulumi.get(__ret__, 'format'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_policy)
def get_policy_output(format: Optional[pulumi.Input[Optional[str]]] = None,
                      policy_id: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      service_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPolicyResult]:
    """
    Get the Global policy definition of the Api Management service.


    :param str format: Policy Export Format.
    :param str policy_id: The identifier of the Policy.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
