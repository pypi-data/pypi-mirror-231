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

__all__ = ['IotSecuritySolutionArgs', 'IotSecuritySolution']

@pulumi.input_type
class IotSecuritySolutionArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 iot_hubs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 resource_group_name: pulumi.Input[str],
                 additional_workspaces: Optional[pulumi.Input[Sequence[pulumi.Input['AdditionalWorkspacesPropertiesArgs']]]] = None,
                 disabled_data_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'DataSource']]]]] = None,
                 export: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'ExportData']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 recommendations_configuration: Optional[pulumi.Input[Sequence[pulumi.Input['RecommendationConfigurationPropertiesArgs']]]] = None,
                 solution_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'SecuritySolutionStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unmasked_ip_logging_status: Optional[pulumi.Input[Union[str, 'UnmaskedIpLoggingStatus']]] = None,
                 user_defined_resources: Optional[pulumi.Input['UserDefinedResourcesPropertiesArgs']] = None,
                 workspace: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IotSecuritySolution resource.
        :param pulumi.Input[str] display_name: Resource display name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] iot_hubs: IoT Hub resource IDs
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['AdditionalWorkspacesPropertiesArgs']]] additional_workspaces: List of additional workspaces
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'DataSource']]]] disabled_data_sources: Disabled data sources. Disabling these data sources compromises the system.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'ExportData']]]] export: List of additional options for exporting to workspace data.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Sequence[pulumi.Input['RecommendationConfigurationPropertiesArgs']]] recommendations_configuration: List of the configuration status for each recommendation type.
        :param pulumi.Input[str] solution_name: The name of the IoT Security solution.
        :param pulumi.Input[Union[str, 'SecuritySolutionStatus']] status: Status of the IoT Security solution.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[Union[str, 'UnmaskedIpLoggingStatus']] unmasked_ip_logging_status: Unmasked IP address logging status
        :param pulumi.Input['UserDefinedResourcesPropertiesArgs'] user_defined_resources: Properties of the IoT Security solution's user defined resources.
        :param pulumi.Input[str] workspace: Workspace resource ID
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "iot_hubs", iot_hubs)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if additional_workspaces is not None:
            pulumi.set(__self__, "additional_workspaces", additional_workspaces)
        if disabled_data_sources is not None:
            pulumi.set(__self__, "disabled_data_sources", disabled_data_sources)
        if export is not None:
            pulumi.set(__self__, "export", export)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if recommendations_configuration is not None:
            pulumi.set(__self__, "recommendations_configuration", recommendations_configuration)
        if solution_name is not None:
            pulumi.set(__self__, "solution_name", solution_name)
        if status is None:
            status = 'Enabled'
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if unmasked_ip_logging_status is None:
            unmasked_ip_logging_status = 'Disabled'
        if unmasked_ip_logging_status is not None:
            pulumi.set(__self__, "unmasked_ip_logging_status", unmasked_ip_logging_status)
        if user_defined_resources is not None:
            pulumi.set(__self__, "user_defined_resources", user_defined_resources)
        if workspace is not None:
            pulumi.set(__self__, "workspace", workspace)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        Resource display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        IoT Hub resource IDs
        """
        return pulumi.get(self, "iot_hubs")

    @iot_hubs.setter
    def iot_hubs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "iot_hubs", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="additionalWorkspaces")
    def additional_workspaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AdditionalWorkspacesPropertiesArgs']]]]:
        """
        List of additional workspaces
        """
        return pulumi.get(self, "additional_workspaces")

    @additional_workspaces.setter
    def additional_workspaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AdditionalWorkspacesPropertiesArgs']]]]):
        pulumi.set(self, "additional_workspaces", value)

    @property
    @pulumi.getter(name="disabledDataSources")
    def disabled_data_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'DataSource']]]]]:
        """
        Disabled data sources. Disabling these data sources compromises the system.
        """
        return pulumi.get(self, "disabled_data_sources")

    @disabled_data_sources.setter
    def disabled_data_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'DataSource']]]]]):
        pulumi.set(self, "disabled_data_sources", value)

    @property
    @pulumi.getter
    def export(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'ExportData']]]]]:
        """
        List of additional options for exporting to workspace data.
        """
        return pulumi.get(self, "export")

    @export.setter
    def export(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'ExportData']]]]]):
        pulumi.set(self, "export", value)

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
    @pulumi.getter(name="recommendationsConfiguration")
    def recommendations_configuration(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RecommendationConfigurationPropertiesArgs']]]]:
        """
        List of the configuration status for each recommendation type.
        """
        return pulumi.get(self, "recommendations_configuration")

    @recommendations_configuration.setter
    def recommendations_configuration(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RecommendationConfigurationPropertiesArgs']]]]):
        pulumi.set(self, "recommendations_configuration", value)

    @property
    @pulumi.getter(name="solutionName")
    def solution_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the IoT Security solution.
        """
        return pulumi.get(self, "solution_name")

    @solution_name.setter
    def solution_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "solution_name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'SecuritySolutionStatus']]]:
        """
        Status of the IoT Security solution.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'SecuritySolutionStatus']]]):
        pulumi.set(self, "status", value)

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

    @property
    @pulumi.getter(name="unmaskedIpLoggingStatus")
    def unmasked_ip_logging_status(self) -> Optional[pulumi.Input[Union[str, 'UnmaskedIpLoggingStatus']]]:
        """
        Unmasked IP address logging status
        """
        return pulumi.get(self, "unmasked_ip_logging_status")

    @unmasked_ip_logging_status.setter
    def unmasked_ip_logging_status(self, value: Optional[pulumi.Input[Union[str, 'UnmaskedIpLoggingStatus']]]):
        pulumi.set(self, "unmasked_ip_logging_status", value)

    @property
    @pulumi.getter(name="userDefinedResources")
    def user_defined_resources(self) -> Optional[pulumi.Input['UserDefinedResourcesPropertiesArgs']]:
        """
        Properties of the IoT Security solution's user defined resources.
        """
        return pulumi.get(self, "user_defined_resources")

    @user_defined_resources.setter
    def user_defined_resources(self, value: Optional[pulumi.Input['UserDefinedResourcesPropertiesArgs']]):
        pulumi.set(self, "user_defined_resources", value)

    @property
    @pulumi.getter
    def workspace(self) -> Optional[pulumi.Input[str]]:
        """
        Workspace resource ID
        """
        return pulumi.get(self, "workspace")

    @workspace.setter
    def workspace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace", value)


class IotSecuritySolution(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_workspaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdditionalWorkspacesPropertiesArgs']]]]] = None,
                 disabled_data_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'DataSource']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 export: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'ExportData']]]]] = None,
                 iot_hubs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 recommendations_configuration: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RecommendationConfigurationPropertiesArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 solution_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'SecuritySolutionStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unmasked_ip_logging_status: Optional[pulumi.Input[Union[str, 'UnmaskedIpLoggingStatus']]] = None,
                 user_defined_resources: Optional[pulumi.Input[pulumi.InputType['UserDefinedResourcesPropertiesArgs']]] = None,
                 workspace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        IoT Security solution configuration and resource information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdditionalWorkspacesPropertiesArgs']]]] additional_workspaces: List of additional workspaces
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'DataSource']]]] disabled_data_sources: Disabled data sources. Disabling these data sources compromises the system.
        :param pulumi.Input[str] display_name: Resource display name.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'ExportData']]]] export: List of additional options for exporting to workspace data.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] iot_hubs: IoT Hub resource IDs
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RecommendationConfigurationPropertiesArgs']]]] recommendations_configuration: List of the configuration status for each recommendation type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] solution_name: The name of the IoT Security solution.
        :param pulumi.Input[Union[str, 'SecuritySolutionStatus']] status: Status of the IoT Security solution.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[Union[str, 'UnmaskedIpLoggingStatus']] unmasked_ip_logging_status: Unmasked IP address logging status
        :param pulumi.Input[pulumi.InputType['UserDefinedResourcesPropertiesArgs']] user_defined_resources: Properties of the IoT Security solution's user defined resources.
        :param pulumi.Input[str] workspace: Workspace resource ID
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IotSecuritySolutionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        IoT Security solution configuration and resource information.

        :param str resource_name: The name of the resource.
        :param IotSecuritySolutionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IotSecuritySolutionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_workspaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdditionalWorkspacesPropertiesArgs']]]]] = None,
                 disabled_data_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'DataSource']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 export: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'ExportData']]]]] = None,
                 iot_hubs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 recommendations_configuration: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RecommendationConfigurationPropertiesArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 solution_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'SecuritySolutionStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unmasked_ip_logging_status: Optional[pulumi.Input[Union[str, 'UnmaskedIpLoggingStatus']]] = None,
                 user_defined_resources: Optional[pulumi.Input[pulumi.InputType['UserDefinedResourcesPropertiesArgs']]] = None,
                 workspace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IotSecuritySolutionArgs.__new__(IotSecuritySolutionArgs)

            __props__.__dict__["additional_workspaces"] = additional_workspaces
            __props__.__dict__["disabled_data_sources"] = disabled_data_sources
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["export"] = export
            if iot_hubs is None and not opts.urn:
                raise TypeError("Missing required property 'iot_hubs'")
            __props__.__dict__["iot_hubs"] = iot_hubs
            __props__.__dict__["location"] = location
            __props__.__dict__["recommendations_configuration"] = recommendations_configuration
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["solution_name"] = solution_name
            if status is None:
                status = 'Enabled'
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            if unmasked_ip_logging_status is None:
                unmasked_ip_logging_status = 'Disabled'
            __props__.__dict__["unmasked_ip_logging_status"] = unmasked_ip_logging_status
            __props__.__dict__["user_defined_resources"] = user_defined_resources
            __props__.__dict__["workspace"] = workspace
            __props__.__dict__["auto_discovered_resources"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security:IotSecuritySolution"), pulumi.Alias(type_="azure-native:security/v20170801preview:IotSecuritySolution")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IotSecuritySolution, __self__).__init__(
            'azure-native:security/v20190801:IotSecuritySolution',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IotSecuritySolution':
        """
        Get an existing IotSecuritySolution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IotSecuritySolutionArgs.__new__(IotSecuritySolutionArgs)

        __props__.__dict__["additional_workspaces"] = None
        __props__.__dict__["auto_discovered_resources"] = None
        __props__.__dict__["disabled_data_sources"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["export"] = None
        __props__.__dict__["iot_hubs"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["recommendations_configuration"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["unmasked_ip_logging_status"] = None
        __props__.__dict__["user_defined_resources"] = None
        __props__.__dict__["workspace"] = None
        return IotSecuritySolution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalWorkspaces")
    def additional_workspaces(self) -> pulumi.Output[Optional[Sequence['outputs.AdditionalWorkspacesPropertiesResponse']]]:
        """
        List of additional workspaces
        """
        return pulumi.get(self, "additional_workspaces")

    @property
    @pulumi.getter(name="autoDiscoveredResources")
    def auto_discovered_resources(self) -> pulumi.Output[Sequence[str]]:
        """
        List of resources that were automatically discovered as relevant to the security solution.
        """
        return pulumi.get(self, "auto_discovered_resources")

    @property
    @pulumi.getter(name="disabledDataSources")
    def disabled_data_sources(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Disabled data sources. Disabling these data sources compromises the system.
        """
        return pulumi.get(self, "disabled_data_sources")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Resource display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def export(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of additional options for exporting to workspace data.
        """
        return pulumi.get(self, "export")

    @property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(self) -> pulumi.Output[Sequence[str]]:
        """
        IoT Hub resource IDs
        """
        return pulumi.get(self, "iot_hubs")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recommendationsConfiguration")
    def recommendations_configuration(self) -> pulumi.Output[Optional[Sequence['outputs.RecommendationConfigurationPropertiesResponse']]]:
        """
        List of the configuration status for each recommendation type.
        """
        return pulumi.get(self, "recommendations_configuration")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Status of the IoT Security solution.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="unmaskedIpLoggingStatus")
    def unmasked_ip_logging_status(self) -> pulumi.Output[Optional[str]]:
        """
        Unmasked IP address logging status
        """
        return pulumi.get(self, "unmasked_ip_logging_status")

    @property
    @pulumi.getter(name="userDefinedResources")
    def user_defined_resources(self) -> pulumi.Output[Optional['outputs.UserDefinedResourcesPropertiesResponse']]:
        """
        Properties of the IoT Security solution's user defined resources.
        """
        return pulumi.get(self, "user_defined_resources")

    @property
    @pulumi.getter
    def workspace(self) -> pulumi.Output[Optional[str]]:
        """
        Workspace resource ID
        """
        return pulumi.get(self, "workspace")

