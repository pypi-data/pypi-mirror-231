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

__all__ = ['ConnectedEnvironmentArgs', 'ConnectedEnvironment']

@pulumi.input_type
class ConnectedEnvironmentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 connected_environment_name: Optional[pulumi.Input[str]] = None,
                 custom_domain_configuration: Optional[pulumi.Input['CustomDomainConfigurationArgs']] = None,
                 dapr_ai_connection_string: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 static_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ConnectedEnvironment resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] connected_environment_name: Name of the connectedEnvironment.
        :param pulumi.Input['CustomDomainConfigurationArgs'] custom_domain_configuration: Custom domain configuration for the environment
        :param pulumi.Input[str] dapr_ai_connection_string: Application Insights connection string used by Dapr to export Service to Service communication telemetry
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The complex type of the extended location.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] static_ip: Static IP of the connectedEnvironment
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if connected_environment_name is not None:
            pulumi.set(__self__, "connected_environment_name", connected_environment_name)
        if custom_domain_configuration is not None:
            pulumi.set(__self__, "custom_domain_configuration", custom_domain_configuration)
        if dapr_ai_connection_string is not None:
            pulumi.set(__self__, "dapr_ai_connection_string", dapr_ai_connection_string)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if static_ip is not None:
            pulumi.set(__self__, "static_ip", static_ip)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="connectedEnvironmentName")
    def connected_environment_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the connectedEnvironment.
        """
        return pulumi.get(self, "connected_environment_name")

    @connected_environment_name.setter
    def connected_environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connected_environment_name", value)

    @property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(self) -> Optional[pulumi.Input['CustomDomainConfigurationArgs']]:
        """
        Custom domain configuration for the environment
        """
        return pulumi.get(self, "custom_domain_configuration")

    @custom_domain_configuration.setter
    def custom_domain_configuration(self, value: Optional[pulumi.Input['CustomDomainConfigurationArgs']]):
        pulumi.set(self, "custom_domain_configuration", value)

    @property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        Application Insights connection string used by Dapr to export Service to Service communication telemetry
        """
        return pulumi.get(self, "dapr_ai_connection_string")

    @dapr_ai_connection_string.setter
    def dapr_ai_connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dapr_ai_connection_string", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The complex type of the extended location.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Static IP of the connectedEnvironment
        """
        return pulumi.get(self, "static_ip")

    @static_ip.setter
    def static_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "static_ip", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ConnectedEnvironment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connected_environment_name: Optional[pulumi.Input[str]] = None,
                 custom_domain_configuration: Optional[pulumi.Input[pulumi.InputType['CustomDomainConfigurationArgs']]] = None,
                 dapr_ai_connection_string: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 static_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        An environment for Kubernetes cluster specialized for web workloads by Azure App Service

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connected_environment_name: Name of the connectedEnvironment.
        :param pulumi.Input[pulumi.InputType['CustomDomainConfigurationArgs']] custom_domain_configuration: Custom domain configuration for the environment
        :param pulumi.Input[str] dapr_ai_connection_string: Application Insights connection string used by Dapr to export Service to Service communication telemetry
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The complex type of the extended location.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] static_ip: Static IP of the connectedEnvironment
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectedEnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An environment for Kubernetes cluster specialized for web workloads by Azure App Service

        :param str resource_name: The name of the resource.
        :param ConnectedEnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectedEnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connected_environment_name: Optional[pulumi.Input[str]] = None,
                 custom_domain_configuration: Optional[pulumi.Input[pulumi.InputType['CustomDomainConfigurationArgs']]] = None,
                 dapr_ai_connection_string: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 static_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectedEnvironmentArgs.__new__(ConnectedEnvironmentArgs)

            __props__.__dict__["connected_environment_name"] = connected_environment_name
            __props__.__dict__["custom_domain_configuration"] = custom_domain_configuration
            __props__.__dict__["dapr_ai_connection_string"] = dapr_ai_connection_string
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["static_ip"] = static_ip
            __props__.__dict__["tags"] = tags
            __props__.__dict__["default_domain"] = None
            __props__.__dict__["deployment_errors"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app:ConnectedEnvironment"), pulumi.Alias(type_="azure-native:app/v20220601preview:ConnectedEnvironment"), pulumi.Alias(type_="azure-native:app/v20221001:ConnectedEnvironment"), pulumi.Alias(type_="azure-native:app/v20221101preview:ConnectedEnvironment"), pulumi.Alias(type_="azure-native:app/v20230401preview:ConnectedEnvironment"), pulumi.Alias(type_="azure-native:app/v20230501:ConnectedEnvironment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConnectedEnvironment, __self__).__init__(
            'azure-native:app/v20230502preview:ConnectedEnvironment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectedEnvironment':
        """
        Get an existing ConnectedEnvironment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectedEnvironmentArgs.__new__(ConnectedEnvironmentArgs)

        __props__.__dict__["custom_domain_configuration"] = None
        __props__.__dict__["dapr_ai_connection_string"] = None
        __props__.__dict__["default_domain"] = None
        __props__.__dict__["deployment_errors"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["static_ip"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ConnectedEnvironment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(self) -> pulumi.Output[Optional['outputs.CustomDomainConfigurationResponse']]:
        """
        Custom domain configuration for the environment
        """
        return pulumi.get(self, "custom_domain_configuration")

    @property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> pulumi.Output[Optional[str]]:
        """
        Application Insights connection string used by Dapr to export Service to Service communication telemetry
        """
        return pulumi.get(self, "dapr_ai_connection_string")

    @property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> pulumi.Output[str]:
        """
        Default Domain Name for the cluster
        """
        return pulumi.get(self, "default_domain")

    @property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> pulumi.Output[str]:
        """
        Any errors that occurred during deployment or deployment validation
        """
        return pulumi.get(self, "deployment_errors")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The complex type of the extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the Kubernetes Environment.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> pulumi.Output[Optional[str]]:
        """
        Static IP of the connectedEnvironment
        """
        return pulumi.get(self, "static_ip")

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
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

