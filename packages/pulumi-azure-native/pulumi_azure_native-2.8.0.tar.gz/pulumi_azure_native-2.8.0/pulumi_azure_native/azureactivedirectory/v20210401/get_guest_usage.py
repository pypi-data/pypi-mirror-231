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
    'GetGuestUsageResult',
    'AwaitableGetGuestUsageResult',
    'get_guest_usage',
    'get_guest_usage_output',
]

@pulumi.output_type
class GetGuestUsageResult:
    """
    Guest Usages Resource
    """
    def __init__(__self__, id=None, location=None, name=None, system_data=None, tags=None, tenant_id=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        An identifier that represents the Guest Usages resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Location of the Guest Usages resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Guest Usages resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Key-value pairs of additional resource provisioning properties.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        An identifier for the tenant for which the resource is being created
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the Guest Usages resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetGuestUsageResult(GetGuestUsageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGuestUsageResult(
            id=self.id,
            location=self.location,
            name=self.name,
            system_data=self.system_data,
            tags=self.tags,
            tenant_id=self.tenant_id,
            type=self.type)


def get_guest_usage(resource_group_name: Optional[str] = None,
                    resource_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGuestUsageResult:
    """
    Gets a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider


    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The initial domain name of the Azure AD B2C tenant.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azureactivedirectory/v20210401:getGuestUsage', __args__, opts=opts, typ=GetGuestUsageResult).value

    return AwaitableGetGuestUsageResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_guest_usage)
def get_guest_usage_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                           resource_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGuestUsageResult]:
    """
    Gets a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider


    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The initial domain name of the Azure AD B2C tenant.
    """
    ...
