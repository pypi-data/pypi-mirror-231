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
    'GetAgentPoolResult',
    'AwaitableGetAgentPoolResult',
    'get_agent_pool',
    'get_agent_pool_output',
]

@pulumi.output_type
class GetAgentPoolResult:
    """
    The agentPool resource definition
    """
    def __init__(__self__, availability_zones=None, cloud_provider_profile=None, count=None, extended_location=None, id=None, location=None, max_count=None, max_pods=None, min_count=None, mode=None, name=None, node_image_version=None, node_labels=None, node_taints=None, os_type=None, provisioning_state=None, status=None, system_data=None, tags=None, type=None, vm_size=None):
        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError("Expected argument 'availability_zones' to be a list")
        pulumi.set(__self__, "availability_zones", availability_zones)
        if cloud_provider_profile and not isinstance(cloud_provider_profile, dict):
            raise TypeError("Expected argument 'cloud_provider_profile' to be a dict")
        pulumi.set(__self__, "cloud_provider_profile", cloud_provider_profile)
        if count and not isinstance(count, int):
            raise TypeError("Expected argument 'count' to be a int")
        pulumi.set(__self__, "count", count)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_count and not isinstance(max_count, int):
            raise TypeError("Expected argument 'max_count' to be a int")
        pulumi.set(__self__, "max_count", max_count)
        if max_pods and not isinstance(max_pods, int):
            raise TypeError("Expected argument 'max_pods' to be a int")
        pulumi.set(__self__, "max_pods", max_pods)
        if min_count and not isinstance(min_count, int):
            raise TypeError("Expected argument 'min_count' to be a int")
        pulumi.set(__self__, "min_count", min_count)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_image_version and not isinstance(node_image_version, str):
            raise TypeError("Expected argument 'node_image_version' to be a str")
        pulumi.set(__self__, "node_image_version", node_image_version)
        if node_labels and not isinstance(node_labels, dict):
            raise TypeError("Expected argument 'node_labels' to be a dict")
        pulumi.set(__self__, "node_labels", node_labels)
        if node_taints and not isinstance(node_taints, list):
            raise TypeError("Expected argument 'node_taints' to be a list")
        pulumi.set(__self__, "node_taints", node_taints)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
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
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[str]]:
        """
        AvailabilityZones - The list of Availability zones to use for nodes. Datacenter racks modelled as zones
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter(name="cloudProviderProfile")
    def cloud_provider_profile(self) -> Optional['outputs.CloudProviderProfileResponse']:
        """
        The underlying cloud infra provider properties.
        """
        return pulumi.get(self, "cloud_provider_profile")

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        Count - Number of agents to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.AgentPoolResponseExtendedLocation']:
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[int]:
        """
        The maximum number of nodes for auto-scaling
        """
        return pulumi.get(self, "max_count")

    @property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[int]:
        """
        The maximum number of pods that can run on a node.
        """
        return pulumi.get(self, "max_pods")

    @property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[int]:
        """
        The minimum number of nodes for auto-scaling
        """
        return pulumi.get(self, "min_count")

    @property
    @pulumi.getter
    def mode(self) -> Optional[str]:
        """
        Mode - AgentPoolMode represents mode of an agent pool. Possible values include: 'System', 'LB', 'User'. Default is 'User'
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> Optional[str]:
        """
        The version of node image
        """
        return pulumi.get(self, "node_image_version")

    @property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> Optional[Mapping[str, str]]:
        """
        NodeLabels - Agent pool node labels to be persisted across all nodes in agent pool.
        """
        return pulumi.get(self, "node_labels")

    @property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Optional[Sequence[str]]:
        """
        NodeTaints - Taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule.
        """
        return pulumi.get(self, "node_taints")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        OsType - OsType to be used to specify os type. Choose from Linux and Windows. Default to Linux. Possible values include: 'Linux', 'Windows'
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> Optional['outputs.AgentPoolProvisioningStatusResponseStatus']:
        """
        HybridAKSNodePoolStatus defines the observed state of HybridAKSNodePool
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[str]:
        """
        VmSize - The size of the agent pool VMs.
        """
        return pulumi.get(self, "vm_size")


class AwaitableGetAgentPoolResult(GetAgentPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgentPoolResult(
            availability_zones=self.availability_zones,
            cloud_provider_profile=self.cloud_provider_profile,
            count=self.count,
            extended_location=self.extended_location,
            id=self.id,
            location=self.location,
            max_count=self.max_count,
            max_pods=self.max_pods,
            min_count=self.min_count,
            mode=self.mode,
            name=self.name,
            node_image_version=self.node_image_version,
            node_labels=self.node_labels,
            node_taints=self.node_taints,
            os_type=self.os_type,
            provisioning_state=self.provisioning_state,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vm_size=self.vm_size)


def get_agent_pool(agent_pool_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   resource_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgentPoolResult:
    """
    Gets the agent pool in the Hybrid AKS provisioned cluster


    :param str agent_pool_name: Parameter for the name of the agent pool in the provisioned cluster
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: Parameter for the name of the provisioned cluster
    """
    __args__ = dict()
    __args__['agentPoolName'] = agent_pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridcontainerservice/v20220901preview:getAgentPool', __args__, opts=opts, typ=GetAgentPoolResult).value

    return AwaitableGetAgentPoolResult(
        availability_zones=pulumi.get(__ret__, 'availability_zones'),
        cloud_provider_profile=pulumi.get(__ret__, 'cloud_provider_profile'),
        count=pulumi.get(__ret__, 'count'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        max_count=pulumi.get(__ret__, 'max_count'),
        max_pods=pulumi.get(__ret__, 'max_pods'),
        min_count=pulumi.get(__ret__, 'min_count'),
        mode=pulumi.get(__ret__, 'mode'),
        name=pulumi.get(__ret__, 'name'),
        node_image_version=pulumi.get(__ret__, 'node_image_version'),
        node_labels=pulumi.get(__ret__, 'node_labels'),
        node_taints=pulumi.get(__ret__, 'node_taints'),
        os_type=pulumi.get(__ret__, 'os_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        vm_size=pulumi.get(__ret__, 'vm_size'))


@_utilities.lift_output_func(get_agent_pool)
def get_agent_pool_output(agent_pool_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          resource_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgentPoolResult]:
    """
    Gets the agent pool in the Hybrid AKS provisioned cluster


    :param str agent_pool_name: Parameter for the name of the agent pool in the provisioned cluster
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: Parameter for the name of the provisioned cluster
    """
    ...
