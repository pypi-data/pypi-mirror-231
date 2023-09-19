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
    'GetServerAzureADOnlyAuthenticationResult',
    'AwaitableGetServerAzureADOnlyAuthenticationResult',
    'get_server_azure_ad_only_authentication',
    'get_server_azure_ad_only_authentication_output',
]

@pulumi.output_type
class GetServerAzureADOnlyAuthenticationResult:
    """
    Azure Active Directory only authentication.
    """
    def __init__(__self__, azure_ad_only_authentication=None, id=None, name=None, type=None):
        if azure_ad_only_authentication and not isinstance(azure_ad_only_authentication, bool):
            raise TypeError("Expected argument 'azure_ad_only_authentication' to be a bool")
        pulumi.set(__self__, "azure_ad_only_authentication", azure_ad_only_authentication)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(self) -> bool:
        """
        Azure Active Directory only Authentication enabled.
        """
        return pulumi.get(self, "azure_ad_only_authentication")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetServerAzureADOnlyAuthenticationResult(GetServerAzureADOnlyAuthenticationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerAzureADOnlyAuthenticationResult(
            azure_ad_only_authentication=self.azure_ad_only_authentication,
            id=self.id,
            name=self.name,
            type=self.type)


def get_server_azure_ad_only_authentication(authentication_name: Optional[str] = None,
                                            resource_group_name: Optional[str] = None,
                                            server_name: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerAzureADOnlyAuthenticationResult:
    """
    Gets a specific Azure Active Directory only authentication property.


    :param str authentication_name: The name of server azure active directory only authentication.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['authenticationName'] = authentication_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20230201preview:getServerAzureADOnlyAuthentication', __args__, opts=opts, typ=GetServerAzureADOnlyAuthenticationResult).value

    return AwaitableGetServerAzureADOnlyAuthenticationResult(
        azure_ad_only_authentication=pulumi.get(__ret__, 'azure_ad_only_authentication'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_server_azure_ad_only_authentication)
def get_server_azure_ad_only_authentication_output(authentication_name: Optional[pulumi.Input[str]] = None,
                                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                                   server_name: Optional[pulumi.Input[str]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerAzureADOnlyAuthenticationResult]:
    """
    Gets a specific Azure Active Directory only authentication property.


    :param str authentication_name: The name of server azure active directory only authentication.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
