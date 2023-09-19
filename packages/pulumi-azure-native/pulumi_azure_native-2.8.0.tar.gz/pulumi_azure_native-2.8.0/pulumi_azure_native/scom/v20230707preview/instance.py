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
from ._enums import *
from ._inputs import *

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['ManagedIdentityArgs']] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['MonitoringInstancePropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validation_mode: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['ManagedIdentityArgs'] identity: The Azure Active Directory identity of the SCOM instance
        :param pulumi.Input[str] instance_name: Name of the Azure Monitor Operations Manager Managed Instance (SCOM MI)
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['MonitoringInstancePropertiesArgs'] properties: The properties of a SCOM instance resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] validation_mode: Validation mode for the SCOM managed instance
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if instance_name is not None:
            pulumi.set(__self__, "instance_name", instance_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if validation_mode is not None:
            pulumi.set(__self__, "validation_mode", validation_mode)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedIdentityArgs']]:
        """
        The Azure Active Directory identity of the SCOM instance
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Azure Monitor Operations Manager Managed Instance (SCOM MI)
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['MonitoringInstancePropertiesArgs']]:
        """
        The properties of a SCOM instance resource
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['MonitoringInstancePropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="validationMode")
    def validation_mode(self) -> Optional[pulumi.Input[bool]]:
        """
        Validation mode for the SCOM managed instance
        """
        return pulumi.get(self, "validation_mode")

    @validation_mode.setter
    def validation_mode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "validation_mode", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedIdentityArgs']]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['MonitoringInstancePropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validation_mode: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        A SCOM instance resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ManagedIdentityArgs']] identity: The Azure Active Directory identity of the SCOM instance
        :param pulumi.Input[str] instance_name: Name of the Azure Monitor Operations Manager Managed Instance (SCOM MI)
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['MonitoringInstancePropertiesArgs']] properties: The properties of a SCOM instance resource
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] validation_mode: Validation mode for the SCOM managed instance
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A SCOM instance resource

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedIdentityArgs']]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['MonitoringInstancePropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validation_mode: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceArgs.__new__(InstanceArgs)

            __props__.__dict__["identity"] = identity
            __props__.__dict__["instance_name"] = instance_name
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["validation_mode"] = validation_mode
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:scom:Instance")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Instance, __self__).__init__(
            'azure-native:scom/v20230707preview:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceArgs.__new__(InstanceArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedIdentityResponse']]:
        """
        The Azure Active Directory identity of the SCOM instance
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.MonitoringInstancePropertiesResponse']:
        """
        The properties of a SCOM instance resource
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

