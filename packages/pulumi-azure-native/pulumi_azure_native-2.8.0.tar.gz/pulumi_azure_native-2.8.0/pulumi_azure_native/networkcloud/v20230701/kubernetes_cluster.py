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

__all__ = ['KubernetesClusterArgs', 'KubernetesCluster']

@pulumi.input_type
class KubernetesClusterArgs:
    def __init__(__self__, *,
                 control_plane_node_configuration: pulumi.Input['ControlPlaneNodeConfigurationArgs'],
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 initial_agent_pool_configurations: pulumi.Input[Sequence[pulumi.Input['InitialAgentPoolConfigurationArgs']]],
                 kubernetes_version: pulumi.Input[str],
                 network_configuration: pulumi.Input['NetworkConfigurationArgs'],
                 resource_group_name: pulumi.Input[str],
                 aad_configuration: Optional[pulumi.Input['AadConfigurationArgs']] = None,
                 administrator_configuration: Optional[pulumi.Input['AdministratorConfigurationArgs']] = None,
                 kubernetes_cluster_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input['ManagedResourceGroupConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a KubernetesCluster resource.
        :param pulumi.Input['ControlPlaneNodeConfigurationArgs'] control_plane_node_configuration: The defining characteristics of the control plane for this Kubernetes Cluster.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[Sequence[pulumi.Input['InitialAgentPoolConfigurationArgs']]] initial_agent_pool_configurations: The agent pools that are created with this Kubernetes cluster for running critical system services and workloads. This data in this field is only used during creation, and the field will be empty following the creation of the Kubernetes Cluster. After creation, the management of agent pools is done using the agentPools sub-resource.
        :param pulumi.Input[str] kubernetes_version: The Kubernetes version for this cluster. Accepts n.n, n.n.n, and n.n.n-n format. The interpreted version used will be resolved into this field after creation or update.
        :param pulumi.Input['NetworkConfigurationArgs'] network_configuration: The configuration of the Kubernetes cluster networking, including the attachment of networks that span the cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['AadConfigurationArgs'] aad_configuration: The Azure Active Directory Integration properties.
        :param pulumi.Input['AdministratorConfigurationArgs'] administrator_configuration: The administrative credentials that will be applied to the control plane and agent pool nodes that do not specify their own values.
        :param pulumi.Input[str] kubernetes_cluster_name: The name of the Kubernetes cluster.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['ManagedResourceGroupConfigurationArgs'] managed_resource_group_configuration: The configuration of the managed resource group associated with the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "control_plane_node_configuration", control_plane_node_configuration)
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "initial_agent_pool_configurations", initial_agent_pool_configurations)
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        pulumi.set(__self__, "network_configuration", network_configuration)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if aad_configuration is not None:
            pulumi.set(__self__, "aad_configuration", aad_configuration)
        if administrator_configuration is not None:
            pulumi.set(__self__, "administrator_configuration", administrator_configuration)
        if kubernetes_cluster_name is not None:
            pulumi.set(__self__, "kubernetes_cluster_name", kubernetes_cluster_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_resource_group_configuration is not None:
            pulumi.set(__self__, "managed_resource_group_configuration", managed_resource_group_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="controlPlaneNodeConfiguration")
    def control_plane_node_configuration(self) -> pulumi.Input['ControlPlaneNodeConfigurationArgs']:
        """
        The defining characteristics of the control plane for this Kubernetes Cluster.
        """
        return pulumi.get(self, "control_plane_node_configuration")

    @control_plane_node_configuration.setter
    def control_plane_node_configuration(self, value: pulumi.Input['ControlPlaneNodeConfigurationArgs']):
        pulumi.set(self, "control_plane_node_configuration", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="initialAgentPoolConfigurations")
    def initial_agent_pool_configurations(self) -> pulumi.Input[Sequence[pulumi.Input['InitialAgentPoolConfigurationArgs']]]:
        """
        The agent pools that are created with this Kubernetes cluster for running critical system services and workloads. This data in this field is only used during creation, and the field will be empty following the creation of the Kubernetes Cluster. After creation, the management of agent pools is done using the agentPools sub-resource.
        """
        return pulumi.get(self, "initial_agent_pool_configurations")

    @initial_agent_pool_configurations.setter
    def initial_agent_pool_configurations(self, value: pulumi.Input[Sequence[pulumi.Input['InitialAgentPoolConfigurationArgs']]]):
        pulumi.set(self, "initial_agent_pool_configurations", value)

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Input[str]:
        """
        The Kubernetes version for this cluster. Accepts n.n, n.n.n, and n.n.n-n format. The interpreted version used will be resolved into this field after creation or update.
        """
        return pulumi.get(self, "kubernetes_version")

    @kubernetes_version.setter
    def kubernetes_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "kubernetes_version", value)

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Input['NetworkConfigurationArgs']:
        """
        The configuration of the Kubernetes cluster networking, including the attachment of networks that span the cluster.
        """
        return pulumi.get(self, "network_configuration")

    @network_configuration.setter
    def network_configuration(self, value: pulumi.Input['NetworkConfigurationArgs']):
        pulumi.set(self, "network_configuration", value)

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
    @pulumi.getter(name="aadConfiguration")
    def aad_configuration(self) -> Optional[pulumi.Input['AadConfigurationArgs']]:
        """
        The Azure Active Directory Integration properties.
        """
        return pulumi.get(self, "aad_configuration")

    @aad_configuration.setter
    def aad_configuration(self, value: Optional[pulumi.Input['AadConfigurationArgs']]):
        pulumi.set(self, "aad_configuration", value)

    @property
    @pulumi.getter(name="administratorConfiguration")
    def administrator_configuration(self) -> Optional[pulumi.Input['AdministratorConfigurationArgs']]:
        """
        The administrative credentials that will be applied to the control plane and agent pool nodes that do not specify their own values.
        """
        return pulumi.get(self, "administrator_configuration")

    @administrator_configuration.setter
    def administrator_configuration(self, value: Optional[pulumi.Input['AdministratorConfigurationArgs']]):
        pulumi.set(self, "administrator_configuration", value)

    @property
    @pulumi.getter(name="kubernetesClusterName")
    def kubernetes_cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kubernetes cluster.
        """
        return pulumi.get(self, "kubernetes_cluster_name")

    @kubernetes_cluster_name.setter
    def kubernetes_cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubernetes_cluster_name", value)

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


class KubernetesCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aad_configuration: Optional[pulumi.Input[pulumi.InputType['AadConfigurationArgs']]] = None,
                 administrator_configuration: Optional[pulumi.Input[pulumi.InputType['AdministratorConfigurationArgs']]] = None,
                 control_plane_node_configuration: Optional[pulumi.Input[pulumi.InputType['ControlPlaneNodeConfigurationArgs']]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 initial_agent_pool_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InitialAgentPoolConfigurationArgs']]]]] = None,
                 kubernetes_cluster_name: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input[pulumi.InputType['ManagedResourceGroupConfigurationArgs']]] = None,
                 network_configuration: Optional[pulumi.Input[pulumi.InputType['NetworkConfigurationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a KubernetesCluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AadConfigurationArgs']] aad_configuration: The Azure Active Directory Integration properties.
        :param pulumi.Input[pulumi.InputType['AdministratorConfigurationArgs']] administrator_configuration: The administrative credentials that will be applied to the control plane and agent pool nodes that do not specify their own values.
        :param pulumi.Input[pulumi.InputType['ControlPlaneNodeConfigurationArgs']] control_plane_node_configuration: The defining characteristics of the control plane for this Kubernetes Cluster.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InitialAgentPoolConfigurationArgs']]]] initial_agent_pool_configurations: The agent pools that are created with this Kubernetes cluster for running critical system services and workloads. This data in this field is only used during creation, and the field will be empty following the creation of the Kubernetes Cluster. After creation, the management of agent pools is done using the agentPools sub-resource.
        :param pulumi.Input[str] kubernetes_cluster_name: The name of the Kubernetes cluster.
        :param pulumi.Input[str] kubernetes_version: The Kubernetes version for this cluster. Accepts n.n, n.n.n, and n.n.n-n format. The interpreted version used will be resolved into this field after creation or update.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['ManagedResourceGroupConfigurationArgs']] managed_resource_group_configuration: The configuration of the managed resource group associated with the resource.
        :param pulumi.Input[pulumi.InputType['NetworkConfigurationArgs']] network_configuration: The configuration of the Kubernetes cluster networking, including the attachment of networks that span the cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KubernetesClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a KubernetesCluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param KubernetesClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KubernetesClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aad_configuration: Optional[pulumi.Input[pulumi.InputType['AadConfigurationArgs']]] = None,
                 administrator_configuration: Optional[pulumi.Input[pulumi.InputType['AdministratorConfigurationArgs']]] = None,
                 control_plane_node_configuration: Optional[pulumi.Input[pulumi.InputType['ControlPlaneNodeConfigurationArgs']]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 initial_agent_pool_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InitialAgentPoolConfigurationArgs']]]]] = None,
                 kubernetes_cluster_name: Optional[pulumi.Input[str]] = None,
                 kubernetes_version: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input[pulumi.InputType['ManagedResourceGroupConfigurationArgs']]] = None,
                 network_configuration: Optional[pulumi.Input[pulumi.InputType['NetworkConfigurationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KubernetesClusterArgs.__new__(KubernetesClusterArgs)

            __props__.__dict__["aad_configuration"] = aad_configuration
            __props__.__dict__["administrator_configuration"] = administrator_configuration
            if control_plane_node_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'control_plane_node_configuration'")
            __props__.__dict__["control_plane_node_configuration"] = control_plane_node_configuration
            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            if initial_agent_pool_configurations is None and not opts.urn:
                raise TypeError("Missing required property 'initial_agent_pool_configurations'")
            __props__.__dict__["initial_agent_pool_configurations"] = initial_agent_pool_configurations
            __props__.__dict__["kubernetes_cluster_name"] = kubernetes_cluster_name
            if kubernetes_version is None and not opts.urn:
                raise TypeError("Missing required property 'kubernetes_version'")
            __props__.__dict__["kubernetes_version"] = kubernetes_version
            __props__.__dict__["location"] = location
            __props__.__dict__["managed_resource_group_configuration"] = managed_resource_group_configuration
            if network_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'network_configuration'")
            __props__.__dict__["network_configuration"] = network_configuration
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["attached_network_ids"] = None
            __props__.__dict__["available_upgrades"] = None
            __props__.__dict__["cluster_id"] = None
            __props__.__dict__["connected_cluster_id"] = None
            __props__.__dict__["control_plane_kubernetes_version"] = None
            __props__.__dict__["detailed_status"] = None
            __props__.__dict__["detailed_status_message"] = None
            __props__.__dict__["feature_statuses"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["nodes"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkcloud:KubernetesCluster"), pulumi.Alias(type_="azure-native:networkcloud/v20230501preview:KubernetesCluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(KubernetesCluster, __self__).__init__(
            'azure-native:networkcloud/v20230701:KubernetesCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'KubernetesCluster':
        """
        Get an existing KubernetesCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = KubernetesClusterArgs.__new__(KubernetesClusterArgs)

        __props__.__dict__["aad_configuration"] = None
        __props__.__dict__["administrator_configuration"] = None
        __props__.__dict__["attached_network_ids"] = None
        __props__.__dict__["available_upgrades"] = None
        __props__.__dict__["cluster_id"] = None
        __props__.__dict__["connected_cluster_id"] = None
        __props__.__dict__["control_plane_kubernetes_version"] = None
        __props__.__dict__["control_plane_node_configuration"] = None
        __props__.__dict__["detailed_status"] = None
        __props__.__dict__["detailed_status_message"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["feature_statuses"] = None
        __props__.__dict__["initial_agent_pool_configurations"] = None
        __props__.__dict__["kubernetes_version"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_resource_group_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_configuration"] = None
        __props__.__dict__["nodes"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return KubernetesCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aadConfiguration")
    def aad_configuration(self) -> pulumi.Output[Optional['outputs.AadConfigurationResponse']]:
        """
        The Azure Active Directory Integration properties.
        """
        return pulumi.get(self, "aad_configuration")

    @property
    @pulumi.getter(name="administratorConfiguration")
    def administrator_configuration(self) -> pulumi.Output[Optional['outputs.AdministratorConfigurationResponse']]:
        """
        The administrative credentials that will be applied to the control plane and agent pool nodes that do not specify their own values.
        """
        return pulumi.get(self, "administrator_configuration")

    @property
    @pulumi.getter(name="attachedNetworkIds")
    def attached_network_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The full list of network resource IDs that are attached to this cluster, including those attached only to specific agent pools.
        """
        return pulumi.get(self, "attached_network_ids")

    @property
    @pulumi.getter(name="availableUpgrades")
    def available_upgrades(self) -> pulumi.Output[Sequence['outputs.AvailableUpgradeResponse']]:
        """
        The list of versions that this Kubernetes cluster can be upgraded to.
        """
        return pulumi.get(self, "available_upgrades")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Network Cloud cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="connectedClusterId")
    def connected_cluster_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the connected cluster set up when this Kubernetes cluster is created.
        """
        return pulumi.get(self, "connected_cluster_id")

    @property
    @pulumi.getter(name="controlPlaneKubernetesVersion")
    def control_plane_kubernetes_version(self) -> pulumi.Output[str]:
        """
        The current running version of Kubernetes on the control plane.
        """
        return pulumi.get(self, "control_plane_kubernetes_version")

    @property
    @pulumi.getter(name="controlPlaneNodeConfiguration")
    def control_plane_node_configuration(self) -> pulumi.Output['outputs.ControlPlaneNodeConfigurationResponse']:
        """
        The defining characteristics of the control plane for this Kubernetes Cluster.
        """
        return pulumi.get(self, "control_plane_node_configuration")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[str]:
        """
        The current status of the Kubernetes cluster.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[str]:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="featureStatuses")
    def feature_statuses(self) -> pulumi.Output[Sequence['outputs.FeatureStatusResponse']]:
        """
        The current feature settings.
        """
        return pulumi.get(self, "feature_statuses")

    @property
    @pulumi.getter(name="initialAgentPoolConfigurations")
    def initial_agent_pool_configurations(self) -> pulumi.Output[Sequence['outputs.InitialAgentPoolConfigurationResponse']]:
        """
        The agent pools that are created with this Kubernetes cluster for running critical system services and workloads. This data in this field is only used during creation, and the field will be empty following the creation of the Kubernetes Cluster. After creation, the management of agent pools is done using the agentPools sub-resource.
        """
        return pulumi.get(self, "initial_agent_pool_configurations")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[str]:
        """
        The Kubernetes version for this cluster. Accepts n.n, n.n.n, and n.n.n-n format. The interpreted version used will be resolved into this field after creation or update.
        """
        return pulumi.get(self, "kubernetes_version")

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
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Output['outputs.NetworkConfigurationResponse']:
        """
        The configuration of the Kubernetes cluster networking, including the attachment of networks that span the cluster.
        """
        return pulumi.get(self, "network_configuration")

    @property
    @pulumi.getter
    def nodes(self) -> pulumi.Output[Sequence['outputs.KubernetesClusterNodeResponse']]:
        """
        The details of the nodes in this cluster.
        """
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the Kubernetes cluster resource.
        """
        return pulumi.get(self, "provisioning_state")

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

