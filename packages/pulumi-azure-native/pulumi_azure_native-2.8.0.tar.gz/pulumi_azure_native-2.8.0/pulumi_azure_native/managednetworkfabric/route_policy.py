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

__all__ = ['RoutePolicyArgs', 'RoutePolicy']

@pulumi.input_type
class RoutePolicyArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 statements: pulumi.Input[Sequence[pulumi.Input['RoutePolicyStatementPropertiesArgs']]],
                 annotation: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 route_policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a RoutePolicy resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['RoutePolicyStatementPropertiesArgs']]] statements: Route Policy statements.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] route_policy_name: Name of the Route Policy
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "statements", statements)
        if annotation is not None:
            pulumi.set(__self__, "annotation", annotation)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if route_policy_name is not None:
            pulumi.set(__self__, "route_policy_name", route_policy_name)
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
    @pulumi.getter
    def statements(self) -> pulumi.Input[Sequence[pulumi.Input['RoutePolicyStatementPropertiesArgs']]]:
        """
        Route Policy statements.
        """
        return pulumi.get(self, "statements")

    @statements.setter
    def statements(self, value: pulumi.Input[Sequence[pulumi.Input['RoutePolicyStatementPropertiesArgs']]]):
        pulumi.set(self, "statements", value)

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
    @pulumi.getter(name="routePolicyName")
    def route_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Route Policy
        """
        return pulumi.get(self, "route_policy_name")

    @route_policy_name.setter
    def route_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_policy_name", value)

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


class RoutePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_policy_name: Optional[pulumi.Input[str]] = None,
                 statements: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutePolicyStatementPropertiesArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The RoutePolicy resource definition.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] route_policy_name: Name of the Route Policy
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutePolicyStatementPropertiesArgs']]]] statements: Route Policy statements.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoutePolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The RoutePolicy resource definition.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview

        :param str resource_name: The name of the resource.
        :param RoutePolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoutePolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_policy_name: Optional[pulumi.Input[str]] = None,
                 statements: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutePolicyStatementPropertiesArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoutePolicyArgs.__new__(RoutePolicyArgs)

            __props__.__dict__["annotation"] = annotation
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["route_policy_name"] = route_policy_name
            if statements is None and not opts.urn:
                raise TypeError("Missing required property 'statements'")
            __props__.__dict__["statements"] = statements
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetworkfabric/v20230201preview:RoutePolicy"), pulumi.Alias(type_="azure-native:managednetworkfabric/v20230615:RoutePolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RoutePolicy, __self__).__init__(
            'azure-native:managednetworkfabric:RoutePolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RoutePolicy':
        """
        Get an existing RoutePolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RoutePolicyArgs.__new__(RoutePolicyArgs)

        __props__.__dict__["annotation"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["statements"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return RoutePolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

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
        Gets the provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def statements(self) -> pulumi.Output[Sequence['outputs.RoutePolicyStatementPropertiesResponse']]:
        """
        Route Policy statements.
        """
        return pulumi.get(self, "statements")

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

