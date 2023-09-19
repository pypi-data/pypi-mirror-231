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
    'AddressPrefixItemResponse',
    'ConfigurationGroupResponse',
    'ConnectivityGroupItemResponse',
    'EffectiveConnectivityConfigurationResponse',
    'EffectiveDefaultSecurityAdminRuleResponse',
    'EffectiveSecurityAdminRuleResponse',
    'HubResponse',
    'NetworkManagerSecurityGroupItemResponse',
]

@pulumi.output_type
class AddressPrefixItemResponse(dict):
    """
    Address prefix item.
    """
    def __init__(__self__, *,
                 address_prefix: Optional[str] = None,
                 address_prefix_type: Optional[str] = None):
        """
        Address prefix item.
        :param str address_prefix: Address prefix.
        :param str address_prefix_type: Address prefix type.
        """
        if address_prefix is not None:
            pulumi.set(__self__, "address_prefix", address_prefix)
        if address_prefix_type is not None:
            pulumi.set(__self__, "address_prefix_type", address_prefix_type)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[str]:
        """
        Address prefix.
        """
        return pulumi.get(self, "address_prefix")

    @property
    @pulumi.getter(name="addressPrefixType")
    def address_prefix_type(self) -> Optional[str]:
        """
        Address prefix type.
        """
        return pulumi.get(self, "address_prefix_type")


@pulumi.output_type
class ConfigurationGroupResponse(dict):
    """
    The network configuration group resource
    """
    def __init__(__self__, *,
                 member_type: str,
                 provisioning_state: str,
                 description: Optional[str] = None,
                 id: Optional[str] = None):
        """
        The network configuration group resource
        :param str member_type: Group member type.
        :param str provisioning_state: The provisioning state of the scope assignment resource.
        :param str description: A description of the network group.
        :param str id: Resource ID.
        """
        pulumi.set(__self__, "member_type", member_type)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="memberType")
    def member_type(self) -> str:
        """
        Group member type.
        """
        return pulumi.get(self, "member_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the scope assignment resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the network group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class ConnectivityGroupItemResponse(dict):
    """
    Connectivity group item.
    """
    def __init__(__self__, *,
                 group_connectivity: str,
                 network_group_id: str,
                 is_global: Optional[str] = None,
                 use_hub_gateway: Optional[str] = None):
        """
        Connectivity group item.
        :param str group_connectivity: Group connectivity type.
        :param str network_group_id: Network group Id.
        :param str is_global: Flag if global is supported.
        :param str use_hub_gateway: Flag if need to use hub gateway.
        """
        pulumi.set(__self__, "group_connectivity", group_connectivity)
        pulumi.set(__self__, "network_group_id", network_group_id)
        if is_global is not None:
            pulumi.set(__self__, "is_global", is_global)
        if use_hub_gateway is not None:
            pulumi.set(__self__, "use_hub_gateway", use_hub_gateway)

    @property
    @pulumi.getter(name="groupConnectivity")
    def group_connectivity(self) -> str:
        """
        Group connectivity type.
        """
        return pulumi.get(self, "group_connectivity")

    @property
    @pulumi.getter(name="networkGroupId")
    def network_group_id(self) -> str:
        """
        Network group Id.
        """
        return pulumi.get(self, "network_group_id")

    @property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[str]:
        """
        Flag if global is supported.
        """
        return pulumi.get(self, "is_global")

    @property
    @pulumi.getter(name="useHubGateway")
    def use_hub_gateway(self) -> Optional[str]:
        """
        Flag if need to use hub gateway.
        """
        return pulumi.get(self, "use_hub_gateway")


@pulumi.output_type
class EffectiveConnectivityConfigurationResponse(dict):
    """
    The network manager effective connectivity configuration
    """
    def __init__(__self__, *,
                 applies_to_groups: Sequence['outputs.ConnectivityGroupItemResponse'],
                 connectivity_topology: str,
                 provisioning_state: str,
                 configuration_groups: Optional[Sequence['outputs.ConfigurationGroupResponse']] = None,
                 delete_existing_peering: Optional[str] = None,
                 description: Optional[str] = None,
                 hubs: Optional[Sequence['outputs.HubResponse']] = None,
                 id: Optional[str] = None,
                 is_global: Optional[str] = None):
        """
        The network manager effective connectivity configuration
        :param Sequence['ConnectivityGroupItemResponse'] applies_to_groups: Groups for configuration
        :param str connectivity_topology: Connectivity topology type.
        :param str provisioning_state: The provisioning state of the connectivity configuration resource.
        :param Sequence['ConfigurationGroupResponse'] configuration_groups: Effective configuration groups.
        :param str delete_existing_peering: Flag if need to remove current existing peerings.
        :param str description: A description of the connectivity configuration.
        :param Sequence['HubResponse'] hubs: List of hubItems
        :param str id: Resource ID.
        :param str is_global: Flag if global mesh is supported.
        """
        pulumi.set(__self__, "applies_to_groups", applies_to_groups)
        pulumi.set(__self__, "connectivity_topology", connectivity_topology)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if configuration_groups is not None:
            pulumi.set(__self__, "configuration_groups", configuration_groups)
        if delete_existing_peering is not None:
            pulumi.set(__self__, "delete_existing_peering", delete_existing_peering)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if hubs is not None:
            pulumi.set(__self__, "hubs", hubs)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if is_global is not None:
            pulumi.set(__self__, "is_global", is_global)

    @property
    @pulumi.getter(name="appliesToGroups")
    def applies_to_groups(self) -> Sequence['outputs.ConnectivityGroupItemResponse']:
        """
        Groups for configuration
        """
        return pulumi.get(self, "applies_to_groups")

    @property
    @pulumi.getter(name="connectivityTopology")
    def connectivity_topology(self) -> str:
        """
        Connectivity topology type.
        """
        return pulumi.get(self, "connectivity_topology")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the connectivity configuration resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="configurationGroups")
    def configuration_groups(self) -> Optional[Sequence['outputs.ConfigurationGroupResponse']]:
        """
        Effective configuration groups.
        """
        return pulumi.get(self, "configuration_groups")

    @property
    @pulumi.getter(name="deleteExistingPeering")
    def delete_existing_peering(self) -> Optional[str]:
        """
        Flag if need to remove current existing peerings.
        """
        return pulumi.get(self, "delete_existing_peering")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the connectivity configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def hubs(self) -> Optional[Sequence['outputs.HubResponse']]:
        """
        List of hubItems
        """
        return pulumi.get(self, "hubs")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[str]:
        """
        Flag if global mesh is supported.
        """
        return pulumi.get(self, "is_global")


