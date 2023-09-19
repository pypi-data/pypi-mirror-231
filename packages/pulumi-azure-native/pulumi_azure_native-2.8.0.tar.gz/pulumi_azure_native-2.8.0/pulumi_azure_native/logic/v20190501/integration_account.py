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

__all__ = ['IntegrationAccountArgs', 'IntegrationAccount']

@pulumi.input_type
class IntegrationAccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 integration_service_environment: Optional[pulumi.Input['ResourceReferenceArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['IntegrationAccountSkuArgs']] = None,
                 state: Optional[pulumi.Input[Union[str, 'WorkflowState']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a IntegrationAccount resource.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input['ResourceReferenceArgs'] integration_service_environment: The integration service environment.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input['IntegrationAccountSkuArgs'] sku: The sku.
        :param pulumi.Input[Union[str, 'WorkflowState']] state: The workflow state.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if integration_account_name is not None:
            pulumi.set(__self__, "integration_account_name", integration_account_name)
        if integration_service_environment is not None:
            pulumi.set(__self__, "integration_service_environment", integration_service_environment)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The integration account name.
        """
        return pulumi.get(self, "integration_account_name")

    @integration_account_name.setter
    def integration_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_account_name", value)

    @property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(self) -> Optional[pulumi.Input['ResourceReferenceArgs']]:
        """
        The integration service environment.
        """
        return pulumi.get(self, "integration_service_environment")

    @integration_service_environment.setter
    def integration_service_environment(self, value: Optional[pulumi.Input['ResourceReferenceArgs']]):
        pulumi.set(self, "integration_service_environment", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['IntegrationAccountSkuArgs']]:
        """
        The sku.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['IntegrationAccountSkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'WorkflowState']]]:
        """
        The workflow state.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'WorkflowState']]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class IntegrationAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 integration_service_environment: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['IntegrationAccountSkuArgs']]] = None,
                 state: Optional[pulumi.Input[Union[str, 'WorkflowState']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The integration account.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input[pulumi.InputType['ResourceReferenceArgs']] integration_service_environment: The integration service environment.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[pulumi.InputType['IntegrationAccountSkuArgs']] sku: The sku.
        :param pulumi.Input[Union[str, 'WorkflowState']] state: The workflow state.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The integration account.

        :param str resource_name: The name of the resource.
        :param IntegrationAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 integration_service_environment: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['IntegrationAccountSkuArgs']]] = None,
                 state: Optional[pulumi.Input[Union[str, 'WorkflowState']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationAccountArgs.__new__(IntegrationAccountArgs)

            __props__.__dict__["integration_account_name"] = integration_account_name
            __props__.__dict__["integration_service_environment"] = integration_service_environment
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["state"] = state
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:logic:IntegrationAccount"), pulumi.Alias(type_="azure-native:logic/v20150801preview:IntegrationAccount"), pulumi.Alias(type_="azure-native:logic/v20160601:IntegrationAccount"), pulumi.Alias(type_="azure-native:logic/v20180701preview:IntegrationAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IntegrationAccount, __self__).__init__(
            'azure-native:logic/v20190501:IntegrationAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IntegrationAccount':
        """
        Get an existing IntegrationAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IntegrationAccountArgs.__new__(IntegrationAccountArgs)

        __props__.__dict__["integration_service_environment"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return IntegrationAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(self) -> pulumi.Output[Optional['outputs.ResourceReferenceResponse']]:
        """
        The integration service environment.
        """
        return pulumi.get(self, "integration_service_environment")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.IntegrationAccountSkuResponse']]:
        """
        The sku.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        The workflow state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")

