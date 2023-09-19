# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WorkflowAccessKeyArgs', 'WorkflowAccessKey']

@pulumi.input_type
class WorkflowAccessKeyArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workflow_name: pulumi.Input[str],
                 access_key_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 not_after: Optional[pulumi.Input[str]] = None,
                 not_before: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkflowAccessKey resource.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] workflow_name: The workflow name.
        :param pulumi.Input[str] access_key_name: The workflow access key name.
        :param pulumi.Input[str] id: Gets or sets the resource id.
        :param pulumi.Input[str] not_after: Gets or sets the not-after time.
        :param pulumi.Input[str] not_before: Gets or sets the not-before time.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workflow_name", workflow_name)
        if access_key_name is not None:
            pulumi.set(__self__, "access_key_name", access_key_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if not_after is not None:
            pulumi.set(__self__, "not_after", not_after)
        if not_before is not None:
            pulumi.set(__self__, "not_before", not_before)

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
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> pulumi.Input[str]:
        """
        The workflow name.
        """
        return pulumi.get(self, "workflow_name")

    @workflow_name.setter
    def workflow_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workflow_name", value)

    @property
    @pulumi.getter(name="accessKeyName")
    def access_key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The workflow access key name.
        """
        return pulumi.get(self, "access_key_name")

    @access_key_name.setter
    def access_key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key_name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the resource id.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the not-after time.
        """
        return pulumi.get(self, "not_after")

    @not_after.setter
    def not_after(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "not_after", value)

    @property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the not-before time.
        """
        return pulumi.get(self, "not_before")

    @not_before.setter
    def not_before(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "not_before", value)


class WorkflowAccessKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 not_after: Optional[pulumi.Input[str]] = None,
                 not_before: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workflow_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Azure REST API version: 2015-02-01-preview. Prior API version in Azure Native 1.x: 2015-02-01-preview

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key_name: The workflow access key name.
        :param pulumi.Input[str] id: Gets or sets the resource id.
        :param pulumi.Input[str] not_after: Gets or sets the not-after time.
        :param pulumi.Input[str] not_before: Gets or sets the not-before time.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] workflow_name: The workflow name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkflowAccessKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure REST API version: 2015-02-01-preview. Prior API version in Azure Native 1.x: 2015-02-01-preview

        :param str resource_name: The name of the resource.
        :param WorkflowAccessKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkflowAccessKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 not_after: Optional[pulumi.Input[str]] = None,
                 not_before: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workflow_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkflowAccessKeyArgs.__new__(WorkflowAccessKeyArgs)

            __props__.__dict__["access_key_name"] = access_key_name
            __props__.__dict__["id"] = id
            __props__.__dict__["not_after"] = not_after
            __props__.__dict__["not_before"] = not_before
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workflow_name is None and not opts.urn:
                raise TypeError("Missing required property 'workflow_name'")
            __props__.__dict__["workflow_name"] = workflow_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:logic/v20150201preview:WorkflowAccessKey")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkflowAccessKey, __self__).__init__(
            'azure-native:logic:WorkflowAccessKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkflowAccessKey':
        """
        Get an existing WorkflowAccessKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkflowAccessKeyArgs.__new__(WorkflowAccessKeyArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["not_after"] = None
        __props__.__dict__["not_before"] = None
        __props__.__dict__["type"] = None
        return WorkflowAccessKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets the workflow access key name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the not-after time.
        """
        return pulumi.get(self, "not_after")

    @property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the not-before time.
        """
        return pulumi.get(self, "not_before")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets the workflow access key type.
        """
        return pulumi.get(self, "type")

