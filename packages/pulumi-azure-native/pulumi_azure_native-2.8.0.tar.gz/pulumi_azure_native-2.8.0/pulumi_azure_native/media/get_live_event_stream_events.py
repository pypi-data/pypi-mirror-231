# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetLiveEventStreamEventsResult',
    'AwaitableGetLiveEventStreamEventsResult',
    'get_live_event_stream_events',
    'get_live_event_stream_events_output',
]

@pulumi.output_type
class GetLiveEventStreamEventsResult:
    """
    Get live event stream events result.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.LiveEventStreamEventResponse']]:
        """
        The result of the get live event stream events.
        """
        return pulumi.get(self, "value")


class AwaitableGetLiveEventStreamEventsResult(GetLiveEventStreamEventsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLiveEventStreamEventsResult(
            value=self.value)


def get_live_event_stream_events(account_name: Optional[str] = None,
                                 live_event_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLiveEventStreamEventsResult:
    """
    Get stream events telemetry of a live event.
    Azure REST API version: 2022-11-01.


    :param str account_name: The Media Services account name.
    :param str live_event_name: The name of the live event, maximum length is 32.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['liveEventName'] = live_event_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media:getLiveEventStreamEvents', __args__, opts=opts, typ=GetLiveEventStreamEventsResult).value

    return AwaitableGetLiveEventStreamEventsResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_live_event_stream_events)
def get_live_event_stream_events_output(account_name: Optional[pulumi.Input[str]] = None,
                                        live_event_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLiveEventStreamEventsResult]:
    """
    Get stream events telemetry of a live event.
    Azure REST API version: 2022-11-01.


    :param str account_name: The Media Services account name.
    :param str live_event_name: The name of the live event, maximum length is 32.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    ...
