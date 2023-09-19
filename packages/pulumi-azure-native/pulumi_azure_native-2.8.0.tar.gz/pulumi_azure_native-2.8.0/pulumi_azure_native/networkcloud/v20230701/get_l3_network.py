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
    'GetL3NetworkResult',
    'AwaitableGetL3NetworkResult',
    'get_l3_network',
    'get_l3_network_output',
]

@pulumi.output_type
class GetL3NetworkResult:
    def __init__(__self__, associated_resource_ids=None, cluster_id=None, detailed_status=None, detailed_status_message=None, extended_location=None, hybrid_aks_clusters_associated_ids=None, hybrid_aks_ipam_enabled=None, hybrid_aks_plugin_type=None, id=None, interface_name=None, ip_allocation_type=None, ipv4_connected_prefix=None, ipv6_connected_prefix=None, l3_isolation_domain_id=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None, virtual_machines_associated_ids=None, vlan=None):
        if associated_resource_ids and not isinstance(associated_resource_ids, list):
            raise TypeError("Expected argument 'associated_resource_ids' to be a list")
        pulumi.set(__self__, "associated_resource_ids", associated_resource_ids)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if detailed_status and not isinstance(detailed_status, str):
            raise TypeError("Expected argument 'detailed_status' to be a str")
        pulumi.set(__self__, "detailed_status", detailed_status)
        if detailed_status_message and not isinstance(detailed_status_message, str):
            raise TypeError("Expected argument 'detailed_status_message' to be a str")
        pulumi.set(__self__, "detailed_status_message", detailed_status_message)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if hybrid_aks_clusters_associated_ids and not isinstance(hybrid_aks_clusters_associated_ids, list):
            raise TypeError("Expected argument 'hybrid_aks_clusters_associated_ids' to be a list")
        pulumi.set(__self__, "hybrid_aks_clusters_associated_ids", hybrid_aks_clusters_associated_ids)
        if hybrid_aks_ipam_enabled and not isinstance(hybrid_aks_ipam_enabled, str):
            raise TypeError("Expected argument 'hybrid_aks_ipam_enabled' to be a str")
        pulumi.set(__self__, "hybrid_aks_ipam_enabled", hybrid_aks_ipam_enabled)
        if hybrid_aks_plugin_type and not isinstance(hybrid_aks_plugin_type, str):
            raise TypeError("Expected argument 'hybrid_aks_plugin_type' to be a str")
        pulumi.set(__self__, "hybrid_aks_plugin_type", hybrid_aks_plugin_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interface_name and not isinstance(interface_name, str):
            raise TypeError("Expected argument 'interface_name' to be a str")
        pulumi.set(__self__, "interface_name", interface_name)
        if ip_allocation_type and not isinstance(ip_allocation_type, str):
            raise TypeError("Expected argument 'ip_allocation_type' to be a str")
        pulumi.set(__self__, "ip_allocation_type", ip_allocation_type)
        if ipv4_connected_prefix and not isinstance(ipv4_connected_prefix, str):
            raise TypeError("Expected argument 'ipv4_connected_prefix' to be a str")
        pulumi.set(__self__, "ipv4_connected_prefix", ipv4_connected_prefix)
        if ipv6_connected_prefix and not isinstance(ipv6_connected_prefix, str):
            raise TypeError("Expected argument 'ipv6_connected_prefix' to be a str")
        pulumi.set(__self__, "ipv6_connected_prefix", ipv6_connected_prefix)
        if l3_isolation_domain_id and not isinstance(l3_isolation_domain_id, str):
            raise TypeError("Expected argument 'l3_isolation_domain_id' to be a str")
        pulumi.set(__self__, "l3_isolation_domain_id", l3_isolation_domain_id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
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
        if virtual_machines_associated_ids and not isinstance(virtual_machines_associated_ids, list):
            raise TypeError("Expected argument 'virtual_machines_associated_ids' to be a list")
        pulumi.set(__self__, "virtual_machines_associated_ids", virtual_machines_associated_ids)
        if vlan and not isinstance(vlan, float):
            raise TypeError("Expected argument 'vlan' to be a float")
        pulumi.set(__self__, "vlan", vlan)

    @property
    @pulumi.getter(name="associatedResourceIds")
    def associated_resource_ids(self) -> Sequence[str]:
        """
        The list of resource IDs for the other Microsoft.NetworkCloud resources that have attached this network.
        """
        return pulumi.get(self, "associated_resource_ids")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The resource ID of the Network Cloud cluster this L3 network is associated with.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> str:
        """
        The more detailed status of the L3 network.
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
    @pulumi.getter(name="hybridAksClustersAssociatedIds")
    def hybrid_aks_clusters_associated_ids(self) -> Sequence[str]:
        """
        Field Deprecated. These fields will be empty/omitted. The list of Hybrid AKS cluster resource IDs that are associated with this L3 network.
        """
        return pulumi.get(self, "hybrid_aks_clusters_associated_ids")

    @property
    @pulumi.getter(name="hybridAksIpamEnabled")
    def hybrid_aks_ipam_enabled(self) -> Optional[str]:
        """
        Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The indicator of whether or not to disable IPAM allocation on the network attachment definition injected into the Hybrid AKS Cluster.
        """
        return pulumi.get(self, "hybrid_aks_ipam_enabled")

    @property
    @pulumi.getter(name="hybridAksPluginType")
    def hybrid_aks_plugin_type(self) -> Optional[str]:
        """
        Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The network plugin type for Hybrid AKS.
        """
        return pulumi.get(self, "hybrid_aks_plugin_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="interfaceName")
    def interface_name(self) -> Optional[str]:
        """
        The default interface name for this L3 network in the virtual machine. This name can be overridden by the name supplied in the network attachment configuration of that virtual machine.
        """
        return pulumi.get(self, "interface_name")

    @property
    @pulumi.getter(name="ipAllocationType")
    def ip_allocation_type(self) -> Optional[str]:
        """
        The type of the IP address allocation, defaulted to "DualStack".
        """
        return pulumi.get(self, "ip_allocation_type")

    @property
    @pulumi.getter(name="ipv4ConnectedPrefix")
    def ipv4_connected_prefix(self) -> Optional[str]:
        """
        The IPV4 prefix (CIDR) assigned to this L3 network. Required when the IP allocation type
        is IPV4 or DualStack.
        """
        return pulumi.get(self, "ipv4_connected_prefix")

    @property
    @pulumi.getter(name="ipv6ConnectedPrefix")
    def ipv6_connected_prefix(self) -> Optional[str]:
        """
        The IPV6 prefix (CIDR) assigned to this L3 network. Required when the IP allocation type
        is IPV6 or DualStack.
        """
        return pulumi.get(self, "ipv6_connected_prefix")

    @property
    @pulumi.getter(name="l3IsolationDomainId")
    def l3_isolation_domain_id(self) -> str:
        """
        The resource ID of the Network Fabric l3IsolationDomain.
        """
        return pulumi.get(self, "l3_isolation_domain_id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

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
        The provisioning state of the L3 network.
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
    @pulumi.getter(name="virtualMachinesAssociatedIds")
    def virtual_machines_associated_ids(self) -> Sequence[str]:
        """
        Field Deprecated. These fields will be empty/omitted. The list of virtual machine resource IDs, excluding any Hybrid AKS virtual machines, that are currently using this L3 network.
        """
        return pulumi.get(self, "virtual_machines_associated_ids")

    @property
    @pulumi.getter
    def vlan(self) -> float:
        """
        The VLAN from the l3IsolationDomain that is used for this network.
        """
        return pulumi.get(self, "vlan")


class AwaitableGetL3NetworkResult(GetL3NetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetL3NetworkResult(
            associated_resource_ids=self.associated_resource_ids,
            cluster_id=self.cluster_id,
            detailed_status=self.detailed_status,
            detailed_status_message=self.detailed_status_message,
            extended_location=self.extended_location,
            hybrid_aks_clusters_associated_ids=self.hybrid_aks_clusters_associated_ids,
            hybrid_aks_ipam_enabled=self.hybrid_aks_ipam_enabled,
            hybrid_aks_plugin_type=self.hybrid_aks_plugin_type,
            id=self.id,
            interface_name=self.interface_name,
            ip_allocation_type=self.ip_allocation_type,
            ipv4_connected_prefix=self.ipv4_connected_prefix,
            ipv6_connected_prefix=self.ipv6_connected_prefix,
            l3_isolation_domain_id=self.l3_isolation_domain_id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            virtual_machines_associated_ids=self.virtual_machines_associated_ids,
            vlan=self.vlan)


def get_l3_network(l3_network_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetL3NetworkResult:
    """
    Get properties of the provided layer 3 (L3) network.


    :param str l3_network_name: The name of the L3 network.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['l3NetworkName'] = l3_network_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkcloud/v20230701:getL3Network', __args__, opts=opts, typ=GetL3NetworkResult).value

    return AwaitableGetL3NetworkResult(
        associated_resource_ids=pulumi.get(__ret__, 'associated_resource_ids'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        detailed_status=pulumi.get(__ret__, 'detailed_status'),
        detailed_status_message=pulumi.get(__ret__, 'detailed_status_message'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        hybrid_aks_clusters_associated_ids=pulumi.get(__ret__, 'hybrid_aks_clusters_associated_ids'),
        hybrid_aks_ipam_enabled=pulumi.get(__ret__, 'hybrid_aks_ipam_enabled'),
        hybrid_aks_plugin_type=pulumi.get(__ret__, 'hybrid_aks_plugin_type'),
        id=pulumi.get(__ret__, 'id'),
        interface_name=pulumi.get(__ret__, 'interface_name'),
        ip_allocation_type=pulumi.get(__ret__, 'ip_allocation_type'),
        ipv4_connected_prefix=pulumi.get(__ret__, 'ipv4_connected_prefix'),
        ipv6_connected_prefix=pulumi.get(__ret__, 'ipv6_connected_prefix'),
        l3_isolation_domain_id=pulumi.get(__ret__, 'l3_isolation_domain_id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        virtual_machines_associated_ids=pulumi.get(__ret__, 'virtual_machines_associated_ids'),
        vlan=pulumi.get(__ret__, 'vlan'))


@_utilities.lift_output_func(get_l3_network)
def get_l3_network_output(l3_network_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetL3NetworkResult]:
    """
    Get properties of the provided layer 3 (L3) network.


    :param str l3_network_name: The name of the L3 network.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
