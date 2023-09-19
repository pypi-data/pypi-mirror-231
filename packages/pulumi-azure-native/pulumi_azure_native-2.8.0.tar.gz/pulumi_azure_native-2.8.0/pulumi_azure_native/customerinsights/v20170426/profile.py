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

__all__ = ['ProfileArgs', 'Profile']

@pulumi.input_type
class ProfileArgs:
    def __init__(__self__, *,
                 hub_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 api_entity_set_name: Optional[pulumi.Input[str]] = None,
                 attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 entity_type: Optional[pulumi.Input['EntityTypes']] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input['PropertyDefinitionArgs']]]] = None,
                 instances_count: Optional[pulumi.Input[int]] = None,
                 large_image: Optional[pulumi.Input[str]] = None,
                 localized_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 medium_image: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 schema_item_type_link: Optional[pulumi.Input[str]] = None,
                 small_image: Optional[pulumi.Input[str]] = None,
                 strong_ids: Optional[pulumi.Input[Sequence[pulumi.Input['StrongIdArgs']]]] = None,
                 timestamp_field_name: Optional[pulumi.Input[str]] = None,
                 type_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Profile resource.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] api_entity_set_name: The api entity set name. This becomes the odata entity set name for the entity Type being referred in this object.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] attributes: The attributes for the Type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Localized descriptions for the property.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Localized display names for the property.
        :param pulumi.Input['EntityTypes'] entity_type: Type of entity.
        :param pulumi.Input[Sequence[pulumi.Input['PropertyDefinitionArgs']]] fields: The properties of the Profile.
        :param pulumi.Input[int] instances_count: The instance count.
        :param pulumi.Input[str] large_image: Large Image associated with the Property or EntityType.
        :param pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[str]]]]] localized_attributes: Any custom localized attributes for the Type.
        :param pulumi.Input[str] medium_image: Medium Image associated with the Property or EntityType.
        :param pulumi.Input[str] profile_name: The name of the profile.
        :param pulumi.Input[str] schema_item_type_link: The schema org link. This helps ACI identify and suggest semantic models.
        :param pulumi.Input[str] small_image: Small Image associated with the Property or EntityType.
        :param pulumi.Input[Sequence[pulumi.Input['StrongIdArgs']]] strong_ids: The strong IDs.
        :param pulumi.Input[str] timestamp_field_name: The timestamp property name. Represents the time when the interaction or profile update happened.
        :param pulumi.Input[str] type_name: The name of the entity.
        """
        pulumi.set(__self__, "hub_name", hub_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if api_entity_set_name is not None:
            pulumi.set(__self__, "api_entity_set_name", api_entity_set_name)
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if entity_type is not None:
            pulumi.set(__self__, "entity_type", entity_type)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if instances_count is not None:
            pulumi.set(__self__, "instances_count", instances_count)
        if large_image is not None:
            pulumi.set(__self__, "large_image", large_image)
        if localized_attributes is not None:
            pulumi.set(__self__, "localized_attributes", localized_attributes)
        if medium_image is not None:
            pulumi.set(__self__, "medium_image", medium_image)
        if profile_name is not None:
            pulumi.set(__self__, "profile_name", profile_name)
        if schema_item_type_link is not None:
            pulumi.set(__self__, "schema_item_type_link", schema_item_type_link)
        if small_image is not None:
            pulumi.set(__self__, "small_image", small_image)
        if strong_ids is not None:
            pulumi.set(__self__, "strong_ids", strong_ids)
        if timestamp_field_name is not None:
            pulumi.set(__self__, "timestamp_field_name", timestamp_field_name)
        if type_name is not None:
            pulumi.set(__self__, "type_name", type_name)

    @property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[str]:
        """
        The name of the hub.
        """
        return pulumi.get(self, "hub_name")

    @hub_name.setter
    def hub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "hub_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="apiEntitySetName")
    def api_entity_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The api entity set name. This becomes the odata entity set name for the entity Type being referred in this object.
        """
        return pulumi.get(self, "api_entity_set_name")

    @api_entity_set_name.setter
    def api_entity_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_entity_set_name", value)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]:
        """
        The attributes for the Type.
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Localized descriptions for the property.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Localized display names for the property.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[pulumi.Input['EntityTypes']]:
        """
        Type of entity.
        """
        return pulumi.get(self, "entity_type")

    @entity_type.setter
    def entity_type(self, value: Optional[pulumi.Input['EntityTypes']]):
        pulumi.set(self, "entity_type", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PropertyDefinitionArgs']]]]:
        """
        The properties of the Profile.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PropertyDefinitionArgs']]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter(name="instancesCount")
    def instances_count(self) -> Optional[pulumi.Input[int]]:
        """
        The instance count.
        """
        return pulumi.get(self, "instances_count")

    @instances_count.setter
    def instances_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instances_count", value)

    @property
    @pulumi.getter(name="largeImage")
    def large_image(self) -> Optional[pulumi.Input[str]]:
        """
        Large Image associated with the Property or EntityType.
        """
        return pulumi.get(self, "large_image")

    @large_image.setter
    def large_image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "large_image", value)

    @property
    @pulumi.getter(name="localizedAttributes")
    def localized_attributes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]:
        """
        Any custom localized attributes for the Type.
        """
        return pulumi.get(self, "localized_attributes")

    @localized_attributes.setter
    def localized_attributes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]):
        pulumi.set(self, "localized_attributes", value)

    @property
    @pulumi.getter(name="mediumImage")
    def medium_image(self) -> Optional[pulumi.Input[str]]:
        """
        Medium Image associated with the Property or EntityType.
        """
        return pulumi.get(self, "medium_image")

    @medium_image.setter
    def medium_image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "medium_image", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the profile.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="schemaItemTypeLink")
    def schema_item_type_link(self) -> Optional[pulumi.Input[str]]:
        """
        The schema org link. This helps ACI identify and suggest semantic models.
        """
        return pulumi.get(self, "schema_item_type_link")

    @schema_item_type_link.setter
    def schema_item_type_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_item_type_link", value)

    @property
    @pulumi.getter(name="smallImage")
    def small_image(self) -> Optional[pulumi.Input[str]]:
        """
        Small Image associated with the Property or EntityType.
        """
        return pulumi.get(self, "small_image")

    @small_image.setter
    def small_image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "small_image", value)

    @property
    @pulumi.getter(name="strongIds")
    def strong_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StrongIdArgs']]]]:
        """
        The strong IDs.
        """
        return pulumi.get(self, "strong_ids")

    @strong_ids.setter
    def strong_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StrongIdArgs']]]]):
        pulumi.set(self, "strong_ids", value)

    @property
    @pulumi.getter(name="timestampFieldName")
    def timestamp_field_name(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp property name. Represents the time when the interaction or profile update happened.
        """
        return pulumi.get(self, "timestamp_field_name")

    @timestamp_field_name.setter
    def timestamp_field_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timestamp_field_name", value)

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the entity.
        """
        return pulumi.get(self, "type_name")

    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type_name", value)


class Profile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_entity_set_name: Optional[pulumi.Input[str]] = None,
                 attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 entity_type: Optional[pulumi.Input['EntityTypes']] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PropertyDefinitionArgs']]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 instances_count: Optional[pulumi.Input[int]] = None,
                 large_image: Optional[pulumi.Input[str]] = None,
                 localized_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 medium_image: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_item_type_link: Optional[pulumi.Input[str]] = None,
                 small_image: Optional[pulumi.Input[str]] = None,
                 strong_ids: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StrongIdArgs']]]]] = None,
                 timestamp_field_name: Optional[pulumi.Input[str]] = None,
                 type_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The profile resource format.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_entity_set_name: The api entity set name. This becomes the odata entity set name for the entity Type being referred in this object.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] attributes: The attributes for the Type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Localized descriptions for the property.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Localized display names for the property.
        :param pulumi.Input['EntityTypes'] entity_type: Type of entity.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PropertyDefinitionArgs']]]] fields: The properties of the Profile.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[int] instances_count: The instance count.
        :param pulumi.Input[str] large_image: Large Image associated with the Property or EntityType.
        :param pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[str]]]]] localized_attributes: Any custom localized attributes for the Type.
        :param pulumi.Input[str] medium_image: Medium Image associated with the Property or EntityType.
        :param pulumi.Input[str] profile_name: The name of the profile.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] schema_item_type_link: The schema org link. This helps ACI identify and suggest semantic models.
        :param pulumi.Input[str] small_image: Small Image associated with the Property or EntityType.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StrongIdArgs']]]] strong_ids: The strong IDs.
        :param pulumi.Input[str] timestamp_field_name: The timestamp property name. Represents the time when the interaction or profile update happened.
        :param pulumi.Input[str] type_name: The name of the entity.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The profile resource format.

        :param str resource_name: The name of the resource.
        :param ProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_entity_set_name: Optional[pulumi.Input[str]] = None,
                 attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 entity_type: Optional[pulumi.Input['EntityTypes']] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PropertyDefinitionArgs']]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 instances_count: Optional[pulumi.Input[int]] = None,
                 large_image: Optional[pulumi.Input[str]] = None,
                 localized_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 medium_image: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_item_type_link: Optional[pulumi.Input[str]] = None,
                 small_image: Optional[pulumi.Input[str]] = None,
                 strong_ids: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StrongIdArgs']]]]] = None,
                 timestamp_field_name: Optional[pulumi.Input[str]] = None,
                 type_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProfileArgs.__new__(ProfileArgs)

            __props__.__dict__["api_entity_set_name"] = api_entity_set_name
            __props__.__dict__["attributes"] = attributes
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["entity_type"] = entity_type
            __props__.__dict__["fields"] = fields
            if hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'hub_name'")
            __props__.__dict__["hub_name"] = hub_name
            __props__.__dict__["instances_count"] = instances_count
            __props__.__dict__["large_image"] = large_image
            __props__.__dict__["localized_attributes"] = localized_attributes
            __props__.__dict__["medium_image"] = medium_image
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["schema_item_type_link"] = schema_item_type_link
            __props__.__dict__["small_image"] = small_image
            __props__.__dict__["strong_ids"] = strong_ids
            __props__.__dict__["timestamp_field_name"] = timestamp_field_name
            __props__.__dict__["type_name"] = type_name
            __props__.__dict__["last_changed_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:customerinsights:Profile"), pulumi.Alias(type_="azure-native:customerinsights/v20170101:Profile")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Profile, __self__).__init__(
            'azure-native:customerinsights/v20170426:Profile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Profile':
        """
        Get an existing Profile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProfileArgs.__new__(ProfileArgs)

        __props__.__dict__["api_entity_set_name"] = None
        __props__.__dict__["attributes"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["entity_type"] = None
        __props__.__dict__["fields"] = None
        __props__.__dict__["instances_count"] = None
        __props__.__dict__["large_image"] = None
        __props__.__dict__["last_changed_utc"] = None
        __props__.__dict__["localized_attributes"] = None
        __props__.__dict__["medium_image"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["schema_item_type_link"] = None
        __props__.__dict__["small_image"] = None
        __props__.__dict__["strong_ids"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["timestamp_field_name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["type_name"] = None
        return Profile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiEntitySetName")
    def api_entity_set_name(self) -> pulumi.Output[Optional[str]]:
        """
        The api entity set name. This becomes the odata entity set name for the entity Type being referred in this object.
        """
        return pulumi.get(self, "api_entity_set_name")

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Mapping[str, Sequence[str]]]]:
        """
        The attributes for the Type.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Localized descriptions for the property.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Localized display names for the property.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of entity.
        """
        return pulumi.get(self, "entity_type")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Optional[Sequence['outputs.PropertyDefinitionResponse']]]:
        """
        The properties of the Profile.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="instancesCount")
    def instances_count(self) -> pulumi.Output[Optional[int]]:
        """
        The instance count.
        """
        return pulumi.get(self, "instances_count")

    @property
    @pulumi.getter(name="largeImage")
    def large_image(self) -> pulumi.Output[Optional[str]]:
        """
        Large Image associated with the Property or EntityType.
        """
        return pulumi.get(self, "large_image")

    @property
    @pulumi.getter(name="lastChangedUtc")
    def last_changed_utc(self) -> pulumi.Output[str]:
        """
        The last changed time for the type definition.
        """
        return pulumi.get(self, "last_changed_utc")

    @property
    @pulumi.getter(name="localizedAttributes")
    def localized_attributes(self) -> pulumi.Output[Optional[Mapping[str, Mapping[str, str]]]]:
        """
        Any custom localized attributes for the Type.
        """
        return pulumi.get(self, "localized_attributes")

    @property
    @pulumi.getter(name="mediumImage")
    def medium_image(self) -> pulumi.Output[Optional[str]]:
        """
        Medium Image associated with the Property or EntityType.
        """
        return pulumi.get(self, "medium_image")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="schemaItemTypeLink")
    def schema_item_type_link(self) -> pulumi.Output[Optional[str]]:
        """
        The schema org link. This helps ACI identify and suggest semantic models.
        """
        return pulumi.get(self, "schema_item_type_link")

    @property
    @pulumi.getter(name="smallImage")
    def small_image(self) -> pulumi.Output[Optional[str]]:
        """
        Small Image associated with the Property or EntityType.
        """
        return pulumi.get(self, "small_image")

    @property
    @pulumi.getter(name="strongIds")
    def strong_ids(self) -> pulumi.Output[Optional[Sequence['outputs.StrongIdResponse']]]:
        """
        The strong IDs.
        """
        return pulumi.get(self, "strong_ids")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="timestampFieldName")
    def timestamp_field_name(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp property name. Represents the time when the interaction or profile update happened.
        """
        return pulumi.get(self, "timestamp_field_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the entity.
        """
        return pulumi.get(self, "type_name")

