# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['CacheArgs', 'Cache']

@pulumi.input_type
class CacheArgs:
    def __init__(__self__, *,
                 connection_string: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 use_from_location: pulumi.Input[str],
                 cache_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Cache resource.
        :param pulumi.Input[str] connection_string: Runtime connection string to cache
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] use_from_location: Location identifier to use cache from (should be either 'default' or valid Azure region identifier)
        :param pulumi.Input[str] cache_id: Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).
        :param pulumi.Input[str] description: Cache description
        :param pulumi.Input[str] resource_id: Original uri of entity in external system cache points to
        """
        pulumi.set(__self__, "connection_string", connection_string)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "use_from_location", use_from_location)
        if cache_id is not None:
            pulumi.set(__self__, "cache_id", cache_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Input[str]:
        """
        Runtime connection string to cache
        """
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_string", value)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="useFromLocation")
    def use_from_location(self) -> pulumi.Input[str]:
        """
        Location identifier to use cache from (should be either 'default' or valid Azure region identifier)
        """
        return pulumi.get(self, "use_from_location")

    @use_from_location.setter
    def use_from_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "use_from_location", value)

    @property
    @pulumi.getter(name="cacheId")
    def cache_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).
        """
        return pulumi.get(self, "cache_id")

    @cache_id.setter
    def cache_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cache_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Cache description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Original uri of entity in external system cache points to
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)


class Cache(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_id: Optional[pulumi.Input[str]] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 use_from_location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Cache details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cache_id: Identifier of the Cache entity. Cache identifier (should be either 'default' or valid Azure region identifier).
        :param pulumi.Input[str] connection_string: Runtime connection string to cache
        :param pulumi.Input[str] description: Cache description
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_id: Original uri of entity in external system cache points to
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] use_from_location: Location identifier to use cache from (should be either 'default' or valid Azure region identifier)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CacheArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Cache details.

        :param str resource_name: The name of the resource.
        :param CacheArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CacheArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_id: Optional[pulumi.Input[str]] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 use_from_location: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CacheArgs.__new__(CacheArgs)

            __props__.__dict__["cache_id"] = cache_id
            if connection_string is None and not opts.urn:
                raise TypeError("Missing required property 'connection_string'")
            __props__.__dict__["connection_string"] = connection_string
            __props__.__dict__["description"] = description
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_id"] = resource_id
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if use_from_location is None and not opts.urn:
                raise TypeError("Missing required property 'use_from_location'")
            __props__.__dict__["use_from_location"] = use_from_location
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20220401preview:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:Cache"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:Cache")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Cache, __self__).__init__(
            'azure-native:apimanagement/v20220801:Cache',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cache':
        """
        Get an existing Cache resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CacheArgs.__new__(CacheArgs)

        __props__.__dict__["connection_string"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["use_from_location"] = None
        return Cache(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Output[str]:
        """
        Runtime connection string to cache
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Cache description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        Original uri of entity in external system cache points to
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="useFromLocation")
    def use_from_location(self) -> pulumi.Output[str]:
        """
        Location identifier to use cache from (should be either 'default' or valid Azure region identifier)
        """
        return pulumi.get(self, "use_from_location")

