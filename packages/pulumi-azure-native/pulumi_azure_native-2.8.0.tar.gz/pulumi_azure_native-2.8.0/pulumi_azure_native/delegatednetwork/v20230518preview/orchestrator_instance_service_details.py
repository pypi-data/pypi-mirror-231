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

__all__ = ['OrchestratorInstanceServiceDetailsArgs', 'OrchestratorInstanceServiceDetails']

@pulumi.input_type
class OrchestratorInstanceServiceDetailsArgs:
    def __init__(__self__, *,
                 controller_details: pulumi.Input['ControllerDetailsArgs'],
                 kind: pulumi.Input[Union[str, 'OrchestratorKind']],
                 resource_group_name: pulumi.Input[str],
                 api_server_endpoint: Optional[pulumi.Input[str]] = None,
                 cluster_root_ca: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['OrchestratorIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 orchestrator_app_id: Optional[pulumi.Input[str]] = None,
                 orchestrator_tenant_id: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a OrchestratorInstanceServiceDetails resource.
        :param pulumi.Input['ControllerDetailsArgs'] controller_details: Properties of the controller.
        :param pulumi.Input[Union[str, 'OrchestratorKind']] kind: The kind of workbook. Choices are user and shared.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] api_server_endpoint: K8s APIServer url. Either one of apiServerEndpoint or privateLinkResourceId can be specified
        :param pulumi.Input[str] cluster_root_ca: RootCA certificate of kubernetes cluster base64 encoded
        :param pulumi.Input['OrchestratorIdentityArgs'] identity: The identity of the orchestrator
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[str] orchestrator_app_id: AAD ID used with apiserver
        :param pulumi.Input[str] orchestrator_tenant_id: TenantID of server App ID
        :param pulumi.Input[str] private_link_resource_id: private link arm resource id. Either one of apiServerEndpoint or privateLinkResourceId can be specified
        :param pulumi.Input[str] resource_name: The name of the resource. It must be a minimum of 3 characters, and a maximum of 63.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "controller_details", controller_details)
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if api_server_endpoint is not None:
            pulumi.set(__self__, "api_server_endpoint", api_server_endpoint)
        if cluster_root_ca is not None:
            pulumi.set(__self__, "cluster_root_ca", cluster_root_ca)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if orchestrator_app_id is not None:
            pulumi.set(__self__, "orchestrator_app_id", orchestrator_app_id)
        if orchestrator_tenant_id is not None:
            pulumi.set(__self__, "orchestrator_tenant_id", orchestrator_tenant_id)
        if private_link_resource_id is not None:
            pulumi.set(__self__, "private_link_resource_id", private_link_resource_id)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="controllerDetails")
    def controller_details(self) -> pulumi.Input['ControllerDetailsArgs']:
        """
        Properties of the controller.
        """
        return pulumi.get(self, "controller_details")

    @controller_details.setter
    def controller_details(self, value: pulumi.Input['ControllerDetailsArgs']):
        pulumi.set(self, "controller_details", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[Union[str, 'OrchestratorKind']]:
        """
        The kind of workbook. Choices are user and shared.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[Union[str, 'OrchestratorKind']]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="apiServerEndpoint")
    def api_server_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        K8s APIServer url. Either one of apiServerEndpoint or privateLinkResourceId can be specified
        """
        return pulumi.get(self, "api_server_endpoint")

    @api_server_endpoint.setter
    def api_server_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_server_endpoint", value)

    @property
    @pulumi.getter(name="clusterRootCA")
    def cluster_root_ca(self) -> Optional[pulumi.Input[str]]:
        """
        RootCA certificate of kubernetes cluster base64 encoded
        """
        return pulumi.get(self, "cluster_root_ca")

    @cluster_root_ca.setter
    def cluster_root_ca(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_root_ca", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['OrchestratorIdentityArgs']]:
        """
        The identity of the orchestrator
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['OrchestratorIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="orchestratorAppId")
    def orchestrator_app_id(self) -> Optional[pulumi.Input[str]]:
        """
        AAD ID used with apiserver
        """
        return pulumi.get(self, "orchestrator_app_id")

    @orchestrator_app_id.setter
    def orchestrator_app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "orchestrator_app_id", value)

    @property
    @pulumi.getter(name="orchestratorTenantId")
    def orchestrator_tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        TenantID of server App ID
        """
        return pulumi.get(self, "orchestrator_tenant_id")

    @orchestrator_tenant_id.setter
    def orchestrator_tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "orchestrator_tenant_id", value)

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        private link arm resource id. Either one of apiServerEndpoint or privateLinkResourceId can be specified
        """
        return pulumi.get(self, "private_link_resource_id")

    @private_link_resource_id.setter
    def private_link_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_resource_id", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource. It must be a minimum of 3 characters, and a maximum of 63.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

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


class OrchestratorInstanceServiceDetails(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_server_endpoint: Optional[pulumi.Input[str]] = None,
                 cluster_root_ca: Optional[pulumi.Input[str]] = None,
                 controller_details: Optional[pulumi.Input[pulumi.InputType['ControllerDetailsArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['OrchestratorIdentityArgs']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'OrchestratorKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 orchestrator_app_id: Optional[pulumi.Input[str]] = None,
                 orchestrator_tenant_id: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents an instance of a orchestrator.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_server_endpoint: K8s APIServer url. Either one of apiServerEndpoint or privateLinkResourceId can be specified
        :param pulumi.Input[str] cluster_root_ca: RootCA certificate of kubernetes cluster base64 encoded
        :param pulumi.Input[pulumi.InputType['ControllerDetailsArgs']] controller_details: Properties of the controller.
        :param pulumi.Input[pulumi.InputType['OrchestratorIdentityArgs']] identity: The identity of the orchestrator
        :param pulumi.Input[Union[str, 'OrchestratorKind']] kind: The kind of workbook. Choices are user and shared.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[str] orchestrator_app_id: AAD ID used with apiserver
        :param pulumi.Input[str] orchestrator_tenant_id: TenantID of server App ID
        :param pulumi.Input[str] private_link_resource_id: private link arm resource id. Either one of apiServerEndpoint or privateLinkResourceId can be specified
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the resource. It must be a minimum of 3 characters, and a maximum of 63.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrchestratorInstanceServiceDetailsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents an instance of a orchestrator.

        :param str resource_name: The name of the resource.
        :param OrchestratorInstanceServiceDetailsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrchestratorInstanceServiceDetailsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_server_endpoint: Optional[pulumi.Input[str]] = None,
                 cluster_root_ca: Optional[pulumi.Input[str]] = None,
                 controller_details: Optional[pulumi.Input[pulumi.InputType['ControllerDetailsArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['OrchestratorIdentityArgs']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'OrchestratorKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 orchestrator_app_id: Optional[pulumi.Input[str]] = None,
                 orchestrator_tenant_id: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrchestratorInstanceServiceDetailsArgs.__new__(OrchestratorInstanceServiceDetailsArgs)

            __props__.__dict__["api_server_endpoint"] = api_server_endpoint
            __props__.__dict__["cluster_root_ca"] = cluster_root_ca
            if controller_details is None and not opts.urn:
                raise TypeError("Missing required property 'controller_details'")
            __props__.__dict__["controller_details"] = controller_details
            __props__.__dict__["identity"] = identity
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["orchestrator_app_id"] = orchestrator_app_id
            __props__.__dict__["orchestrator_tenant_id"] = orchestrator_tenant_id
            __props__.__dict__["private_link_resource_id"] = private_link_resource_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_guid"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:delegatednetwork:OrchestratorInstanceServiceDetails"), pulumi.Alias(type_="azure-native:delegatednetwork/v20200808preview:OrchestratorInstanceServiceDetails"), pulumi.Alias(type_="azure-native:delegatednetwork/v20210315:OrchestratorInstanceServiceDetails"), pulumi.Alias(type_="azure-native:delegatednetwork/v20230627preview:OrchestratorInstanceServiceDetails")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OrchestratorInstanceServiceDetails, __self__).__init__(
            'azure-native:delegatednetwork/v20230518preview:OrchestratorInstanceServiceDetails',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrchestratorInstanceServiceDetails':
        """
        Get an existing OrchestratorInstanceServiceDetails resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrchestratorInstanceServiceDetailsArgs.__new__(OrchestratorInstanceServiceDetailsArgs)

        __props__.__dict__["api_server_endpoint"] = None
        __props__.__dict__["cluster_root_ca"] = None
        __props__.__dict__["controller_details"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["orchestrator_app_id"] = None
        __props__.__dict__["orchestrator_tenant_id"] = None
        __props__.__dict__["private_link_resource_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return OrchestratorInstanceServiceDetails(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiServerEndpoint")
    def api_server_endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        K8s APIServer url. Either one of apiServerEndpoint or privateLinkResourceId can be specified
        """
        return pulumi.get(self, "api_server_endpoint")

    @property
    @pulumi.getter(name="clusterRootCA")
    def cluster_root_ca(self) -> pulumi.Output[Optional[str]]:
        """
        RootCA certificate of kubernetes cluster base64 encoded
        """
        return pulumi.get(self, "cluster_root_ca")

    @property
    @pulumi.getter(name="controllerDetails")
    def controller_details(self) -> pulumi.Output['outputs.ControllerDetailsResponse']:
        """
        Properties of the controller.
        """
        return pulumi.get(self, "controller_details")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.OrchestratorIdentityResponse']]:
        """
        The identity of the orchestrator
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of workbook. Choices are user and shared.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Location of the resource.
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
    @pulumi.getter(name="orchestratorAppId")
    def orchestrator_app_id(self) -> pulumi.Output[Optional[str]]:
        """
        AAD ID used with apiserver
        """
        return pulumi.get(self, "orchestrator_app_id")

    @property
    @pulumi.getter(name="orchestratorTenantId")
    def orchestrator_tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        TenantID of server App ID
        """
        return pulumi.get(self, "orchestrator_tenant_id")

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        private link arm resource id. Either one of apiServerEndpoint or privateLinkResourceId can be specified
        """
        return pulumi.get(self, "private_link_resource_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current state of orchestratorInstance resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        Resource guid.
        """
        return pulumi.get(self, "resource_guid")

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
        The type of resource.
        """
        return pulumi.get(self, "type")

