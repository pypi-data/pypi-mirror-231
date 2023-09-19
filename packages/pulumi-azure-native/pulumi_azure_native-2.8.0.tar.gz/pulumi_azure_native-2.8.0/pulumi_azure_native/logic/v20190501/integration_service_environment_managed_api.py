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

__all__ = ['IntegrationServiceEnvironmentManagedApiArgs', 'IntegrationServiceEnvironmentManagedApi']

@pulumi.input_type
class IntegrationServiceEnvironmentManagedApiArgs:
    def __init__(__self__, *,
                 integration_service_environment_name: pulumi.Input[str],
                 resource_group: pulumi.Input[str],
                 api_name: Optional[pulumi.Input[str]] = None,
                 deployment_parameters: Optional[pulumi.Input['IntegrationServiceEnvironmentManagedApiDeploymentParametersArgs']] = None,
                 integration_service_environment: Optional[pulumi.Input['ResourceReferenceArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a IntegrationServiceEnvironmentManagedApi resource.
        :param pulumi.Input[str] integration_service_environment_name: The integration service environment name.
        :param pulumi.Input[str] resource_group: The resource group name.
        :param pulumi.Input[str] api_name: The api name.
        :param pulumi.Input['IntegrationServiceEnvironmentManagedApiDeploymentParametersArgs'] deployment_parameters: The integration service environment managed api deployment parameters.
        :param pulumi.Input['ResourceReferenceArgs'] integration_service_environment: The integration service environment reference.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "integration_service_environment_name", integration_service_environment_name)
        pulumi.set(__self__, "resource_group", resource_group)
        if api_name is not None:
            pulumi.set(__self__, "api_name", api_name)
        if deployment_parameters is not None:
            pulumi.set(__self__, "deployment_parameters", deployment_parameters)
        if integration_service_environment is not None:
            pulumi.set(__self__, "integration_service_environment", integration_service_environment)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="integrationServiceEnvironmentName")
    def integration_service_environment_name(self) -> pulumi.Input[str]:
        """
        The integration service environment name.
        """
        return pulumi.get(self, "integration_service_environment_name")

    @integration_service_environment_name.setter
    def integration_service_environment_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_service_environment_name", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group", value)

    @property
    @pulumi.getter(name="apiName")
    def api_name(self) -> Optional[pulumi.Input[str]]:
        """
        The api name.
        """
        return pulumi.get(self, "api_name")

    @api_name.setter
    def api_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_name", value)

    @property
    @pulumi.getter(name="deploymentParameters")
    def deployment_parameters(self) -> Optional[pulumi.Input['IntegrationServiceEnvironmentManagedApiDeploymentParametersArgs']]:
        """
        The integration service environment managed api deployment parameters.
        """
        return pulumi.get(self, "deployment_parameters")

    @deployment_parameters.setter
    def deployment_parameters(self, value: Optional[pulumi.Input['IntegrationServiceEnvironmentManagedApiDeploymentParametersArgs']]):
        pulumi.set(self, "deployment_parameters", value)

    @property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(self) -> Optional[pulumi.Input['ResourceReferenceArgs']]:
        """
        The integration service environment reference.
        """
        return pulumi.get(self, "integration_service_environment")

    @integration_service_environment.setter
    def integration_service_environment(self, value: Optional[pulumi.Input['ResourceReferenceArgs']]):
        pulumi.set(self, "integration_service_environment", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class IntegrationServiceEnvironmentManagedApi(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_name: Optional[pulumi.Input[str]] = None,
                 deployment_parameters: Optional[pulumi.Input[pulumi.InputType['IntegrationServiceEnvironmentManagedApiDeploymentParametersArgs']]] = None,
                 integration_service_environment: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 integration_service_environment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The integration service environment managed api.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_name: The api name.
        :param pulumi.Input[pulumi.InputType['IntegrationServiceEnvironmentManagedApiDeploymentParametersArgs']] deployment_parameters: The integration service environment managed api deployment parameters.
        :param pulumi.Input[pulumi.InputType['ResourceReferenceArgs']] integration_service_environment: The integration service environment reference.
        :param pulumi.Input[str] integration_service_environment_name: The integration service environment name.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] resource_group: The resource group name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationServiceEnvironmentManagedApiArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The integration service environment managed api.

        :param str resource_name: The name of the resource.
        :param IntegrationServiceEnvironmentManagedApiArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationServiceEnvironmentManagedApiArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_name: Optional[pulumi.Input[str]] = None,
                 deployment_parameters: Optional[pulumi.Input[pulumi.InputType['IntegrationServiceEnvironmentManagedApiDeploymentParametersArgs']]] = None,
                 integration_service_environment: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 integration_service_environment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationServiceEnvironmentManagedApiArgs.__new__(IntegrationServiceEnvironmentManagedApiArgs)

            __props__.__dict__["api_name"] = api_name
            __props__.__dict__["deployment_parameters"] = deployment_parameters
            __props__.__dict__["integration_service_environment"] = integration_service_environment
            if integration_service_environment_name is None and not opts.urn:
                raise TypeError("Missing required property 'integration_service_environment_name'")
            __props__.__dict__["integration_service_environment_name"] = integration_service_environment_name
            __props__.__dict__["location"] = location
            if resource_group is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group'")
            __props__.__dict__["resource_group"] = resource_group
            __props__.__dict__["tags"] = tags
            __props__.__dict__["api_definition_url"] = None
            __props__.__dict__["api_definitions"] = None
            __props__.__dict__["backend_service"] = None
            __props__.__dict__["capabilities"] = None
            __props__.__dict__["category"] = None
            __props__.__dict__["connection_parameters"] = None
            __props__.__dict__["general_information"] = None
            __props__.__dict__["metadata"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["policies"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["runtime_urls"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:logic:IntegrationServiceEnvironmentManagedApi")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IntegrationServiceEnvironmentManagedApi, __self__).__init__(
            'azure-native:logic/v20190501:IntegrationServiceEnvironmentManagedApi',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IntegrationServiceEnvironmentManagedApi':
        """
        Get an existing IntegrationServiceEnvironmentManagedApi resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IntegrationServiceEnvironmentManagedApiArgs.__new__(IntegrationServiceEnvironmentManagedApiArgs)

        __props__.__dict__["api_definition_url"] = None
        __props__.__dict__["api_definitions"] = None
        __props__.__dict__["backend_service"] = None
        __props__.__dict__["capabilities"] = None
        __props__.__dict__["category"] = None
        __props__.__dict__["connection_parameters"] = None
        __props__.__dict__["deployment_parameters"] = None
        __props__.__dict__["general_information"] = None
        __props__.__dict__["integration_service_environment"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["policies"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["runtime_urls"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return IntegrationServiceEnvironmentManagedApi(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiDefinitionUrl")
    def api_definition_url(self) -> pulumi.Output[str]:
        """
        The API definition.
        """
        return pulumi.get(self, "api_definition_url")

    @property
    @pulumi.getter(name="apiDefinitions")
    def api_definitions(self) -> pulumi.Output['outputs.ApiResourceDefinitionsResponse']:
        """
        The api definitions.
        """
        return pulumi.get(self, "api_definitions")

    @property
    @pulumi.getter(name="backendService")
    def backend_service(self) -> pulumi.Output['outputs.ApiResourceBackendServiceResponse']:
        """
        The backend service.
        """
        return pulumi.get(self, "backend_service")

    @property
    @pulumi.getter
    def capabilities(self) -> pulumi.Output[Sequence[str]]:
        """
        The capabilities.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        """
        The category.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="connectionParameters")
    def connection_parameters(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        The connection parameters.
        """
        return pulumi.get(self, "connection_parameters")

    @property
    @pulumi.getter(name="deploymentParameters")
    def deployment_parameters(self) -> pulumi.Output[Optional['outputs.IntegrationServiceEnvironmentManagedApiDeploymentParametersResponse']]:
        """
        The integration service environment managed api deployment parameters.
        """
        return pulumi.get(self, "deployment_parameters")

    @property
    @pulumi.getter(name="generalInformation")
    def general_information(self) -> pulumi.Output['outputs.ApiResourceGeneralInformationResponse']:
        """
        The api general information.
        """
        return pulumi.get(self, "general_information")

    @property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(self) -> pulumi.Output[Optional['outputs.ResourceReferenceResponse']]:
        """
        The integration service environment reference.
        """
        return pulumi.get(self, "integration_service_environment")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['outputs.ApiResourceMetadataResponse']:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output['outputs.ApiResourcePoliciesResponse']:
        """
        The policies for the API.
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="runtimeUrls")
    def runtime_urls(self) -> pulumi.Output[Sequence[str]]:
        """
        The runtime urls.
        """
        return pulumi.get(self, "runtime_urls")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")

