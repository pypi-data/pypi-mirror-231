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

__all__ = ['NetworkinterfaceRetrieveArgs', 'NetworkinterfaceRetrieve']

@pulumi.input_type
class NetworkinterfaceRetrieveArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 dns_settings: Optional[pulumi.Input['InterfaceDNSSettingsArgs']] = None,
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['IpConfigurationArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 networkinterfaces_name: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkinterfaceRetrieve resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['InterfaceDNSSettingsArgs'] dns_settings: DNS Settings for the interface
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extendedLocation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input['IpConfigurationArgs']]] ip_configurations: IPConfigurations - A list of IPConfigurations of the network interface.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] mac_address: MacAddress - The MAC address of the network interface.
        :param pulumi.Input[str] resource_name: name of the object to be used in moc
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if dns_settings is not None:
            pulumi.set(__self__, "dns_settings", dns_settings)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if ip_configurations is not None:
            pulumi.set(__self__, "ip_configurations", ip_configurations)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mac_address is not None:
            pulumi.set(__self__, "mac_address", mac_address)
        if networkinterfaces_name is not None:
            pulumi.set(__self__, "networkinterfaces_name", networkinterfaces_name)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input['InterfaceDNSSettingsArgs']]:
        """
        DNS Settings for the interface
        """
        return pulumi.get(self, "dns_settings")

    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input['InterfaceDNSSettingsArgs']]):
        pulumi.set(self, "dns_settings", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpConfigurationArgs']]]]:
        """
        IPConfigurations - A list of IPConfigurations of the network interface.
        """
        return pulumi.get(self, "ip_configurations")

    @ip_configurations.setter
    def ip_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpConfigurationArgs']]]]):
        pulumi.set(self, "ip_configurations", value)

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
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[str]]:
        """
        MacAddress - The MAC address of the network interface.
        """
        return pulumi.get(self, "mac_address")

    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac_address", value)

    @property
    @pulumi.getter(name="networkinterfacesName")
    def networkinterfaces_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "networkinterfaces_name")

    @networkinterfaces_name.setter
    def networkinterfaces_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "networkinterfaces_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the object to be used in moc
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

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


class NetworkinterfaceRetrieve(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_settings: Optional[pulumi.Input[pulumi.InputType['InterfaceDNSSettingsArgs']]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpConfigurationArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 networkinterfaces_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The network interface resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['InterfaceDNSSettingsArgs']] dns_settings: DNS Settings for the interface
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extendedLocation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpConfigurationArgs']]]] ip_configurations: IPConfigurations - A list of IPConfigurations of the network interface.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] mac_address: MacAddress - The MAC address of the network interface.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: name of the object to be used in moc
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkinterfaceRetrieveArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The network interface resource definition.

        :param str resource_name: The name of the resource.
        :param NetworkinterfaceRetrieveArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkinterfaceRetrieveArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_settings: Optional[pulumi.Input[pulumi.InputType['InterfaceDNSSettingsArgs']]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpConfigurationArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 networkinterfaces_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkinterfaceRetrieveArgs.__new__(NetworkinterfaceRetrieveArgs)

            __props__.__dict__["dns_settings"] = dns_settings
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["ip_configurations"] = ip_configurations
            __props__.__dict__["location"] = location
            __props__.__dict__["mac_address"] = mac_address
            __props__.__dict__["networkinterfaces_name"] = networkinterfaces_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci/v20210901preview:networkinterfaceRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci:NetworkinterfaceRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci:networkinterfaceRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20210701preview:NetworkinterfaceRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20210701preview:networkinterfaceRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:NetworkinterfaceRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:networkinterfaceRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20230701preview:NetworkinterfaceRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20230701preview:networkinterfaceRetrieve")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkinterfaceRetrieve, __self__).__init__(
            'azure-native:azurestackhci/v20210901preview:NetworkinterfaceRetrieve',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkinterfaceRetrieve':
        """
        Get an existing NetworkinterfaceRetrieve resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkinterfaceRetrieveArgs.__new__(NetworkinterfaceRetrieveArgs)

        __props__.__dict__["dns_settings"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["ip_configurations"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mac_address"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return NetworkinterfaceRetrieve(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Output[Optional['outputs.InterfaceDNSSettingsResponse']]:
        """
        DNS Settings for the interface
        """
        return pulumi.get(self, "dns_settings")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.IpConfigurationResponse']]]:
        """
        IPConfigurations - A list of IPConfigurations of the network interface.
        """
        return pulumi.get(self, "ip_configurations")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> pulumi.Output[Optional[str]]:
        """
        MacAddress - The MAC address of the network interface.
        """
        return pulumi.get(self, "mac_address")

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
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Output[Optional[str]]:
        """
        name of the object to be used in moc
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.NetworkInterfaceStatusResponse']:
        """
        NetworkInterfaceStatus defines the observed state of network interfaces
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
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

