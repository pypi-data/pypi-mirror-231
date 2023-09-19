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

__all__ = ['InternetGatewayRuleArgs', 'InternetGatewayRule']

@pulumi.input_type
class InternetGatewayRuleArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 rule_properties: pulumi.Input['RulePropertiesArgs'],
                 annotation: Optional[pulumi.Input[str]] = None,
                 internet_gateway_rule_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a InternetGatewayRule resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['RulePropertiesArgs'] rule_properties: Rules for the InternetGateways
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] internet_gateway_rule_name: Name of the Internet Gateway rule.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "rule_properties", rule_properties)
        if annotation is not None:
            pulumi.set(__self__, "annotation", annotation)
        if internet_gateway_rule_name is not None:
            pulumi.set(__self__, "internet_gateway_rule_name", internet_gateway_rule_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
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
    @pulumi.getter(name="ruleProperties")
    def rule_properties(self) -> pulumi.Input['RulePropertiesArgs']:
        """
        Rules for the InternetGateways
        """
        return pulumi.get(self, "rule_properties")

    @rule_properties.setter
    def rule_properties(self, value: pulumi.Input['RulePropertiesArgs']):
        pulumi.set(self, "rule_properties", value)

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
    @pulumi.getter(name="internetGatewayRuleName")
    def internet_gateway_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Internet Gateway rule.
        """
        return pulumi.get(self, "internet_gateway_rule_name")

    @internet_gateway_rule_name.setter
    def internet_gateway_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "internet_gateway_rule_name", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class InternetGatewayRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 internet_gateway_rule_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_properties: Optional[pulumi.Input[pulumi.InputType['RulePropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The Internet Gateway Rule resource definition.
        Azure REST API version: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] internet_gateway_rule_name: Name of the Internet Gateway rule.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['RulePropertiesArgs']] rule_properties: Rules for the InternetGateways
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InternetGatewayRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Internet Gateway Rule resource definition.
        Azure REST API version: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param InternetGatewayRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InternetGatewayRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 internet_gateway_rule_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_properties: Optional[pulumi.Input[pulumi.InputType['RulePropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InternetGatewayRuleArgs.__new__(InternetGatewayRuleArgs)

            __props__.__dict__["annotation"] = annotation
            __props__.__dict__["internet_gateway_rule_name"] = internet_gateway_rule_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if rule_properties is None and not opts.urn:
                raise TypeError("Missing required property 'rule_properties'")
            __props__.__dict__["rule_properties"] = rule_properties
            __props__.__dict__["tags"] = tags
            __props__.__dict__["internet_gateway_ids"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetworkfabric/v20230615:InternetGatewayRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(InternetGatewayRule, __self__).__init__(
            'azure-native:managednetworkfabric:InternetGatewayRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InternetGatewayRule':
        """
        Get an existing InternetGatewayRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InternetGatewayRuleArgs.__new__(InternetGatewayRuleArgs)

        __props__.__dict__["annotation"] = None
        __props__.__dict__["internet_gateway_ids"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rule_properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return InternetGatewayRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="internetGatewayIds")
    def internet_gateway_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        List of Internet Gateway resource Id.
        """
        return pulumi.get(self, "internet_gateway_ids")

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
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ruleProperties")
    def rule_properties(self) -> pulumi.Output['outputs.RulePropertiesResponse']:
        """
        Rules for the InternetGateways
        """
        return pulumi.get(self, "rule_properties")

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

