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

__all__ = ['MediaServiceArgs', 'MediaService']

@pulumi.input_type
class MediaServiceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 media_service_name: Optional[pulumi.Input[str]] = None,
                 storage_accounts: Optional[pulumi.Input[Sequence[pulumi.Input['StorageAccountArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MediaService resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the Azure subscription.
        :param pulumi.Input[str] location: The geographic location of the resource. This must be one of the supported and registered Azure Geo Regions (for example, West US, East US, Southeast Asia, and so forth).
        :param pulumi.Input[str] media_service_name: Name of the Media Service.
        :param pulumi.Input[Sequence[pulumi.Input['StorageAccountArgs']]] storage_accounts: The storage accounts for this resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags to help categorize the resource in the Azure portal.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if media_service_name is not None:
            pulumi.set(__self__, "media_service_name", media_service_name)
        if storage_accounts is not None:
            pulumi.set(__self__, "storage_accounts", storage_accounts)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geographic location of the resource. This must be one of the supported and registered Azure Geo Regions (for example, West US, East US, Southeast Asia, and so forth).
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mediaServiceName")
    def media_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Media Service.
        """
        return pulumi.get(self, "media_service_name")

    @media_service_name.setter
    def media_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "media_service_name", value)

    @property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StorageAccountArgs']]]]:
        """
        The storage accounts for this resource.
        """
        return pulumi.get(self, "storage_accounts")

    @storage_accounts.setter
    def storage_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StorageAccountArgs']]]]):
        pulumi.set(self, "storage_accounts", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags to help categorize the resource in the Azure portal.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class MediaService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 media_service_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StorageAccountArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The properties of a Media Service resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The geographic location of the resource. This must be one of the supported and registered Azure Geo Regions (for example, West US, East US, Southeast Asia, and so forth).
        :param pulumi.Input[str] media_service_name: Name of the Media Service.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the Azure subscription.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StorageAccountArgs']]]] storage_accounts: The storage accounts for this resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags to help categorize the resource in the Azure portal.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MediaServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The properties of a Media Service resource.

        :param str resource_name: The name of the resource.
        :param MediaServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MediaServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 media_service_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StorageAccountArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MediaServiceArgs.__new__(MediaServiceArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["media_service_name"] = media_service_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["storage_accounts"] = storage_accounts
            __props__.__dict__["tags"] = tags
            __props__.__dict__["api_endpoints"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:media:MediaService"), pulumi.Alias(type_="azure-native:media/v20180330preview:MediaService"), pulumi.Alias(type_="azure-native:media/v20180601preview:MediaService"), pulumi.Alias(type_="azure-native:media/v20180701:MediaService"), pulumi.Alias(type_="azure-native:media/v20200501:MediaService"), pulumi.Alias(type_="azure-native:media/v20210501:MediaService"), pulumi.Alias(type_="azure-native:media/v20210601:MediaService"), pulumi.Alias(type_="azure-native:media/v20211101:MediaService"), pulumi.Alias(type_="azure-native:media/v20230101:MediaService")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MediaService, __self__).__init__(
            'azure-native:media/v20151001:MediaService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MediaService':
        """
        Get an existing MediaService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MediaServiceArgs.__new__(MediaServiceArgs)

        __props__.__dict__["api_endpoints"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["storage_accounts"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return MediaService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiEndpoints")
    def api_endpoints(self) -> pulumi.Output[Sequence['outputs.ApiEndpointResponse']]:
        """
        Read-only property that lists the Media Services REST API endpoints for this resource. If supplied on a PUT or PATCH, the value will be ignored.
        """
        return pulumi.get(self, "api_endpoints")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The geographic location of the resource. This must be one of the supported and registered Azure Geo Regions (for example, West US, East US, Southeast Asia, and so forth).
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(self) -> pulumi.Output[Optional[Sequence['outputs.StorageAccountResponse']]]:
        """
        The storage accounts for this resource.
        """
        return pulumi.get(self, "storage_accounts")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags to help categorize the resource in the Azure portal.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource
        """
        return pulumi.get(self, "type")

