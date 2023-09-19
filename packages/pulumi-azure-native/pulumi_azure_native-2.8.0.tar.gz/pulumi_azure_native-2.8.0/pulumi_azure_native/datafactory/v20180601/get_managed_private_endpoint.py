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
    'GetManagedPrivateEndpointResult',
    'AwaitableGetManagedPrivateEndpointResult',
    'get_managed_private_endpoint',
    'get_managed_private_endpoint_output',
]

@pulumi.output_type
class GetManagedPrivateEndpointResult:
    """
    Managed private endpoint resource type.
    """
    def __init__(__self__, etag=None, id=None, name=None, properties=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Etag identifies change in the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ManagedPrivateEndpointResponse':
        """
        Managed private endpoint properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedPrivateEndpointResult(GetManagedPrivateEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedPrivateEndpointResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_managed_private_endpoint(factory_name: Optional[str] = None,
                                 managed_private_endpoint_name: Optional[str] = None,
                                 managed_virtual_network_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedPrivateEndpointResult:
    """
    Gets a managed private endpoint.


    :param str factory_name: The factory name.
    :param str managed_private_endpoint_name: Managed private endpoint name
    :param str managed_virtual_network_name: Managed virtual network name
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['factoryName'] = factory_name
    __args__['managedPrivateEndpointName'] = managed_private_endpoint_name
    __args__['managedVirtualNetworkName'] = managed_virtual_network_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datafactory/v20180601:getManagedPrivateEndpoint', __args__, opts=opts, typ=GetManagedPrivateEndpointResult).value

    return AwaitableGetManagedPrivateEndpointResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_managed_private_endpoint)
def get_managed_private_endpoint_output(factory_name: Optional[pulumi.Input[str]] = None,
                                        managed_private_endpoint_name: Optional[pulumi.Input[str]] = None,
                                        managed_virtual_network_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedPrivateEndpointResult]:
    """
    Gets a managed private endpoint.


    :param str factory_name: The factory name.
    :param str managed_private_endpoint_name: Managed private endpoint name
    :param str managed_virtual_network_name: Managed virtual network name
    :param str resource_group_name: The resource group name.
    """
    ...
