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
    'GetDppResourceGuardProxyResult',
    'AwaitableGetDppResourceGuardProxyResult',
    'get_dpp_resource_guard_proxy',
    'get_dpp_resource_guard_proxy_output',
]

@pulumi.output_type
class GetDppResourceGuardProxyResult:
    """
    ResourceGuardProxyBaseResource object, used for response and request bodies for ResourceGuardProxy APIs
    """
    def __init__(__self__, id=None, name=None, properties=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
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
        Resource Id represents the complete path to the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name associated with the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ResourceGuardProxyBaseResponse':
        """
        ResourceGuardProxyBaseResource properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/...
        """
        return pulumi.get(self, "type")


class AwaitableGetDppResourceGuardProxyResult(GetDppResourceGuardProxyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDppResourceGuardProxyResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_dpp_resource_guard_proxy(resource_group_name: Optional[str] = None,
                                 resource_guard_proxy_name: Optional[str] = None,
                                 vault_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDppResourceGuardProxyResult:
    """
    ResourceGuardProxyBaseResource object, used for response and request bodies for ResourceGuardProxy APIs


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_guard_proxy_name: name of the resource guard proxy
    :param str vault_name: The name of the backup vault.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceGuardProxyName'] = resource_guard_proxy_name
    __args__['vaultName'] = vault_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dataprotection/v20230101:getDppResourceGuardProxy', __args__, opts=opts, typ=GetDppResourceGuardProxyResult).value

    return AwaitableGetDppResourceGuardProxyResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_dpp_resource_guard_proxy)
def get_dpp_resource_guard_proxy_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                        resource_guard_proxy_name: Optional[pulumi.Input[str]] = None,
                                        vault_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDppResourceGuardProxyResult]:
    """
    ResourceGuardProxyBaseResource object, used for response and request bodies for ResourceGuardProxy APIs


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_guard_proxy_name: name of the resource guard proxy
    :param str vault_name: The name of the backup vault.
    """
    ...
