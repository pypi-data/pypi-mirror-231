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

__all__ = ['WorkbookTemplateArgs', 'WorkbookTemplate']

@pulumi.input_type
class WorkbookTemplateArgs:
    def __init__(__self__, *,
                 galleries: pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateGalleryArgs']]],
                 resource_group_name: pulumi.Input[str],
                 template_data: Any,
                 author: Optional[pulumi.Input[str]] = None,
                 localized: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateLocalizedGalleryArgs']]]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a WorkbookTemplate resource.
        :param pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateGalleryArgs']]] galleries: Workbook galleries supported by the template.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param Any template_data: Valid JSON object containing workbook template payload.
        :param pulumi.Input[str] author: Information about the author of the workbook template.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateLocalizedGalleryArgs']]]]] localized: Key value pair of localized gallery. Each key is the locale code of languages supported by the Azure portal.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[int] priority: Priority of the template. Determines which template to open when a workbook gallery is opened in viewer mode.
        :param pulumi.Input[str] resource_name: The name of the Application Insights component resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "galleries", galleries)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "template_data", template_data)
        if author is not None:
            pulumi.set(__self__, "author", author)
        if localized is not None:
            pulumi.set(__self__, "localized", localized)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def galleries(self) -> pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateGalleryArgs']]]:
        """
        Workbook galleries supported by the template.
        """
        return pulumi.get(self, "galleries")

    @galleries.setter
    def galleries(self, value: pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateGalleryArgs']]]):
        pulumi.set(self, "galleries", value)

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
    @pulumi.getter(name="templateData")
    def template_data(self) -> Any:
        """
        Valid JSON object containing workbook template payload.
        """
        return pulumi.get(self, "template_data")

    @template_data.setter
    def template_data(self, value: Any):
        pulumi.set(self, "template_data", value)

    @property
    @pulumi.getter
    def author(self) -> Optional[pulumi.Input[str]]:
        """
        Information about the author of the workbook template.
        """
        return pulumi.get(self, "author")

    @author.setter
    def author(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "author", value)

    @property
    @pulumi.getter
    def localized(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateLocalizedGalleryArgs']]]]]]:
        """
        Key value pair of localized gallery. Each key is the locale code of languages supported by the Azure portal.
        """
        return pulumi.get(self, "localized")

    @localized.setter
    def localized(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['WorkbookTemplateLocalizedGalleryArgs']]]]]]):
        pulumi.set(self, "localized", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority of the template. Determines which template to open when a workbook gallery is opened in viewer mode.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Application Insights component resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class WorkbookTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 author: Optional[pulumi.Input[str]] = None,
                 galleries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkbookTemplateGalleryArgs']]]]] = None,
                 localized: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkbookTemplateLocalizedGalleryArgs']]]]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template_data: Optional[Any] = None,
                 __props__=None):
        """
        An Application Insights workbook template definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] author: Information about the author of the workbook template.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkbookTemplateGalleryArgs']]]] galleries: Workbook galleries supported by the template.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkbookTemplateLocalizedGalleryArgs']]]]]] localized: Key value pair of localized gallery. Each key is the locale code of languages supported by the Azure portal.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[int] priority: Priority of the template. Determines which template to open when a workbook gallery is opened in viewer mode.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the Application Insights component resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param Any template_data: Valid JSON object containing workbook template payload.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkbookTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Application Insights workbook template definition.

        :param str resource_name: The name of the resource.
        :param WorkbookTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkbookTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 author: Optional[pulumi.Input[str]] = None,
                 galleries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkbookTemplateGalleryArgs']]]]] = None,
                 localized: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkbookTemplateLocalizedGalleryArgs']]]]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template_data: Optional[Any] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkbookTemplateArgs.__new__(WorkbookTemplateArgs)

            __props__.__dict__["author"] = author
            if galleries is None and not opts.urn:
                raise TypeError("Missing required property 'galleries'")
            __props__.__dict__["galleries"] = galleries
            __props__.__dict__["localized"] = localized
            __props__.__dict__["location"] = location
            __props__.__dict__["priority"] = priority
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["tags"] = tags
            if template_data is None and not opts.urn:
                raise TypeError("Missing required property 'template_data'")
            __props__.__dict__["template_data"] = template_data
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights:WorkbookTemplate"), pulumi.Alias(type_="azure-native:insights/v20191017preview:WorkbookTemplate")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkbookTemplate, __self__).__init__(
            'azure-native:insights/v20201120:WorkbookTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkbookTemplate':
        """
        Get an existing WorkbookTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkbookTemplateArgs.__new__(WorkbookTemplateArgs)

        __props__.__dict__["author"] = None
        __props__.__dict__["galleries"] = None
        __props__.__dict__["localized"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["template_data"] = None
        __props__.__dict__["type"] = None
        return WorkbookTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def author(self) -> pulumi.Output[Optional[str]]:
        """
        Information about the author of the workbook template.
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter
    def galleries(self) -> pulumi.Output[Sequence['outputs.WorkbookTemplateGalleryResponse']]:
        """
        Workbook galleries supported by the template.
        """
        return pulumi.get(self, "galleries")

    @property
    @pulumi.getter
    def localized(self) -> pulumi.Output[Optional[Mapping[str, Sequence['outputs.WorkbookTemplateLocalizedGalleryResponse']]]]:
        """
        Key value pair of localized gallery. Each key is the locale code of languages supported by the Azure portal.
        """
        return pulumi.get(self, "localized")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Priority of the template. Determines which template to open when a workbook gallery is opened in viewer mode.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateData")
    def template_data(self) -> pulumi.Output[Any]:
        """
        Valid JSON object containing workbook template payload.
        """
        return pulumi.get(self, "template_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

