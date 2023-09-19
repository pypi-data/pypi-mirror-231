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

__all__ = ['NetworkFabricArgs', 'NetworkFabric']

@pulumi.input_type
class NetworkFabricArgs:
    def __init__(__self__, *,
                 fabric_asn: pulumi.Input[float],
                 ipv4_prefix: pulumi.Input[str],
                 management_network_configuration: pulumi.Input['ManagementNetworkConfigurationPropertiesArgs'],
                 network_fabric_controller_id: pulumi.Input[str],
                 network_fabric_sku: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 server_count_per_rack: pulumi.Input[int],
                 terminal_server_configuration: pulumi.Input['TerminalServerConfigurationArgs'],
                 annotation: Optional[pulumi.Input[str]] = None,
                 ipv6_prefix: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_fabric_name: Optional[pulumi.Input[str]] = None,
                 rack_count: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkFabric resource.
        :param pulumi.Input[float] fabric_asn: ASN of CE devices for CE/PE connectivity.
        :param pulumi.Input[str] ipv4_prefix: IPv4Prefix for Management Network. Example: 10.1.0.0/19.
        :param pulumi.Input['ManagementNetworkConfigurationPropertiesArgs'] management_network_configuration: Configuration to be used to setup the management network.
        :param pulumi.Input[str] network_fabric_controller_id: Azure resource ID for the NetworkFabricController the NetworkFabric belongs.
        :param pulumi.Input[str] network_fabric_sku: Supported Network Fabric SKU.Example: Compute / Aggregate racks. Once the user chooses a particular SKU, only supported racks can be added to the Network Fabric. The SKU determines whether it is a single / multi rack Network Fabric.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[int] server_count_per_rack: Number of servers.Possible values are from 1-16.
        :param pulumi.Input['TerminalServerConfigurationArgs'] terminal_server_configuration: Network and credentials configuration currently applied to terminal server.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] ipv6_prefix: IPv6Prefix for Management Network. Example: 3FFE:FFFF:0:CD40::/59
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] network_fabric_name: Name of the Network Fabric.
        :param pulumi.Input[int] rack_count: Number of compute racks associated to Network Fabric.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "fabric_asn", fabric_asn)
        pulumi.set(__self__, "ipv4_prefix", ipv4_prefix)
        pulumi.set(__self__, "management_network_configuration", management_network_configuration)
        pulumi.set(__self__, "network_fabric_controller_id", network_fabric_controller_id)
        pulumi.set(__self__, "network_fabric_sku", network_fabric_sku)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_count_per_rack", server_count_per_rack)
        pulumi.set(__self__, "terminal_server_configuration", terminal_server_configuration)
        if annotation is not None:
            pulumi.set(__self__, "annotation", annotation)
        if ipv6_prefix is not None:
            pulumi.set(__self__, "ipv6_prefix", ipv6_prefix)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_fabric_name is not None:
            pulumi.set(__self__, "network_fabric_name", network_fabric_name)
        if rack_count is not None:
            pulumi.set(__self__, "rack_count", rack_count)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="fabricASN")
    def fabric_asn(self) -> pulumi.Input[float]:
        """
        ASN of CE devices for CE/PE connectivity.
        """
        return pulumi.get(self, "fabric_asn")

    @fabric_asn.setter
    def fabric_asn(self, value: pulumi.Input[float]):
        pulumi.set(self, "fabric_asn", value)

    @property
    @pulumi.getter(name="ipv4Prefix")
    def ipv4_prefix(self) -> pulumi.Input[str]:
        """
        IPv4Prefix for Management Network. Example: 10.1.0.0/19.
        """
        return pulumi.get(self, "ipv4_prefix")

    @ipv4_prefix.setter
    def ipv4_prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "ipv4_prefix", value)

    @property
    @pulumi.getter(name="managementNetworkConfiguration")
    def management_network_configuration(self) -> pulumi.Input['ManagementNetworkConfigurationPropertiesArgs']:
        """
        Configuration to be used to setup the management network.
        """
        return pulumi.get(self, "management_network_configuration")

    @management_network_configuration.setter
    def management_network_configuration(self, value: pulumi.Input['ManagementNetworkConfigurationPropertiesArgs']):
        pulumi.set(self, "management_network_configuration", value)

    @property
    @pulumi.getter(name="networkFabricControllerId")
    def network_fabric_controller_id(self) -> pulumi.Input[str]:
        """
        Azure resource ID for the NetworkFabricController the NetworkFabric belongs.
        """
        return pulumi.get(self, "network_fabric_controller_id")

    @network_fabric_controller_id.setter
    def network_fabric_controller_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_fabric_controller_id", value)

    @property
    @pulumi.getter(name="networkFabricSku")
    def network_fabric_sku(self) -> pulumi.Input[str]:
        """
        Supported Network Fabric SKU.Example: Compute / Aggregate racks. Once the user chooses a particular SKU, only supported racks can be added to the Network Fabric. The SKU determines whether it is a single / multi rack Network Fabric.
        """
        return pulumi.get(self, "network_fabric_sku")

    @network_fabric_sku.setter
    def network_fabric_sku(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_fabric_sku", value)

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
    @pulumi.getter(name="serverCountPerRack")
    def server_count_per_rack(self) -> pulumi.Input[int]:
        """
        Number of servers.Possible values are from 1-16.
        """
        return pulumi.get(self, "server_count_per_rack")

    @server_count_per_rack.setter
    def server_count_per_rack(self, value: pulumi.Input[int]):
        pulumi.set(self, "server_count_per_rack", value)

    @property
    @pulumi.getter(name="terminalServerConfiguration")
    def terminal_server_configuration(self) -> pulumi.Input['TerminalServerConfigurationArgs']:
        """
        Network and credentials configuration currently applied to terminal server.
        """
        return pulumi.get(self, "terminal_server_configuration")

    @terminal_server_configuration.setter
    def terminal_server_configuration(self, value: pulumi.Input['TerminalServerConfigurationArgs']):
        pulumi.set(self, "terminal_server_configuration", value)

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
    @pulumi.getter(name="ipv6Prefix")
    def ipv6_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        IPv6Prefix for Management Network. Example: 3FFE:FFFF:0:CD40::/59
        """
        return pulumi.get(self, "ipv6_prefix")

    @ipv6_prefix.setter
    def ipv6_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_prefix", value)

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
    @pulumi.getter(name="networkFabricName")
    def network_fabric_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Network Fabric.
        """
        return pulumi.get(self, "network_fabric_name")

    @network_fabric_name.setter
    def network_fabric_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_fabric_name", value)

    @property
    @pulumi.getter(name="rackCount")
    def rack_count(self) -> Optional[pulumi.Input[int]]:
        """
        Number of compute racks associated to Network Fabric.
        """
        return pulumi.get(self, "rack_count")

    @rack_count.setter
    def rack_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rack_count", value)

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


class NetworkFabric(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 fabric_asn: Optional[pulumi.Input[float]] = None,
                 ipv4_prefix: Optional[pulumi.Input[str]] = None,
                 ipv6_prefix: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_network_configuration: Optional[pulumi.Input[pulumi.InputType['ManagementNetworkConfigurationPropertiesArgs']]] = None,
                 network_fabric_controller_id: Optional[pulumi.Input[str]] = None,
                 network_fabric_name: Optional[pulumi.Input[str]] = None,
                 network_fabric_sku: Optional[pulumi.Input[str]] = None,
                 rack_count: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_count_per_rack: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 terminal_server_configuration: Optional[pulumi.Input[pulumi.InputType['TerminalServerConfigurationArgs']]] = None,
                 __props__=None):
        """
        The Network Fabric resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[float] fabric_asn: ASN of CE devices for CE/PE connectivity.
        :param pulumi.Input[str] ipv4_prefix: IPv4Prefix for Management Network. Example: 10.1.0.0/19.
        :param pulumi.Input[str] ipv6_prefix: IPv6Prefix for Management Network. Example: 3FFE:FFFF:0:CD40::/59
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['ManagementNetworkConfigurationPropertiesArgs']] management_network_configuration: Configuration to be used to setup the management network.
        :param pulumi.Input[str] network_fabric_controller_id: Azure resource ID for the NetworkFabricController the NetworkFabric belongs.
        :param pulumi.Input[str] network_fabric_name: Name of the Network Fabric.
        :param pulumi.Input[str] network_fabric_sku: Supported Network Fabric SKU.Example: Compute / Aggregate racks. Once the user chooses a particular SKU, only supported racks can be added to the Network Fabric. The SKU determines whether it is a single / multi rack Network Fabric.
        :param pulumi.Input[int] rack_count: Number of compute racks associated to Network Fabric.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[int] server_count_per_rack: Number of servers.Possible values are from 1-16.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['TerminalServerConfigurationArgs']] terminal_server_configuration: Network and credentials configuration currently applied to terminal server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkFabricArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Network Fabric resource definition.

        :param str resource_name: The name of the resource.
        :param NetworkFabricArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkFabricArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 fabric_asn: Optional[pulumi.Input[float]] = None,
                 ipv4_prefix: Optional[pulumi.Input[str]] = None,
                 ipv6_prefix: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_network_configuration: Optional[pulumi.Input[pulumi.InputType['ManagementNetworkConfigurationPropertiesArgs']]] = None,
                 network_fabric_controller_id: Optional[pulumi.Input[str]] = None,
                 network_fabric_name: Optional[pulumi.Input[str]] = None,
                 network_fabric_sku: Optional[pulumi.Input[str]] = None,
                 rack_count: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_count_per_rack: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 terminal_server_configuration: Optional[pulumi.Input[pulumi.InputType['TerminalServerConfigurationArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkFabricArgs.__new__(NetworkFabricArgs)

            __props__.__dict__["annotation"] = annotation
            if fabric_asn is None and not opts.urn:
                raise TypeError("Missing required property 'fabric_asn'")
            __props__.__dict__["fabric_asn"] = fabric_asn
            if ipv4_prefix is None and not opts.urn:
                raise TypeError("Missing required property 'ipv4_prefix'")
            __props__.__dict__["ipv4_prefix"] = ipv4_prefix
            __props__.__dict__["ipv6_prefix"] = ipv6_prefix
            __props__.__dict__["location"] = location
            if management_network_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'management_network_configuration'")
            __props__.__dict__["management_network_configuration"] = management_network_configuration
            if network_fabric_controller_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_fabric_controller_id'")
            __props__.__dict__["network_fabric_controller_id"] = network_fabric_controller_id
            __props__.__dict__["network_fabric_name"] = network_fabric_name
            if network_fabric_sku is None and not opts.urn:
                raise TypeError("Missing required property 'network_fabric_sku'")
            __props__.__dict__["network_fabric_sku"] = network_fabric_sku
            __props__.__dict__["rack_count"] = rack_count
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_count_per_rack is None and not opts.urn:
                raise TypeError("Missing required property 'server_count_per_rack'")
            __props__.__dict__["server_count_per_rack"] = server_count_per_rack
            __props__.__dict__["tags"] = tags
            if terminal_server_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'terminal_server_configuration'")
            __props__.__dict__["terminal_server_configuration"] = terminal_server_configuration
            __props__.__dict__["administrative_state"] = None
            __props__.__dict__["configuration_state"] = None
            __props__.__dict__["fabric_version"] = None
            __props__.__dict__["l2_isolation_domains"] = None
            __props__.__dict__["l3_isolation_domains"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["racks"] = None
            __props__.__dict__["router_ids"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetworkfabric:NetworkFabric"), pulumi.Alias(type_="azure-native:managednetworkfabric/v20230201preview:NetworkFabric")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkFabric, __self__).__init__(
            'azure-native:managednetworkfabric/v20230615:NetworkFabric',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkFabric':
        """
        Get an existing NetworkFabric resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkFabricArgs.__new__(NetworkFabricArgs)

        __props__.__dict__["administrative_state"] = None
        __props__.__dict__["annotation"] = None
        __props__.__dict__["configuration_state"] = None
        __props__.__dict__["fabric_asn"] = None
        __props__.__dict__["fabric_version"] = None
        __props__.__dict__["ipv4_prefix"] = None
        __props__.__dict__["ipv6_prefix"] = None
        __props__.__dict__["l2_isolation_domains"] = None
        __props__.__dict__["l3_isolation_domains"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["management_network_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_fabric_controller_id"] = None
        __props__.__dict__["network_fabric_sku"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rack_count"] = None
        __props__.__dict__["racks"] = None
        __props__.__dict__["router_ids"] = None
        __props__.__dict__["server_count_per_rack"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["terminal_server_configuration"] = None
        __props__.__dict__["type"] = None
        return NetworkFabric(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[str]:
        """
        Administrative state of the resource.
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
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> pulumi.Output[str]:
        """
        Configuration state of the resource.
        """
        return pulumi.get(self, "configuration_state")

    @property
    @pulumi.getter(name="fabricASN")
    def fabric_asn(self) -> pulumi.Output[float]:
        """
        ASN of CE devices for CE/PE connectivity.
        """
        return pulumi.get(self, "fabric_asn")

    @property
    @pulumi.getter(name="fabricVersion")
    def fabric_version(self) -> pulumi.Output[str]:
        """
        The version of Network Fabric.
        """
        return pulumi.get(self, "fabric_version")

    @property
    @pulumi.getter(name="ipv4Prefix")
    def ipv4_prefix(self) -> pulumi.Output[str]:
        """
        IPv4Prefix for Management Network. Example: 10.1.0.0/19.
        """
        return pulumi.get(self, "ipv4_prefix")

    @property
    @pulumi.getter(name="ipv6Prefix")
    def ipv6_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        IPv6Prefix for Management Network. Example: 3FFE:FFFF:0:CD40::/59
        """
        return pulumi.get(self, "ipv6_prefix")

    @property
    @pulumi.getter(name="l2IsolationDomains")
    def l2_isolation_domains(self) -> pulumi.Output[Sequence[str]]:
        """
        List of L2 Isolation Domain resource IDs under the Network Fabric.
        """
        return pulumi.get(self, "l2_isolation_domains")

    @property
    @pulumi.getter(name="l3IsolationDomains")
    def l3_isolation_domains(self) -> pulumi.Output[Sequence[str]]:
        """
        List of L3 Isolation Domain resource IDs under the Network Fabric.
        """
        return pulumi.get(self, "l3_isolation_domains")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementNetworkConfiguration")
    def management_network_configuration(self) -> pulumi.Output['outputs.ManagementNetworkConfigurationPropertiesResponse']:
        """
        Configuration to be used to setup the management network.
        """
        return pulumi.get(self, "management_network_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkFabricControllerId")
    def network_fabric_controller_id(self) -> pulumi.Output[str]:
        """
        Azure resource ID for the NetworkFabricController the NetworkFabric belongs.
        """
        return pulumi.get(self, "network_fabric_controller_id")

    @property
    @pulumi.getter(name="networkFabricSku")
    def network_fabric_sku(self) -> pulumi.Output[str]:
        """
        Supported Network Fabric SKU.Example: Compute / Aggregate racks. Once the user chooses a particular SKU, only supported racks can be added to the Network Fabric. The SKU determines whether it is a single / multi rack Network Fabric.
        """
        return pulumi.get(self, "network_fabric_sku")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provides you the latest status of the NFC service, whether it is Accepted, updating, Succeeded or Failed. During this process, the states keep changing based on the status of NFC provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rackCount")
    def rack_count(self) -> pulumi.Output[Optional[int]]:
        """
        Number of compute racks associated to Network Fabric.
        """
        return pulumi.get(self, "rack_count")

    @property
    @pulumi.getter
    def racks(self) -> pulumi.Output[Sequence[str]]:
        """
        List of NetworkRack resource IDs under the Network Fabric. The number of racks allowed depends on the Network Fabric SKU.
        """
        return pulumi.get(self, "racks")

    @property
    @pulumi.getter(name="routerIds")
    def router_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Array of router IDs.
        """
        return pulumi.get(self, "router_ids")

    @property
    @pulumi.getter(name="serverCountPerRack")
    def server_count_per_rack(self) -> pulumi.Output[int]:
        """
        Number of servers.Possible values are from 1-16.
        """
        return pulumi.get(self, "server_count_per_rack")

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
    @pulumi.getter(name="terminalServerConfiguration")
    def terminal_server_configuration(self) -> pulumi.Output['outputs.TerminalServerConfigurationResponse']:
        """
        Network and credentials configuration currently applied to terminal server.
        """
        return pulumi.get(self, "terminal_server_configuration")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

