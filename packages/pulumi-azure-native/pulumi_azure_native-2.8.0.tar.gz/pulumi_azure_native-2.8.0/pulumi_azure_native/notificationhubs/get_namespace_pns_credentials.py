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
    'GetNamespacePnsCredentialsResult',
    'AwaitableGetNamespacePnsCredentialsResult',
    'get_namespace_pns_credentials',
    'get_namespace_pns_credentials_output',
]

@pulumi.output_type
class GetNamespacePnsCredentialsResult:
    """
    Description of a NotificationHub PNS Credentials. This is a response of the POST requests that return namespace or hubs
    PNS credentials.
    """
    def __init__(__self__, id=None, location=None, name=None, properties=None, system_data=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Deprecated - only for compatibility.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.PnsCredentialsResponse':
        """
        Collection of Notification Hub or Notification Hub Namespace PNS credentials.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Deprecated - only for compatibility.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetNamespacePnsCredentialsResult(GetNamespacePnsCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespacePnsCredentialsResult(
            id=self.id,
            location=self.location,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_namespace_pns_credentials(namespace_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespacePnsCredentialsResult:
    """
    Description of a NotificationHub PNS Credentials. This is a response of the POST requests that return namespace or hubs
    PNS credentials.
    Azure REST API version: 2023-01-01-preview.


    :param str namespace_name: Namespace name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:notificationhubs:getNamespacePnsCredentials', __args__, opts=opts, typ=GetNamespacePnsCredentialsResult).value

    return AwaitableGetNamespacePnsCredentialsResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_namespace_pns_credentials)
def get_namespace_pns_credentials_output(namespace_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespacePnsCredentialsResult]:
    """
    Description of a NotificationHub PNS Credentials. This is a response of the POST requests that return namespace or hubs
    PNS credentials.
    Azure REST API version: 2023-01-01-preview.


    :param str namespace_name: Namespace name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
