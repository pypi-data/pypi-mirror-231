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
from ._enums import *
from ._inputs import *

__all__ = ['ManagedNetworkGroupArgs', 'ManagedNetworkGroup']

@pulumi.input_type
class ManagedNetworkGroupArgs:
    def __init__(__self__, *,
                 managed_network_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_network_group_name: Optional[pulumi.Input[str]] = None,
                 management_groups: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]] = None,
                 subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]] = None,
                 virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]] = None):
        """
        The set of arguments for constructing a ManagedNetworkGroup resource.
        :param pulumi.Input[str] managed_network_name: The name of the Managed Network.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[str, 'Kind']] kind: Responsibility role under which this Managed Network Group will be created
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] managed_network_group_name: The name of the Managed Network Group.
        :param pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]] management_groups: The collection of management groups covered by the Managed Network
        :param pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]] subnets: The collection of  subnets covered by the Managed Network
        :param pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]] subscriptions: The collection of subscriptions covered by the Managed Network
        :param pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]] virtual_networks: The collection of virtual nets covered by the Managed Network
        """
        pulumi.set(__self__, "managed_network_name", managed_network_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_network_group_name is not None:
            pulumi.set(__self__, "managed_network_group_name", managed_network_group_name)
        if management_groups is not None:
            pulumi.set(__self__, "management_groups", management_groups)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if subscriptions is not None:
            pulumi.set(__self__, "subscriptions", subscriptions)
        if virtual_networks is not None:
            pulumi.set(__self__, "virtual_networks", virtual_networks)

    @property
    @pulumi.getter(name="managedNetworkName")
    def managed_network_name(self) -> pulumi.Input[str]:
        """
        The name of the Managed Network.
        """
        return pulumi.get(self, "managed_network_name")

    @managed_network_name.setter
    def managed_network_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_network_name", value)

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
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'Kind']]]:
        """
        Responsibility role under which this Managed Network Group will be created
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'Kind']]]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="managedNetworkGroupName")
    def managed_network_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Managed Network Group.
        """
        return pulumi.get(self, "managed_network_group_name")

    @managed_network_group_name.setter
    def managed_network_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_network_group_name", value)

    @property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]]:
        """
        The collection of management groups covered by the Managed Network
        """
        return pulumi.get(self, "management_groups")

    @management_groups.setter
    def management_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]]):
        pulumi.set(self, "management_groups", value)

    @property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]]:
        """
        The collection of  subnets covered by the Managed Network
        """
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]]):
        pulumi.set(self, "subnets", value)

    @property
    @pulumi.getter
    def subscriptions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]]:
        """
        The collection of subscriptions covered by the Managed Network
        """
        return pulumi.get(self, "subscriptions")

    @subscriptions.setter
    def subscriptions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]]):
        pulumi.set(self, "subscriptions", value)

    @property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]]:
        """
        The collection of virtual nets covered by the Managed Network
        """
        return pulumi.get(self, "virtual_networks")

    @virtual_networks.setter
    def virtual_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceIdArgs']]]]):
        pulumi.set(self, "virtual_networks", value)


class ManagedNetworkGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_network_group_name: Optional[pulumi.Input[str]] = None,
                 managed_network_name: Optional[pulumi.Input[str]] = None,
                 management_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]]] = None,
                 subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]]] = None,
                 virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]]] = None,
                 __props__=None):
        """
        The Managed Network Group resource
        Azure REST API version: 2019-06-01-preview. Prior API version in Azure Native 1.x: 2019-06-01-preview

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'Kind']] kind: Responsibility role under which this Managed Network Group will be created
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] managed_network_group_name: The name of the Managed Network Group.
        :param pulumi.Input[str] managed_network_name: The name of the Managed Network.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]] management_groups: The collection of management groups covered by the Managed Network
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]] subnets: The collection of  subnets covered by the Managed Network
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]] subscriptions: The collection of subscriptions covered by the Managed Network
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]] virtual_networks: The collection of virtual nets covered by the Managed Network
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedNetworkGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Managed Network Group resource
        Azure REST API version: 2019-06-01-preview. Prior API version in Azure Native 1.x: 2019-06-01-preview

        :param str resource_name: The name of the resource.
        :param ManagedNetworkGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedNetworkGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_network_group_name: Optional[pulumi.Input[str]] = None,
                 managed_network_name: Optional[pulumi.Input[str]] = None,
                 management_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]]] = None,
                 subscriptions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]]] = None,
                 virtual_networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceIdArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedNetworkGroupArgs.__new__(ManagedNetworkGroupArgs)

            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["managed_network_group_name"] = managed_network_group_name
            if managed_network_name is None and not opts.urn:
                raise TypeError("Missing required property 'managed_network_name'")
            __props__.__dict__["managed_network_name"] = managed_network_name
            __props__.__dict__["management_groups"] = management_groups
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["subnets"] = subnets
            __props__.__dict__["subscriptions"] = subscriptions
            __props__.__dict__["virtual_networks"] = virtual_networks
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetwork/v20190601preview:ManagedNetworkGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedNetworkGroup, __self__).__init__(
            'azure-native:managednetwork:ManagedNetworkGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedNetworkGroup':
        """
        Get an existing ManagedNetworkGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedNetworkGroupArgs.__new__(ManagedNetworkGroupArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["management_groups"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["subnets"] = None
        __props__.__dict__["subscriptions"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_networks"] = None
        return ManagedNetworkGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Responsibility role under which this Managed Network Group will be created
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> pulumi.Output[Optional[Sequence['outputs.ResourceIdResponse']]]:
        """
        The collection of management groups covered by the Managed Network
        """
        return pulumi.get(self, "management_groups")

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
        Provisioning state of the ManagedNetwork resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Optional[Sequence['outputs.ResourceIdResponse']]]:
        """
        The collection of  subnets covered by the Managed Network
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def subscriptions(self) -> pulumi.Output[Optional[Sequence['outputs.ResourceIdResponse']]]:
        """
        The collection of subscriptions covered by the Managed Network
        """
        return pulumi.get(self, "subscriptions")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> pulumi.Output[Optional[Sequence['outputs.ResourceIdResponse']]]:
        """
        The collection of virtual nets covered by the Managed Network
        """
        return pulumi.get(self, "virtual_networks")

