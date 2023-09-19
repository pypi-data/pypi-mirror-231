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
    'GetSecurityPartnerProviderResult',
    'AwaitableGetSecurityPartnerProviderResult',
    'get_security_partner_provider',
    'get_security_partner_provider_output',
]

@pulumi.output_type
class GetSecurityPartnerProviderResult:
    """
    Security Partner Provider resource.
    """
    def __init__(__self__, connection_status=None, etag=None, id=None, location=None, name=None, provisioning_state=None, security_provider_name=None, tags=None, type=None, virtual_hub=None):
        if connection_status and not isinstance(connection_status, str):
            raise TypeError("Expected argument 'connection_status' to be a str")
        pulumi.set(__self__, "connection_status", connection_status)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if security_provider_name and not isinstance(security_provider_name, str):
            raise TypeError("Expected argument 'security_provider_name' to be a str")
        pulumi.set(__self__, "security_provider_name", security_provider_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_hub and not isinstance(virtual_hub, dict):
            raise TypeError("Expected argument 'virtual_hub' to be a dict")
        pulumi.set(__self__, "virtual_hub", virtual_hub)

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> str:
        """
        The connection status with the Security Partner Provider.
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the Security Partner Provider resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="securityProviderName")
    def security_provider_name(self) -> Optional[str]:
        """
        The security provider name.
        """
        return pulumi.get(self, "security_provider_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional['outputs.SubResourceResponse']:
        """
        The virtualHub to which the Security Partner Provider belongs.
        """
        return pulumi.get(self, "virtual_hub")


class AwaitableGetSecurityPartnerProviderResult(GetSecurityPartnerProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityPartnerProviderResult(
            connection_status=self.connection_status,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            security_provider_name=self.security_provider_name,
            tags=self.tags,
            type=self.type,
            virtual_hub=self.virtual_hub)


def get_security_partner_provider(resource_group_name: Optional[str] = None,
                                  security_partner_provider_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityPartnerProviderResult:
    """
    Gets the specified Security Partner Provider.


    :param str resource_group_name: The name of the resource group.
    :param str security_partner_provider_name: The name of the Security Partner Provider.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['securityPartnerProviderName'] = security_partner_provider_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230401:getSecurityPartnerProvider', __args__, opts=opts, typ=GetSecurityPartnerProviderResult).value

    return AwaitableGetSecurityPartnerProviderResult(
        connection_status=pulumi.get(__ret__, 'connection_status'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        security_provider_name=pulumi.get(__ret__, 'security_provider_name'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        virtual_hub=pulumi.get(__ret__, 'virtual_hub'))


@_utilities.lift_output_func(get_security_partner_provider)
def get_security_partner_provider_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                         security_partner_provider_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityPartnerProviderResult]:
    """
    Gets the specified Security Partner Provider.


    :param str resource_group_name: The name of the resource group.
    :param str security_partner_provider_name: The name of the Security Partner Provider.
    """
    ...
