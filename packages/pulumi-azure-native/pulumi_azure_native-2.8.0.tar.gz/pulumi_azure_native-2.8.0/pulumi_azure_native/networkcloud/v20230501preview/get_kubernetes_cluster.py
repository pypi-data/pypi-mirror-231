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

__all__ = [
    'GetKubernetesClusterResult',
    'AwaitableGetKubernetesClusterResult',
    'get_kubernetes_cluster',
    'get_kubernetes_cluster_output',
]

@pulumi.output_type
class GetKubernetesClusterResult:
    def __init__(__self__, aad_configuration=None, administrator_configuration=None, attached_network_ids=None, available_upgrades=None, cluster_id=None, connected_cluster_id=None, control_plane_kubernetes_version=None, control_plane_node_configuration=None, detailed_status=None, detailed_status_message=None, extended_location=None, feature_statuses=None, id=None, initial_agent_pool_configurations=None, kubernetes_version=None, location=None, managed_resource_group_configuration=None, name=None, network_configuration=None, nodes=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if aad_configuration and not isinstance(aad_configuration, dict):
            raise TypeError("Expected argument 'aad_configuration' to be a dict")
        pulumi.set(__self__, "aad_configuration", aad_configuration)
        if administrator_configuration and not isinstance(administrator_configuration, dict):
            raise TypeError("Expected argument 'administrator_configuration' to be a dict")
        pulumi.set(__self__, "administrator_configuration", administrator_configuration)
        if attached_network_ids and not isinstance(attached_network_ids, list):
            raise TypeError("Expected argument 'attached_network_ids' to be a list")
        pulumi.set(__self__, "attached_network_ids", attached_network_ids)
        if available_upgrades and not isinstance(available_upgrades, list):
            raise TypeError("Expected argument 'available_upgrades' to be a list")
        pulumi.set(__self__, "available_upgrades", available_upgrades)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if connected_cluster_id and not isinstance(connected_cluster_id, str):
            raise TypeError("Expected argument 'connected_cluster_id' to be a str")
        pulumi.set(__self__, "connected_cluster_id", connected_cluster_id)
        if control_plane_kubernetes_version and not isinstance(control_plane_kubernetes_version, str):
            raise TypeError("Expected argument 'control_plane_kubernetes_version' to be a str")
        pulumi.set(__self__, "control_plane_kubernetes_version", control_plane_kubernetes_version)
        if control_plane_node_configuration and not isinstance(control_plane_node_configuration, dict):
            raise TypeError("Expected argument 'control_plane_node_configuration' to be a dict")
        pulumi.set(__self__, "control_plane_node_configuration", control_plane_node_configuration)
        if detailed_status and not isinstance(detailed_status, str):
            raise TypeError("Expected argument 'detailed_status' to be a str")
        pulumi.set(__self__, "detailed_status", detailed_status)
        if detailed_status_message and not isinstance(detailed_status_message, str):
            raise TypeError("Expected argument 'detailed_status_message' to be a str")
        pulumi.set(__self__, "detailed_status_message", detailed_status_message)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if feature_statuses and not isinstance(feature_statuses, list):
            raise TypeError("Expected argument 'feature_statuses' to be a list")
        pulumi.set(__self__, "feature_statuses", feature_statuses)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if initial_agent_pool_configurations and not isinstance(initial_agent_pool_configurations, list):
            raise TypeError("Expected argument 'initial_agent_pool_configurations' to be a list")
        pulumi.set(__self__, "initial_agent_pool_configurations", initial_agent_pool_configurations)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_resource_group_configuration and not isinstance(managed_resource_group_configuration, dict):
            raise TypeError("Expected argument 'managed_resource_group_configuration' to be a dict")
        pulumi.set(__self__, "managed_resource_group_configuration", managed_resource_group_configuration)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_configuration and not isinstance(network_configuration, dict):
            raise TypeError("Expected argument 'network_configuration' to be a dict")
        pulumi.set(__self__, "network_configuration", network_configuration)
        if nodes and not isinstance(nodes, list):
            raise TypeError("Expected argument 'nodes' to be a list")
        pulumi.set(__self__, "nodes", nodes)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="aadConfiguration")
    def aad_configuration(self) -> Optional['outputs.AadConfigurationResponse']:
        """
        The Azure Active Directory Integration properties.
        """
        return pulumi.get(self, "aad_configuration")

    @property
    @pulumi.getter(name="administratorConfiguration")
    def administrator_configuration(self) -> Optional['outputs.AdministratorConfigurationResponse']:
        """
        The administrative credentials that will be applied to the control plane and agent pool nodes that do not specify their own values.
        """
        return pulumi.get(self, "administrator_configuration")

    @property
    @pulumi.getter(name="attachedNetworkIds")
    def attached_network_ids(self) -> Sequence[str]:
        """
        The full list of network resource IDs that are attached to this cluster, including those attached only to specific agent pools.
        """
        return pulumi.get(self, "attached_network_ids")

    @property
    @pulumi.getter(name="availableUpgrades")
    def available_upgrades(self) -> Sequence['outputs.AvailableUpgradeResponse']:
        """
        The list of versions that this Kubernetes cluster can be upgraded to.
        """
        return pulumi.get(self, "available_upgrades")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The resource ID of the Network Cloud cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="connectedClusterId")
    def connected_cluster_id(self) -> str:
        """
        The resource ID of the connected cluster set up when this Kubernetes cluster is created.
        """
        return pulumi.get(self, "connected_cluster_id")

    @property
    @pulumi.getter(name="controlPlaneKubernetesVersion")
    def control_plane_kubernetes_version(self) -> str:
        """
        The current running version of Kubernetes on the control plane.
        """
        return pulumi.get(self, "control_plane_kubernetes_version")

    @property
    @pulumi.getter(name="controlPlaneNodeConfiguration")
    def control_plane_node_configuration(self) -> 'outputs.ControlPlaneNodeConfigurationResponse':
        """
        The defining characteristics of the control plane for this Kubernetes Cluster.
        """
        return pulumi.get(self, "control_plane_node_configuration")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> str:
        """
        The current status of the Kubernetes cluster.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> str:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="featureStatuses")
    def feature_statuses(self) -> Sequence['outputs.FeatureStatusResponse']:
        """
        The current feature settings.
        """
        return pulumi.get(self, "feature_statuses")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="initialAgentPoolConfigurations")
    def initial_agent_pool_configurations(self) -> Sequence['outputs.InitialAgentPoolConfigurationResponse']:
        """
        The agent pools that are created with this Kubernetes cluster for running critical system services and workloads. This data in this field is only used during creation, and the field will be empty following the creation of the Kubernetes Cluster. After creation, the management of agent pools is done using the agentPools sub-resource.
        """
        return pulumi.get(self, "initial_agent_pool_configurations")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> str:
        """
        The Kubernetes version for this cluster. Accepts n.n, n.n.n, and n.n.n-n format. The interpreted version used will be resolved into this field after creation or update.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> Optional['outputs.ManagedResourceGroupConfigurationResponse']:
        """
        The configuration of the managed resource group associated with the resource.
        """
        return pulumi.get(self, "managed_resource_group_configuration")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> 'outputs.NetworkConfigurationResponse':
        """
        The configuration of the Kubernetes cluster networking, including the attachment of networks that span the cluster.
        """
        return pulumi.get(self, "network_configuration")

    @property
    @pulumi.getter
    def nodes(self) -> Sequence['outputs.KubernetesClusterNodeResponse']:
        """
        The details of the nodes in this cluster.
        """
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the Kubernetes cluster resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetKubernetesClusterResult(GetKubernetesClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKubernetesClusterResult(
            aad_configuration=self.aad_configuration,
            administrator_configuration=self.administrator_configuration,
            attached_network_ids=self.attached_network_ids,
            available_upgrades=self.available_upgrades,
            cluster_id=self.cluster_id,
            connected_cluster_id=self.connected_cluster_id,
            control_plane_kubernetes_version=self.control_plane_kubernetes_version,
            control_plane_node_configuration=self.control_plane_node_configuration,
            detailed_status=self.detailed_status,
            detailed_status_message=self.detailed_status_message,
            extended_location=self.extended_location,
            feature_statuses=self.feature_statuses,
            id=self.id,
            initial_agent_pool_configurations=self.initial_agent_pool_configurations,
            kubernetes_version=self.kubernetes_version,
            location=self.location,
            managed_resource_group_configuration=self.managed_resource_group_configuration,
            name=self.name,
            network_configuration=self.network_configuration,
            nodes=self.nodes,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_kubernetes_cluster(kubernetes_cluster_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKubernetesClusterResult:
    """
    Get properties of the provided the Kubernetes cluster.


    :param str kubernetes_cluster_name: The name of the Kubernetes cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['kubernetesClusterName'] = kubernetes_cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkcloud/v20230501preview:getKubernetesCluster', __args__, opts=opts, typ=GetKubernetesClusterResult).value

    return AwaitableGetKubernetesClusterResult(
        aad_configuration=pulumi.get(__ret__, 'aad_configuration'),
        administrator_configuration=pulumi.get(__ret__, 'administrator_configuration'),
        attached_network_ids=pulumi.get(__ret__, 'attached_network_ids'),
        available_upgrades=pulumi.get(__ret__, 'available_upgrades'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        connected_cluster_id=pulumi.get(__ret__, 'connected_cluster_id'),
        control_plane_kubernetes_version=pulumi.get(__ret__, 'control_plane_kubernetes_version'),
        control_plane_node_configuration=pulumi.get(__ret__, 'control_plane_node_configuration'),
        detailed_status=pulumi.get(__ret__, 'detailed_status'),
        detailed_status_message=pulumi.get(__ret__, 'detailed_status_message'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        feature_statuses=pulumi.get(__ret__, 'feature_statuses'),
        id=pulumi.get(__ret__, 'id'),
        initial_agent_pool_configurations=pulumi.get(__ret__, 'initial_agent_pool_configurations'),
        kubernetes_version=pulumi.get(__ret__, 'kubernetes_version'),
        location=pulumi.get(__ret__, 'location'),
        managed_resource_group_configuration=pulumi.get(__ret__, 'managed_resource_group_configuration'),
        name=pulumi.get(__ret__, 'name'),
        network_configuration=pulumi.get(__ret__, 'network_configuration'),
        nodes=pulumi.get(__ret__, 'nodes'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_kubernetes_cluster)
def get_kubernetes_cluster_output(kubernetes_cluster_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKubernetesClusterResult]:
    """
    Get properties of the provided the Kubernetes cluster.


    :param str kubernetes_cluster_name: The name of the Kubernetes cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
