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
from ._enums import *
from ._inputs import *

__all__ = ['TriggerArgs', 'Trigger']

@pulumi.input_type
class TriggerArgs:
    def __init__(__self__, *,
                 factory_name: pulumi.Input[str],
                 properties: pulumi.Input[Union['BlobEventsTriggerArgs', 'BlobTriggerArgs', 'ChainingTriggerArgs', 'CustomEventsTriggerArgs', 'MultiplePipelineTriggerArgs', 'RerunTumblingWindowTriggerArgs', 'ScheduleTriggerArgs', 'TumblingWindowTriggerArgs']],
                 resource_group_name: pulumi.Input[str],
                 trigger_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Trigger resource.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[Union['BlobEventsTriggerArgs', 'BlobTriggerArgs', 'ChainingTriggerArgs', 'CustomEventsTriggerArgs', 'MultiplePipelineTriggerArgs', 'RerunTumblingWindowTriggerArgs', 'ScheduleTriggerArgs', 'TumblingWindowTriggerArgs']] properties: Properties of the trigger.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] trigger_name: The trigger name.
        """
        pulumi.set(__self__, "factory_name", factory_name)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if trigger_name is not None:
            pulumi.set(__self__, "trigger_name", trigger_name)

    @property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[str]:
        """
        The factory name.
        """
        return pulumi.get(self, "factory_name")

    @factory_name.setter
    def factory_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "factory_name", value)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union['BlobEventsTriggerArgs', 'BlobTriggerArgs', 'ChainingTriggerArgs', 'CustomEventsTriggerArgs', 'MultiplePipelineTriggerArgs', 'RerunTumblingWindowTriggerArgs', 'ScheduleTriggerArgs', 'TumblingWindowTriggerArgs']]:
        """
        Properties of the trigger.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input[Union['BlobEventsTriggerArgs', 'BlobTriggerArgs', 'ChainingTriggerArgs', 'CustomEventsTriggerArgs', 'MultiplePipelineTriggerArgs', 'RerunTumblingWindowTriggerArgs', 'ScheduleTriggerArgs', 'TumblingWindowTriggerArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="triggerName")
    def trigger_name(self) -> Optional[pulumi.Input[str]]:
        """
        The trigger name.
        """
        return pulumi.get(self, "trigger_name")

    @trigger_name.setter
    def trigger_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trigger_name", value)


class Trigger(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['BlobEventsTriggerArgs'], pulumi.InputType['BlobTriggerArgs'], pulumi.InputType['ChainingTriggerArgs'], pulumi.InputType['CustomEventsTriggerArgs'], pulumi.InputType['MultiplePipelineTriggerArgs'], pulumi.InputType['RerunTumblingWindowTriggerArgs'], pulumi.InputType['ScheduleTriggerArgs'], pulumi.InputType['TumblingWindowTriggerArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 trigger_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Trigger resource type.
        Azure REST API version: 2018-06-01. Prior API version in Azure Native 1.x: 2018-06-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[Union[pulumi.InputType['BlobEventsTriggerArgs'], pulumi.InputType['BlobTriggerArgs'], pulumi.InputType['ChainingTriggerArgs'], pulumi.InputType['CustomEventsTriggerArgs'], pulumi.InputType['MultiplePipelineTriggerArgs'], pulumi.InputType['RerunTumblingWindowTriggerArgs'], pulumi.InputType['ScheduleTriggerArgs'], pulumi.InputType['TumblingWindowTriggerArgs']]] properties: Properties of the trigger.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] trigger_name: The trigger name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TriggerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Trigger resource type.
        Azure REST API version: 2018-06-01. Prior API version in Azure Native 1.x: 2018-06-01

        :param str resource_name: The name of the resource.
        :param TriggerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TriggerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['BlobEventsTriggerArgs'], pulumi.InputType['BlobTriggerArgs'], pulumi.InputType['ChainingTriggerArgs'], pulumi.InputType['CustomEventsTriggerArgs'], pulumi.InputType['MultiplePipelineTriggerArgs'], pulumi.InputType['RerunTumblingWindowTriggerArgs'], pulumi.InputType['ScheduleTriggerArgs'], pulumi.InputType['TumblingWindowTriggerArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 trigger_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TriggerArgs.__new__(TriggerArgs)

            if factory_name is None and not opts.urn:
                raise TypeError("Missing required property 'factory_name'")
            __props__.__dict__["factory_name"] = factory_name
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["trigger_name"] = trigger_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datafactory/v20170901preview:Trigger"), pulumi.Alias(type_="azure-native:datafactory/v20180601:Trigger")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Trigger, __self__).__init__(
            'azure-native:datafactory:Trigger',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Trigger':
        """
        Get an existing Trigger resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TriggerArgs.__new__(TriggerArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return Trigger(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Etag identifies change in the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        Properties of the trigger.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

