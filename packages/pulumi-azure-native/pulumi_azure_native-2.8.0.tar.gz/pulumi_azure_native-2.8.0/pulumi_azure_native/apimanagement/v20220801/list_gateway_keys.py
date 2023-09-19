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
    'ListGatewayKeysResult',
    'AwaitableListGatewayKeysResult',
    'list_gateway_keys',
    'list_gateway_keys_output',
]

@pulumi.output_type
class ListGatewayKeysResult:
    """
    Gateway authentication keys.
    """
    def __init__(__self__, primary=None, secondary=None):
        if primary and not isinstance(primary, str):
            raise TypeError("Expected argument 'primary' to be a str")
        pulumi.set(__self__, "primary", primary)
        if secondary and not isinstance(secondary, str):
            raise TypeError("Expected argument 'secondary' to be a str")
        pulumi.set(__self__, "secondary", secondary)

    @property
    @pulumi.getter
    def primary(self) -> Optional[str]:
        """
        Primary gateway key.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def secondary(self) -> Optional[str]:
        """
        Secondary gateway key.
        """
        return pulumi.get(self, "secondary")


class AwaitableListGatewayKeysResult(ListGatewayKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListGatewayKeysResult(
            primary=self.primary,
            secondary=self.secondary)


def list_gateway_keys(gateway_id: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      service_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListGatewayKeysResult:
    """
    Retrieves gateway keys.


    :param str gateway_id: Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['gatewayId'] = gateway_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20220801:listGatewayKeys', __args__, opts=opts, typ=ListGatewayKeysResult).value

    return AwaitableListGatewayKeysResult(
        primary=pulumi.get(__ret__, 'primary'),
        secondary=pulumi.get(__ret__, 'secondary'))


@_utilities.lift_output_func(list_gateway_keys)
def list_gateway_keys_output(gateway_id: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             service_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListGatewayKeysResult]:
    """
    Retrieves gateway keys.


    :param str gateway_id: Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
