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
    'ListOnlineEndpointKeysResult',
    'AwaitableListOnlineEndpointKeysResult',
    'list_online_endpoint_keys',
    'list_online_endpoint_keys_output',
]

@pulumi.output_type
class ListOnlineEndpointKeysResult:
    """
    Keys for endpoint authentication.
    """
    def __init__(__self__, primary_key=None, secondary_key=None):
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[str]:
        """
        The primary key.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[str]:
        """
        The secondary key.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListOnlineEndpointKeysResult(ListOnlineEndpointKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListOnlineEndpointKeysResult(
            primary_key=self.primary_key,
            secondary_key=self.secondary_key)


def list_online_endpoint_keys(endpoint_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              workspace_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListOnlineEndpointKeysResult:
    """
    Keys for endpoint authentication.


    :param str endpoint_name: Online Endpoint name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20230601preview:listOnlineEndpointKeys', __args__, opts=opts, typ=ListOnlineEndpointKeysResult).value

    return AwaitableListOnlineEndpointKeysResult(
        primary_key=pulumi.get(__ret__, 'primary_key'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'))


@_utilities.lift_output_func(list_online_endpoint_keys)
def list_online_endpoint_keys_output(endpoint_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     workspace_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListOnlineEndpointKeysResult]:
    """
    Keys for endpoint authentication.


    :param str endpoint_name: Online Endpoint name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
