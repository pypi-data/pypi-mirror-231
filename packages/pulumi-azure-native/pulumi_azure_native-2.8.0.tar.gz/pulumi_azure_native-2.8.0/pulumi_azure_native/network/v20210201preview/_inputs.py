# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AddressPrefixItemArgs',
    'ConnectivityGroupItemArgs',
    'GroupMembersItemArgs',
    'HubArgs',
    'NetworkManagerPropertiesNetworkManagerScopesArgs',
    'NetworkManagerSecurityGroupItemArgs',
    'SubResourceArgs',
    'SubscriptionIdArgs',
]

@pulumi.input_type
class AddressPrefixItemArgs:
    def __init__(__self__, *,
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 address_prefix_type: Optional[pulumi.Input[Union[str, 'AddressPrefixType']]] = None):
        """
        Address prefix item.
        :param pulumi.Input[str] address_prefix: Address prefix.
        :param pulumi.Input[Union[str, 'AddressPrefixType']] address_prefix_type: Address prefix type.
        """
        if address_prefix is not None:
            pulumi.set(__self__, "address_prefix", address_prefix)
        if address_prefix_type is not None:
            pulumi.set(__self__, "address_prefix_type", address_prefix_type)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Address prefix.
        """
        return pulumi.get(self, "address_prefix")

    @address_prefix.setter
    def address_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_prefix", value)

    @property
    @pulumi.getter(name="addressPrefixType")
    def address_prefix_type(self) -> Optional[pulumi.Input[Union[str, 'AddressPrefixType']]]:
        """
        Address prefix type.
        """
        return pulumi.get(self, "address_prefix_type")

    @address_prefix_type.setter
    def address_prefix_type(self, value: Optional[pulumi.Input[Union[str, 'AddressPrefixType']]]):
        pulumi.set(self, "address_prefix_type", value)


@pulumi.input_type
class ConnectivityGroupItemArgs:
    def __init__(__self__, *,
                 group_connectivity: Optional[pulumi.Input[Union[str, 'GroupConnectivity']]] = None,
                 is_global: Optional[pulumi.Input[Union[str, 'IsGlobal']]] = None,
                 network_group_id: Optional[pulumi.Input[str]] = None,
                 use_hub_gateway: Optional[pulumi.Input[Union[str, 'UseHubGateway']]] = None):
        """
        :param pulumi.Input[Union[str, 'GroupConnectivity']] group_connectivity: Group connectivity type.
        :param pulumi.Input[Union[str, 'IsGlobal']] is_global: Flag if global is supported.
        :param pulumi.Input[str] network_group_id: Network group Id.
        :param pulumi.Input[Union[str, 'UseHubGateway']] use_hub_gateway: Flag if need to use hub gateway.
        """
        if group_connectivity is not None:
            pulumi.set(__self__, "group_connectivity", group_connectivity)
        if is_global is not None:
            pulumi.set(__self__, "is_global", is_global)
        if network_group_id is not None:
            pulumi.set(__self__, "network_group_id", network_group_id)
        if use_hub_gateway is not None:
            pulumi.set(__self__, "use_hub_gateway", use_hub_gateway)

    @property
    @pulumi.getter(name="groupConnectivity")
    def group_connectivity(self) -> Optional[pulumi.Input[Union[str, 'GroupConnectivity']]]:
        """
        Group connectivity type.
        """
        return pulumi.get(self, "group_connectivity")

    @group_connectivity.setter
    def group_connectivity(self, value: Optional[pulumi.Input[Union[str, 'GroupConnectivity']]]):
        pulumi.set(self, "group_connectivity", value)

    @property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[pulumi.Input[Union[str, 'IsGlobal']]]:
        """
        Flag if global is supported.
        """
        return pulumi.get(self, "is_global")

    @is_global.setter
    def is_global(self, value: Optional[pulumi.Input[Union[str, 'IsGlobal']]]):
        pulumi.set(self, "is_global", value)

    @property
    @pulumi.getter(name="networkGroupId")
    def network_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Network group Id.
        """
        return pulumi.get(self, "network_group_id")

    @network_group_id.setter
    def network_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_group_id", value)

    @property
    @pulumi.getter(name="useHubGateway")
    def use_hub_gateway(self) -> Optional[pulumi.Input[Union[str, 'UseHubGateway']]]:
        """
        Flag if need to use hub gateway.
        """
        return pulumi.get(self, "use_hub_gateway")

    @use_hub_gateway.setter
    def use_hub_gateway(self, value: Optional[pulumi.Input[Union[str, 'UseHubGateway']]]):
        pulumi.set(self, "use_hub_gateway", value)


@pulumi.input_type
class GroupMembersItemArgs:
    def __init__(__self__, *,
                 resource_id: Optional[pulumi.Input[str]] = None):
        """
        GroupMembers Item.
        :param pulumi.Input[str] resource_id: Resource Id.
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)


@pulumi.input_type
class HubArgs:
    def __init__(__self__, *,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None):
        """
        Hub Item.
        :param pulumi.Input[str] resource_id: Resource Id.
        :param pulumi.Input[str] resource_type: Resource Type.
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Type.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)


@pulumi.input_type
class NetworkManagerPropertiesNetworkManagerScopesArgs:
    def __init__(__self__, *,
                 management_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Scope of Network Manager.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] management_groups: List of management groups.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subscriptions: List of subscriptions.
        """
        if management_groups is not None:
            pulumi.set(__self__, "management_groups", management_groups)
        if subscriptions is not None:
            pulumi.set(__self__, "subscriptions", subscriptions)

    @property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of management groups.
        """
        return pulumi.get(self, "management_groups")

    @management_groups.setter
    def management_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "management_groups", value)

    @property
    @pulumi.getter
    def subscriptions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of subscriptions.
        """
        return pulumi.get(self, "subscriptions")

    @subscriptions.setter
    def subscriptions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subscriptions", value)


@pulumi.input_type
class NetworkManagerSecurityGroupItemArgs:
    def __init__(__self__, *,
                 network_group_id: Optional[pulumi.Input[str]] = None):
        """
        Network manager security group item.
        :param pulumi.Input[str] network_group_id: Network manager group Id.
        """
        if network_group_id is not None:
            pulumi.set(__self__, "network_group_id", network_group_id)

    @property
    @pulumi.getter(name="networkGroupId")
    def network_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Network manager group Id.
        """
        return pulumi.get(self, "network_group_id")

    @network_group_id.setter
    def network_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_group_id", value)


@pulumi.input_type
class SubResourceArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        Reference to another subresource.
        :param pulumi.Input[str] id: Sub-resource ID. Both absolute resource ID and a relative resource ID are accepted.
               An absolute ID starts with /subscriptions/ and contains the entire ID of the parent resource and the ID of the sub-resource in the end.
               A relative ID replaces the ID of the parent resource with a token '$self', followed by the sub-resource ID itself.
               Example of a relative ID: $self/frontEndConfigurations/my-frontend.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Sub-resource ID. Both absolute resource ID and a relative resource ID are accepted.
        An absolute ID starts with /subscriptions/ and contains the entire ID of the parent resource and the ID of the sub-resource in the end.
        A relative ID replaces the ID of the parent resource with a token '$self', followed by the sub-resource ID itself.
        Example of a relative ID: $self/frontEndConfigurations/my-frontend.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class SubscriptionIdArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] id: Subscription id in the ARM id format.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Subscription id in the ARM id format.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


