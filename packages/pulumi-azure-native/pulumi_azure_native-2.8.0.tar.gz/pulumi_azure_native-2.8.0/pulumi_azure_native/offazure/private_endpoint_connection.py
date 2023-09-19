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

__all__ = ['PrivateEndpointConnectionArgs', 'PrivateEndpointConnection']

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 site_name: pulumi.Input[str],
                 pe_connection_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PrivateEndpointConnection resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] site_name: Site name.
        :param pulumi.Input[str] pe_connection_name: Private link resource name.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "site_name", site_name)
        if pe_connection_name is not None:
            pulumi.set(__self__, "pe_connection_name", pe_connection_name)

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
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Input[str]:
        """
        Site name.
        """
        return pulumi.get(self, "site_name")

    @site_name.setter
    def site_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "site_name", value)

    @property
    @pulumi.getter(name="peConnectionName")
    def pe_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        Private link resource name.
        """
        return pulumi.get(self, "pe_connection_name")

    @pe_connection_name.setter
    def pe_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pe_connection_name", value)


class PrivateEndpointConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pe_connection_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        REST model used to encapsulate the user visible state of a PrivateEndpoint.
        Azure REST API version: 2020-07-07. Prior API version in Azure Native 1.x: 2020-07-07

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] pe_connection_name: Private link resource name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] site_name: Site name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateEndpointConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        REST model used to encapsulate the user visible state of a PrivateEndpoint.
        Azure REST API version: 2020-07-07. Prior API version in Azure Native 1.x: 2020-07-07

        :param str resource_name: The name of the resource.
        :param PrivateEndpointConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateEndpointConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pe_connection_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateEndpointConnectionArgs.__new__(PrivateEndpointConnectionArgs)

            __props__.__dict__["pe_connection_name"] = pe_connection_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if site_name is None and not opts.urn:
                raise TypeError("Missing required property 'site_name'")
            __props__.__dict__["site_name"] = site_name
            __props__.__dict__["e_tag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["properties"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:offazure/v20200707:PrivateEndpointConnection"), pulumi.Alias(type_="azure-native:offazure/v20230606:PrivateEndpointConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateEndpointConnection, __self__).__init__(
            'azure-native:offazure:PrivateEndpointConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateEndpointConnection':
        """
        Get an existing PrivateEndpointConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateEndpointConnectionArgs.__new__(PrivateEndpointConnectionArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PrivateEndpointConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[str]:
        """
        Gets the tag for optimistic concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.PrivateEndpointConnectionPropertiesResponse']:
        """
        Gets the properties of the object.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")

