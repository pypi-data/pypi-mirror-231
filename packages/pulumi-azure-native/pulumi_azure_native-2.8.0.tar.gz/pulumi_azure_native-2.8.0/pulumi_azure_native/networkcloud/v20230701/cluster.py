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

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 aggregator_or_single_rack_definition: pulumi.Input['RackDefinitionArgs'],
                 cluster_type: pulumi.Input[Union[str, 'ClusterType']],
                 cluster_version: pulumi.Input[str],
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 network_fabric_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 cluster_location: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_service_principal: Optional[pulumi.Input['ServicePrincipalInformationArgs']] = None,
                 compute_deployment_threshold: Optional[pulumi.Input['ValidationThresholdArgs']] = None,
                 compute_rack_definitions: Optional[pulumi.Input[Sequence[pulumi.Input['RackDefinitionArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input['ManagedResourceGroupConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input['RackDefinitionArgs'] aggregator_or_single_rack_definition: The rack definition that is intended to reflect only a single rack in a single rack cluster, or an aggregator rack in a multi-rack cluster.
        :param pulumi.Input[Union[str, 'ClusterType']] cluster_type: The type of rack configuration for the cluster.
        :param pulumi.Input[str] cluster_version: The current runtime version of the cluster.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location of the cluster manager associated with the cluster.
        :param pulumi.Input[str] network_fabric_id: The resource ID of the Network Fabric associated with the cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] analytics_workspace_id: The resource ID of the Log Analytics Workspace that will be used for storing relevant logs.
        :param pulumi.Input[str] cluster_location: The customer-provided location information to identify where the cluster resides.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input['ServicePrincipalInformationArgs'] cluster_service_principal: The service principal to be used by the cluster during Arc Appliance installation.
        :param pulumi.Input['ValidationThresholdArgs'] compute_deployment_threshold: The validation threshold indicating the allowable failures of compute machines during environment validation and deployment.
        :param pulumi.Input[Sequence[pulumi.Input['RackDefinitionArgs']]] compute_rack_definitions: The list of rack definitions for the compute racks in a multi-rack
               cluster, or an empty list in a single-rack cluster.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['ManagedResourceGroupConfigurationArgs'] managed_resource_group_configuration: The configuration of the managed resource group associated with the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "aggregator_or_single_rack_definition", aggregator_or_single_rack_definition)
        pulumi.set(__self__, "cluster_type", cluster_type)
        pulumi.set(__self__, "cluster_version", cluster_version)
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "network_fabric_id", network_fabric_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if analytics_workspace_id is not None:
            pulumi.set(__self__, "analytics_workspace_id", analytics_workspace_id)
        if cluster_location is not None:
            pulumi.set(__self__, "cluster_location", cluster_location)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if cluster_service_principal is not None:
            pulumi.set(__self__, "cluster_service_principal", cluster_service_principal)
        if compute_deployment_threshold is not None:
            pulumi.set(__self__, "compute_deployment_threshold", compute_deployment_threshold)
        if compute_rack_definitions is not None:
            pulumi.set(__self__, "compute_rack_definitions", compute_rack_definitions)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_resource_group_configuration is not None:
            pulumi.set(__self__, "managed_resource_group_configuration", managed_resource_group_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="aggregatorOrSingleRackDefinition")
    def aggregator_or_single_rack_definition(self) -> pulumi.Input['RackDefinitionArgs']:
        """
        The rack definition that is intended to reflect only a single rack in a single rack cluster, or an aggregator rack in a multi-rack cluster.
        """
        return pulumi.get(self, "aggregator_or_single_rack_definition")

    @aggregator_or_single_rack_definition.setter
    def aggregator_or_single_rack_definition(self, value: pulumi.Input['RackDefinitionArgs']):
        pulumi.set(self, "aggregator_or_single_rack_definition", value)

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Input[Union[str, 'ClusterType']]:
        """
        The type of rack configuration for the cluster.
        """
        return pulumi.get(self, "cluster_type")

    @cluster_type.setter
    def cluster_type(self, value: pulumi.Input[Union[str, 'ClusterType']]):
        pulumi.set(self, "cluster_type", value)

    @property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> pulumi.Input[str]:
        """
        The current runtime version of the cluster.
        """
        return pulumi.get(self, "cluster_version")

    @cluster_version.setter
    def cluster_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_version", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        The extended location of the cluster manager associated with the cluster.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Network Fabric associated with the cluster.
        """
        return pulumi.get(self, "network_fabric_id")

    @network_fabric_id.setter
    def network_fabric_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_fabric_id", value)

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
    @pulumi.getter(name="analyticsWorkspaceId")
    def analytics_workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Log Analytics Workspace that will be used for storing relevant logs.
        """
        return pulumi.get(self, "analytics_workspace_id")

    @analytics_workspace_id.setter
    def analytics_workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "analytics_workspace_id", value)

    @property
    @pulumi.getter(name="clusterLocation")
    def cluster_location(self) -> Optional[pulumi.Input[str]]:
        """
        The customer-provided location information to identify where the cluster resides.
        """
        return pulumi.get(self, "cluster_location")

    @cluster_location.setter
    def cluster_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_location", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="clusterServicePrincipal")
    def cluster_service_principal(self) -> Optional[pulumi.Input['ServicePrincipalInformationArgs']]:
        """
        The service principal to be used by the cluster during Arc Appliance installation.
        """
        return pulumi.get(self, "cluster_service_principal")

    @cluster_service_principal.setter
    def cluster_service_principal(self, value: Optional[pulumi.Input['ServicePrincipalInformationArgs']]):
        pulumi.set(self, "cluster_service_principal", value)

    @property
    @pulumi.getter(name="computeDeploymentThreshold")
    def compute_deployment_threshold(self) -> Optional[pulumi.Input['ValidationThresholdArgs']]:
        """
        The validation threshold indicating the allowable failures of compute machines during environment validation and deployment.
        """
        return pulumi.get(self, "compute_deployment_threshold")

    @compute_deployment_threshold.setter
    def compute_deployment_threshold(self, value: Optional[pulumi.Input['ValidationThresholdArgs']]):
        pulumi.set(self, "compute_deployment_threshold", value)

    @property
    @pulumi.getter(name="computeRackDefinitions")
    def compute_rack_definitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RackDefinitionArgs']]]]:
        """
        The list of rack definitions for the compute racks in a multi-rack
        cluster, or an empty list in a single-rack cluster.
        """
        return pulumi.get(self, "compute_rack_definitions")

    @compute_rack_definitions.setter
    def compute_rack_definitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RackDefinitionArgs']]]]):
        pulumi.set(self, "compute_rack_definitions", value)

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
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> Optional[pulumi.Input['ManagedResourceGroupConfigurationArgs']]:
        """
        The configuration of the managed resource group associated with the resource.
        """
        return pulumi.get(self, "managed_resource_group_configuration")

    @managed_resource_group_configuration.setter
    def managed_resource_group_configuration(self, value: Optional[pulumi.Input['ManagedResourceGroupConfigurationArgs']]):
        pulumi.set(self, "managed_resource_group_configuration", value)

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


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aggregator_or_single_rack_definition: Optional[pulumi.Input[pulumi.InputType['RackDefinitionArgs']]] = None,
                 analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 cluster_location: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_service_principal: Optional[pulumi.Input[pulumi.InputType['ServicePrincipalInformationArgs']]] = None,
                 cluster_type: Optional[pulumi.Input[Union[str, 'ClusterType']]] = None,
                 cluster_version: Optional[pulumi.Input[str]] = None,
                 compute_deployment_threshold: Optional[pulumi.Input[pulumi.InputType['ValidationThresholdArgs']]] = None,
                 compute_rack_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RackDefinitionArgs']]]]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input[pulumi.InputType['ManagedResourceGroupConfigurationArgs']]] = None,
                 network_fabric_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RackDefinitionArgs']] aggregator_or_single_rack_definition: The rack definition that is intended to reflect only a single rack in a single rack cluster, or an aggregator rack in a multi-rack cluster.
        :param pulumi.Input[str] analytics_workspace_id: The resource ID of the Log Analytics Workspace that will be used for storing relevant logs.
        :param pulumi.Input[str] cluster_location: The customer-provided location information to identify where the cluster resides.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[pulumi.InputType['ServicePrincipalInformationArgs']] cluster_service_principal: The service principal to be used by the cluster during Arc Appliance installation.
        :param pulumi.Input[Union[str, 'ClusterType']] cluster_type: The type of rack configuration for the cluster.
        :param pulumi.Input[str] cluster_version: The current runtime version of the cluster.
        :param pulumi.Input[pulumi.InputType['ValidationThresholdArgs']] compute_deployment_threshold: The validation threshold indicating the allowable failures of compute machines during environment validation and deployment.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RackDefinitionArgs']]]] compute_rack_definitions: The list of rack definitions for the compute racks in a multi-rack
               cluster, or an empty list in a single-rack cluster.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location of the cluster manager associated with the cluster.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['ManagedResourceGroupConfigurationArgs']] managed_resource_group_configuration: The configuration of the managed resource group associated with the resource.
        :param pulumi.Input[str] network_fabric_id: The resource ID of the Network Fabric associated with the cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aggregator_or_single_rack_definition: Optional[pulumi.Input[pulumi.InputType['RackDefinitionArgs']]] = None,
                 analytics_workspace_id: Optional[pulumi.Input[str]] = None,
                 cluster_location: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_service_principal: Optional[pulumi.Input[pulumi.InputType['ServicePrincipalInformationArgs']]] = None,
                 cluster_type: Optional[pulumi.Input[Union[str, 'ClusterType']]] = None,
                 cluster_version: Optional[pulumi.Input[str]] = None,
                 compute_deployment_threshold: Optional[pulumi.Input[pulumi.InputType['ValidationThresholdArgs']]] = None,
                 compute_rack_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RackDefinitionArgs']]]]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input[pulumi.InputType['ManagedResourceGroupConfigurationArgs']]] = None,
                 network_fabric_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            if aggregator_or_single_rack_definition is None and not opts.urn:
                raise TypeError("Missing required property 'aggregator_or_single_rack_definition'")
            __props__.__dict__["aggregator_or_single_rack_definition"] = aggregator_or_single_rack_definition
            __props__.__dict__["analytics_workspace_id"] = analytics_workspace_id
            __props__.__dict__["cluster_location"] = cluster_location
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["cluster_service_principal"] = cluster_service_principal
            if cluster_type is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_type'")
            __props__.__dict__["cluster_type"] = cluster_type
            if cluster_version is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_version'")
            __props__.__dict__["cluster_version"] = cluster_version
            __props__.__dict__["compute_deployment_threshold"] = compute_deployment_threshold
            __props__.__dict__["compute_rack_definitions"] = compute_rack_definitions
            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            __props__.__dict__["managed_resource_group_configuration"] = managed_resource_group_configuration
            if network_fabric_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_fabric_id'")
            __props__.__dict__["network_fabric_id"] = network_fabric_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["available_upgrade_versions"] = None
            __props__.__dict__["cluster_capacity"] = None
            __props__.__dict__["cluster_connection_status"] = None
            __props__.__dict__["cluster_extended_location"] = None
            __props__.__dict__["cluster_manager_connection_status"] = None
            __props__.__dict__["cluster_manager_id"] = None
            __props__.__dict__["detailed_status"] = None
            __props__.__dict__["detailed_status_message"] = None
            __props__.__dict__["hybrid_aks_extended_location"] = None
            __props__.__dict__["manual_action_count"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["support_expiry_date"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["workload_resource_ids"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkcloud:Cluster"), pulumi.Alias(type_="azure-native:networkcloud/v20221212preview:Cluster"), pulumi.Alias(type_="azure-native:networkcloud/v20230501preview:Cluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Cluster, __self__).__init__(
            'azure-native:networkcloud/v20230701:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["aggregator_or_single_rack_definition"] = None
        __props__.__dict__["analytics_workspace_id"] = None
        __props__.__dict__["available_upgrade_versions"] = None
        __props__.__dict__["cluster_capacity"] = None
        __props__.__dict__["cluster_connection_status"] = None
        __props__.__dict__["cluster_extended_location"] = None
        __props__.__dict__["cluster_location"] = None
        __props__.__dict__["cluster_manager_connection_status"] = None
        __props__.__dict__["cluster_manager_id"] = None
        __props__.__dict__["cluster_service_principal"] = None
        __props__.__dict__["cluster_type"] = None
        __props__.__dict__["cluster_version"] = None
        __props__.__dict__["compute_deployment_threshold"] = None
        __props__.__dict__["compute_rack_definitions"] = None
        __props__.__dict__["detailed_status"] = None
        __props__.__dict__["detailed_status_message"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["hybrid_aks_extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_resource_group_configuration"] = None
        __props__.__dict__["manual_action_count"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_fabric_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["support_expiry_date"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["workload_resource_ids"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aggregatorOrSingleRackDefinition")
    def aggregator_or_single_rack_definition(self) -> pulumi.Output['outputs.RackDefinitionResponse']:
        """
        The rack definition that is intended to reflect only a single rack in a single rack cluster, or an aggregator rack in a multi-rack cluster.
        """
        return pulumi.get(self, "aggregator_or_single_rack_definition")

    @property
    @pulumi.getter(name="analyticsWorkspaceId")
    def analytics_workspace_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID of the Log Analytics Workspace that will be used for storing relevant logs.
        """
        return pulumi.get(self, "analytics_workspace_id")

    @property
    @pulumi.getter(name="availableUpgradeVersions")
    def available_upgrade_versions(self) -> pulumi.Output[Sequence['outputs.ClusterAvailableUpgradeVersionResponse']]:
        """
        The list of cluster runtime version upgrades available for this cluster.
        """
        return pulumi.get(self, "available_upgrade_versions")

    @property
    @pulumi.getter(name="clusterCapacity")
    def cluster_capacity(self) -> pulumi.Output['outputs.ClusterCapacityResponse']:
        """
        The capacity supported by this cluster.
        """
        return pulumi.get(self, "cluster_capacity")

    @property
    @pulumi.getter(name="clusterConnectionStatus")
    def cluster_connection_status(self) -> pulumi.Output[str]:
        """
        The latest heartbeat status between the cluster manager and the cluster.
        """
        return pulumi.get(self, "cluster_connection_status")

    @property
    @pulumi.getter(name="clusterExtendedLocation")
    def cluster_extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location (custom location) that represents the cluster's control plane location. This extended location is used to route the requests of child objects of the cluster that are handled by the platform operator.
        """
        return pulumi.get(self, "cluster_extended_location")

    @property
    @pulumi.getter(name="clusterLocation")
    def cluster_location(self) -> pulumi.Output[Optional[str]]:
        """
        The customer-provided location information to identify where the cluster resides.
        """
        return pulumi.get(self, "cluster_location")

    @property
    @pulumi.getter(name="clusterManagerConnectionStatus")
    def cluster_manager_connection_status(self) -> pulumi.Output[str]:
        """
        The latest connectivity status between cluster manager and the cluster.
        """
        return pulumi.get(self, "cluster_manager_connection_status")

    @property
    @pulumi.getter(name="clusterManagerId")
    def cluster_manager_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the cluster manager that manages this cluster. This is set by the Cluster Manager when the cluster is created.
        """
        return pulumi.get(self, "cluster_manager_id")

    @property
    @pulumi.getter(name="clusterServicePrincipal")
    def cluster_service_principal(self) -> pulumi.Output[Optional['outputs.ServicePrincipalInformationResponse']]:
        """
        The service principal to be used by the cluster during Arc Appliance installation.
        """
        return pulumi.get(self, "cluster_service_principal")

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Output[str]:
        """
        The type of rack configuration for the cluster.
        """
        return pulumi.get(self, "cluster_type")

    @property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> pulumi.Output[str]:
        """
        The current runtime version of the cluster.
        """
        return pulumi.get(self, "cluster_version")

    @property
    @pulumi.getter(name="computeDeploymentThreshold")
    def compute_deployment_threshold(self) -> pulumi.Output[Optional['outputs.ValidationThresholdResponse']]:
        """
        The validation threshold indicating the allowable failures of compute machines during environment validation and deployment.
        """
        return pulumi.get(self, "compute_deployment_threshold")

    @property
    @pulumi.getter(name="computeRackDefinitions")
    def compute_rack_definitions(self) -> pulumi.Output[Optional[Sequence['outputs.RackDefinitionResponse']]]:
        """
        The list of rack definitions for the compute racks in a multi-rack
        cluster, or an empty list in a single-rack cluster.
        """
        return pulumi.get(self, "compute_rack_definitions")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[str]:
        """
        The current detailed status of the cluster.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[str]:
        """
        The descriptive message about the detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location of the cluster manager associated with the cluster.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hybridAksExtendedLocation")
    def hybrid_aks_extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        Field Deprecated. This field will not be populated in an upcoming version. The extended location (custom location) that represents the Hybrid AKS control plane location. This extended location is used when creating provisioned clusters (Hybrid AKS clusters).
        """
        return pulumi.get(self, "hybrid_aks_extended_location")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> pulumi.Output[Optional['outputs.ManagedResourceGroupConfigurationResponse']]:
        """
        The configuration of the managed resource group associated with the resource.
        """
        return pulumi.get(self, "managed_resource_group_configuration")

    @property
    @pulumi.getter(name="manualActionCount")
    def manual_action_count(self) -> pulumi.Output[float]:
        """
        The count of Manual Action Taken (MAT) events that have not been validated.
        """
        return pulumi.get(self, "manual_action_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Network Fabric associated with the cluster.
        """
        return pulumi.get(self, "network_fabric_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the cluster.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="supportExpiryDate")
    def support_expiry_date(self) -> pulumi.Output[str]:
        """
        The support end date of the runtime version of the cluster.
        """
        return pulumi.get(self, "support_expiry_date")

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

    @property
    @pulumi.getter(name="workloadResourceIds")
    def workload_resource_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of workload resource IDs that are hosted within this cluster.
        """
        return pulumi.get(self, "workload_resource_ids")

