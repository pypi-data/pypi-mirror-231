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

__all__ = ['FavoriteArgs', 'Favorite']

@pulumi.input_type
class FavoriteArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 category: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 favorite_id: Optional[pulumi.Input[str]] = None,
                 favorite_type: Optional[pulumi.Input['FavoriteType']] = None,
                 is_generated_from_template: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Favorite resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name: The name of the Application Insights component resource.
        :param pulumi.Input[str] category: Favorite category, as defined by the user at creation time.
        :param pulumi.Input[str] config: Configuration of this particular favorite, which are driven by the Azure portal UX. Configuration data is a string containing valid JSON
        :param pulumi.Input[str] favorite_id: The Id of a specific favorite defined in the Application Insights component
        :param pulumi.Input['FavoriteType'] favorite_type: Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component.
        :param pulumi.Input[bool] is_generated_from_template: Flag denoting wether or not this favorite was generated from a template.
        :param pulumi.Input[str] name: The user-defined name of the favorite.
        :param pulumi.Input[str] source_type: The source of the favorite definition.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of 0 or more tags that are associated with this favorite definition
        :param pulumi.Input[str] version: This instance's version of the data model. This can change as new features are added that can be marked favorite. Current examples include MetricsExplorer (ME) and Search.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if favorite_id is not None:
            pulumi.set(__self__, "favorite_id", favorite_id)
        if favorite_type is not None:
            pulumi.set(__self__, "favorite_type", favorite_type)
        if is_generated_from_template is not None:
            pulumi.set(__self__, "is_generated_from_template", is_generated_from_template)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if source_type is not None:
            pulumi.set(__self__, "source_type", source_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version is not None:
            pulumi.set(__self__, "version", version)

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
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        Favorite category, as defined by the user at creation time.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[str]]:
        """
        Configuration of this particular favorite, which are driven by the Azure portal UX. Configuration data is a string containing valid JSON
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="favoriteId")
    def favorite_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Id of a specific favorite defined in the Application Insights component
        """
        return pulumi.get(self, "favorite_id")

    @favorite_id.setter
    def favorite_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "favorite_id", value)

    @property
    @pulumi.getter(name="favoriteType")
    def favorite_type(self) -> Optional[pulumi.Input['FavoriteType']]:
        """
        Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component.
        """
        return pulumi.get(self, "favorite_type")

    @favorite_type.setter
    def favorite_type(self, value: Optional[pulumi.Input['FavoriteType']]):
        pulumi.set(self, "favorite_type", value)

    @property
    @pulumi.getter(name="isGeneratedFromTemplate")
    def is_generated_from_template(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag denoting wether or not this favorite was generated from a template.
        """
        return pulumi.get(self, "is_generated_from_template")

    @is_generated_from_template.setter
    def is_generated_from_template(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_generated_from_template", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The user-defined name of the favorite.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[str]]:
        """
        The source of the favorite definition.
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of 0 or more tags that are associated with this favorite definition
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        This instance's version of the data model. This can change as new features are added that can be marked favorite. Current examples include MetricsExplorer (ME) and Search.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Favorite(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 favorite_id: Optional[pulumi.Input[str]] = None,
                 favorite_type: Optional[pulumi.Input['FavoriteType']] = None,
                 is_generated_from_template: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Properties that define a favorite that is associated to an Application Insights component.
        Azure REST API version: 2015-05-01. Prior API version in Azure Native 1.x: 2015-05-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: Favorite category, as defined by the user at creation time.
        :param pulumi.Input[str] config: Configuration of this particular favorite, which are driven by the Azure portal UX. Configuration data is a string containing valid JSON
        :param pulumi.Input[str] favorite_id: The Id of a specific favorite defined in the Application Insights component
        :param pulumi.Input['FavoriteType'] favorite_type: Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component.
        :param pulumi.Input[bool] is_generated_from_template: Flag denoting wether or not this favorite was generated from a template.
        :param pulumi.Input[str] name: The user-defined name of the favorite.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the Application Insights component resource.
        :param pulumi.Input[str] source_type: The source of the favorite definition.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of 0 or more tags that are associated with this favorite definition
        :param pulumi.Input[str] version: This instance's version of the data model. This can change as new features are added that can be marked favorite. Current examples include MetricsExplorer (ME) and Search.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FavoriteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Properties that define a favorite that is associated to an Application Insights component.
        Azure REST API version: 2015-05-01. Prior API version in Azure Native 1.x: 2015-05-01

        :param str resource_name: The name of the resource.
        :param FavoriteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FavoriteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 favorite_id: Optional[pulumi.Input[str]] = None,
                 favorite_type: Optional[pulumi.Input['FavoriteType']] = None,
                 is_generated_from_template: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FavoriteArgs.__new__(FavoriteArgs)

            __props__.__dict__["category"] = category
            __props__.__dict__["config"] = config
            __props__.__dict__["favorite_id"] = favorite_id
            __props__.__dict__["favorite_type"] = favorite_type
            __props__.__dict__["is_generated_from_template"] = is_generated_from_template
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["source_type"] = source_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["version"] = version
            __props__.__dict__["time_modified"] = None
            __props__.__dict__["user_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights/v20150501:Favorite")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Favorite, __self__).__init__(
            'azure-native:insights:Favorite',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Favorite':
        """
        Get an existing Favorite resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FavoriteArgs.__new__(FavoriteArgs)

        __props__.__dict__["category"] = None
        __props__.__dict__["config"] = None
        __props__.__dict__["favorite_id"] = None
        __props__.__dict__["favorite_type"] = None
        __props__.__dict__["is_generated_from_template"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["source_type"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["time_modified"] = None
        __props__.__dict__["user_id"] = None
        __props__.__dict__["version"] = None
        return Favorite(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[Optional[str]]:
        """
        Favorite category, as defined by the user at creation time.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[str]]:
        """
        Configuration of this particular favorite, which are driven by the Azure portal UX. Configuration data is a string containing valid JSON
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="favoriteId")
    def favorite_id(self) -> pulumi.Output[str]:
        """
        Internally assigned unique id of the favorite definition.
        """
        return pulumi.get(self, "favorite_id")

    @property
    @pulumi.getter(name="favoriteType")
    def favorite_type(self) -> pulumi.Output[Optional[str]]:
        """
        Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component.
        """
        return pulumi.get(self, "favorite_type")

    @property
    @pulumi.getter(name="isGeneratedFromTemplate")
    def is_generated_from_template(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag denoting wether or not this favorite was generated from a template.
        """
        return pulumi.get(self, "is_generated_from_template")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The user-defined name of the favorite.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[Optional[str]]:
        """
        The source of the favorite definition.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of 0 or more tags that are associated with this favorite definition
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> pulumi.Output[str]:
        """
        Date and time in UTC of the last modification that was made to this favorite definition.
        """
        return pulumi.get(self, "time_modified")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        Unique user id of the specific user that owns this favorite.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        This instance's version of the data model. This can change as new features are added that can be marked favorite. Current examples include MetricsExplorer (ME) and Search.
        """
        return pulumi.get(self, "version")

