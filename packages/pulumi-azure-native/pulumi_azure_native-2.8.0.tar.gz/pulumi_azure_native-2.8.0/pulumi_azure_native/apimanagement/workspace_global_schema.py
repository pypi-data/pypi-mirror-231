# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['WorkspaceGlobalSchemaArgs', 'WorkspaceGlobalSchema']

@pulumi.input_type
class WorkspaceGlobalSchemaArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 schema_type: pulumi.Input[Union[str, 'SchemaType']],
                 service_name: pulumi.Input[str],
                 workspace_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 schema_id: Optional[pulumi.Input[str]] = None,
                 value: Optional[Any] = None):
        """
        The set of arguments for constructing a WorkspaceGlobalSchema resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'SchemaType']] schema_type: Schema Type. Immutable.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] description: Free-form schema entity description.
        :param pulumi.Input[str] schema_id: Schema id identifier. Must be unique in the current API Management service instance.
        :param Any value: Json-encoded string for non json-based schema.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "schema_type", schema_type)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "workspace_id", workspace_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if schema_id is not None:
            pulumi.set(__self__, "schema_id", schema_id)
        if value is not None:
            pulumi.set(__self__, "value", value)

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
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> pulumi.Input[Union[str, 'SchemaType']]:
        """
        Schema Type. Immutable.
        """
        return pulumi.get(self, "schema_type")

    @schema_type.setter
    def schema_type(self, value: pulumi.Input[Union[str, 'SchemaType']]):
        pulumi.set(self, "schema_type", value)

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
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[str]:
        """
        Workspace identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Free-form schema entity description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[pulumi.Input[str]]:
        """
        Schema id identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "schema_id")

    @schema_id.setter
    def schema_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_id", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        """
        Json-encoded string for non json-based schema.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[Any]):
        pulumi.set(self, "value", value)


class WorkspaceGlobalSchema(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_id: Optional[pulumi.Input[str]] = None,
                 schema_type: Optional[pulumi.Input[Union[str, 'SchemaType']]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[Any] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Global Schema Contract details.
        Azure REST API version: 2022-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Free-form schema entity description.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] schema_id: Schema id identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[Union[str, 'SchemaType']] schema_type: Schema Type. Immutable.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param Any value: Json-encoded string for non json-based schema.
        :param pulumi.Input[str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceGlobalSchemaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Global Schema Contract details.
        Azure REST API version: 2022-09-01-preview.

        :param str resource_name: The name of the resource.
        :param WorkspaceGlobalSchemaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceGlobalSchemaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_id: Optional[pulumi.Input[str]] = None,
                 schema_type: Optional[pulumi.Input[Union[str, 'SchemaType']]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[Any] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceGlobalSchemaArgs.__new__(WorkspaceGlobalSchemaArgs)

            __props__.__dict__["description"] = description
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["schema_id"] = schema_id
            if schema_type is None and not opts.urn:
                raise TypeError("Missing required property 'schema_type'")
            __props__.__dict__["schema_type"] = schema_type
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["value"] = value
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:WorkspaceGlobalSchema"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:WorkspaceGlobalSchema")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkspaceGlobalSchema, __self__).__init__(
            'azure-native:apimanagement:WorkspaceGlobalSchema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkspaceGlobalSchema':
        """
        Get an existing WorkspaceGlobalSchema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceGlobalSchemaArgs.__new__(WorkspaceGlobalSchemaArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schema_type"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["value"] = None
        return WorkspaceGlobalSchema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Free-form schema entity description.
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
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> pulumi.Output[str]:
        """
        Schema Type. Immutable.
        """
        return pulumi.get(self, "schema_type")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[Any]]:
        """
        Json-encoded string for non json-based schema.
        """
        return pulumi.get(self, "value")

