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
    'GetDomainTopicEventSubscriptionDeliveryAttributesResult',
    'AwaitableGetDomainTopicEventSubscriptionDeliveryAttributesResult',
    'get_domain_topic_event_subscription_delivery_attributes',
    'get_domain_topic_event_subscription_delivery_attributes_output',
]

@pulumi.output_type
class GetDomainTopicEventSubscriptionDeliveryAttributesResult:
    """
    Result of the Get delivery attributes operation.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence[Any]]:
        """
        A collection of DeliveryAttributeMapping
        """
        return pulumi.get(self, "value")


class AwaitableGetDomainTopicEventSubscriptionDeliveryAttributesResult(GetDomainTopicEventSubscriptionDeliveryAttributesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainTopicEventSubscriptionDeliveryAttributesResult(
            value=self.value)


def get_domain_topic_event_subscription_delivery_attributes(domain_name: Optional[str] = None,
                                                            event_subscription_name: Optional[str] = None,
                                                            resource_group_name: Optional[str] = None,
                                                            topic_name: Optional[str] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainTopicEventSubscriptionDeliveryAttributesResult:
    """
    Get all delivery attributes for an event subscription for domain topic.
    Azure REST API version: 2022-06-15.


    :param str domain_name: Name of the top level domain.
    :param str event_subscription_name: Name of the event subscription.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    :param str topic_name: Name of the domain topic.
    """
    __args__ = dict()
    __args__['domainName'] = domain_name
    __args__['eventSubscriptionName'] = event_subscription_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['topicName'] = topic_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid:getDomainTopicEventSubscriptionDeliveryAttributes', __args__, opts=opts, typ=GetDomainTopicEventSubscriptionDeliveryAttributesResult).value

    return AwaitableGetDomainTopicEventSubscriptionDeliveryAttributesResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_domain_topic_event_subscription_delivery_attributes)
def get_domain_topic_event_subscription_delivery_attributes_output(domain_name: Optional[pulumi.Input[str]] = None,
                                                                   event_subscription_name: Optional[pulumi.Input[str]] = None,
                                                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                                                   topic_name: Optional[pulumi.Input[str]] = None,
                                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainTopicEventSubscriptionDeliveryAttributesResult]:
    """
    Get all delivery attributes for an event subscription for domain topic.
    Azure REST API version: 2022-06-15.


    :param str domain_name: Name of the top level domain.
    :param str event_subscription_name: Name of the event subscription.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    :param str topic_name: Name of the domain topic.
    """
    ...
