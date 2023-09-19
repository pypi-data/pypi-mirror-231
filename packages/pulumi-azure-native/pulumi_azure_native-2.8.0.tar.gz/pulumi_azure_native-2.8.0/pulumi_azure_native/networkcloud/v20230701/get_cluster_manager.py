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
    'GetClusterManagerResult',
    'AwaitableGetClusterManagerResult',
    'get_cluster_manager',
    'get_cluster_manager_output',
]

@pulumi.output_type
class GetClusterManagerResult:
    def __init__(__self__, analytics_workspace_id=None, availability_zones=None, cluster_versions=None, detailed_status=None, detailed_status_message=None, fabric_controller_id=None, id=None, location=None, managed_resource_group_configuration=None, manager_extended_location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None, vm_size=None):
        if analytics_workspace_id and not isinstance(analytics_workspace_id, str):
            raise TypeError("Expected argument 'analytics_workspace_id' to be a str")
        pulumi.set(__self__, "analytics_workspace_id", analytics_workspace_id)
        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError("Expected argument 'availability_zones' to be a list")
        pulumi.set(__self__, "availability_zones", availability_zones)
        if cluster_versions and not isinstance(cluster_versions, list):
            raise TypeError("Expected argument 'cluster_versions' to be a list")
        pulumi.set(__self__, "cluster_versions", cluster_versions)
        if detailed_status and not isinstance(detailed_status, str):
            raise TypeError("Expected argument 'detailed_status' to be a str")
        pulumi.set(__self__, "detailed_status", detailed_status)
        if detailed_status_message and not isinstance(detailed_status_message, str):
            raise TypeError("Expected argument 'detailed_status_message' to be a str")
        pulumi.set(__self__, "detailed_status_message", detailed_status_message)
        if fabric_controller_id and not isinstance(fabric_controller_id, str):
            raise TypeError("Expected argument 'fabric_controller_id' to be a str")
        pulumi.set(__self__, "fabric_controller_id", fabric_controller_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_resource_group_configuration and not isinstance(managed_resource_group_configuration, dict):
            raise TypeError("Expected argument 'managed_resource_group_configuration' to be a dict")
        pulumi.set(__self__, "managed_resource_group_configuration", managed_resource_group_configuration)
        if manager_extended_location and not isinstance(manager_extended_location, dict):
            raise TypeError("Expected argument 'manager_extended_location' to be a dict")
        pulumi.set(__self__, "manager_extended_location", manager_extended_location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
        if vm_size and not isinstance(vm_size, str):
            raise TypeError("Expected argument 'vm_size' to be a str")
        pulumi.set(__self__, "vm_size", vm_size)

    @property
    @pulumi.getter(name="analyticsWorkspaceId")
    def analytics_workspace_id(self) -> Optional[str]:
        """
        The resource ID of the Log Analytics workspace that is used for the logs collection.
        """
        return pulumi.get(self, "analytics_workspace_id")

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[str]]:
        """
        Field deprecated, this value will no longer influence the cluster manager allocation process and will be removed in a future version. The Azure availability zones within the region that will be used to support the cluster manager resource.
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="clusterVersions")
    def cluster_versions(self) -> Sequence['outputs.ClusterAvailableVersionResponse']:
        """
        The list of the cluster versions the manager supports. It is used as input in clusterVersion property of a cluster resource.
        """
        return pulumi.get(self, "cluster_versions")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> str:
        """
        The detailed status that provides additional information about the cluster manager.
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
    @pulumi.getter(name="fabricControllerId")
    def fabric_controller_id(self) -> str:
        """
        The resource ID of the fabric controller that has one to one mapping with the cluster manager.
        """
        return pulumi.get(self, "fabric_controller_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

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
    @pulumi.getter(name="managerExtendedLocation")
    def manager_extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location (custom location) that represents the cluster manager's control plane location. This extended location is used when creating cluster and rack manifest resources.
        """
        return pulumi.get(self, "manager_extended_location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the cluster manager.
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

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[str]:
        """
        Field deprecated, this value will no longer influence the cluster manager allocation process and will be removed in a future version. The size of the Azure virtual machines to use for hosting the cluster manager resource.
        """
        return pulumi.get(self, "vm_size")


class AwaitableGetClusterManagerResult(GetClusterManagerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterManagerResult(
            analytics_workspace_id=self.analytics_workspace_id,
            availability_zones=self.availability_zones,
            cluster_versions=self.cluster_versions,
            detailed_status=self.detailed_status,
            detailed_status_message=self.detailed_status_message,
            fabric_controller_id=self.fabric_controller_id,
            id=self.id,
            location=self.location,
            managed_resource_group_configuration=self.managed_resource_group_configuration,
            manager_extended_location=self.manager_extended_location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vm_size=self.vm_size)


def get_cluster_manager(cluster_manager_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterManagerResult:
    """
    Get the properties of the provided cluster manager.


    :param str cluster_manager_name: The name of the cluster manager.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterManagerName'] = cluster_manager_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkcloud/v20230701:getClusterManager', __args__, opts=opts, typ=GetClusterManagerResult).value

    return AwaitableGetClusterManagerResult(
        analytics_workspace_id=pulumi.get(__ret__, 'analytics_workspace_id'),
        availability_zones=pulumi.get(__ret__, 'availability_zones'),
        cluster_versions=pulumi.get(__ret__, 'cluster_versions'),
        detailed_status=pulumi.get(__ret__, 'detailed_status'),
        detailed_status_message=pulumi.get(__ret__, 'detailed_status_message'),
        fabric_controller_id=pulumi.get(__ret__, 'fabric_controller_id'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        managed_resource_group_configuration=pulumi.get(__ret__, 'managed_resource_group_configuration'),
        manager_extended_location=pulumi.get(__ret__, 'manager_extended_location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        vm_size=pulumi.get(__ret__, 'vm_size'))


@_utilities.lift_output_func(get_cluster_manager)
def get_cluster_manager_output(cluster_manager_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterManagerResult]:
    """
    Get the properties of the provided cluster manager.


    :param str cluster_manager_name: The name of the cluster manager.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
