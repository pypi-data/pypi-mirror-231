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
    'GetAuthorizationLoginLinkPostResult',
    'AwaitableGetAuthorizationLoginLinkPostResult',
    'get_authorization_login_link_post',
    'get_authorization_login_link_post_output',
]

@pulumi.output_type
class GetAuthorizationLoginLinkPostResult:
    """
    Authorization login response contract.
    """
    def __init__(__self__, login_link=None):
        if login_link and not isinstance(login_link, str):
            raise TypeError("Expected argument 'login_link' to be a str")
        pulumi.set(__self__, "login_link", login_link)

    @property
    @pulumi.getter(name="loginLink")
    def login_link(self) -> Optional[str]:
        """
        The login link
        """
        return pulumi.get(self, "login_link")


class AwaitableGetAuthorizationLoginLinkPostResult(GetAuthorizationLoginLinkPostResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAuthorizationLoginLinkPostResult(
            login_link=self.login_link)


def get_authorization_login_link_post(authorization_id: Optional[str] = None,
                                      authorization_provider_id: Optional[str] = None,
                                      post_login_redirect_url: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      service_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAuthorizationLoginLinkPostResult:
    """
    Gets authorization login links.


    :param str authorization_id: Identifier of the authorization.
    :param str authorization_provider_id: Identifier of the authorization provider.
    :param str post_login_redirect_url: The redirect URL after login has completed.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['authorizationId'] = authorization_id
    __args__['authorizationProviderId'] = authorization_provider_id
    __args__['postLoginRedirectUrl'] = post_login_redirect_url
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230301preview:getAuthorizationLoginLinkPost', __args__, opts=opts, typ=GetAuthorizationLoginLinkPostResult).value

    return AwaitableGetAuthorizationLoginLinkPostResult(
        login_link=pulumi.get(__ret__, 'login_link'))


@_utilities.lift_output_func(get_authorization_login_link_post)
def get_authorization_login_link_post_output(authorization_id: Optional[pulumi.Input[str]] = None,
                                             authorization_provider_id: Optional[pulumi.Input[str]] = None,
                                             post_login_redirect_url: Optional[pulumi.Input[Optional[str]]] = None,
                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                             service_name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAuthorizationLoginLinkPostResult]:
    """
    Gets authorization login links.


    :param str authorization_id: Identifier of the authorization.
    :param str authorization_provider_id: Identifier of the authorization provider.
    :param str post_login_redirect_url: The redirect URL after login has completed.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
