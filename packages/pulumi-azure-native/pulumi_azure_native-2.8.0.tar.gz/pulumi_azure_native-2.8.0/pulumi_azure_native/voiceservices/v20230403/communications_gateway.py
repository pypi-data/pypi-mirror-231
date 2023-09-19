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

__all__ = ['CommunicationsGatewayArgs', 'CommunicationsGateway']

@pulumi.input_type
class CommunicationsGatewayArgs:
    def __init__(__self__, *,
                 codecs: pulumi.Input[Sequence[pulumi.Input[Union[str, 'TeamsCodecs']]]],
                 connectivity: pulumi.Input[Union[str, 'Connectivity']],
                 e911_type: pulumi.Input[Union[str, 'E911Type']],
                 platforms: pulumi.Input[Sequence[pulumi.Input[Union[str, 'CommunicationsPlatform']]]],
                 resource_group_name: pulumi.Input[str],
                 service_locations: pulumi.Input[Sequence[pulumi.Input['ServiceRegionPropertiesArgs']]],
                 api_bridge: Optional[Any] = None,
                 auto_generated_domain_name_label_scope: Optional[pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']]] = None,
                 communications_gateway_name: Optional[pulumi.Input[str]] = None,
                 emergency_dial_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 integrated_mcp_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 on_prem_mcp_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 teams_voicemail_pilot_number: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CommunicationsGateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'TeamsCodecs']]]] codecs: Voice codecs to support
        :param pulumi.Input[Union[str, 'Connectivity']] connectivity: How to connect back to the operator network, e.g. MAPS
        :param pulumi.Input[Union[str, 'E911Type']] e911_type: How to handle 911 calls
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'CommunicationsPlatform']]]] platforms: What platforms to support
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['ServiceRegionPropertiesArgs']]] service_locations: The regions in which to deploy the resources needed for Teams Calling
        :param Any api_bridge: Details of API bridge functionality, if required
        :param pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']] auto_generated_domain_name_label_scope: The scope at which the auto-generated domain name can be re-used
        :param pulumi.Input[str] communications_gateway_name: Unique identifier for this deployment
        :param pulumi.Input[Sequence[pulumi.Input[str]]] emergency_dial_strings: A list of dial strings used for emergency calling.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[bool] integrated_mcp_enabled: Whether an integrated Mobile Control Point is in use.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[bool] on_prem_mcp_enabled: Whether an on-premises Mobile Control Point is in use.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] teams_voicemail_pilot_number: This number is used in Teams Phone Mobile scenarios for access to the voicemail IVR from the native dialer.
        """
        pulumi.set(__self__, "codecs", codecs)
        pulumi.set(__self__, "connectivity", connectivity)
        pulumi.set(__self__, "e911_type", e911_type)
        pulumi.set(__self__, "platforms", platforms)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_locations", service_locations)
        if api_bridge is not None:
            pulumi.set(__self__, "api_bridge", api_bridge)
        if auto_generated_domain_name_label_scope is None:
            auto_generated_domain_name_label_scope = 'TenantReuse'
        if auto_generated_domain_name_label_scope is not None:
            pulumi.set(__self__, "auto_generated_domain_name_label_scope", auto_generated_domain_name_label_scope)
        if communications_gateway_name is not None:
            pulumi.set(__self__, "communications_gateway_name", communications_gateway_name)
        if emergency_dial_strings is not None:
            pulumi.set(__self__, "emergency_dial_strings", emergency_dial_strings)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if integrated_mcp_enabled is None:
            integrated_mcp_enabled = False
        if integrated_mcp_enabled is not None:
            pulumi.set(__self__, "integrated_mcp_enabled", integrated_mcp_enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if on_prem_mcp_enabled is None:
            on_prem_mcp_enabled = False
        if on_prem_mcp_enabled is not None:
            pulumi.set(__self__, "on_prem_mcp_enabled", on_prem_mcp_enabled)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if teams_voicemail_pilot_number is not None:
            pulumi.set(__self__, "teams_voicemail_pilot_number", teams_voicemail_pilot_number)

    @property
    @pulumi.getter
    def codecs(self) -> pulumi.Input[Sequence[pulumi.Input[Union[str, 'TeamsCodecs']]]]:
        """
        Voice codecs to support
        """
        return pulumi.get(self, "codecs")

    @codecs.setter
    def codecs(self, value: pulumi.Input[Sequence[pulumi.Input[Union[str, 'TeamsCodecs']]]]):
        pulumi.set(self, "codecs", value)

    @property
    @pulumi.getter
    def connectivity(self) -> pulumi.Input[Union[str, 'Connectivity']]:
        """
        How to connect back to the operator network, e.g. MAPS
        """
        return pulumi.get(self, "connectivity")

    @connectivity.setter
    def connectivity(self, value: pulumi.Input[Union[str, 'Connectivity']]):
        pulumi.set(self, "connectivity", value)

    @property
    @pulumi.getter(name="e911Type")
    def e911_type(self) -> pulumi.Input[Union[str, 'E911Type']]:
        """
        How to handle 911 calls
        """
        return pulumi.get(self, "e911_type")

    @e911_type.setter
    def e911_type(self, value: pulumi.Input[Union[str, 'E911Type']]):
        pulumi.set(self, "e911_type", value)

    @property
    @pulumi.getter
    def platforms(self) -> pulumi.Input[Sequence[pulumi.Input[Union[str, 'CommunicationsPlatform']]]]:
        """
        What platforms to support
        """
        return pulumi.get(self, "platforms")

    @platforms.setter
    def platforms(self, value: pulumi.Input[Sequence[pulumi.Input[Union[str, 'CommunicationsPlatform']]]]):
        pulumi.set(self, "platforms", value)

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
    @pulumi.getter(name="serviceLocations")
    def service_locations(self) -> pulumi.Input[Sequence[pulumi.Input['ServiceRegionPropertiesArgs']]]:
        """
        The regions in which to deploy the resources needed for Teams Calling
        """
        return pulumi.get(self, "service_locations")

    @service_locations.setter
    def service_locations(self, value: pulumi.Input[Sequence[pulumi.Input['ServiceRegionPropertiesArgs']]]):
        pulumi.set(self, "service_locations", value)

    @property
    @pulumi.getter(name="apiBridge")
    def api_bridge(self) -> Optional[Any]:
        """
        Details of API bridge functionality, if required
        """
        return pulumi.get(self, "api_bridge")

    @api_bridge.setter
    def api_bridge(self, value: Optional[Any]):
        pulumi.set(self, "api_bridge", value)

    @property
    @pulumi.getter(name="autoGeneratedDomainNameLabelScope")
    def auto_generated_domain_name_label_scope(self) -> Optional[pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']]]:
        """
        The scope at which the auto-generated domain name can be re-used
        """
        return pulumi.get(self, "auto_generated_domain_name_label_scope")

    @auto_generated_domain_name_label_scope.setter
    def auto_generated_domain_name_label_scope(self, value: Optional[pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']]]):
        pulumi.set(self, "auto_generated_domain_name_label_scope", value)

    @property
    @pulumi.getter(name="communicationsGatewayName")
    def communications_gateway_name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier for this deployment
        """
        return pulumi.get(self, "communications_gateway_name")

    @communications_gateway_name.setter
    def communications_gateway_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "communications_gateway_name", value)

    @property
    @pulumi.getter(name="emergencyDialStrings")
    def emergency_dial_strings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of dial strings used for emergency calling.
        """
        return pulumi.get(self, "emergency_dial_strings")

    @emergency_dial_strings.setter
    def emergency_dial_strings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "emergency_dial_strings", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="integratedMcpEnabled")
    def integrated_mcp_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an integrated Mobile Control Point is in use.
        """
        return pulumi.get(self, "integrated_mcp_enabled")

    @integrated_mcp_enabled.setter
    def integrated_mcp_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "integrated_mcp_enabled", value)

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
    @pulumi.getter(name="onPremMcpEnabled")
    def on_prem_mcp_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether an on-premises Mobile Control Point is in use.
        """
        return pulumi.get(self, "on_prem_mcp_enabled")

    @on_prem_mcp_enabled.setter
    def on_prem_mcp_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_prem_mcp_enabled", value)

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

    @property
    @pulumi.getter(name="teamsVoicemailPilotNumber")
    def teams_voicemail_pilot_number(self) -> Optional[pulumi.Input[str]]:
        """
        This number is used in Teams Phone Mobile scenarios for access to the voicemail IVR from the native dialer.
        """
        return pulumi.get(self, "teams_voicemail_pilot_number")

    @teams_voicemail_pilot_number.setter
    def teams_voicemail_pilot_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "teams_voicemail_pilot_number", value)


class CommunicationsGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_bridge: Optional[Any] = None,
                 auto_generated_domain_name_label_scope: Optional[pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']]] = None,
                 codecs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'TeamsCodecs']]]]] = None,
                 communications_gateway_name: Optional[pulumi.Input[str]] = None,
                 connectivity: Optional[pulumi.Input[Union[str, 'Connectivity']]] = None,
                 e911_type: Optional[pulumi.Input[Union[str, 'E911Type']]] = None,
                 emergency_dial_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 integrated_mcp_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 on_prem_mcp_enabled: Optional[pulumi.Input[bool]] = None,
                 platforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'CommunicationsPlatform']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_locations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceRegionPropertiesArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 teams_voicemail_pilot_number: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A CommunicationsGateway resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any api_bridge: Details of API bridge functionality, if required
        :param pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']] auto_generated_domain_name_label_scope: The scope at which the auto-generated domain name can be re-used
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'TeamsCodecs']]]] codecs: Voice codecs to support
        :param pulumi.Input[str] communications_gateway_name: Unique identifier for this deployment
        :param pulumi.Input[Union[str, 'Connectivity']] connectivity: How to connect back to the operator network, e.g. MAPS
        :param pulumi.Input[Union[str, 'E911Type']] e911_type: How to handle 911 calls
        :param pulumi.Input[Sequence[pulumi.Input[str]]] emergency_dial_strings: A list of dial strings used for emergency calling.
        :param pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[bool] integrated_mcp_enabled: Whether an integrated Mobile Control Point is in use.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[bool] on_prem_mcp_enabled: Whether an on-premises Mobile Control Point is in use.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'CommunicationsPlatform']]]] platforms: What platforms to support
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceRegionPropertiesArgs']]]] service_locations: The regions in which to deploy the resources needed for Teams Calling
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] teams_voicemail_pilot_number: This number is used in Teams Phone Mobile scenarios for access to the voicemail IVR from the native dialer.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CommunicationsGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A CommunicationsGateway resource

        :param str resource_name: The name of the resource.
        :param CommunicationsGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CommunicationsGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_bridge: Optional[Any] = None,
                 auto_generated_domain_name_label_scope: Optional[pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']]] = None,
                 codecs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'TeamsCodecs']]]]] = None,
                 communications_gateway_name: Optional[pulumi.Input[str]] = None,
                 connectivity: Optional[pulumi.Input[Union[str, 'Connectivity']]] = None,
                 e911_type: Optional[pulumi.Input[Union[str, 'E911Type']]] = None,
                 emergency_dial_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 integrated_mcp_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 on_prem_mcp_enabled: Optional[pulumi.Input[bool]] = None,
                 platforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'CommunicationsPlatform']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_locations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceRegionPropertiesArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 teams_voicemail_pilot_number: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CommunicationsGatewayArgs.__new__(CommunicationsGatewayArgs)

            __props__.__dict__["api_bridge"] = api_bridge
            if auto_generated_domain_name_label_scope is None:
                auto_generated_domain_name_label_scope = 'TenantReuse'
            __props__.__dict__["auto_generated_domain_name_label_scope"] = auto_generated_domain_name_label_scope
            if codecs is None and not opts.urn:
                raise TypeError("Missing required property 'codecs'")
            __props__.__dict__["codecs"] = codecs
            __props__.__dict__["communications_gateway_name"] = communications_gateway_name
            if connectivity is None and not opts.urn:
                raise TypeError("Missing required property 'connectivity'")
            __props__.__dict__["connectivity"] = connectivity
            if e911_type is None and not opts.urn:
                raise TypeError("Missing required property 'e911_type'")
            __props__.__dict__["e911_type"] = e911_type
            __props__.__dict__["emergency_dial_strings"] = emergency_dial_strings
            __props__.__dict__["identity"] = identity
            if integrated_mcp_enabled is None:
                integrated_mcp_enabled = False
            __props__.__dict__["integrated_mcp_enabled"] = integrated_mcp_enabled
            __props__.__dict__["location"] = location
            if on_prem_mcp_enabled is None:
                on_prem_mcp_enabled = False
            __props__.__dict__["on_prem_mcp_enabled"] = on_prem_mcp_enabled
            if platforms is None and not opts.urn:
                raise TypeError("Missing required property 'platforms'")
            __props__.__dict__["platforms"] = platforms
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_locations is None and not opts.urn:
                raise TypeError("Missing required property 'service_locations'")
            __props__.__dict__["service_locations"] = service_locations
            __props__.__dict__["tags"] = tags
            __props__.__dict__["teams_voicemail_pilot_number"] = teams_voicemail_pilot_number
            __props__.__dict__["auto_generated_domain_name_label"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:voiceservices:CommunicationsGateway"), pulumi.Alias(type_="azure-native:voiceservices/v20221201preview:CommunicationsGateway"), pulumi.Alias(type_="azure-native:voiceservices/v20230131:CommunicationsGateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CommunicationsGateway, __self__).__init__(
            'azure-native:voiceservices/v20230403:CommunicationsGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CommunicationsGateway':
        """
        Get an existing CommunicationsGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CommunicationsGatewayArgs.__new__(CommunicationsGatewayArgs)

        __props__.__dict__["api_bridge"] = None
        __props__.__dict__["auto_generated_domain_name_label"] = None
        __props__.__dict__["auto_generated_domain_name_label_scope"] = None
        __props__.__dict__["codecs"] = None
        __props__.__dict__["connectivity"] = None
        __props__.__dict__["e911_type"] = None
        __props__.__dict__["emergency_dial_strings"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["integrated_mcp_enabled"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["on_prem_mcp_enabled"] = None
        __props__.__dict__["platforms"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_locations"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["teams_voicemail_pilot_number"] = None
        __props__.__dict__["type"] = None
        return CommunicationsGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiBridge")
    def api_bridge(self) -> pulumi.Output[Optional[Any]]:
        """
        Details of API bridge functionality, if required
        """
        return pulumi.get(self, "api_bridge")

    @property
    @pulumi.getter(name="autoGeneratedDomainNameLabel")
    def auto_generated_domain_name_label(self) -> pulumi.Output[str]:
        """
        The autogenerated label used as part of the FQDNs for accessing the Communications Gateway
        """
        return pulumi.get(self, "auto_generated_domain_name_label")

    @property
    @pulumi.getter(name="autoGeneratedDomainNameLabelScope")
    def auto_generated_domain_name_label_scope(self) -> pulumi.Output[Optional[str]]:
        """
        The scope at which the auto-generated domain name can be re-used
        """
        return pulumi.get(self, "auto_generated_domain_name_label_scope")

    @property
    @pulumi.getter
    def codecs(self) -> pulumi.Output[Sequence[str]]:
        """
        Voice codecs to support
        """
        return pulumi.get(self, "codecs")

    @property
    @pulumi.getter
    def connectivity(self) -> pulumi.Output[str]:
        """
        How to connect back to the operator network, e.g. MAPS
        """
        return pulumi.get(self, "connectivity")

    @property
    @pulumi.getter(name="e911Type")
    def e911_type(self) -> pulumi.Output[str]:
        """
        How to handle 911 calls
        """
        return pulumi.get(self, "e911_type")

    @property
    @pulumi.getter(name="emergencyDialStrings")
    def emergency_dial_strings(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of dial strings used for emergency calling.
        """
        return pulumi.get(self, "emergency_dial_strings")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="integratedMcpEnabled")
    def integrated_mcp_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether an integrated Mobile Control Point is in use.
        """
        return pulumi.get(self, "integrated_mcp_enabled")

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
    @pulumi.getter(name="onPremMcpEnabled")
    def on_prem_mcp_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether an on-premises Mobile Control Point is in use.
        """
        return pulumi.get(self, "on_prem_mcp_enabled")

    @property
    @pulumi.getter
    def platforms(self) -> pulumi.Output[Sequence[str]]:
        """
        What platforms to support
        """
        return pulumi.get(self, "platforms")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceLocations")
    def service_locations(self) -> pulumi.Output[Sequence['outputs.ServiceRegionPropertiesResponse']]:
        """
        The regions in which to deploy the resources needed for Teams Calling
        """
        return pulumi.get(self, "service_locations")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The current status of the deployment.
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
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="teamsVoicemailPilotNumber")
    def teams_voicemail_pilot_number(self) -> pulumi.Output[Optional[str]]:
        """
        This number is used in Teams Phone Mobile scenarios for access to the voicemail IVR from the native dialer.
        """
        return pulumi.get(self, "teams_voicemail_pilot_number")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

