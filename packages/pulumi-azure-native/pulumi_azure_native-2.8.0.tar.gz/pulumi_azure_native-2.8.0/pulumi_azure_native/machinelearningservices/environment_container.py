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
from ._inputs import *

__all__ = ['EnvironmentContainerInitArgs', 'EnvironmentContainer']

@pulumi.input_type
class EnvironmentContainerInitArgs:
    def __init__(__self__, *,
                 environment_container_properties: pulumi.Input['EnvironmentContainerArgs'],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EnvironmentContainer resource.
        :param pulumi.Input['EnvironmentContainerArgs'] environment_container_properties: [Required] Additional attributes of the entity.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[str] name: Container name. This is case-sensitive.
        """
        pulumi.set(__self__, "environment_container_properties", environment_container_properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="environmentContainerProperties")
    def environment_container_properties(self) -> pulumi.Input['EnvironmentContainerArgs']:
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "environment_container_properties")

    @environment_container_properties.setter
    def environment_container_properties(self, value: pulumi.Input['EnvironmentContainerArgs']):
        pulumi.set(self, "environment_container_properties", value)

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
        Name of Azure Machine Learning workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Container name. This is case-sensitive.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class EnvironmentContainer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environment_container_properties: Optional[pulumi.Input[pulumi.InputType['EnvironmentContainerArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Azure Resource Manager resource envelope.
        Azure REST API version: 2023-04-01. Prior API version in Azure Native 1.x: 2021-03-01-preview

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['EnvironmentContainerArgs']] environment_container_properties: [Required] Additional attributes of the entity.
        :param pulumi.Input[str] name: Container name. This is case-sensitive.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentContainerInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure Resource Manager resource envelope.
        Azure REST API version: 2023-04-01. Prior API version in Azure Native 1.x: 2021-03-01-preview

        :param str resource_name: The name of the resource.
        :param EnvironmentContainerInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentContainerInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environment_container_properties: Optional[pulumi.Input[pulumi.InputType['EnvironmentContainerArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentContainerInitArgs.__new__(EnvironmentContainerInitArgs)

            if environment_container_properties is None and not opts.urn:
                raise TypeError("Missing required property 'environment_container_properties'")
            __props__.__dict__["environment_container_properties"] = environment_container_properties
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:machinelearningservices/v20210301preview:EnvironmentContainer"), pulumi.Alias(type_="azure-native:machinelearningservices/v20220201preview:EnvironmentContainer"), pulumi.Alias(type_="azure-native:machinelearningservices/v20220501:EnvironmentContainer"), pulumi.Alias(type_="azure-native:machinelearningservices/v20220601preview:EnvironmentContainer"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221001:EnvironmentContainer"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221001preview:EnvironmentContainer"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221201preview:EnvironmentContainer"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230201preview:EnvironmentContainer"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230401:EnvironmentContainer"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230401preview:EnvironmentContainer"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230601preview:EnvironmentContainer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EnvironmentContainer, __self__).__init__(
            'azure-native:machinelearningservices:EnvironmentContainer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EnvironmentContainer':
        """
        Get an existing EnvironmentContainer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnvironmentContainerInitArgs.__new__(EnvironmentContainerInitArgs)

        __props__.__dict__["environment_container_properties"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return EnvironmentContainer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="environmentContainerProperties")
    def environment_container_properties(self) -> pulumi.Output['outputs.EnvironmentContainerResponse']:
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "environment_container_properties")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

