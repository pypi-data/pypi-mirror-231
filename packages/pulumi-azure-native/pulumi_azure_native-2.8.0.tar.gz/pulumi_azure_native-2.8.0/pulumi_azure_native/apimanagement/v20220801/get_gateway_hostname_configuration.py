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
    'GetGatewayHostnameConfigurationResult',
    'AwaitableGetGatewayHostnameConfigurationResult',
    'get_gateway_hostname_configuration',
    'get_gateway_hostname_configuration_output',
]

@pulumi.output_type
class GetGatewayHostnameConfigurationResult:
    """
    Gateway hostname configuration details.
    """
    def __init__(__self__, certificate_id=None, hostname=None, http2_enabled=None, id=None, name=None, negotiate_client_certificate=None, tls10_enabled=None, tls11_enabled=None, type=None):
        if certificate_id and not isinstance(certificate_id, str):
            raise TypeError("Expected argument 'certificate_id' to be a str")
        pulumi.set(__self__, "certificate_id", certificate_id)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if http2_enabled and not isinstance(http2_enabled, bool):
            raise TypeError("Expected argument 'http2_enabled' to be a bool")
        pulumi.set(__self__, "http2_enabled", http2_enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if negotiate_client_certificate and not isinstance(negotiate_client_certificate, bool):
            raise TypeError("Expected argument 'negotiate_client_certificate' to be a bool")
        pulumi.set(__self__, "negotiate_client_certificate", negotiate_client_certificate)
        if tls10_enabled and not isinstance(tls10_enabled, bool):
            raise TypeError("Expected argument 'tls10_enabled' to be a bool")
        pulumi.set(__self__, "tls10_enabled", tls10_enabled)
        if tls11_enabled and not isinstance(tls11_enabled, bool):
            raise TypeError("Expected argument 'tls11_enabled' to be a bool")
        pulumi.set(__self__, "tls11_enabled", tls11_enabled)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[str]:
        """
        Identifier of Certificate entity that will be used for TLS connection establishment
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        """
        Hostname value. Supports valid domain name, partial or full wildcard
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="http2Enabled")
    def http2_enabled(self) -> Optional[bool]:
        """
        Specifies if HTTP/2.0 is supported
        """
        return pulumi.get(self, "http2_enabled")

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
    @pulumi.getter(name="negotiateClientCertificate")
    def negotiate_client_certificate(self) -> Optional[bool]:
        """
        Determines whether gateway requests client certificate
        """
        return pulumi.get(self, "negotiate_client_certificate")

    @property
    @pulumi.getter(name="tls10Enabled")
    def tls10_enabled(self) -> Optional[bool]:
        """
        Specifies if TLS 1.0 is supported
        """
        return pulumi.get(self, "tls10_enabled")

    @property
    @pulumi.getter(name="tls11Enabled")
    def tls11_enabled(self) -> Optional[bool]:
        """
        Specifies if TLS 1.1 is supported
        """
        return pulumi.get(self, "tls11_enabled")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetGatewayHostnameConfigurationResult(GetGatewayHostnameConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGatewayHostnameConfigurationResult(
            certificate_id=self.certificate_id,
            hostname=self.hostname,
            http2_enabled=self.http2_enabled,
            id=self.id,
            name=self.name,
            negotiate_client_certificate=self.negotiate_client_certificate,
            tls10_enabled=self.tls10_enabled,
            tls11_enabled=self.tls11_enabled,
            type=self.type)


def get_gateway_hostname_configuration(gateway_id: Optional[str] = None,
                                       hc_id: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       service_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGatewayHostnameConfigurationResult:
    """
    Get details of a hostname configuration


    :param str gateway_id: Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
    :param str hc_id: Gateway hostname configuration identifier. Must be unique in the scope of parent Gateway entity.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['gatewayId'] = gateway_id
    __args__['hcId'] = hc_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20220801:getGatewayHostnameConfiguration', __args__, opts=opts, typ=GetGatewayHostnameConfigurationResult).value

    return AwaitableGetGatewayHostnameConfigurationResult(
        certificate_id=pulumi.get(__ret__, 'certificate_id'),
        hostname=pulumi.get(__ret__, 'hostname'),
        http2_enabled=pulumi.get(__ret__, 'http2_enabled'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        negotiate_client_certificate=pulumi.get(__ret__, 'negotiate_client_certificate'),
        tls10_enabled=pulumi.get(__ret__, 'tls10_enabled'),
        tls11_enabled=pulumi.get(__ret__, 'tls11_enabled'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_gateway_hostname_configuration)
def get_gateway_hostname_configuration_output(gateway_id: Optional[pulumi.Input[str]] = None,
                                              hc_id: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              service_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGatewayHostnameConfigurationResult]:
    """
    Get details of a hostname configuration


    :param str gateway_id: Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
    :param str hc_id: Gateway hostname configuration identifier. Must be unique in the scope of parent Gateway entity.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
