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

__all__ = ['OnPremiseSensorArgs', 'OnPremiseSensor']

@pulumi.input_type
class OnPremiseSensorArgs:
    def __init__(__self__, *,
                 on_premise_sensor_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OnPremiseSensor resource.
        :param pulumi.Input[str] on_premise_sensor_name: Name of the on-premise IoT sensor
        """
        if on_premise_sensor_name is not None:
            pulumi.set(__self__, "on_premise_sensor_name", on_premise_sensor_name)

    @property
    @pulumi.getter(name="onPremiseSensorName")
    def on_premise_sensor_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the on-premise IoT sensor
        """
        return pulumi.get(self, "on_premise_sensor_name")

    @on_premise_sensor_name.setter
    def on_premise_sensor_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "on_premise_sensor_name", value)


class OnPremiseSensor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 on_premise_sensor_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        On-premise IoT sensor

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] on_premise_sensor_name: Name of the on-premise IoT sensor
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[OnPremiseSensorArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        On-premise IoT sensor

        :param str resource_name: The name of the resource.
        :param OnPremiseSensorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OnPremiseSensorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 on_premise_sensor_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OnPremiseSensorArgs.__new__(OnPremiseSensorArgs)

            __props__.__dict__["on_premise_sensor_name"] = on_premise_sensor_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:iotsecurity:OnPremiseSensor")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OnPremiseSensor, __self__).__init__(
            'azure-native:iotsecurity/v20210201preview:OnPremiseSensor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OnPremiseSensor':
        """
        Get an existing OnPremiseSensor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OnPremiseSensorArgs.__new__(OnPremiseSensorArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return OnPremiseSensor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

