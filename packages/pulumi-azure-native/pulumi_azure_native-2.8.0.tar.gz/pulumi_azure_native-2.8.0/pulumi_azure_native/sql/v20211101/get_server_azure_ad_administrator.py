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
    'GetServerAzureADAdministratorResult',
    'AwaitableGetServerAzureADAdministratorResult',
    'get_server_azure_ad_administrator',
    'get_server_azure_ad_administrator_output',
]

@pulumi.output_type
class GetServerAzureADAdministratorResult:
    """
    Azure Active Directory administrator.
    """
    def __init__(__self__, administrator_type=None, azure_ad_only_authentication=None, id=None, login=None, name=None, sid=None, tenant_id=None, type=None):
        if administrator_type and not isinstance(administrator_type, str):
            raise TypeError("Expected argument 'administrator_type' to be a str")
        pulumi.set(__self__, "administrator_type", administrator_type)
        if azure_ad_only_authentication and not isinstance(azure_ad_only_authentication, bool):
            raise TypeError("Expected argument 'azure_ad_only_authentication' to be a bool")
        pulumi.set(__self__, "azure_ad_only_authentication", azure_ad_only_authentication)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if login and not isinstance(login, str):
            raise TypeError("Expected argument 'login' to be a str")
        pulumi.set(__self__, "login", login)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sid and not isinstance(sid, str):
            raise TypeError("Expected argument 'sid' to be a str")
        pulumi.set(__self__, "sid", sid)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> str:
        """
        Type of the sever administrator.
        """
        return pulumi.get(self, "administrator_type")

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
    def login(self) -> str:
        """
        Login name of the server administrator.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sid(self) -> str:
        """
        SID (object ID) of the server administrator.
        """
        return pulumi.get(self, "sid")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        Tenant ID of the administrator.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetServerAzureADAdministratorResult(GetServerAzureADAdministratorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerAzureADAdministratorResult(
            administrator_type=self.administrator_type,
            azure_ad_only_authentication=self.azure_ad_only_authentication,
            id=self.id,
            login=self.login,
            name=self.name,
            sid=self.sid,
            tenant_id=self.tenant_id,
            type=self.type)


def get_server_azure_ad_administrator(administrator_name: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      server_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerAzureADAdministratorResult:
    """
    Gets a Azure Active Directory administrator.


    :param str administrator_name: The name of server active directory administrator.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['administratorName'] = administrator_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20211101:getServerAzureADAdministrator', __args__, opts=opts, typ=GetServerAzureADAdministratorResult).value

    return AwaitableGetServerAzureADAdministratorResult(
        administrator_type=pulumi.get(__ret__, 'administrator_type'),
        azure_ad_only_authentication=pulumi.get(__ret__, 'azure_ad_only_authentication'),
        id=pulumi.get(__ret__, 'id'),
        login=pulumi.get(__ret__, 'login'),
        name=pulumi.get(__ret__, 'name'),
        sid=pulumi.get(__ret__, 'sid'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_server_azure_ad_administrator)
def get_server_azure_ad_administrator_output(administrator_name: Optional[pulumi.Input[str]] = None,
                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                             server_name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerAzureADAdministratorResult]:
    """
    Gets a Azure Active Directory administrator.


    :param str administrator_name: The name of server active directory administrator.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
