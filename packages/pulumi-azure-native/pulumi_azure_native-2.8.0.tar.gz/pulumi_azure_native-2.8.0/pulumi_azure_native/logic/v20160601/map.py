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

__all__ = ['MapArgs', 'Map']

@pulumi.input_type
class MapArgs:
    def __init__(__self__, *,
                 integration_account_name: pulumi.Input[str],
                 map_type: pulumi.Input['MapType'],
                 resource_group_name: pulumi.Input[str],
                 content: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 map_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 parameters_schema: Optional[pulumi.Input['IntegrationAccountMapPropertiesParametersSchemaArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Map resource.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input['MapType'] map_type: The map type.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] content: The content.
        :param pulumi.Input[str] content_type: The content type.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] map_name: The integration account map name.
        :param Any metadata: The metadata.
        :param pulumi.Input['IntegrationAccountMapPropertiesParametersSchemaArgs'] parameters_schema: The parameters schema of integration account map.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "integration_account_name", integration_account_name)
        pulumi.set(__self__, "map_type", map_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if map_name is not None:
            pulumi.set(__self__, "map_name", map_name)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if parameters_schema is not None:
            pulumi.set(__self__, "parameters_schema", parameters_schema)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Input[str]:
        """
        The integration account name.
        """
        return pulumi.get(self, "integration_account_name")

    @integration_account_name.setter
    def integration_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_account_name", value)

    @property
    @pulumi.getter(name="mapType")
    def map_type(self) -> pulumi.Input['MapType']:
        """
        The map type.
        """
        return pulumi.get(self, "map_type")

    @map_type.setter
    def map_type(self, value: pulumi.Input['MapType']):
        pulumi.set(self, "map_type", value)

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
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        The content.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        """
        The content type.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

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
    @pulumi.getter(name="mapName")
    def map_name(self) -> Optional[pulumi.Input[str]]:
        """
        The integration account map name.
        """
        return pulumi.get(self, "map_name")

    @map_name.setter
    def map_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "map_name", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="parametersSchema")
    def parameters_schema(self) -> Optional[pulumi.Input['IntegrationAccountMapPropertiesParametersSchemaArgs']]:
        """
        The parameters schema of integration account map.
        """
        return pulumi.get(self, "parameters_schema")

    @parameters_schema.setter
    def parameters_schema(self, value: Optional[pulumi.Input['IntegrationAccountMapPropertiesParametersSchemaArgs']]):
        pulumi.set(self, "parameters_schema", value)

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


class Map(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 map_name: Optional[pulumi.Input[str]] = None,
                 map_type: Optional[pulumi.Input['MapType']] = None,
                 metadata: Optional[Any] = None,
                 parameters_schema: Optional[pulumi.Input[pulumi.InputType['IntegrationAccountMapPropertiesParametersSchemaArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The integration account map.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: The content.
        :param pulumi.Input[str] content_type: The content type.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] map_name: The integration account map name.
        :param pulumi.Input['MapType'] map_type: The map type.
        :param Any metadata: The metadata.
        :param pulumi.Input[pulumi.InputType['IntegrationAccountMapPropertiesParametersSchemaArgs']] parameters_schema: The parameters schema of integration account map.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MapArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The integration account map.

        :param str resource_name: The name of the resource.
        :param MapArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MapArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 map_name: Optional[pulumi.Input[str]] = None,
                 map_type: Optional[pulumi.Input['MapType']] = None,
                 metadata: Optional[Any] = None,
                 parameters_schema: Optional[pulumi.Input[pulumi.InputType['IntegrationAccountMapPropertiesParametersSchemaArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MapArgs.__new__(MapArgs)

            __props__.__dict__["content"] = content
            __props__.__dict__["content_type"] = content_type
            if integration_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'integration_account_name'")
            __props__.__dict__["integration_account_name"] = integration_account_name
            __props__.__dict__["location"] = location
            __props__.__dict__["map_name"] = map_name
            if map_type is None and not opts.urn:
                raise TypeError("Missing required property 'map_type'")
            __props__.__dict__["map_type"] = map_type
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["parameters_schema"] = parameters_schema
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["changed_time"] = None
            __props__.__dict__["content_link"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:logic:Map"), pulumi.Alias(type_="azure-native:logic/v20150801preview:Map"), pulumi.Alias(type_="azure-native:logic/v20180701preview:Map"), pulumi.Alias(type_="azure-native:logic/v20190501:Map")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Map, __self__).__init__(
            'azure-native:logic/v20160601:Map',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Map':
        """
        Get an existing Map resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MapArgs.__new__(MapArgs)

        __props__.__dict__["changed_time"] = None
        __props__.__dict__["content"] = None
        __props__.__dict__["content_link"] = None
        __props__.__dict__["content_type"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["map_type"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters_schema"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Map(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[str]:
        """
        The changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional[str]]:
        """
        The content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> pulumi.Output['outputs.ContentLinkResponse']:
        """
        The content link.
        """
        return pulumi.get(self, "content_link")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[str]]:
        """
        The content type.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        The created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mapType")
    def map_type(self) -> pulumi.Output[str]:
        """
        The map type.
        """
        return pulumi.get(self, "map_type")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parametersSchema")
    def parameters_schema(self) -> pulumi.Output[Optional['outputs.IntegrationAccountMapPropertiesResponseParametersSchema']]:
        """
        The parameters schema of integration account map.
        """
        return pulumi.get(self, "parameters_schema")

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

