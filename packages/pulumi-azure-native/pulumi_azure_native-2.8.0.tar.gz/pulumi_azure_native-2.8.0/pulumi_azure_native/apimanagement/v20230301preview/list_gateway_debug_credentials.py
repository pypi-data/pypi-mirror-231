# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'ListGatewayDebugCredentialsResult',
    'AwaitableListGatewayDebugCredentialsResult',
    'list_gateway_debug_credentials',
    'list_gateway_debug_credentials_output',
]

@pulumi.output_type
class ListGatewayDebugCredentialsResult:
    """
    Gateway debug credentials.
    """
    def __init__(__self__, token=None):
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def token(self) -> Optional[str]:
        """
        Gateway debug token.
        """
        return pulumi.get(self, "token")


class AwaitableListGatewayDebugCredentialsResult(ListGatewayDebugCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListGatewayDebugCredentialsResult(
            token=self.token)


def list_gateway_debug_credentials(api_id: Optional[str] = None,
                                   credentials_expire_after: Optional[str] = None,
                                   gateway_id: Optional[str] = None,
                                   purposes: Optional[Sequence[Union[str, 'GatewayListDebugCredentialsContractPurpose']]] = None,
                                   resource_group_name: Optional[str] = None,
                                   service_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListGatewayDebugCredentialsResult:
    """
    Create new debug credentials for gateway.


    :param str api_id: Full resource Id of an API.
    :param str credentials_expire_after: Credentials expiration in ISO8601 format. Maximum duration of the credentials is PT1H. When property is not specified, them value PT1H is used.
    :param str gateway_id: Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
    :param Sequence[Union[str, 'GatewayListDebugCredentialsContractPurpose']] purposes: Purposes of debug credential.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['credentialsExpireAfter'] = credentials_expire_after
    __args__['gatewayId'] = gateway_id
    __args__['purposes'] = purposes
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230301preview:listGatewayDebugCredentials', __args__, opts=opts, typ=ListGatewayDebugCredentialsResult).value

    return AwaitableListGatewayDebugCredentialsResult(
        token=pulumi.get(__ret__, 'token'))


@_utilities.lift_output_func(list_gateway_debug_credentials)
def list_gateway_debug_credentials_output(api_id: Optional[pulumi.Input[str]] = None,
                                          credentials_expire_after: Optional[pulumi.Input[Optional[str]]] = None,
                                          gateway_id: Optional[pulumi.Input[str]] = None,
                                          purposes: Optional[pulumi.Input[Sequence[Union[str, 'GatewayListDebugCredentialsContractPurpose']]]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          service_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListGatewayDebugCredentialsResult]:
    """
    Create new debug credentials for gateway.


    :param str api_id: Full resource Id of an API.
    :param str credentials_expire_after: Credentials expiration in ISO8601 format. Maximum duration of the credentials is PT1H. When property is not specified, them value PT1H is used.
    :param str gateway_id: Gateway entity identifier. Must be unique in the current API Management service instance. Must not have value 'managed'
    :param Sequence[Union[str, 'GatewayListDebugCredentialsContractPurpose']] purposes: Purposes of debug credential.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
