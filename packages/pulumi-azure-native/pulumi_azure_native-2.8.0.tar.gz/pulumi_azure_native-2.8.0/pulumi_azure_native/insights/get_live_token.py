# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetLiveTokenResult',
    'AwaitableGetLiveTokenResult',
    'get_live_token',
    'get_live_token_output',
]

@pulumi.output_type
class GetLiveTokenResult:
    """
    The response to a live token query.
    """
    def __init__(__self__, live_token=None):
        if live_token and not isinstance(live_token, str):
            raise TypeError("Expected argument 'live_token' to be a str")
        pulumi.set(__self__, "live_token", live_token)

    @property
    @pulumi.getter(name="liveToken")
    def live_token(self) -> str:
        """
        JWT token for accessing live metrics stream data.
        """
        return pulumi.get(self, "live_token")


class AwaitableGetLiveTokenResult(GetLiveTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLiveTokenResult(
            live_token=self.live_token)


def get_live_token(resource_uri: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLiveTokenResult:
    """
    **Gets an access token for live metrics stream data.**
    Azure REST API version: 2021-10-14.


    :param str resource_uri: The identifier of the resource.
    """
    __args__ = dict()
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights:getLiveToken', __args__, opts=opts, typ=GetLiveTokenResult).value

    return AwaitableGetLiveTokenResult(
        live_token=pulumi.get(__ret__, 'live_token'))


@_utilities.lift_output_func(get_live_token)
def get_live_token_output(resource_uri: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLiveTokenResult]:
    """
    **Gets an access token for live metrics stream data.**
    Azure REST API version: 2021-10-14.


    :param str resource_uri: The identifier of the resource.
    """
    ...
