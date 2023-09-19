# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ComponentLinkedStorageAccountArgs', 'ComponentLinkedStorageAccount']

@pulumi.input_type
class ComponentLinkedStorageAccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 linked_storage_account: Optional[pulumi.Input[str]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ComponentLinkedStorageAccount resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name: The name of the Application Insights component resource.
        :param pulumi.Input[str] linked_storage_account: Linked storage account resource ID
        :param pulumi.Input[str] storage_type: The type of the Application Insights component data source for the linked storage account.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if linked_storage_account is not None:
            pulumi.set(__self__, "linked_storage_account", linked_storage_account)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)

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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the Application Insights component resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="linkedStorageAccount")
    def linked_storage_account(self) -> Optional[pulumi.Input[str]]:
        """
        Linked storage account resource ID
        """
        return pulumi.get(self, "linked_storage_account")

    @linked_storage_account.setter
    def linked_storage_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "linked_storage_account", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the Application Insights component data source for the linked storage account.
        """
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)


class ComponentLinkedStorageAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 linked_storage_account: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Application Insights component linked storage accounts

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] linked_storage_account: Linked storage account resource ID
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the Application Insights component resource.
        :param pulumi.Input[str] storage_type: The type of the Application Insights component data source for the linked storage account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComponentLinkedStorageAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Application Insights component linked storage accounts

        :param str resource_name: The name of the resource.
        :param ComponentLinkedStorageAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentLinkedStorageAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 linked_storage_account: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentLinkedStorageAccountArgs.__new__(ComponentLinkedStorageAccountArgs)

            __props__.__dict__["linked_storage_account"] = linked_storage_account
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["storage_type"] = storage_type
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights:ComponentLinkedStorageAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ComponentLinkedStorageAccount, __self__).__init__(
            'azure-native:insights/v20200301preview:ComponentLinkedStorageAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ComponentLinkedStorageAccount':
        """
        Get an existing ComponentLinkedStorageAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ComponentLinkedStorageAccountArgs.__new__(ComponentLinkedStorageAccountArgs)

        __props__.__dict__["linked_storage_account"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return ComponentLinkedStorageAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="linkedStorageAccount")
    def linked_storage_account(self) -> pulumi.Output[Optional[str]]:
        """
        Linked storage account resource ID
        """
        return pulumi.get(self, "linked_storage_account")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

