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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    """
    A Stream Analytics Cluster object
    """
    def __init__(__self__, capacity_allocated=None, capacity_assigned=None, cluster_id=None, created_date=None, etag=None, id=None, location=None, name=None, provisioning_state=None, sku=None, tags=None, type=None):
        if capacity_allocated and not isinstance(capacity_allocated, int):
            raise TypeError("Expected argument 'capacity_allocated' to be a int")
        pulumi.set(__self__, "capacity_allocated", capacity_allocated)
        if capacity_assigned and not isinstance(capacity_assigned, int):
            raise TypeError("Expected argument 'capacity_assigned' to be a int")
        pulumi.set(__self__, "capacity_assigned", capacity_assigned)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="capacityAllocated")
    def capacity_allocated(self) -> int:
        """
        Represents the number of streaming units currently being used on the cluster.
        """
        return pulumi.get(self, "capacity_allocated")

    @property
    @pulumi.getter(name="capacityAssigned")
    def capacity_assigned(self) -> int:
        """
        Represents the sum of the SUs of all streaming jobs associated with the cluster. If all of the jobs were running, this would be the capacity allocated.
        """
        return pulumi.get(self, "capacity_assigned")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        Unique identifier for the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        """
        The date this cluster was created.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The current entity tag for the cluster. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
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
        The status of the cluster provisioning. The three terminal states are: Succeeded, Failed and Canceled
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.ClusterSkuResponse']:
        """
        The SKU of the cluster. This determines the size/capacity of the cluster. Required on PUT (CreateOrUpdate) requests.
        """
        return pulumi.get(self, "sku")

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
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            capacity_allocated=self.capacity_allocated,
            capacity_assigned=self.capacity_assigned,
            cluster_id=self.cluster_id,
            created_date=self.created_date,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            tags=self.tags,
            type=self.type)


def get_cluster(cluster_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Gets information about the specified cluster.
    Azure REST API version: 2020-03-01.


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:streamanalytics:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        capacity_allocated=pulumi.get(__ret__, 'capacity_allocated'),
        capacity_assigned=pulumi.get(__ret__, 'capacity_assigned'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        created_date=pulumi.get(__ret__, 'created_date'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        sku=pulumi.get(__ret__, 'sku'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(cluster_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    Gets information about the specified cluster.
    Azure REST API version: 2020-03-01.


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