@pulumi.output_type
class EffectiveDefaultSecurityAdminRuleResponse(dict):
    """
    Network default admin rule.
    """
    def __init__(__self__, *,
                 access: str,
                 description: str,
                 destination_port_ranges: Sequence[str],
                 destinations: Sequence['outputs.AddressPrefixItemResponse'],
                 direction: str,
                 kind: str,
                 priority: int,
                 protocol: str,
                 provisioning_state: str,
                 source_port_ranges: Sequence[str],
                 sources: Sequence['outputs.AddressPrefixItemResponse'],
                 configuration_description: Optional[str] = None,
                 flag: Optional[str] = None,
                 id: Optional[str] = None,
                 rule_collection_applies_to_groups: Optional[Sequence['outputs.NetworkManagerSecurityGroupItemResponse']] = None,
                 rule_collection_description: Optional[str] = None,
                 rule_groups: Optional[Sequence['outputs.ConfigurationGroupResponse']] = None):
        """
        Network default admin rule.
        :param str access: Indicates the access allowed for this particular rule
        :param str description: A description for this rule. Restricted to 140 chars.
        :param Sequence[str] destination_port_ranges: The destination port ranges.
        :param Sequence['AddressPrefixItemResponse'] destinations: The destination address prefixes. CIDR or destination IP ranges.
        :param str direction: Indicates if the traffic matched against the rule in inbound or outbound.
        :param str kind: Whether the rule is custom or default.
               Expected value is 'Default'.
        :param int priority: The priority of the rule. The value can be between 1 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.
        :param str protocol: Network protocol this rule applies to.
        :param str provisioning_state: The provisioning state of the resource.
        :param Sequence[str] source_port_ranges: The source port ranges.
        :param Sequence['AddressPrefixItemResponse'] sources: The CIDR or source IP ranges.
        :param str configuration_description: A description of the security admin configuration.
        :param str flag: Default rule flag.
        :param str id: Resource ID.
        :param Sequence['NetworkManagerSecurityGroupItemResponse'] rule_collection_applies_to_groups: Groups for rule collection
        :param str rule_collection_description: A description of the rule collection.
        :param Sequence['ConfigurationGroupResponse'] rule_groups: Effective configuration groups.
        """
        pulumi.set(__self__, "access", access)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "destination_port_ranges", destination_port_ranges)
        pulumi.set(__self__, "destinations", destinations)
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "kind", 'Default')
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "source_port_ranges", source_port_ranges)
        pulumi.set(__self__, "sources", sources)
        if configuration_description is not None:
            pulumi.set(__self__, "configuration_description", configuration_description)
        if flag is not None:
            pulumi.set(__self__, "flag", flag)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if rule_collection_applies_to_groups is not None:
            pulumi.set(__self__, "rule_collection_applies_to_groups", rule_collection_applies_to_groups)
        if rule_collection_description is not None:
            pulumi.set(__self__, "rule_collection_description", rule_collection_description)
        if rule_groups is not None:
            pulumi.set(__self__, "rule_groups", rule_groups)

    @property
    @pulumi.getter
    def access(self) -> str:
        """
        Indicates the access allowed for this particular rule
        """
        return pulumi.get(self, "access")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A description for this rule. Restricted to 140 chars.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Sequence[str]:
        """
        The destination port ranges.
        """
        return pulumi.get(self, "destination_port_ranges")

    @property
    @pulumi.getter
    def destinations(self) -> Sequence['outputs.AddressPrefixItemResponse']:
        """
        The destination address prefixes. CIDR or destination IP ranges.
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def direction(self) -> str:
        """
        Indicates if the traffic matched against the rule in inbound or outbound.
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Whether the rule is custom or default.
        Expected value is 'Default'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        The priority of the rule. The value can be between 1 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Network protocol this rule applies to.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Sequence[str]:
        """
        The source port ranges.
        """
        return pulumi.get(self, "source_port_ranges")

    @property
    @pulumi.getter
    def sources(self) -> Sequence['outputs.AddressPrefixItemResponse']:
        """
        The CIDR or source IP ranges.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter(name="configurationDescription")
    def configuration_description(self) -> Optional[str]:
        """
        A description of the security admin configuration.
        """
        return pulumi.get(self, "configuration_description")

    @property
    @pulumi.getter
    def flag(self) -> Optional[str]:
        """
        Default rule flag.
        """
        return pulumi.get(self, "flag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ruleCollectionAppliesToGroups")
    def rule_collection_applies_to_groups(self) -> Optional[Sequence['outputs.NetworkManagerSecurityGroupItemResponse']]:
        """
        Groups for rule collection
        """
        return pulumi.get(self, "rule_collection_applies_to_groups")

    @property
    @pulumi.getter(name="ruleCollectionDescription")
    def rule_collection_description(self) -> Optional[str]:
        """
        A description of the rule collection.
        """
        return pulumi.get(self, "rule_collection_description")

    @property
    @pulumi.getter(name="ruleGroups")
    def rule_groups(self) -> Optional[Sequence['outputs.ConfigurationGroupResponse']]:
        """
        Effective configuration groups.
        """
        return pulumi.get(self, "rule_groups")


@pulumi.output_type
class EffectiveSecurityAdminRuleResponse(dict):
    """
    Network admin rule.
    """
    def __init__(__self__, *,
                 access: str,
                 direction: str,
                 kind: str,
                 priority: int,
                 protocol: str,
                 provisioning_state: str,
                 configuration_description: Optional[str] = None,
                 description: Optional[str] = None,
                 destination_port_ranges: Optional[Sequence[str]] = None,
                 destinations: Optional[Sequence['outputs.AddressPrefixItemResponse']] = None,
                 id: Optional[str] = None,
                 rule_collection_applies_to_groups: Optional[Sequence['outputs.NetworkManagerSecurityGroupItemResponse']] = None,
                 rule_collection_description: Optional[str] = None,
                 rule_groups: Optional[Sequence['outputs.ConfigurationGroupResponse']] = None,
                 source_port_ranges: Optional[Sequence[str]] = None,
                 sources: Optional[Sequence['outputs.AddressPrefixItemResponse']] = None):
        """
        Network admin rule.
        :param str access: Indicates the access allowed for this particular rule
        :param str direction: Indicates if the traffic matched against the rule in inbound or outbound.
        :param str kind: Whether the rule is custom or default.
               Expected value is 'Custom'.
        :param int priority: The priority of the rule. The value can be between 1 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.
        :param str protocol: Network protocol this rule applies to.
        :param str provisioning_state: The provisioning state of the resource.
        :param str configuration_description: A description of the security admin configuration.
        :param str description: A description for this rule. Restricted to 140 chars.
        :param Sequence[str] destination_port_ranges: The destination port ranges.
        :param Sequence['AddressPrefixItemResponse'] destinations: The destination address prefixes. CIDR or destination IP ranges.
        :param str id: Resource ID.
        :param Sequence['NetworkManagerSecurityGroupItemResponse'] rule_collection_applies_to_groups: Groups for rule collection
        :param str rule_collection_description: A description of the rule collection.
        :param Sequence['ConfigurationGroupResponse'] rule_groups: Effective configuration groups.
        :param Sequence[str] source_port_ranges: The source port ranges.
        :param Sequence['AddressPrefixItemResponse'] sources: The CIDR or source IP ranges.
        """
        pulumi.set(__self__, "access", access)
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "kind", 'Custom')
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if configuration_description is not None:
            pulumi.set(__self__, "configuration_description", configuration_description)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if destination_port_ranges is not None:
            pulumi.set(__self__, "destination_port_ranges", destination_port_ranges)
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if rule_collection_applies_to_groups is not None:
            pulumi.set(__self__, "rule_collection_applies_to_groups", rule_collection_applies_to_groups)
        if rule_collection_description is not None:
            pulumi.set(__self__, "rule_collection_description", rule_collection_description)
        if rule_groups is not None:
            pulumi.set(__self__, "rule_groups", rule_groups)
        if source_port_ranges is not None:
            pulumi.set(__self__, "source_port_ranges", source_port_ranges)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)

    @property
    @pulumi.getter
    def access(self) -> str:
        """
        Indicates the access allowed for this particular rule
        """
        return pulumi.get(self, "access")

    @property
    @pulumi.getter
    def direction(self) -> str:
        """
        Indicates if the traffic matched against the rule in inbound or outbound.
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Whether the rule is custom or default.
        Expected value is 'Custom'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        The priority of the rule. The value can be between 1 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Network protocol this rule applies to.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="configurationDescription")
    def configuration_description(self) -> Optional[str]:
        """
        A description of the security admin configuration.
        """
        return pulumi.get(self, "configuration_description")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for this rule. Restricted to 140 chars.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[Sequence[str]]:
        """
        The destination port ranges.
        """
        return pulumi.get(self, "destination_port_ranges")

    @property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence['outputs.AddressPrefixItemResponse']]:
        """
        The destination address prefixes. CIDR or destination IP ranges.
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ruleCollectionAppliesToGroups")
    def rule_collection_applies_to_groups(self) -> Optional[Sequence['outputs.NetworkManagerSecurityGroupItemResponse']]:
        """
        Groups for rule collection
        """
        return pulumi.get(self, "rule_collection_applies_to_groups")

    @property
    @pulumi.getter(name="ruleCollectionDescription")
    def rule_collection_description(self) -> Optional[str]:
        """
        A description of the rule collection.
        """
        return pulumi.get(self, "rule_collection_description")

    @property
    @pulumi.getter(name="ruleGroups")
    def rule_groups(self) -> Optional[Sequence['outputs.ConfigurationGroupResponse']]:
        """
        Effective configuration groups.
        """
        return pulumi.get(self, "rule_groups")

    @property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence[str]]:
        """
        The source port ranges.
        """
        return pulumi.get(self, "source_port_ranges")

    @property
    @pulumi.getter
    def sources(self) -> Optional[Sequence['outputs.AddressPrefixItemResponse']]:
        """
        The CIDR or source IP ranges.
        """
        return pulumi.get(self, "sources")


@pulumi.output_type
class HubResponse(dict):
    """
    Hub Item.
    """
    def __init__(__self__, *,
                 resource_id: Optional[str] = None,
                 resource_type: Optional[str] = None):
        """
        Hub Item.
        :param str resource_id: Resource Id.
        :param str resource_type: Resource Type.
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        Resource Id.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        """
        Resource Type.
        """
        return pulumi.get(self, "resource_type")


@pulumi.output_type
class NetworkManagerSecurityGroupItemResponse(dict):
    """
    Network manager security group item.
    """
    def __init__(__self__, *,
                 network_group_id: str):
        """
        Network manager security group item.
        :param str network_group_id: Network manager group Id.
        """
        pulumi.set(__self__, "network_group_id", network_group_id)

    @property
    @pulumi.getter(name="networkGroupId")
    def network_group_id(self) -> str:
        """
        Network manager group Id.
        """
        return pulumi.get(self, "network_group_id")


