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
    'GetNamespaceTopicResult',
    'AwaitableGetNamespaceTopicResult',
    'get_namespace_topic',
    'get_namespace_topic_output',
]

@pulumi.output_type
class GetNamespaceTopicResult:
    """
    Namespace topic details.
    """
    def __init__(__self__, event_retention_in_days=None, id=None, input_schema=None, name=None, provisioning_state=None, publisher_type=None, system_data=None, type=None):
        if event_retention_in_days and not isinstance(event_retention_in_days, int):
            raise TypeError("Expected argument 'event_retention_in_days' to be a int")
        pulumi.set(__self__, "event_retention_in_days", event_retention_in_days)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if input_schema and not isinstance(input_schema, str):
            raise TypeError("Expected argument 'input_schema' to be a str")
        pulumi.set(__self__, "input_schema", input_schema)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if publisher_type and not isinstance(publisher_type, str):
            raise TypeError("Expected argument 'publisher_type' to be a str")
        pulumi.set(__self__, "publisher_type", publisher_type)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eventRetentionInDays")
    def event_retention_in_days(self) -> Optional[int]:
        """
        Event retention for the namespace topic expressed in days. The property default value is 1 day.
        Min event retention duration value is 1 day and max event retention duration value is 1 day.
        """
        return pulumi.get(self, "event_retention_in_days")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> Optional[str]:
        """
        This determines the format that is expected for incoming events published to the topic.
        """
        return pulumi.get(self, "input_schema")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the namespace topic.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publisherType")
    def publisher_type(self) -> Optional[str]:
        """
        Publisher type of the namespace topic.
        """
        return pulumi.get(self, "publisher_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to namespace topic resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetNamespaceTopicResult(GetNamespaceTopicResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceTopicResult(
            event_retention_in_days=self.event_retention_in_days,
            id=self.id,
            input_schema=self.input_schema,
            name=self.name,
            provisioning_state=self.provisioning_state,
            publisher_type=self.publisher_type,
            system_data=self.system_data,
            type=self.type)


def get_namespace_topic(namespace_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        topic_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceTopicResult:
    """
    Get properties of a namespace topic.


    :param str namespace_name: Name of the namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    :param str topic_name: Name of the namespace topic.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['topicName'] = topic_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid/v20230601preview:getNamespaceTopic', __args__, opts=opts, typ=GetNamespaceTopicResult).value

    return AwaitableGetNamespaceTopicResult(
        event_retention_in_days=pulumi.get(__ret__, 'event_retention_in_days'),
        id=pulumi.get(__ret__, 'id'),
        input_schema=pulumi.get(__ret__, 'input_schema'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        publisher_type=pulumi.get(__ret__, 'publisher_type'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_namespace_topic)
def get_namespace_topic_output(namespace_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               topic_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceTopicResult]:
    """
    Get properties of a namespace topic.


    :param str namespace_name: Name of the namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    :param str topic_name: Name of the namespace topic.
    """
    ...
