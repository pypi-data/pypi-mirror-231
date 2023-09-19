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

__all__ = ['BuildTaskArgs', 'BuildTask']

@pulumi.input_type
class BuildTaskArgs:
    def __init__(__self__, *,
                 alias: pulumi.Input[str],
                 platform: pulumi.Input['PlatformPropertiesArgs'],
                 registry_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 source_repository: pulumi.Input['SourceRepositoryPropertiesArgs'],
                 build_task_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'BuildTaskStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeout: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a BuildTask resource.
        :param pulumi.Input[str] alias: The alternative updatable name for a build task.
        :param pulumi.Input['PlatformPropertiesArgs'] platform: The platform properties against which the build has to happen.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input['SourceRepositoryPropertiesArgs'] source_repository: The properties that describes the source(code) for the build task.
        :param pulumi.Input[str] build_task_name: The name of the container registry build task.
        :param pulumi.Input[str] location: The location of the resource. This cannot be changed after the resource is created.
        :param pulumi.Input[Union[str, 'BuildTaskStatus']] status: The current status of build task.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[int] timeout: Build timeout in seconds.
        """
        pulumi.set(__self__, "alias", alias)
        pulumi.set(__self__, "platform", platform)
        pulumi.set(__self__, "registry_name", registry_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source_repository", source_repository)
        if build_task_name is not None:
            pulumi.set(__self__, "build_task_name", build_task_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if timeout is None:
            timeout = 3600
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Input[str]:
        """
        The alternative updatable name for a build task.
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: pulumi.Input[str]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Input['PlatformPropertiesArgs']:
        """
        The platform properties against which the build has to happen.
        """
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: pulumi.Input['PlatformPropertiesArgs']):
        pulumi.set(self, "platform", value)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @registry_name.setter
    def registry_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to which the container registry belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sourceRepository")
    def source_repository(self) -> pulumi.Input['SourceRepositoryPropertiesArgs']:
        """
        The properties that describes the source(code) for the build task.
        """
        return pulumi.get(self, "source_repository")

    @source_repository.setter
    def source_repository(self, value: pulumi.Input['SourceRepositoryPropertiesArgs']):
        pulumi.set(self, "source_repository", value)

    @property
    @pulumi.getter(name="buildTaskName")
    def build_task_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the container registry build task.
        """
        return pulumi.get(self, "build_task_name")

    @build_task_name.setter
    def build_task_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "build_task_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource. This cannot be changed after the resource is created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'BuildTaskStatus']]]:
        """
        The current status of build task.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'BuildTaskStatus']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Build timeout in seconds.
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)


class BuildTask(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 build_task_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[pulumi.InputType['PlatformPropertiesArgs']]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_repository: Optional[pulumi.Input[pulumi.InputType['SourceRepositoryPropertiesArgs']]] = None,
                 status: Optional[pulumi.Input[Union[str, 'BuildTaskStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        The build task that has the resource properties and all build items. The build task will have all information to schedule a build against it.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The alternative updatable name for a build task.
        :param pulumi.Input[str] build_task_name: The name of the container registry build task.
        :param pulumi.Input[str] location: The location of the resource. This cannot be changed after the resource is created.
        :param pulumi.Input[pulumi.InputType['PlatformPropertiesArgs']] platform: The platform properties against which the build has to happen.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[pulumi.InputType['SourceRepositoryPropertiesArgs']] source_repository: The properties that describes the source(code) for the build task.
        :param pulumi.Input[Union[str, 'BuildTaskStatus']] status: The current status of build task.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[int] timeout: Build timeout in seconds.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BuildTaskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The build task that has the resource properties and all build items. The build task will have all information to schedule a build against it.

        :param str resource_name: The name of the resource.
        :param BuildTaskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BuildTaskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 build_task_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[pulumi.InputType['PlatformPropertiesArgs']]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_repository: Optional[pulumi.Input[pulumi.InputType['SourceRepositoryPropertiesArgs']]] = None,
                 status: Optional[pulumi.Input[Union[str, 'BuildTaskStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BuildTaskArgs.__new__(BuildTaskArgs)

            if alias is None and not opts.urn:
                raise TypeError("Missing required property 'alias'")
            __props__.__dict__["alias"] = alias
            __props__.__dict__["build_task_name"] = build_task_name
            __props__.__dict__["location"] = location
            if platform is None and not opts.urn:
                raise TypeError("Missing required property 'platform'")
            __props__.__dict__["platform"] = platform
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__.__dict__["registry_name"] = registry_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source_repository is None and not opts.urn:
                raise TypeError("Missing required property 'source_repository'")
            __props__.__dict__["source_repository"] = source_repository
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            if timeout is None:
                timeout = 3600
            __props__.__dict__["timeout"] = timeout
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerregistry:BuildTask"), pulumi.Alias(type_="azure-native:containerregistry/v20180901:BuildTask"), pulumi.Alias(type_="azure-native:containerregistry/v20190401:BuildTask"), pulumi.Alias(type_="azure-native:containerregistry/v20190601preview:BuildTask")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BuildTask, __self__).__init__(
            'azure-native:containerregistry/v20180201preview:BuildTask',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BuildTask':
        """
        Get an existing BuildTask resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BuildTaskArgs.__new__(BuildTaskArgs)

        __props__.__dict__["alias"] = None
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["platform"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source_repository"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["timeout"] = None
        __props__.__dict__["type"] = None
        return BuildTask(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Output[str]:
        """
        The alternative updatable name for a build task.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The creation date of build task.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the resource. This cannot be changed after the resource is created.
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
    @pulumi.getter
    def platform(self) -> pulumi.Output['outputs.PlatformPropertiesResponse']:
        """
        The platform properties against which the build has to happen.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the build task.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceRepository")
    def source_repository(self) -> pulumi.Output['outputs.SourceRepositoryPropertiesResponse']:
        """
        The properties that describes the source(code) for the build task.
        """
        return pulumi.get(self, "source_repository")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The current status of build task.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[int]]:
        """
        Build timeout in seconds.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

