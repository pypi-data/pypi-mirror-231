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

__all__ = ['UserRuleArgs', 'UserRule']

@pulumi.input_type
class UserRuleArgs:
    def __init__(__self__, *,
                 configuration_name: pulumi.Input[str],
                 direction: pulumi.Input[Union[str, 'SecurityConfigurationRuleDirection']],
                 kind: pulumi.Input[str],
                 network_manager_name: pulumi.Input[str],
                 protocol: pulumi.Input[Union[str, 'SecurityConfigurationRuleProtocol']],
                 resource_group_name: pulumi.Input[str],
                 rule_collection_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input['AddressPrefixItemArgs']]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['AddressPrefixItemArgs']]]] = None):
        """
        The set of arguments for constructing a UserRule resource.
        :param pulumi.Input[str] configuration_name: The name of the network manager Security Configuration.
        :param pulumi.Input[Union[str, 'SecurityConfigurationRuleDirection']] direction: Indicates if the traffic matched against the rule in inbound or outbound.
        :param pulumi.Input[str] kind: Whether the rule is custom or default.
               Expected value is 'Custom'.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[Union[str, 'SecurityConfigurationRuleProtocol']] protocol: Network protocol this rule applies to.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] rule_collection_name: The name of the network manager security Configuration rule collection.
        :param pulumi.Input[str] description: A description for this rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] destination_port_ranges: The destination port ranges.
        :param pulumi.Input[Sequence[pulumi.Input['AddressPrefixItemArgs']]] destinations: The destination address prefixes. CIDR or destination IP ranges.
        :param pulumi.Input[str] display_name: A friendly name for the rule.
        :param pulumi.Input[str] rule_name: The name of the rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] source_port_ranges: The source port ranges.
        :param pulumi.Input[Sequence[pulumi.Input['AddressPrefixItemArgs']]] sources: The CIDR or source IP ranges.
        """
        pulumi.set(__self__, "configuration_name", configuration_name)
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "kind", 'Custom')
        pulumi.set(__self__, "network_manager_name", network_manager_name)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "rule_collection_name", rule_collection_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if destination_port_ranges is not None:
            pulumi.set(__self__, "destination_port_ranges", destination_port_ranges)
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)
        if source_port_ranges is not None:
            pulumi.set(__self__, "source_port_ranges", source_port_ranges)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> pulumi.Input[str]:
        """
        The name of the network manager Security Configuration.
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Input[Union[str, 'SecurityConfigurationRuleDirection']]:
        """
        Indicates if the traffic matched against the rule in inbound or outbound.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: pulumi.Input[Union[str, 'SecurityConfigurationRuleDirection']]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Whether the rule is custom or default.
        Expected value is 'Custom'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="networkManagerName")
    def network_manager_name(self) -> pulumi.Input[str]:
        """
        The name of the network manager.
        """
        return pulumi.get(self, "network_manager_name")

    @network_manager_name.setter
    def network_manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_manager_name", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[Union[str, 'SecurityConfigurationRuleProtocol']]:
        """
        Network protocol this rule applies to.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[Union[str, 'SecurityConfigurationRuleProtocol']]):
        pulumi.set(self, "protocol", value)

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
    @pulumi.getter(name="ruleCollectionName")
    def rule_collection_name(self) -> pulumi.Input[str]:
        """
        The name of the network manager security Configuration rule collection.
        """
        return pulumi.get(self, "rule_collection_name")

    @rule_collection_name.setter
    def rule_collection_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_collection_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for this rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The destination port ranges.
        """
        return pulumi.get(self, "destination_port_ranges")

    @destination_port_ranges.setter
    def destination_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "destination_port_ranges", value)

    @property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AddressPrefixItemArgs']]]]:
        """
        The destination address prefixes. CIDR or destination IP ranges.
        """
        return pulumi.get(self, "destinations")

    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AddressPrefixItemArgs']]]]):
        pulumi.set(self, "destinations", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A friendly name for the rule.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the rule.
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)

    @property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The source port ranges.
        """
        return pulumi.get(self, "source_port_ranges")

    @source_port_ranges.setter
    def source_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "source_port_ranges", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AddressPrefixItemArgs']]]]:
        """
        The CIDR or source IP ranges.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AddressPrefixItemArgs']]]]):
        pulumi.set(self, "sources", value)


class UserRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressPrefixItemArgs']]]]] = None,
                 direction: Optional[pulumi.Input[Union[str, 'SecurityConfigurationRuleDirection']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'SecurityConfigurationRuleProtocol']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collection_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressPrefixItemArgs']]]]] = None,
                 __props__=None):
        """
        Network security user rule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] configuration_name: The name of the network manager Security Configuration.
        :param pulumi.Input[str] description: A description for this rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] destination_port_ranges: The destination port ranges.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressPrefixItemArgs']]]] destinations: The destination address prefixes. CIDR or destination IP ranges.
        :param pulumi.Input[Union[str, 'SecurityConfigurationRuleDirection']] direction: Indicates if the traffic matched against the rule in inbound or outbound.
        :param pulumi.Input[str] display_name: A friendly name for the rule.
        :param pulumi.Input[str] kind: Whether the rule is custom or default.
               Expected value is 'Custom'.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[Union[str, 'SecurityConfigurationRuleProtocol']] protocol: Network protocol this rule applies to.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] rule_collection_name: The name of the network manager security Configuration rule collection.
        :param pulumi.Input[str] rule_name: The name of the rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] source_port_ranges: The source port ranges.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressPrefixItemArgs']]]] sources: The CIDR or source IP ranges.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Network security user rule.

        :param str resource_name: The name of the resource.
        :param UserRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressPrefixItemArgs']]]]] = None,
                 direction: Optional[pulumi.Input[Union[str, 'SecurityConfigurationRuleDirection']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[Union[str, 'SecurityConfigurationRuleProtocol']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collection_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AddressPrefixItemArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserRuleArgs.__new__(UserRuleArgs)

            if configuration_name is None and not opts.urn:
                raise TypeError("Missing required property 'configuration_name'")
            __props__.__dict__["configuration_name"] = configuration_name
            __props__.__dict__["description"] = description
            __props__.__dict__["destination_port_ranges"] = destination_port_ranges
            __props__.__dict__["destinations"] = destinations
            if direction is None and not opts.urn:
                raise TypeError("Missing required property 'direction'")
            __props__.__dict__["direction"] = direction
            __props__.__dict__["display_name"] = display_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'Custom'
            if network_manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_manager_name'")
            __props__.__dict__["network_manager_name"] = network_manager_name
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if rule_collection_name is None and not opts.urn:
                raise TypeError("Missing required property 'rule_collection_name'")
            __props__.__dict__["rule_collection_name"] = rule_collection_name
            __props__.__dict__["rule_name"] = rule_name
            __props__.__dict__["source_port_ranges"] = source_port_ranges
            __props__.__dict__["sources"] = sources
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:UserRule"), pulumi.Alias(type_="azure-native:network/v20210201preview:UserRule"), pulumi.Alias(type_="azure-native:network/v20220201preview:UserRule"), pulumi.Alias(type_="azure-native:network/v20220401preview:UserRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(UserRule, __self__).__init__(
            'azure-native:network/v20210501preview:UserRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserRule':
        """
        Get an existing UserRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserRuleArgs.__new__(UserRuleArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["destination_port_ranges"] = None
        __props__.__dict__["destinations"] = None
        __props__.__dict__["direction"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["protocol"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source_port_ranges"] = None
        __props__.__dict__["sources"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return UserRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for this rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The destination port ranges.
        """
        return pulumi.get(self, "destination_port_ranges")

    @property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Optional[Sequence['outputs.AddressPrefixItemResponse']]]:
        """
        The destination address prefixes. CIDR or destination IP ranges.
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Output[str]:
        """
        Indicates if the traffic matched against the rule in inbound or outbound.
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        A friendly name for the rule.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Whether the rule is custom or default.
        Expected value is 'Custom'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        Network protocol this rule applies to.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the security configuration user rule resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The source port ranges.
        """
        return pulumi.get(self, "source_port_ranges")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Optional[Sequence['outputs.AddressPrefixItemResponse']]]:
        """
        The CIDR or source IP ranges.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

