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

__all__ = ['AzureFirewallArgs', 'AzureFirewall']

@pulumi.input_type
class AzureFirewallArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 application_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallApplicationRuleCollectionArgs']]]] = None,
                 azure_firewall_name: Optional[pulumi.Input[str]] = None,
                 firewall_policy: Optional[pulumi.Input['SubResourceArgs']] = None,
                 hub_ip_addresses: Optional[pulumi.Input['HubIPAddressesArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallIPConfigurationArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_ip_configuration: Optional[pulumi.Input['AzureFirewallIPConfigurationArgs']] = None,
                 nat_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallNatRuleCollectionArgs']]]] = None,
                 network_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallNetworkRuleCollectionArgs']]]] = None,
                 sku: Optional[pulumi.Input['AzureFirewallSkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 threat_intel_mode: Optional[pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']]] = None,
                 virtual_hub: Optional[pulumi.Input['SubResourceArgs']] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AzureFirewall resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_properties: The additional properties used to further config this azure firewall.
        :param pulumi.Input[Sequence[pulumi.Input['AzureFirewallApplicationRuleCollectionArgs']]] application_rule_collections: Collection of application rule collections used by Azure Firewall.
        :param pulumi.Input[str] azure_firewall_name: The name of the Azure Firewall.
        :param pulumi.Input['SubResourceArgs'] firewall_policy: The firewallPolicy associated with this azure firewall.
        :param pulumi.Input['HubIPAddressesArgs'] hub_ip_addresses: IP addresses associated with AzureFirewall.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[Sequence[pulumi.Input['AzureFirewallIPConfigurationArgs']]] ip_configurations: IP configuration of the Azure Firewall resource.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input['AzureFirewallIPConfigurationArgs'] management_ip_configuration: IP configuration of the Azure Firewall used for management traffic.
        :param pulumi.Input[Sequence[pulumi.Input['AzureFirewallNatRuleCollectionArgs']]] nat_rule_collections: Collection of NAT rule collections used by Azure Firewall.
        :param pulumi.Input[Sequence[pulumi.Input['AzureFirewallNetworkRuleCollectionArgs']]] network_rule_collections: Collection of network rule collections used by Azure Firewall.
        :param pulumi.Input['AzureFirewallSkuArgs'] sku: The Azure Firewall Resource SKU.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']] threat_intel_mode: The operation mode for Threat Intelligence.
        :param pulumi.Input['SubResourceArgs'] virtual_hub: The virtualHub to which the firewall belongs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A list of availability zones denoting where the resource needs to come from.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if additional_properties is not None:
            pulumi.set(__self__, "additional_properties", additional_properties)
        if application_rule_collections is not None:
            pulumi.set(__self__, "application_rule_collections", application_rule_collections)
        if azure_firewall_name is not None:
            pulumi.set(__self__, "azure_firewall_name", azure_firewall_name)
        if firewall_policy is not None:
            pulumi.set(__self__, "firewall_policy", firewall_policy)
        if hub_ip_addresses is not None:
            pulumi.set(__self__, "hub_ip_addresses", hub_ip_addresses)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if ip_configurations is not None:
            pulumi.set(__self__, "ip_configurations", ip_configurations)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if management_ip_configuration is not None:
            pulumi.set(__self__, "management_ip_configuration", management_ip_configuration)
        if nat_rule_collections is not None:
            pulumi.set(__self__, "nat_rule_collections", nat_rule_collections)
        if network_rule_collections is not None:
            pulumi.set(__self__, "network_rule_collections", network_rule_collections)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if threat_intel_mode is not None:
            pulumi.set(__self__, "threat_intel_mode", threat_intel_mode)
        if virtual_hub is not None:
            pulumi.set(__self__, "virtual_hub", virtual_hub)
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The additional properties used to further config this azure firewall.
        """
        return pulumi.get(self, "additional_properties")

    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "additional_properties", value)

    @property
    @pulumi.getter(name="applicationRuleCollections")
    def application_rule_collections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallApplicationRuleCollectionArgs']]]]:
        """
        Collection of application rule collections used by Azure Firewall.
        """
        return pulumi.get(self, "application_rule_collections")

    @application_rule_collections.setter
    def application_rule_collections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallApplicationRuleCollectionArgs']]]]):
        pulumi.set(self, "application_rule_collections", value)

    @property
    @pulumi.getter(name="azureFirewallName")
    def azure_firewall_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Azure Firewall.
        """
        return pulumi.get(self, "azure_firewall_name")

    @azure_firewall_name.setter
    def azure_firewall_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_firewall_name", value)

    @property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The firewallPolicy associated with this azure firewall.
        """
        return pulumi.get(self, "firewall_policy")

    @firewall_policy.setter
    def firewall_policy(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "firewall_policy", value)

    @property
    @pulumi.getter(name="hubIPAddresses")
    def hub_ip_addresses(self) -> Optional[pulumi.Input['HubIPAddressesArgs']]:
        """
        IP addresses associated with AzureFirewall.
        """
        return pulumi.get(self, "hub_ip_addresses")

    @hub_ip_addresses.setter
    def hub_ip_addresses(self, value: Optional[pulumi.Input['HubIPAddressesArgs']]):
        pulumi.set(self, "hub_ip_addresses", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallIPConfigurationArgs']]]]:
        """
        IP configuration of the Azure Firewall resource.
        """
        return pulumi.get(self, "ip_configurations")

    @ip_configurations.setter
    def ip_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallIPConfigurationArgs']]]]):
        pulumi.set(self, "ip_configurations", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managementIpConfiguration")
    def management_ip_configuration(self) -> Optional[pulumi.Input['AzureFirewallIPConfigurationArgs']]:
        """
        IP configuration of the Azure Firewall used for management traffic.
        """
        return pulumi.get(self, "management_ip_configuration")

    @management_ip_configuration.setter
    def management_ip_configuration(self, value: Optional[pulumi.Input['AzureFirewallIPConfigurationArgs']]):
        pulumi.set(self, "management_ip_configuration", value)

    @property
    @pulumi.getter(name="natRuleCollections")
    def nat_rule_collections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallNatRuleCollectionArgs']]]]:
        """
        Collection of NAT rule collections used by Azure Firewall.
        """
        return pulumi.get(self, "nat_rule_collections")

    @nat_rule_collections.setter
    def nat_rule_collections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallNatRuleCollectionArgs']]]]):
        pulumi.set(self, "nat_rule_collections", value)

    @property
    @pulumi.getter(name="networkRuleCollections")
    def network_rule_collections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallNetworkRuleCollectionArgs']]]]:
        """
        Collection of network rule collections used by Azure Firewall.
        """
        return pulumi.get(self, "network_rule_collections")

    @network_rule_collections.setter
    def network_rule_collections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AzureFirewallNetworkRuleCollectionArgs']]]]):
        pulumi.set(self, "network_rule_collections", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['AzureFirewallSkuArgs']]:
        """
        The Azure Firewall Resource SKU.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['AzureFirewallSkuArgs']]):
        pulumi.set(self, "sku", value)

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
    @pulumi.getter(name="threatIntelMode")
    def threat_intel_mode(self) -> Optional[pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']]]:
        """
        The operation mode for Threat Intelligence.
        """
        return pulumi.get(self, "threat_intel_mode")

    @threat_intel_mode.setter
    def threat_intel_mode(self, value: Optional[pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']]]):
        pulumi.set(self, "threat_intel_mode", value)

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The virtualHub to which the firewall belongs.
        """
        return pulumi.get(self, "virtual_hub")

    @virtual_hub.setter
    def virtual_hub(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "virtual_hub", value)

    @property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of availability zones denoting where the resource needs to come from.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


class AzureFirewall(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 application_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallApplicationRuleCollectionArgs']]]]] = None,
                 azure_firewall_name: Optional[pulumi.Input[str]] = None,
                 firewall_policy: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 hub_ip_addresses: Optional[pulumi.Input[pulumi.InputType['HubIPAddressesArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallIPConfigurationArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_ip_configuration: Optional[pulumi.Input[pulumi.InputType['AzureFirewallIPConfigurationArgs']]] = None,
                 nat_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallNatRuleCollectionArgs']]]]] = None,
                 network_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallNetworkRuleCollectionArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['AzureFirewallSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 threat_intel_mode: Optional[pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Azure Firewall resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_properties: The additional properties used to further config this azure firewall.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallApplicationRuleCollectionArgs']]]] application_rule_collections: Collection of application rule collections used by Azure Firewall.
        :param pulumi.Input[str] azure_firewall_name: The name of the Azure Firewall.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] firewall_policy: The firewallPolicy associated with this azure firewall.
        :param pulumi.Input[pulumi.InputType['HubIPAddressesArgs']] hub_ip_addresses: IP addresses associated with AzureFirewall.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallIPConfigurationArgs']]]] ip_configurations: IP configuration of the Azure Firewall resource.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[pulumi.InputType['AzureFirewallIPConfigurationArgs']] management_ip_configuration: IP configuration of the Azure Firewall used for management traffic.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallNatRuleCollectionArgs']]]] nat_rule_collections: Collection of NAT rule collections used by Azure Firewall.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallNetworkRuleCollectionArgs']]]] network_rule_collections: Collection of network rule collections used by Azure Firewall.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['AzureFirewallSkuArgs']] sku: The Azure Firewall Resource SKU.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']] threat_intel_mode: The operation mode for Threat Intelligence.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] virtual_hub: The virtualHub to which the firewall belongs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A list of availability zones denoting where the resource needs to come from.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AzureFirewallArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure Firewall resource.

        :param str resource_name: The name of the resource.
        :param AzureFirewallArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AzureFirewallArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 application_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallApplicationRuleCollectionArgs']]]]] = None,
                 azure_firewall_name: Optional[pulumi.Input[str]] = None,
                 firewall_policy: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 hub_ip_addresses: Optional[pulumi.Input[pulumi.InputType['HubIPAddressesArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallIPConfigurationArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_ip_configuration: Optional[pulumi.Input[pulumi.InputType['AzureFirewallIPConfigurationArgs']]] = None,
                 nat_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallNatRuleCollectionArgs']]]]] = None,
                 network_rule_collections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureFirewallNetworkRuleCollectionArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['AzureFirewallSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 threat_intel_mode: Optional[pulumi.Input[Union[str, 'AzureFirewallThreatIntelMode']]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AzureFirewallArgs.__new__(AzureFirewallArgs)

            __props__.__dict__["additional_properties"] = additional_properties
            __props__.__dict__["application_rule_collections"] = application_rule_collections
            __props__.__dict__["azure_firewall_name"] = azure_firewall_name
            __props__.__dict__["firewall_policy"] = firewall_policy
            __props__.__dict__["hub_ip_addresses"] = hub_ip_addresses
            __props__.__dict__["id"] = id
            __props__.__dict__["ip_configurations"] = ip_configurations
            __props__.__dict__["location"] = location
            __props__.__dict__["management_ip_configuration"] = management_ip_configuration
            __props__.__dict__["nat_rule_collections"] = nat_rule_collections
            __props__.__dict__["network_rule_collections"] = network_rule_collections
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["threat_intel_mode"] = threat_intel_mode
            __props__.__dict__["virtual_hub"] = virtual_hub
            __props__.__dict__["zones"] = zones
            __props__.__dict__["etag"] = None
            __props__.__dict__["ip_groups"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20180401:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20180601:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20180701:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20180801:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20181001:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20181101:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20181201:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20190201:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20190401:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20190601:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20190701:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20190801:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20190901:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20191101:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20191201:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20200301:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20200401:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20200501:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20200601:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20200701:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20200801:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20201101:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20210201:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20210301:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20210501:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20210801:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20220101:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20220501:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20220701:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20220901:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20221101:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20230401:AzureFirewall"), pulumi.Alias(type_="azure-native:network/v20230501:AzureFirewall")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AzureFirewall, __self__).__init__(
            'azure-native:network/v20230201:AzureFirewall',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AzureFirewall':
        """
        Get an existing AzureFirewall resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AzureFirewallArgs.__new__(AzureFirewallArgs)

        __props__.__dict__["additional_properties"] = None
        __props__.__dict__["application_rule_collections"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["firewall_policy"] = None
        __props__.__dict__["hub_ip_addresses"] = None
        __props__.__dict__["ip_configurations"] = None
        __props__.__dict__["ip_groups"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["management_ip_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["nat_rule_collections"] = None
        __props__.__dict__["network_rule_collections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["threat_intel_mode"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_hub"] = None
        __props__.__dict__["zones"] = None
        return AzureFirewall(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The additional properties used to further config this azure firewall.
        """
        return pulumi.get(self, "additional_properties")

    @property
    @pulumi.getter(name="applicationRuleCollections")
    def application_rule_collections(self) -> pulumi.Output[Optional[Sequence['outputs.AzureFirewallApplicationRuleCollectionResponse']]]:
        """
        Collection of application rule collections used by Azure Firewall.
        """
        return pulumi.get(self, "application_rule_collections")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The firewallPolicy associated with this azure firewall.
        """
        return pulumi.get(self, "firewall_policy")

    @property
    @pulumi.getter(name="hubIPAddresses")
    def hub_ip_addresses(self) -> pulumi.Output[Optional['outputs.HubIPAddressesResponse']]:
        """
        IP addresses associated with AzureFirewall.
        """
        return pulumi.get(self, "hub_ip_addresses")

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.AzureFirewallIPConfigurationResponse']]]:
        """
        IP configuration of the Azure Firewall resource.
        """
        return pulumi.get(self, "ip_configurations")

    @property
    @pulumi.getter(name="ipGroups")
    def ip_groups(self) -> pulumi.Output[Sequence['outputs.AzureFirewallIpGroupsResponse']]:
        """
        IpGroups associated with AzureFirewall.
        """
        return pulumi.get(self, "ip_groups")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementIpConfiguration")
    def management_ip_configuration(self) -> pulumi.Output[Optional['outputs.AzureFirewallIPConfigurationResponse']]:
        """
        IP configuration of the Azure Firewall used for management traffic.
        """
        return pulumi.get(self, "management_ip_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natRuleCollections")
    def nat_rule_collections(self) -> pulumi.Output[Optional[Sequence['outputs.AzureFirewallNatRuleCollectionResponse']]]:
        """
        Collection of NAT rule collections used by Azure Firewall.
        """
        return pulumi.get(self, "nat_rule_collections")

    @property
    @pulumi.getter(name="networkRuleCollections")
    def network_rule_collections(self) -> pulumi.Output[Optional[Sequence['outputs.AzureFirewallNetworkRuleCollectionResponse']]]:
        """
        Collection of network rule collections used by Azure Firewall.
        """
        return pulumi.get(self, "network_rule_collections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the Azure firewall resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.AzureFirewallSkuResponse']]:
        """
        The Azure Firewall Resource SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="threatIntelMode")
    def threat_intel_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The operation mode for Threat Intelligence.
        """
        return pulumi.get(self, "threat_intel_mode")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The virtualHub to which the firewall belongs.
        """
        return pulumi.get(self, "virtual_hub")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of availability zones denoting where the resource needs to come from.
        """
        return pulumi.get(self, "zones")

