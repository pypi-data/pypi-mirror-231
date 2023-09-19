# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WebAppDomainOwnershipIdentifierArgs', 'WebAppDomainOwnershipIdentifier']

@pulumi.input_type
class WebAppDomainOwnershipIdentifierArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 domain_ownership_identifier_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebAppDomainOwnershipIdentifier resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] domain_ownership_identifier_name: Name of domain ownership identifier.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] value: String representation of the identity.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if domain_ownership_identifier_name is not None:
            pulumi.set(__self__, "domain_ownership_identifier_name", domain_ownership_identifier_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the app.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="domainOwnershipIdentifierName")
    def domain_ownership_identifier_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of domain ownership identifier.
        """
        return pulumi.get(self, "domain_ownership_identifier_name")

    @domain_ownership_identifier_name.setter
    def domain_ownership_identifier_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_ownership_identifier_name", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        String representation of the identity.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class WebAppDomainOwnershipIdentifier(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_ownership_identifier_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A domain specific resource identifier.
        Azure REST API version: 2022-09-01. Prior API version in Azure Native 1.x: 2020-12-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_ownership_identifier_name: Name of domain ownership identifier.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] value: String representation of the identity.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAppDomainOwnershipIdentifierArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A domain specific resource identifier.
        Azure REST API version: 2022-09-01. Prior API version in Azure Native 1.x: 2020-12-01

        :param str resource_name: The name of the resource.
        :param WebAppDomainOwnershipIdentifierArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAppDomainOwnershipIdentifierArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_ownership_identifier_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebAppDomainOwnershipIdentifierArgs.__new__(WebAppDomainOwnershipIdentifierArgs)

            __props__.__dict__["domain_ownership_identifier_name"] = domain_ownership_identifier_name
            __props__.__dict__["kind"] = kind
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["value"] = value
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web/v20160801:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20180201:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20181101:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20190801:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20200601:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20200901:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20201001:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20201201:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20210101:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20210115:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20210201:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20210301:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20220301:WebAppDomainOwnershipIdentifier"), pulumi.Alias(type_="azure-native:web/v20220901:WebAppDomainOwnershipIdentifier")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WebAppDomainOwnershipIdentifier, __self__).__init__(
            'azure-native:web:WebAppDomainOwnershipIdentifier',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebAppDomainOwnershipIdentifier':
        """
        Get an existing WebAppDomainOwnershipIdentifier resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebAppDomainOwnershipIdentifierArgs.__new__(WebAppDomainOwnershipIdentifierArgs)

        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["value"] = None
        return WebAppDomainOwnershipIdentifier(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[str]]:
        """
        String representation of the identity.
        """
        return pulumi.get(self, "value")

