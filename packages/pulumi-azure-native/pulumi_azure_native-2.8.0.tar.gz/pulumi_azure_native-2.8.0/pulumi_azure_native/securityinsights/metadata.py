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
from ._enums import *
from ._inputs import *

__all__ = ['MetadataArgs', 'Metadata']

@pulumi.input_type
class MetadataArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 parent_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 author: Optional[pulumi.Input['MetadataAuthorArgs']] = None,
                 categories: Optional[pulumi.Input['MetadataCategoriesArgs']] = None,
                 content_id: Optional[pulumi.Input[str]] = None,
                 content_schema_version: Optional[pulumi.Input[str]] = None,
                 custom_version: Optional[pulumi.Input[str]] = None,
                 dependencies: Optional[pulumi.Input['MetadataDependenciesArgs']] = None,
                 first_publish_date: Optional[pulumi.Input[str]] = None,
                 icon: Optional[pulumi.Input[str]] = None,
                 last_publish_date: Optional[pulumi.Input[str]] = None,
                 metadata_name: Optional[pulumi.Input[str]] = None,
                 preview_images: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 preview_images_dark: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 source: Optional[pulumi.Input['MetadataSourceArgs']] = None,
                 support: Optional[pulumi.Input['MetadataSupportArgs']] = None,
                 threat_analysis_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 threat_analysis_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Metadata resource.
        :param pulumi.Input[str] kind: The kind of content the metadata is for.
        :param pulumi.Input[str] parent_id: Full parent resource ID of the content item the metadata is for.  This is the full resource ID including the scope (subscription and resource group)
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input['MetadataAuthorArgs'] author: The creator of the content item.
        :param pulumi.Input['MetadataCategoriesArgs'] categories: Categories for the solution content item
        :param pulumi.Input[str] content_id: Static ID for the content.  Used to identify dependencies and content from solutions or community.  Hard-coded/static for out of the box content and solutions. Dynamic for user-created.  This is the resource name
        :param pulumi.Input[str] content_schema_version: Schema version of the content. Can be used to distinguish between different flow based on the schema version
        :param pulumi.Input[str] custom_version: The custom version of the content. A optional free text
        :param pulumi.Input['MetadataDependenciesArgs'] dependencies: Dependencies for the content item, what other content items it requires to work.  Can describe more complex dependencies using a recursive/nested structure. For a single dependency an id/kind/version can be supplied or operator/criteria for complex formats.
        :param pulumi.Input[str] first_publish_date: first publish date solution content item
        :param pulumi.Input[str] icon: the icon identifier. this id can later be fetched from the solution template
        :param pulumi.Input[str] last_publish_date: last publish date for the solution content item
        :param pulumi.Input[str] metadata_name: The Metadata name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] preview_images: preview image file names. These will be taken from the solution artifacts
        :param pulumi.Input[Sequence[pulumi.Input[str]]] preview_images_dark: preview image file names. These will be taken from the solution artifacts. used for dark theme support
        :param pulumi.Input[Sequence[pulumi.Input[str]]] providers: Providers for the solution content item
        :param pulumi.Input['MetadataSourceArgs'] source: Source of the content.  This is where/how it was created.
        :param pulumi.Input['MetadataSupportArgs'] support: Support information for the metadata - type, name, contact information
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_analysis_tactics: the tactics the resource covers
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_analysis_techniques: the techniques the resource covers, these have to be aligned with the tactics being used
        :param pulumi.Input[str] version: Version of the content.  Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM template best practices.  Can also be any string, but then we cannot guarantee any version checks
        """
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "parent_id", parent_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if author is not None:
            pulumi.set(__self__, "author", author)
        if categories is not None:
            pulumi.set(__self__, "categories", categories)
        if content_id is not None:
            pulumi.set(__self__, "content_id", content_id)
        if content_schema_version is not None:
            pulumi.set(__self__, "content_schema_version", content_schema_version)
        if custom_version is not None:
            pulumi.set(__self__, "custom_version", custom_version)
        if dependencies is not None:
            pulumi.set(__self__, "dependencies", dependencies)
        if first_publish_date is not None:
            pulumi.set(__self__, "first_publish_date", first_publish_date)
        if icon is not None:
            pulumi.set(__self__, "icon", icon)
        if last_publish_date is not None:
            pulumi.set(__self__, "last_publish_date", last_publish_date)
        if metadata_name is not None:
            pulumi.set(__self__, "metadata_name", metadata_name)
        if preview_images is not None:
            pulumi.set(__self__, "preview_images", preview_images)
        if preview_images_dark is not None:
            pulumi.set(__self__, "preview_images_dark", preview_images_dark)
        if providers is not None:
            pulumi.set(__self__, "providers", providers)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if support is not None:
            pulumi.set(__self__, "support", support)
        if threat_analysis_tactics is not None:
            pulumi.set(__self__, "threat_analysis_tactics", threat_analysis_tactics)
        if threat_analysis_techniques is not None:
            pulumi.set(__self__, "threat_analysis_techniques", threat_analysis_techniques)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of content the metadata is for.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Input[str]:
        """
        Full parent resource ID of the content item the metadata is for.  This is the full resource ID including the scope (subscription and resource group)
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_id", value)

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
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter
    def author(self) -> Optional[pulumi.Input['MetadataAuthorArgs']]:
        """
        The creator of the content item.
        """
        return pulumi.get(self, "author")

    @author.setter
    def author(self, value: Optional[pulumi.Input['MetadataAuthorArgs']]):
        pulumi.set(self, "author", value)

    @property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input['MetadataCategoriesArgs']]:
        """
        Categories for the solution content item
        """
        return pulumi.get(self, "categories")

    @categories.setter
    def categories(self, value: Optional[pulumi.Input['MetadataCategoriesArgs']]):
        pulumi.set(self, "categories", value)

    @property
    @pulumi.getter(name="contentId")
    def content_id(self) -> Optional[pulumi.Input[str]]:
        """
        Static ID for the content.  Used to identify dependencies and content from solutions or community.  Hard-coded/static for out of the box content and solutions. Dynamic for user-created.  This is the resource name
        """
        return pulumi.get(self, "content_id")

    @content_id.setter
    def content_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_id", value)

    @property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> Optional[pulumi.Input[str]]:
        """
        Schema version of the content. Can be used to distinguish between different flow based on the schema version
        """
        return pulumi.get(self, "content_schema_version")

    @content_schema_version.setter
    def content_schema_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_schema_version", value)

    @property
    @pulumi.getter(name="customVersion")
    def custom_version(self) -> Optional[pulumi.Input[str]]:
        """
        The custom version of the content. A optional free text
        """
        return pulumi.get(self, "custom_version")

    @custom_version.setter
    def custom_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_version", value)

    @property
    @pulumi.getter
    def dependencies(self) -> Optional[pulumi.Input['MetadataDependenciesArgs']]:
        """
        Dependencies for the content item, what other content items it requires to work.  Can describe more complex dependencies using a recursive/nested structure. For a single dependency an id/kind/version can be supplied or operator/criteria for complex formats.
        """
        return pulumi.get(self, "dependencies")

    @dependencies.setter
    def dependencies(self, value: Optional[pulumi.Input['MetadataDependenciesArgs']]):
        pulumi.set(self, "dependencies", value)

    @property
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> Optional[pulumi.Input[str]]:
        """
        first publish date solution content item
        """
        return pulumi.get(self, "first_publish_date")

    @first_publish_date.setter
    def first_publish_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_publish_date", value)

    @property
    @pulumi.getter
    def icon(self) -> Optional[pulumi.Input[str]]:
        """
        the icon identifier. this id can later be fetched from the solution template
        """
        return pulumi.get(self, "icon")

    @icon.setter
    def icon(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon", value)

    @property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> Optional[pulumi.Input[str]]:
        """
        last publish date for the solution content item
        """
        return pulumi.get(self, "last_publish_date")

    @last_publish_date.setter
    def last_publish_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_publish_date", value)

    @property
    @pulumi.getter(name="metadataName")
    def metadata_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Metadata name.
        """
        return pulumi.get(self, "metadata_name")

    @metadata_name.setter
    def metadata_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata_name", value)

    @property
    @pulumi.getter(name="previewImages")
    def preview_images(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        preview image file names. These will be taken from the solution artifacts
        """
        return pulumi.get(self, "preview_images")

    @preview_images.setter
    def preview_images(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "preview_images", value)

    @property
    @pulumi.getter(name="previewImagesDark")
    def preview_images_dark(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        preview image file names. These will be taken from the solution artifacts. used for dark theme support
        """
        return pulumi.get(self, "preview_images_dark")

    @preview_images_dark.setter
    def preview_images_dark(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "preview_images_dark", value)

    @property
    @pulumi.getter
    def providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Providers for the solution content item
        """
        return pulumi.get(self, "providers")

    @providers.setter
    def providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "providers", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input['MetadataSourceArgs']]:
        """
        Source of the content.  This is where/how it was created.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input['MetadataSourceArgs']]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def support(self) -> Optional[pulumi.Input['MetadataSupportArgs']]:
        """
        Support information for the metadata - type, name, contact information
        """
        return pulumi.get(self, "support")

    @support.setter
    def support(self, value: Optional[pulumi.Input['MetadataSupportArgs']]):
        pulumi.set(self, "support", value)

    @property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        the tactics the resource covers
        """
        return pulumi.get(self, "threat_analysis_tactics")

    @threat_analysis_tactics.setter
    def threat_analysis_tactics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "threat_analysis_tactics", value)

    @property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        the techniques the resource covers, these have to be aligned with the tactics being used
        """
        return pulumi.get(self, "threat_analysis_techniques")

    @threat_analysis_techniques.setter
    def threat_analysis_techniques(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "threat_analysis_techniques", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Version of the content.  Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM template best practices.  Can also be any string, but then we cannot guarantee any version checks
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Metadata(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 author: Optional[pulumi.Input[pulumi.InputType['MetadataAuthorArgs']]] = None,
                 categories: Optional[pulumi.Input[pulumi.InputType['MetadataCategoriesArgs']]] = None,
                 content_id: Optional[pulumi.Input[str]] = None,
                 content_schema_version: Optional[pulumi.Input[str]] = None,
                 custom_version: Optional[pulumi.Input[str]] = None,
                 dependencies: Optional[pulumi.Input[pulumi.InputType['MetadataDependenciesArgs']]] = None,
                 first_publish_date: Optional[pulumi.Input[str]] = None,
                 icon: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 last_publish_date: Optional[pulumi.Input[str]] = None,
                 metadata_name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 preview_images: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 preview_images_dark: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['MetadataSourceArgs']]] = None,
                 support: Optional[pulumi.Input[pulumi.InputType['MetadataSupportArgs']]] = None,
                 threat_analysis_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 threat_analysis_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Metadata resource definition.
        Azure REST API version: 2023-02-01. Prior API version in Azure Native 1.x: 2021-03-01-preview

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['MetadataAuthorArgs']] author: The creator of the content item.
        :param pulumi.Input[pulumi.InputType['MetadataCategoriesArgs']] categories: Categories for the solution content item
        :param pulumi.Input[str] content_id: Static ID for the content.  Used to identify dependencies and content from solutions or community.  Hard-coded/static for out of the box content and solutions. Dynamic for user-created.  This is the resource name
        :param pulumi.Input[str] content_schema_version: Schema version of the content. Can be used to distinguish between different flow based on the schema version
        :param pulumi.Input[str] custom_version: The custom version of the content. A optional free text
        :param pulumi.Input[pulumi.InputType['MetadataDependenciesArgs']] dependencies: Dependencies for the content item, what other content items it requires to work.  Can describe more complex dependencies using a recursive/nested structure. For a single dependency an id/kind/version can be supplied or operator/criteria for complex formats.
        :param pulumi.Input[str] first_publish_date: first publish date solution content item
        :param pulumi.Input[str] icon: the icon identifier. this id can later be fetched from the solution template
        :param pulumi.Input[str] kind: The kind of content the metadata is for.
        :param pulumi.Input[str] last_publish_date: last publish date for the solution content item
        :param pulumi.Input[str] metadata_name: The Metadata name.
        :param pulumi.Input[str] parent_id: Full parent resource ID of the content item the metadata is for.  This is the full resource ID including the scope (subscription and resource group)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] preview_images: preview image file names. These will be taken from the solution artifacts
        :param pulumi.Input[Sequence[pulumi.Input[str]]] preview_images_dark: preview image file names. These will be taken from the solution artifacts. used for dark theme support
        :param pulumi.Input[Sequence[pulumi.Input[str]]] providers: Providers for the solution content item
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['MetadataSourceArgs']] source: Source of the content.  This is where/how it was created.
        :param pulumi.Input[pulumi.InputType['MetadataSupportArgs']] support: Support information for the metadata - type, name, contact information
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_analysis_tactics: the tactics the resource covers
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_analysis_techniques: the techniques the resource covers, these have to be aligned with the tactics being used
        :param pulumi.Input[str] version: Version of the content.  Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM template best practices.  Can also be any string, but then we cannot guarantee any version checks
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetadataArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Metadata resource definition.
        Azure REST API version: 2023-02-01. Prior API version in Azure Native 1.x: 2021-03-01-preview

        :param str resource_name: The name of the resource.
        :param MetadataArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetadataArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 author: Optional[pulumi.Input[pulumi.InputType['MetadataAuthorArgs']]] = None,
                 categories: Optional[pulumi.Input[pulumi.InputType['MetadataCategoriesArgs']]] = None,
                 content_id: Optional[pulumi.Input[str]] = None,
                 content_schema_version: Optional[pulumi.Input[str]] = None,
                 custom_version: Optional[pulumi.Input[str]] = None,
                 dependencies: Optional[pulumi.Input[pulumi.InputType['MetadataDependenciesArgs']]] = None,
                 first_publish_date: Optional[pulumi.Input[str]] = None,
                 icon: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 last_publish_date: Optional[pulumi.Input[str]] = None,
                 metadata_name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 preview_images: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 preview_images_dark: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['MetadataSourceArgs']]] = None,
                 support: Optional[pulumi.Input[pulumi.InputType['MetadataSupportArgs']]] = None,
                 threat_analysis_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 threat_analysis_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MetadataArgs.__new__(MetadataArgs)

            __props__.__dict__["author"] = author
            __props__.__dict__["categories"] = categories
            __props__.__dict__["content_id"] = content_id
            __props__.__dict__["content_schema_version"] = content_schema_version
            __props__.__dict__["custom_version"] = custom_version
            __props__.__dict__["dependencies"] = dependencies
            __props__.__dict__["first_publish_date"] = first_publish_date
            __props__.__dict__["icon"] = icon
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            __props__.__dict__["last_publish_date"] = last_publish_date
            __props__.__dict__["metadata_name"] = metadata_name
            if parent_id is None and not opts.urn:
                raise TypeError("Missing required property 'parent_id'")
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["preview_images"] = preview_images
            __props__.__dict__["preview_images_dark"] = preview_images_dark
            __props__.__dict__["providers"] = providers
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source"] = source
            __props__.__dict__["support"] = support
            __props__.__dict__["threat_analysis_tactics"] = threat_analysis_tactics
            __props__.__dict__["threat_analysis_techniques"] = threat_analysis_techniques
            __props__.__dict__["version"] = version
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20230201:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20230201preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20230301preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20230601preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:Metadata"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:Metadata")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Metadata, __self__).__init__(
            'azure-native:securityinsights:Metadata',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Metadata':
        """
        Get an existing Metadata resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MetadataArgs.__new__(MetadataArgs)

        __props__.__dict__["author"] = None
        __props__.__dict__["categories"] = None
        __props__.__dict__["content_id"] = None
        __props__.__dict__["content_schema_version"] = None
        __props__.__dict__["custom_version"] = None
        __props__.__dict__["dependencies"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["first_publish_date"] = None
        __props__.__dict__["icon"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["last_publish_date"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parent_id"] = None
        __props__.__dict__["preview_images"] = None
        __props__.__dict__["preview_images_dark"] = None
        __props__.__dict__["providers"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["support"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["threat_analysis_tactics"] = None
        __props__.__dict__["threat_analysis_techniques"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return Metadata(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def author(self) -> pulumi.Output[Optional['outputs.MetadataAuthorResponse']]:
        """
        The creator of the content item.
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter
    def categories(self) -> pulumi.Output[Optional['outputs.MetadataCategoriesResponse']]:
        """
        Categories for the solution content item
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter(name="contentId")
    def content_id(self) -> pulumi.Output[Optional[str]]:
        """
        Static ID for the content.  Used to identify dependencies and content from solutions or community.  Hard-coded/static for out of the box content and solutions. Dynamic for user-created.  This is the resource name
        """
        return pulumi.get(self, "content_id")

    @property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> pulumi.Output[Optional[str]]:
        """
        Schema version of the content. Can be used to distinguish between different flow based on the schema version
        """
        return pulumi.get(self, "content_schema_version")

    @property
    @pulumi.getter(name="customVersion")
    def custom_version(self) -> pulumi.Output[Optional[str]]:
        """
        The custom version of the content. A optional free text
        """
        return pulumi.get(self, "custom_version")

    @property
    @pulumi.getter
    def dependencies(self) -> pulumi.Output[Optional['outputs.MetadataDependenciesResponse']]:
        """
        Dependencies for the content item, what other content items it requires to work.  Can describe more complex dependencies using a recursive/nested structure. For a single dependency an id/kind/version can be supplied or operator/criteria for complex formats.
        """
        return pulumi.get(self, "dependencies")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> pulumi.Output[Optional[str]]:
        """
        first publish date solution content item
        """
        return pulumi.get(self, "first_publish_date")

    @property
    @pulumi.getter
    def icon(self) -> pulumi.Output[Optional[str]]:
        """
        the icon identifier. this id can later be fetched from the solution template
        """
        return pulumi.get(self, "icon")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of content the metadata is for.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> pulumi.Output[Optional[str]]:
        """
        last publish date for the solution content item
        """
        return pulumi.get(self, "last_publish_date")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        Full parent resource ID of the content item the metadata is for.  This is the full resource ID including the scope (subscription and resource group)
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="previewImages")
    def preview_images(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        preview image file names. These will be taken from the solution artifacts
        """
        return pulumi.get(self, "preview_images")

    @property
    @pulumi.getter(name="previewImagesDark")
    def preview_images_dark(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        preview image file names. These will be taken from the solution artifacts. used for dark theme support
        """
        return pulumi.get(self, "preview_images_dark")

    @property
    @pulumi.getter
    def providers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Providers for the solution content item
        """
        return pulumi.get(self, "providers")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional['outputs.MetadataSourceResponse']]:
        """
        Source of the content.  This is where/how it was created.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def support(self) -> pulumi.Output[Optional['outputs.MetadataSupportResponse']]:
        """
        Support information for the metadata - type, name, contact information
        """
        return pulumi.get(self, "support")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        the tactics the resource covers
        """
        return pulumi.get(self, "threat_analysis_tactics")

    @property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        the techniques the resource covers, these have to be aligned with the tactics being used
        """
        return pulumi.get(self, "threat_analysis_techniques")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Version of the content.  Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM template best practices.  Can also be any string, but then we cannot guarantee any version checks
        """
        return pulumi.get(self, "version")

