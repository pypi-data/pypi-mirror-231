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
from ._inputs import *

__all__ = ['PacketCoreDataPlaneArgs', 'PacketCoreDataPlane']

@pulumi.input_type
class PacketCoreDataPlaneArgs:
    def __init__(__self__, *,
                 packet_core_control_plane_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 user_plane_access_interface: pulumi.Input['InterfacePropertiesArgs'],
                 location: Optional[pulumi.Input[str]] = None,
                 packet_core_data_plane_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PacketCoreDataPlane resource.
        :param pulumi.Input[str] packet_core_control_plane_name: The name of the packet core control plane.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['InterfacePropertiesArgs'] user_plane_access_interface: The user plane interface on the access network. For 5G networks, this is the N3 interface. For 4G networks, this is the S1-U interface.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] packet_core_data_plane_name: The name of the packet core data plane.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "packet_core_control_plane_name", packet_core_control_plane_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "user_plane_access_interface", user_plane_access_interface)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if packet_core_data_plane_name is not None:
            pulumi.set(__self__, "packet_core_data_plane_name", packet_core_data_plane_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="packetCoreControlPlaneName")
    def packet_core_control_plane_name(self) -> pulumi.Input[str]:
        """
        The name of the packet core control plane.
        """
        return pulumi.get(self, "packet_core_control_plane_name")

    @packet_core_control_plane_name.setter
    def packet_core_control_plane_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "packet_core_control_plane_name", value)

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
    @pulumi.getter(name="userPlaneAccessInterface")
    def user_plane_access_interface(self) -> pulumi.Input['InterfacePropertiesArgs']:
        """
        The user plane interface on the access network. For 5G networks, this is the N3 interface. For 4G networks, this is the S1-U interface.
        """
        return pulumi.get(self, "user_plane_access_interface")

    @user_plane_access_interface.setter
    def user_plane_access_interface(self, value: pulumi.Input['InterfacePropertiesArgs']):
        pulumi.set(self, "user_plane_access_interface", value)

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
    @pulumi.getter(name="packetCoreDataPlaneName")
    def packet_core_data_plane_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the packet core data plane.
        """
        return pulumi.get(self, "packet_core_data_plane_name")

    @packet_core_data_plane_name.setter
    def packet_core_data_plane_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "packet_core_data_plane_name", value)

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


class PacketCoreDataPlane(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                 packet_core_data_plane_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_plane_access_interface: Optional[pulumi.Input[pulumi.InputType['InterfacePropertiesArgs']]] = None,
                 __props__=None):
        """
        Packet core data plane resource. Must be created in the same location as its parent packet core control plane.
        Azure REST API version: 2023-06-01. Prior API version in Azure Native 1.x: 2022-04-01-preview

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] packet_core_control_plane_name: The name of the packet core control plane.
        :param pulumi.Input[str] packet_core_data_plane_name: The name of the packet core data plane.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['InterfacePropertiesArgs']] user_plane_access_interface: The user plane interface on the access network. For 5G networks, this is the N3 interface. For 4G networks, this is the S1-U interface.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PacketCoreDataPlaneArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Packet core data plane resource. Must be created in the same location as its parent packet core control plane.
        Azure REST API version: 2023-06-01. Prior API version in Azure Native 1.x: 2022-04-01-preview

        :param str resource_name: The name of the resource.
        :param PacketCoreDataPlaneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PacketCoreDataPlaneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                 packet_core_data_plane_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_plane_access_interface: Optional[pulumi.Input[pulumi.InputType['InterfacePropertiesArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PacketCoreDataPlaneArgs.__new__(PacketCoreDataPlaneArgs)

            __props__.__dict__["location"] = location
            if packet_core_control_plane_name is None and not opts.urn:
                raise TypeError("Missing required property 'packet_core_control_plane_name'")
            __props__.__dict__["packet_core_control_plane_name"] = packet_core_control_plane_name
            __props__.__dict__["packet_core_data_plane_name"] = packet_core_data_plane_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if user_plane_access_interface is None and not opts.urn:
                raise TypeError("Missing required property 'user_plane_access_interface'")
            __props__.__dict__["user_plane_access_interface"] = user_plane_access_interface
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:mobilenetwork/v20220301preview:PacketCoreDataPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20220401preview:PacketCoreDataPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20221101:PacketCoreDataPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230601:PacketCoreDataPlane")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PacketCoreDataPlane, __self__).__init__(
            'azure-native:mobilenetwork:PacketCoreDataPlane',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PacketCoreDataPlane':
        """
        Get an existing PacketCoreDataPlane resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PacketCoreDataPlaneArgs.__new__(PacketCoreDataPlaneArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_plane_access_interface"] = None
        return PacketCoreDataPlane(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the packet core data plane resource.
        """
        return pulumi.get(self, "provisioning_state")

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

    @property
    @pulumi.getter(name="userPlaneAccessInterface")
    def user_plane_access_interface(self) -> pulumi.Output['outputs.InterfacePropertiesResponse']:
        """
        The user plane interface on the access network. For 5G networks, this is the N3 interface. For 4G networks, this is the S1-U interface.
        """
        return pulumi.get(self, "user_plane_access_interface")

