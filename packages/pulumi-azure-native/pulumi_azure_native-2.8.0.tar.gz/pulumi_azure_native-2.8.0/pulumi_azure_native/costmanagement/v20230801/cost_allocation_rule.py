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

__all__ = ['CostAllocationRuleArgs', 'CostAllocationRule']

@pulumi.input_type
class CostAllocationRuleArgs:
    def __init__(__self__, *,
                 billing_account_id: pulumi.Input[str],
                 properties: Optional[pulumi.Input['CostAllocationRulePropertiesArgs']] = None,
                 rule_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CostAllocationRule resource.
        :param pulumi.Input[str] billing_account_id: BillingAccount ID
        :param pulumi.Input['CostAllocationRulePropertiesArgs'] properties: Cost allocation rule properties
        :param pulumi.Input[str] rule_name: Cost allocation rule name. The name cannot include spaces or any non alphanumeric characters other than '_' and '-'. The max length is 260 characters.
        """
        pulumi.set(__self__, "billing_account_id", billing_account_id)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)

    @property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Input[str]:
        """
        BillingAccount ID
        """
        return pulumi.get(self, "billing_account_id")

    @billing_account_id.setter
    def billing_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_account_id", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['CostAllocationRulePropertiesArgs']]:
        """
        Cost allocation rule properties
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['CostAllocationRulePropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        Cost allocation rule name. The name cannot include spaces or any non alphanumeric characters other than '_' and '-'. The max length is 260 characters.
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)


class CostAllocationRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account_id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['CostAllocationRulePropertiesArgs']]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The cost allocation rule model definition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] billing_account_id: BillingAccount ID
        :param pulumi.Input[pulumi.InputType['CostAllocationRulePropertiesArgs']] properties: Cost allocation rule properties
        :param pulumi.Input[str] rule_name: Cost allocation rule name. The name cannot include spaces or any non alphanumeric characters other than '_' and '-'. The max length is 260 characters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CostAllocationRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The cost allocation rule model definition

        :param str resource_name: The name of the resource.
        :param CostAllocationRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CostAllocationRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account_id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['CostAllocationRulePropertiesArgs']]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CostAllocationRuleArgs.__new__(CostAllocationRuleArgs)

            if billing_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'billing_account_id'")
            __props__.__dict__["billing_account_id"] = billing_account_id
            __props__.__dict__["properties"] = properties
            __props__.__dict__["rule_name"] = rule_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:costmanagement:CostAllocationRule"), pulumi.Alias(type_="azure-native:costmanagement/v20200301preview:CostAllocationRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CostAllocationRule, __self__).__init__(
            'azure-native:costmanagement/v20230801:CostAllocationRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CostAllocationRule':
        """
        Get an existing CostAllocationRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CostAllocationRuleArgs.__new__(CostAllocationRuleArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return CostAllocationRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the rule. This is a read only value.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.CostAllocationRulePropertiesResponse']:
        """
        Cost allocation rule properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type of the rule. This is a read only value of Microsoft.CostManagement/CostAllocationRule.
        """
        return pulumi.get(self, "type")

