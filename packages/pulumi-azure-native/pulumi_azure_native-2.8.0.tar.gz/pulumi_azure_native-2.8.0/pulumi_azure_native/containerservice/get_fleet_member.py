# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetFleetMemberResult',
    'AwaitableGetFleetMemberResult',
    'get_fleet_member',
    'get_fleet_member_output',
]

@pulumi.output_type
class GetFleetMemberResult:
    """
    A member of the Fleet. It contains a reference to an existing Kubernetes cluster on Azure.
    """
    def __init__(__self__, cluster_resource_id=None, e_tag=None, group=None, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if cluster_resource_id and not isinstance(cluster_resource_id, str):
            raise TypeError("Expected argument 'cluster_resource_id' to be a str")
        pulumi.set(__self__, "cluster_resource_id", cluster_resource_id)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if group and not isinstance(group, str):
            raise TypeError("Expected argument 'group' to be a str")
        pulumi.set(__self__, "group", group)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> str:
        """
        The ARM resource id of the cluster that joins the Fleet. Must be a valid Azure resource id. e.g.: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{clusterName}'.
        """
        return pulumi.get(self, "cluster_resource_id")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> str:
        """
        If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def group(self) -> Optional[str]:
        """
        The group this member belongs to for multi-cluster update management.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

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
        The status of the last operation.
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
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetFleetMemberResult(GetFleetMemberResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFleetMemberResult(
            cluster_resource_id=self.cluster_resource_id,
            e_tag=self.e_tag,
            group=self.group,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_fleet_member(fleet_member_name: Optional[str] = None,
                     fleet_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFleetMemberResult:
    """
    Get a FleetMember
    Azure REST API version: 2023-03-15-preview.


    :param str fleet_member_name: The name of the Fleet member resource.
    :param str fleet_name: The name of the Fleet resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['fleetMemberName'] = fleet_member_name
    __args__['fleetName'] = fleet_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice:getFleetMember', __args__, opts=opts, typ=GetFleetMemberResult).value

    return AwaitableGetFleetMemberResult(
        cluster_resource_id=pulumi.get(__ret__, 'cluster_resource_id'),
        e_tag=pulumi.get(__ret__, 'e_tag'),
        group=pulumi.get(__ret__, 'group'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_fleet_member)
def get_fleet_member_output(fleet_member_name: Optional[pulumi.Input[str]] = None,
                            fleet_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFleetMemberResult]:
    """
    Get a FleetMember
    Azure REST API version: 2023-03-15-preview.


    :param str fleet_member_name: The name of the Fleet member resource.
    :param str fleet_name: The name of the Fleet resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
