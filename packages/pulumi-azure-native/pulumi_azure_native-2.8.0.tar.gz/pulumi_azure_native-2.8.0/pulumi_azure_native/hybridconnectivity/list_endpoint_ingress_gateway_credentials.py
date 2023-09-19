# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'ListEndpointIngressGatewayCredentialsResult',
    'AwaitableListEndpointIngressGatewayCredentialsResult',
    'list_endpoint_ingress_gateway_credentials',
    'list_endpoint_ingress_gateway_credentials_output',
]

@pulumi.output_type
class ListEndpointIngressGatewayCredentialsResult:
    """
    The ingress gateway access credentials
    """
    def __init__(__self__, access_key=None, expires_on=None, hostname=None, hybrid_connection_name=None, namespace_name=None, namespace_name_suffix=None, server_id=None, service_configuration_token=None, tenant_id=None):
        if access_key and not isinstance(access_key, str):
            raise TypeError("Expected argument 'access_key' to be a str")
        pulumi.set(__self__, "access_key", access_key)
        if expires_on and not isinstance(expires_on, float):
            raise TypeError("Expected argument 'expires_on' to be a float")
        pulumi.set(__self__, "expires_on", expires_on)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if hybrid_connection_name and not isinstance(hybrid_connection_name, str):
            raise TypeError("Expected argument 'hybrid_connection_name' to be a str")
        pulumi.set(__self__, "hybrid_connection_name", hybrid_connection_name)
        if namespace_name and not isinstance(namespace_name, str):
            raise TypeError("Expected argument 'namespace_name' to be a str")
        pulumi.set(__self__, "namespace_name", namespace_name)
        if namespace_name_suffix and not isinstance(namespace_name_suffix, str):
            raise TypeError("Expected argument 'namespace_name_suffix' to be a str")
        pulumi.set(__self__, "namespace_name_suffix", namespace_name_suffix)
        if server_id and not isinstance(server_id, str):
            raise TypeError("Expected argument 'server_id' to be a str")
        pulumi.set(__self__, "server_id", server_id)
        if service_configuration_token and not isinstance(service_configuration_token, str):
            raise TypeError("Expected argument 'service_configuration_token' to be a str")
        pulumi.set(__self__, "service_configuration_token", service_configuration_token)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> str:
        """
        Access key for hybrid connection.
        """
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[float]:
        """
        The expiration of access key in unix time.
        """
        return pulumi.get(self, "expires_on")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        The ingress hostname.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="hybridConnectionName")
    def hybrid_connection_name(self) -> str:
        """
        Azure Relay hybrid connection name for the resource.
        """
        return pulumi.get(self, "hybrid_connection_name")

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> str:
        """
        The namespace name.
        """
        return pulumi.get(self, "namespace_name")

    @property
    @pulumi.getter(name="namespaceNameSuffix")
    def namespace_name_suffix(self) -> str:
        """
        The suffix domain name of relay namespace.
        """
        return pulumi.get(self, "namespace_name_suffix")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> str:
        """
        The arc ingress gateway server app id.
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="serviceConfigurationToken")
    def service_configuration_token(self) -> Optional[str]:
        """
        The token to access the enabled service.
        """
        return pulumi.get(self, "service_configuration_token")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The target resource home tenant id.
        """
        return pulumi.get(self, "tenant_id")


class AwaitableListEndpointIngressGatewayCredentialsResult(ListEndpointIngressGatewayCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListEndpointIngressGatewayCredentialsResult(
            access_key=self.access_key,
            expires_on=self.expires_on,
            hostname=self.hostname,
            hybrid_connection_name=self.hybrid_connection_name,
            namespace_name=self.namespace_name,
            namespace_name_suffix=self.namespace_name_suffix,
            server_id=self.server_id,
            service_configuration_token=self.service_configuration_token,
            tenant_id=self.tenant_id)


def list_endpoint_ingress_gateway_credentials(endpoint_name: Optional[str] = None,
                                              expiresin: Optional[int] = None,
                                              resource_uri: Optional[str] = None,
                                              service_name: Optional[Union[str, 'ServiceName']] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListEndpointIngressGatewayCredentialsResult:
    """
    Gets the ingress gateway endpoint credentials
    Azure REST API version: 2023-03-15.


    :param str endpoint_name: The endpoint name.
    :param int expiresin: The is how long the endpoint access token is valid (in seconds).
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
    :param Union[str, 'ServiceName'] service_name: The name of the service.
    """
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['expiresin'] = expiresin
    __args__['resourceUri'] = resource_uri
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridconnectivity:listEndpointIngressGatewayCredentials', __args__, opts=opts, typ=ListEndpointIngressGatewayCredentialsResult).value

    return AwaitableListEndpointIngressGatewayCredentialsResult(
        access_key=pulumi.get(__ret__, 'access_key'),
        expires_on=pulumi.get(__ret__, 'expires_on'),
        hostname=pulumi.get(__ret__, 'hostname'),
        hybrid_connection_name=pulumi.get(__ret__, 'hybrid_connection_name'),
        namespace_name=pulumi.get(__ret__, 'namespace_name'),
        namespace_name_suffix=pulumi.get(__ret__, 'namespace_name_suffix'),
        server_id=pulumi.get(__ret__, 'server_id'),
        service_configuration_token=pulumi.get(__ret__, 'service_configuration_token'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'))


@_utilities.lift_output_func(list_endpoint_ingress_gateway_credentials)
def list_endpoint_ingress_gateway_credentials_output(endpoint_name: Optional[pulumi.Input[str]] = None,
                                                     expiresin: Optional[pulumi.Input[Optional[int]]] = None,
                                                     resource_uri: Optional[pulumi.Input[str]] = None,
                                                     service_name: Optional[pulumi.Input[Optional[Union[str, 'ServiceName']]]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListEndpointIngressGatewayCredentialsResult]:
    """
    Gets the ingress gateway endpoint credentials
    Azure REST API version: 2023-03-15.


    :param str endpoint_name: The endpoint name.
    :param int expiresin: The is how long the endpoint access token is valid (in seconds).
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
    :param Union[str, 'ServiceName'] service_name: The name of the service.
    """
    ...
