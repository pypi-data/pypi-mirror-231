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

__all__ = ['SecurityAdminConfigurationArgs', 'SecurityAdminConfiguration']

@pulumi.input_type
class SecurityAdminConfigurationArgs:
    def __init__(__self__, *,
                 network_manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 apply_on_network_intent_policy_based_services: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'NetworkIntentPolicyBasedService']]]]] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityAdminConfiguration resource.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'NetworkIntentPolicyBasedService']]]] apply_on_network_intent_policy_based_services: Enum list of network intent policy based services.
        :param pulumi.Input[str] configuration_name: The name of the network manager Security Configuration.
        :param pulumi.Input[str] description: A description of the security configuration.
        """
        pulumi.set(__self__, "network_manager_name", network_manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if apply_on_network_intent_policy_based_services is not None:
            pulumi.set(__self__, "apply_on_network_intent_policy_based_services", apply_on_network_intent_policy_based_services)
        if configuration_name is not None:
            pulumi.set(__self__, "configuration_name", configuration_name)
        if description is not None:
            pulumi.set(__self__, "description", description)

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
    @pulumi.getter(name="applyOnNetworkIntentPolicyBasedServices")
    def apply_on_network_intent_policy_based_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'NetworkIntentPolicyBasedService']]]]]:
        """
        Enum list of network intent policy based services.
        """
        return pulumi.get(self, "apply_on_network_intent_policy_based_services")

    @apply_on_network_intent_policy_based_services.setter
    def apply_on_network_intent_policy_based_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'NetworkIntentPolicyBasedService']]]]]):
        pulumi.set(self, "apply_on_network_intent_policy_based_services", value)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network manager Security Configuration.
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the security configuration.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


class SecurityAdminConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apply_on_network_intent_policy_based_services: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'NetworkIntentPolicyBasedService']]]]] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Defines the security admin configuration
        Azure REST API version: 2023-02-01. Prior API version in Azure Native 1.x: 2021-02-01-preview

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'NetworkIntentPolicyBasedService']]]] apply_on_network_intent_policy_based_services: Enum list of network intent policy based services.
        :param pulumi.Input[str] configuration_name: The name of the network manager Security Configuration.
        :param pulumi.Input[str] description: A description of the security configuration.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityAdminConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the security admin configuration
        Azure REST API version: 2023-02-01. Prior API version in Azure Native 1.x: 2021-02-01-preview

        :param str resource_name: The name of the resource.
        :param SecurityAdminConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityAdminConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apply_on_network_intent_policy_based_services: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'NetworkIntentPolicyBasedService']]]]] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityAdminConfigurationArgs.__new__(SecurityAdminConfigurationArgs)

            __props__.__dict__["apply_on_network_intent_policy_based_services"] = apply_on_network_intent_policy_based_services
            __props__.__dict__["configuration_name"] = configuration_name
            __props__.__dict__["description"] = description
            if network_manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_manager_name'")
            __props__.__dict__["network_manager_name"] = network_manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_guid"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network/v20210201preview:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20210501preview:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20220101:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20220201preview:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20220401preview:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20220501:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20220701:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20220901:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20221101:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20230201:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20230401:SecurityAdminConfiguration"), pulumi.Alias(type_="azure-native:network/v20230501:SecurityAdminConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SecurityAdminConfiguration, __self__).__init__(
            'azure-native:network:SecurityAdminConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityAdminConfiguration':
        """
        Get an existing SecurityAdminConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityAdminConfigurationArgs.__new__(SecurityAdminConfigurationArgs)

        __props__.__dict__["apply_on_network_intent_policy_based_services"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SecurityAdminConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applyOnNetworkIntentPolicyBasedServices")
    def apply_on_network_intent_policy_based_services(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Enum list of network intent policy based services.
        """
        return pulumi.get(self, "apply_on_network_intent_policy_based_services")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the security configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        Unique identifier for this resource.
        """
        return pulumi.get(self, "resource_guid")

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

