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
    'ListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult',
    'AwaitableListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult',
    'list_security_advisory_impacted_resource_by_subscription_id_and_event_id',
    'list_security_advisory_impacted_resource_by_subscription_id_and_event_id_output',
]

@pulumi.output_type
class ListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult:
    """
    The List of eventImpactedResources operation response.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The URI to fetch the next page of events. Call ListNext() with this URI to fetch the next page of impacted resource.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.EventImpactedResourceResponse']:
        """
        The list of eventImpactedResources.
        """
        return pulumi.get(self, "value")


class AwaitableListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult(ListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult(
            next_link=self.next_link,
            value=self.value)


def list_security_advisory_impacted_resource_by_subscription_id_and_event_id(event_tracking_id: Optional[str] = None,
                                                                             filter: Optional[str] = None,
                                                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult:
    """
    Lists impacted resources in the subscription by an event (Security Advisory).


    :param str event_tracking_id: Event Id which uniquely identifies ServiceHealth event.
    :param str filter: The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    """
    __args__ = dict()
    __args__['eventTrackingId'] = event_tracking_id
    __args__['filter'] = filter
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:resourcehealth/v20221001preview:listSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventId', __args__, opts=opts, typ=ListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult).value

    return AwaitableListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_security_advisory_impacted_resource_by_subscription_id_and_event_id)
def list_security_advisory_impacted_resource_by_subscription_id_and_event_id_output(event_tracking_id: Optional[pulumi.Input[str]] = None,
                                                                                    filter: Optional[pulumi.Input[Optional[str]]] = None,
                                                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListSecurityAdvisoryImpactedResourceBySubscriptionIdAndEventIdResult]:
    """
    Lists impacted resources in the subscription by an event (Security Advisory).


    :param str event_tracking_id: Event Id which uniquely identifies ServiceHealth event.
    :param str filter: The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    """
    ...
