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

__all__ = ['ServerSitesControllerArgs', 'ServerSitesController']

@pulumi.input_type
class ServerSitesControllerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 agent_details: Optional[pulumi.Input['SiteAgentPropertiesArgs']] = None,
                 appliance_name: Optional[pulumi.Input[str]] = None,
                 discovery_solution_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 service_principal_identity_details: Optional[pulumi.Input['SiteSpnPropertiesArgs']] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ServerSitesController resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['SiteAgentPropertiesArgs'] agent_details: Gets or sets the on-premises agent details.
        :param pulumi.Input[str] appliance_name: Gets or sets the Appliance Name.
        :param pulumi.Input[str] discovery_solution_id: Gets or sets the ARM ID of migration hub solution for SDS.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['SiteSpnPropertiesArgs'] service_principal_identity_details: Gets or sets the service principal identity details used by agent for
               communication
                           to the service.
        :param pulumi.Input[str] site_name: Site name
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if agent_details is not None:
            pulumi.set(__self__, "agent_details", agent_details)
        if appliance_name is not None:
            pulumi.set(__self__, "appliance_name", appliance_name)
        if discovery_solution_id is not None:
            pulumi.set(__self__, "discovery_solution_id", discovery_solution_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if service_principal_identity_details is not None:
            pulumi.set(__self__, "service_principal_identity_details", service_principal_identity_details)
        if site_name is not None:
            pulumi.set(__self__, "site_name", site_name)
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
    @pulumi.getter(name="agentDetails")
    def agent_details(self) -> Optional[pulumi.Input['SiteAgentPropertiesArgs']]:
        """
        Gets or sets the on-premises agent details.
        """
        return pulumi.get(self, "agent_details")

    @agent_details.setter
    def agent_details(self, value: Optional[pulumi.Input['SiteAgentPropertiesArgs']]):
        pulumi.set(self, "agent_details", value)

    @property
    @pulumi.getter(name="applianceName")
    def appliance_name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the Appliance Name.
        """
        return pulumi.get(self, "appliance_name")

    @appliance_name.setter
    def appliance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "appliance_name", value)

    @property
    @pulumi.getter(name="discoverySolutionId")
    def discovery_solution_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the ARM ID of migration hub solution for SDS.
        """
        return pulumi.get(self, "discovery_solution_id")

    @discovery_solution_id.setter
    def discovery_solution_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "discovery_solution_id", value)

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
    @pulumi.getter(name="servicePrincipalIdentityDetails")
    def service_principal_identity_details(self) -> Optional[pulumi.Input['SiteSpnPropertiesArgs']]:
        """
        Gets or sets the service principal identity details used by agent for
        communication
                    to the service.
        """
        return pulumi.get(self, "service_principal_identity_details")

    @service_principal_identity_details.setter
    def service_principal_identity_details(self, value: Optional[pulumi.Input['SiteSpnPropertiesArgs']]):
        pulumi.set(self, "service_principal_identity_details", value)

    @property
    @pulumi.getter(name="siteName")
    def site_name(self) -> Optional[pulumi.Input[str]]:
        """
        Site name
        """
        return pulumi.get(self, "site_name")

    @site_name.setter
    def site_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_name", value)

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


class ServerSitesController(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_details: Optional[pulumi.Input[pulumi.InputType['SiteAgentPropertiesArgs']]] = None,
                 appliance_name: Optional[pulumi.Input[str]] = None,
                 discovery_solution_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_principal_identity_details: Optional[pulumi.Input[pulumi.InputType['SiteSpnPropertiesArgs']]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A ServerSiteResource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SiteAgentPropertiesArgs']] agent_details: Gets or sets the on-premises agent details.
        :param pulumi.Input[str] appliance_name: Gets or sets the Appliance Name.
        :param pulumi.Input[str] discovery_solution_id: Gets or sets the ARM ID of migration hub solution for SDS.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SiteSpnPropertiesArgs']] service_principal_identity_details: Gets or sets the service principal identity details used by agent for
               communication
                           to the service.
        :param pulumi.Input[str] site_name: Site name
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerSitesControllerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A ServerSiteResource

        :param str resource_name: The name of the resource.
        :param ServerSitesControllerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerSitesControllerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_details: Optional[pulumi.Input[pulumi.InputType['SiteAgentPropertiesArgs']]] = None,
                 appliance_name: Optional[pulumi.Input[str]] = None,
                 discovery_solution_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_principal_identity_details: Optional[pulumi.Input[pulumi.InputType['SiteSpnPropertiesArgs']]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerSitesControllerArgs.__new__(ServerSitesControllerArgs)

            __props__.__dict__["agent_details"] = agent_details
            __props__.__dict__["appliance_name"] = appliance_name
            __props__.__dict__["discovery_solution_id"] = discovery_solution_id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["service_principal_identity_details"] = service_principal_identity_details
            __props__.__dict__["site_name"] = site_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["master_site_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["service_endpoint"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:offazure:ServerSitesController")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerSitesController, __self__).__init__(
            'azure-native:offazure/v20230606:ServerSitesController',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerSitesController':
        """
        Get an existing ServerSitesController resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerSitesControllerArgs.__new__(ServerSitesControllerArgs)

        __props__.__dict__["agent_details"] = None
        __props__.__dict__["appliance_name"] = None
        __props__.__dict__["discovery_solution_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["master_site_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_endpoint"] = None
        __props__.__dict__["service_principal_identity_details"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ServerSitesController(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentDetails")
    def agent_details(self) -> pulumi.Output[Optional['outputs.SiteAgentPropertiesResponse']]:
        """
        Gets or sets the on-premises agent details.
        """
        return pulumi.get(self, "agent_details")

    @property
    @pulumi.getter(name="applianceName")
    def appliance_name(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the Appliance Name.
        """
        return pulumi.get(self, "appliance_name")

    @property
    @pulumi.getter(name="discoverySolutionId")
    def discovery_solution_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the ARM ID of migration hub solution for SDS.
        """
        return pulumi.get(self, "discovery_solution_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="masterSiteId")
    def master_site_id(self) -> pulumi.Output[str]:
        """
        Gets the Master Site this site is linked to.
        """
        return pulumi.get(self, "master_site_id")

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
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> pulumi.Output[str]:
        """
        Gets the service endpoint.
        """
        return pulumi.get(self, "service_endpoint")

    @property
    @pulumi.getter(name="servicePrincipalIdentityDetails")
    def service_principal_identity_details(self) -> pulumi.Output[Optional['outputs.SiteSpnPropertiesResponse']]:
        """
        Gets or sets the service principal identity details used by agent for
        communication
                    to the service.
        """
        return pulumi.get(self, "service_principal_identity_details")

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

