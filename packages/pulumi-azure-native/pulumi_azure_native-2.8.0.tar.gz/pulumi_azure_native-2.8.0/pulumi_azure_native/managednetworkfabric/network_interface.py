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

__all__ = ['NetworkInterfaceArgs', 'NetworkInterface']

@pulumi.input_type
class NetworkInterfaceArgs:
    def __init__(__self__, *,
                 network_device_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 annotation: Optional[pulumi.Input[str]] = None,
                 network_interface_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NetworkInterface resource.
        :param pulumi.Input[str] network_device_name: Name of the NetworkDevice
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] network_interface_name: Name of the NetworkInterface
        """
        pulumi.set(__self__, "network_device_name", network_device_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if annotation is not None:
            pulumi.set(__self__, "annotation", annotation)
        if network_interface_name is not None:
            pulumi.set(__self__, "network_interface_name", network_interface_name)

    @property
    @pulumi.getter(name="networkDeviceName")
    def network_device_name(self) -> pulumi.Input[str]:
        """
        Name of the NetworkDevice
        """
        return pulumi.get(self, "network_device_name")

    @network_device_name.setter
    def network_device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_device_name", value)

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
    def annotation(self) -> Optional[pulumi.Input[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "annotation", value)

    @property
    @pulumi.getter(name="networkInterfaceName")
    def network_interface_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the NetworkInterface
        """
        return pulumi.get(self, "network_interface_name")

    @network_interface_name.setter
    def network_interface_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_interface_name", value)


class NetworkInterface(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 network_device_name: Optional[pulumi.Input[str]] = None,
                 network_interface_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Defines the NetworkInterface resource.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] network_device_name: Name of the NetworkDevice
        :param pulumi.Input[str] network_interface_name: Name of the NetworkInterface
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInterfaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the NetworkInterface resource.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview

        :param str resource_name: The name of the resource.
        :param NetworkInterfaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInterfaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 network_device_name: Optional[pulumi.Input[str]] = None,
                 network_interface_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkInterfaceArgs.__new__(NetworkInterfaceArgs)

            __props__.__dict__["annotation"] = annotation
            if network_device_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_device_name'")
            __props__.__dict__["network_device_name"] = network_device_name
            __props__.__dict__["network_interface_name"] = network_interface_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["administrative_state"] = None
            __props__.__dict__["connected_to"] = None
            __props__.__dict__["interface_type"] = None
            __props__.__dict__["ipv4_address"] = None
            __props__.__dict__["ipv6_address"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["physical_identifier"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetworkfabric/v20230201preview:NetworkInterface"), pulumi.Alias(type_="azure-native:managednetworkfabric/v20230615:NetworkInterface")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkInterface, __self__).__init__(
            'azure-native:managednetworkfabric:NetworkInterface',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkInterface':
        """
        Get an existing NetworkInterface resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkInterfaceArgs.__new__(NetworkInterfaceArgs)

        __props__.__dict__["administrative_state"] = None
        __props__.__dict__["annotation"] = None
        __props__.__dict__["connected_to"] = None
        __props__.__dict__["interface_type"] = None
        __props__.__dict__["ipv4_address"] = None
        __props__.__dict__["ipv6_address"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["physical_identifier"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return NetworkInterface(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[str]:
        """
        administrativeState of the network interface. Example: Enabled | Disabled.
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="connectedTo")
    def connected_to(self) -> pulumi.Output[str]:
        """
        The arm resource id of the interface or compute server its connected to.
        """
        return pulumi.get(self, "connected_to")

    @property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> pulumi.Output[str]:
        """
        The Interface Type. Example: Management/Data
        """
        return pulumi.get(self, "interface_type")

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> pulumi.Output[str]:
        """
        ipv4Address.
        """
        return pulumi.get(self, "ipv4_address")

    @property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> pulumi.Output[str]:
        """
        ipv6Address.
        """
        return pulumi.get(self, "ipv6_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="physicalIdentifier")
    def physical_identifier(self) -> pulumi.Output[str]:
        """
        physicalIdentifier of the network interface.
        """
        return pulumi.get(self, "physical_identifier")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets the provisioning state of the resource.
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
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

