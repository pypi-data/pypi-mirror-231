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
    'ListEndpointCredentialsResult',
    'AwaitableListEndpointCredentialsResult',
    'list_endpoint_credentials',
    'list_endpoint_credentials_output',
]

@pulumi.output_type
class ListEndpointCredentialsResult:
    """
    The endpoint access for the target resource.
    """
    def __init__(__self__, access_key=None, expires_on=None, hybrid_connection_name=None, namespace_name=None, namespace_name_suffix=None):
        if access_key and not isinstance(access_key, str):
            raise TypeError("Expected argument 'access_key' to be a str")
        pulumi.set(__self__, "access_key", access_key)
        if expires_on and not isinstance(expires_on, float):
            raise TypeError("Expected argument 'expires_on' to be a float")
        pulumi.set(__self__, "expires_on", expires_on)
        if hybrid_connection_name and not isinstance(hybrid_connection_name, str):
            raise TypeError("Expected argument 'hybrid_connection_name' to be a str")
        pulumi.set(__self__, "hybrid_connection_name", hybrid_connection_name)
        if namespace_name and not isinstance(namespace_name, str):
            raise TypeError("Expected argument 'namespace_name' to be a str")
        pulumi.set(__self__, "namespace_name", namespace_name)
        if namespace_name_suffix and not isinstance(namespace_name_suffix, str):
            raise TypeError("Expected argument 'namespace_name_suffix' to be a str")
        pulumi.set(__self__, "namespace_name_suffix", namespace_name_suffix)

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


class AwaitableListEndpointCredentialsResult(ListEndpointCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListEndpointCredentialsResult(
            access_key=self.access_key,
            expires_on=self.expires_on,
            hybrid_connection_name=self.hybrid_connection_name,
            namespace_name=self.namespace_name,
            namespace_name_suffix=self.namespace_name_suffix)


def list_endpoint_credentials(endpoint_name: Optional[str] = None,
                              expiresin: Optional[int] = None,
                              resource_uri: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListEndpointCredentialsResult:
    """
    Gets the endpoint access credentials to the resource.


    :param str endpoint_name: The endpoint name.
    :param int expiresin: The is how long the endpoint access token is valid (in seconds).
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
    """
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['expiresin'] = expiresin
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridconnectivity/v20220501preview:listEndpointCredentials', __args__, opts=opts, typ=ListEndpointCredentialsResult).value

    return AwaitableListEndpointCredentialsResult(
        access_key=pulumi.get(__ret__, 'access_key'),
        expires_on=pulumi.get(__ret__, 'expires_on'),
        hybrid_connection_name=pulumi.get(__ret__, 'hybrid_connection_name'),
        namespace_name=pulumi.get(__ret__, 'namespace_name'),
        namespace_name_suffix=pulumi.get(__ret__, 'namespace_name_suffix'))


@_utilities.lift_output_func(list_endpoint_credentials)
def list_endpoint_credentials_output(endpoint_name: Optional[pulumi.Input[str]] = None,
                                     expiresin: Optional[pulumi.Input[Optional[int]]] = None,
                                     resource_uri: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListEndpointCredentialsResult]:
    """
    Gets the endpoint access credentials to the resource.


    :param str endpoint_name: The endpoint name.
    :param int expiresin: The is how long the endpoint access token is valid (in seconds).
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
    """
    ...
