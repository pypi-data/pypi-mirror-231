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
    'GetAuthorizationAccessPolicyResult',
    'AwaitableGetAuthorizationAccessPolicyResult',
    'get_authorization_access_policy',
    'get_authorization_access_policy_output',
]

@pulumi.output_type
class GetAuthorizationAccessPolicyResult:
    """
    Authorization access policy contract.
    """
    def __init__(__self__, id=None, name=None, object_id=None, tenant_id=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        pulumi.set(__self__, "object_id", object_id)
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
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[str]:
        """
        The Object Id
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The Tenant Id
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAuthorizationAccessPolicyResult(GetAuthorizationAccessPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAuthorizationAccessPolicyResult(
            id=self.id,
            name=self.name,
            object_id=self.object_id,
            tenant_id=self.tenant_id,
            type=self.type)


def get_authorization_access_policy(authorization_access_policy_id: Optional[str] = None,
                                    authorization_id: Optional[str] = None,
                                    authorization_provider_id: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    service_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAuthorizationAccessPolicyResult:
    """
    Gets the details of the authorization access policy specified by its identifier.


    :param str authorization_access_policy_id: Identifier of the authorization access policy.
    :param str authorization_id: Identifier of the authorization.
    :param str authorization_provider_id: Identifier of the authorization provider.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['authorizationAccessPolicyId'] = authorization_access_policy_id
    __args__['authorizationId'] = authorization_id
    __args__['authorizationProviderId'] = authorization_provider_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20220901preview:getAuthorizationAccessPolicy', __args__, opts=opts, typ=GetAuthorizationAccessPolicyResult).value

    return AwaitableGetAuthorizationAccessPolicyResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        object_id=pulumi.get(__ret__, 'object_id'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_authorization_access_policy)
def get_authorization_access_policy_output(authorization_access_policy_id: Optional[pulumi.Input[str]] = None,
                                           authorization_id: Optional[pulumi.Input[str]] = None,
                                           authorization_provider_id: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           service_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAuthorizationAccessPolicyResult]:
    """
    Gets the details of the authorization access policy specified by its identifier.


    :param str authorization_access_policy_id: Identifier of the authorization access policy.
    :param str authorization_id: Identifier of the authorization.
    :param str authorization_provider_id: Identifier of the authorization provider.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
