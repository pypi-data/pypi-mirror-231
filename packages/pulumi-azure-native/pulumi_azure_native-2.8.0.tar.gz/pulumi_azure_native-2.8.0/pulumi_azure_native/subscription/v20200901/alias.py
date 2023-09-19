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

__all__ = ['AliasArgs', 'Alias']

@pulumi.input_type
class AliasArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input['PutAliasRequestPropertiesArgs'],
                 alias_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Alias resource.
        :param pulumi.Input['PutAliasRequestPropertiesArgs'] properties: Put alias request properties.
        :param pulumi.Input[str] alias_name: Name for this subscription creation request also known as alias. Note that this is not the same as subscription name and this doesn’t have any other lifecycle need beyond the request for subscription creation.
        """
        pulumi.set(__self__, "properties", properties)
        if alias_name is not None:
            pulumi.set(__self__, "alias_name", alias_name)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['PutAliasRequestPropertiesArgs']:
        """
        Put alias request properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['PutAliasRequestPropertiesArgs']):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="aliasName")
    def alias_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for this subscription creation request also known as alias. Note that this is not the same as subscription name and this doesn’t have any other lifecycle need beyond the request for subscription creation.
        """
        return pulumi.get(self, "alias_name")

    @alias_name.setter
    def alias_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias_name", value)


class Alias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['PutAliasRequestPropertiesArgs']]] = None,
                 __props__=None):
        """
        Subscription Information with the alias.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias_name: Name for this subscription creation request also known as alias. Note that this is not the same as subscription name and this doesn’t have any other lifecycle need beyond the request for subscription creation.
        :param pulumi.Input[pulumi.InputType['PutAliasRequestPropertiesArgs']] properties: Put alias request properties.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Subscription Information with the alias.

        :param str resource_name: The name of the resource.
        :param AliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['PutAliasRequestPropertiesArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AliasArgs.__new__(AliasArgs)

            __props__.__dict__["alias_name"] = alias_name
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:subscription:Alias"), pulumi.Alias(type_="azure-native:subscription/v20191001preview:Alias"), pulumi.Alias(type_="azure-native:subscription/v20211001:Alias")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Alias, __self__).__init__(
            'azure-native:subscription/v20200901:Alias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Alias':
        """
        Get an existing Alias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AliasArgs.__new__(AliasArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return Alias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Alias ID.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.PutAliasResponsePropertiesResponse']:
        """
        Put Alias response properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type, Microsoft.Subscription/aliases.
        """
        return pulumi.get(self, "type")

