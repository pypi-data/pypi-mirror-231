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
from ._inputs import *

__all__ = ['ConnectedEnvironmentsCertificateArgs', 'ConnectedEnvironmentsCertificate']

@pulumi.input_type
class ConnectedEnvironmentsCertificateArgs:
    def __init__(__self__, *,
                 connected_environment_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['CertificatePropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ConnectedEnvironmentsCertificate resource.
        :param pulumi.Input[str] connected_environment_name: Name of the Connected Environment.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] certificate_name: Name of the Certificate.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['CertificatePropertiesArgs'] properties: Certificate resource specific properties
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "connected_environment_name", connected_environment_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if certificate_name is not None:
            pulumi.set(__self__, "certificate_name", certificate_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="connectedEnvironmentName")
    def connected_environment_name(self) -> pulumi.Input[str]:
        """
        Name of the Connected Environment.
        """
        return pulumi.get(self, "connected_environment_name")

    @connected_environment_name.setter
    def connected_environment_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "connected_environment_name", value)

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
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Certificate.
        """
        return pulumi.get(self, "certificate_name")

    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_name", value)

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
    def properties(self) -> Optional[pulumi.Input['CertificatePropertiesArgs']]:
        """
        Certificate resource specific properties
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['CertificatePropertiesArgs']]):
        pulumi.set(self, "properties", value)

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


class ConnectedEnvironmentsCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 connected_environment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['CertificatePropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Certificate used for Custom Domain bindings of Container Apps in a Managed Environment

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_name: Name of the Certificate.
        :param pulumi.Input[str] connected_environment_name: Name of the Connected Environment.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['CertificatePropertiesArgs']] properties: Certificate resource specific properties
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectedEnvironmentsCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Certificate used for Custom Domain bindings of Container Apps in a Managed Environment

        :param str resource_name: The name of the resource.
        :param ConnectedEnvironmentsCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectedEnvironmentsCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 connected_environment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['CertificatePropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectedEnvironmentsCertificateArgs.__new__(ConnectedEnvironmentsCertificateArgs)

            __props__.__dict__["certificate_name"] = certificate_name
            if connected_environment_name is None and not opts.urn:
                raise TypeError("Missing required property 'connected_environment_name'")
            __props__.__dict__["connected_environment_name"] = connected_environment_name
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app:ConnectedEnvironmentsCertificate"), pulumi.Alias(type_="azure-native:app/v20220601preview:ConnectedEnvironmentsCertificate"), pulumi.Alias(type_="azure-native:app/v20221001:ConnectedEnvironmentsCertificate"), pulumi.Alias(type_="azure-native:app/v20221101preview:ConnectedEnvironmentsCertificate"), pulumi.Alias(type_="azure-native:app/v20230501:ConnectedEnvironmentsCertificate"), pulumi.Alias(type_="azure-native:app/v20230502preview:ConnectedEnvironmentsCertificate")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConnectedEnvironmentsCertificate, __self__).__init__(
            'azure-native:app/v20230401preview:ConnectedEnvironmentsCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectedEnvironmentsCertificate':
        """
        Get an existing ConnectedEnvironmentsCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectedEnvironmentsCertificateArgs.__new__(ConnectedEnvironmentsCertificateArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ConnectedEnvironmentsCertificate(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.CertificateResponseProperties']:
        """
        Certificate resource specific properties
        """
        return pulumi.get(self, "properties")

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

