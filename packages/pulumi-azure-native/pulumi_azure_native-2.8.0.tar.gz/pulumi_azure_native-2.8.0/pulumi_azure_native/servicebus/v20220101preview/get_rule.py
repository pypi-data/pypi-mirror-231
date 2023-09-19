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
    'GetRuleResult',
    'AwaitableGetRuleResult',
    'get_rule',
    'get_rule_output',
]

@pulumi.output_type
class GetRuleResult:
    """
    Description of Rule Resource.
    """
    def __init__(__self__, action=None, correlation_filter=None, filter_type=None, id=None, location=None, name=None, sql_filter=None, system_data=None, type=None):
        if action and not isinstance(action, dict):
            raise TypeError("Expected argument 'action' to be a dict")
        pulumi.set(__self__, "action", action)
        if correlation_filter and not isinstance(correlation_filter, dict):
            raise TypeError("Expected argument 'correlation_filter' to be a dict")
        pulumi.set(__self__, "correlation_filter", correlation_filter)
        if filter_type and not isinstance(filter_type, str):
            raise TypeError("Expected argument 'filter_type' to be a str")
        pulumi.set(__self__, "filter_type", filter_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sql_filter and not isinstance(sql_filter, dict):
            raise TypeError("Expected argument 'sql_filter' to be a dict")
        pulumi.set(__self__, "sql_filter", sql_filter)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def action(self) -> Optional['outputs.ActionResponse']:
        """
        Represents the filter actions which are allowed for the transformation of a message that have been matched by a filter expression.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="correlationFilter")
    def correlation_filter(self) -> Optional['outputs.CorrelationFilterResponse']:
        """
        Properties of correlationFilter
        """
        return pulumi.get(self, "correlation_filter")

    @property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> Optional[str]:
        """
        Filter type that is evaluated against a BrokeredMessage.
        """
        return pulumi.get(self, "filter_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sqlFilter")
    def sql_filter(self) -> Optional['outputs.SqlFilterResponse']:
        """
        Properties of sqlFilter
        """
        return pulumi.get(self, "sql_filter")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs"
        """
        return pulumi.get(self, "type")


class AwaitableGetRuleResult(GetRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRuleResult(
            action=self.action,
            correlation_filter=self.correlation_filter,
            filter_type=self.filter_type,
            id=self.id,
            location=self.location,
            name=self.name,
            sql_filter=self.sql_filter,
            system_data=self.system_data,
            type=self.type)


def get_rule(namespace_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             rule_name: Optional[str] = None,
             subscription_name: Optional[str] = None,
             topic_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRuleResult:
    """
    Retrieves the description for the specified rule.


    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    :param str rule_name: The rule name.
    :param str subscription_name: The subscription name.
    :param str topic_name: The topic name.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['ruleName'] = rule_name
    __args__['subscriptionName'] = subscription_name
    __args__['topicName'] = topic_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicebus/v20220101preview:getRule', __args__, opts=opts, typ=GetRuleResult).value

    return AwaitableGetRuleResult(
        action=pulumi.get(__ret__, 'action'),
        correlation_filter=pulumi.get(__ret__, 'correlation_filter'),
        filter_type=pulumi.get(__ret__, 'filter_type'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        sql_filter=pulumi.get(__ret__, 'sql_filter'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_rule)
def get_rule_output(namespace_name: Optional[pulumi.Input[str]] = None,
                    resource_group_name: Optional[pulumi.Input[str]] = None,
                    rule_name: Optional[pulumi.Input[str]] = None,
                    subscription_name: Optional[pulumi.Input[str]] = None,
                    topic_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRuleResult]:
    """
    Retrieves the description for the specified rule.


    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    :param str rule_name: The rule name.
    :param str subscription_name: The subscription name.
    :param str topic_name: The topic name.
    """
    ...
