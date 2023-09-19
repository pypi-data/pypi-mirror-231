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

__all__ = ['RuleSetArgs', 'RuleSet']

@pulumi.input_type
class RuleSetArgs:
    def __init__(__self__, *,
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 rule_set_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RuleSet resource.
        :param pulumi.Input[str] profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] rule_set_name: Name of the rule set under the profile which is unique globally
        """
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if rule_set_name is not None:
            pulumi.set(__self__, "rule_set_name", rule_set_name)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="ruleSetName")
    def rule_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the rule set under the profile which is unique globally
        """
        return pulumi.get(self, "rule_set_name")

    @rule_set_name.setter
    def rule_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_set_name", value)


class RuleSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_set_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Friendly RuleSet name mapping to the any RuleSet or secret related information.
        Azure REST API version: 2023-05-01. Prior API version in Azure Native 1.x: 2020-09-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] rule_set_name: Name of the rule set under the profile which is unique globally
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RuleSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Friendly RuleSet name mapping to the any RuleSet or secret related information.
        Azure REST API version: 2023-05-01. Prior API version in Azure Native 1.x: 2020-09-01

        :param str resource_name: The name of the resource.
        :param RuleSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RuleSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_set_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RuleSetArgs.__new__(RuleSetArgs)

            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rule_set_name"] = rule_set_name
            __props__.__dict__["deployment_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn/v20200901:RuleSet"), pulumi.Alias(type_="azure-native:cdn/v20210601:RuleSet"), pulumi.Alias(type_="azure-native:cdn/v20220501preview:RuleSet"), pulumi.Alias(type_="azure-native:cdn/v20221101preview:RuleSet"), pulumi.Alias(type_="azure-native:cdn/v20230501:RuleSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RuleSet, __self__).__init__(
            'azure-native:cdn:RuleSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RuleSet':
        """
        Get an existing RuleSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RuleSetArgs.__new__(RuleSetArgs)

        __props__.__dict__["deployment_status"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["profile_name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return RuleSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[str]:
        """
        The name of the profile which holds the rule set.
        """
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

