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
    'GetPoolResult',
    'AwaitableGetPoolResult',
    'get_pool',
    'get_pool_output',
]

@pulumi.output_type
class GetPoolResult:
    """
    Pool resource
    """
    def __init__(__self__, assignments=None, id=None, location=None, name=None, pool_type=None, provisioning_state=None, reclaim_policy=None, resources=None, status=None, system_data=None, tags=None, type=None, zones=None):
        if assignments and not isinstance(assignments, list):
            raise TypeError("Expected argument 'assignments' to be a list")
        pulumi.set(__self__, "assignments", assignments)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pool_type and not isinstance(pool_type, dict):
            raise TypeError("Expected argument 'pool_type' to be a dict")
        pulumi.set(__self__, "pool_type", pool_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if reclaim_policy and not isinstance(reclaim_policy, str):
            raise TypeError("Expected argument 'reclaim_policy' to be a str")
        pulumi.set(__self__, "reclaim_policy", reclaim_policy)
        if resources and not isinstance(resources, dict):
            raise TypeError("Expected argument 'resources' to be a dict")
        pulumi.set(__self__, "resources", resources)
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
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def assignments(self) -> Optional[Sequence['outputs.AssignmentResponse']]:
        """
        List of resources that should have access to the pool. Typically ARM references to AKS clusters or ACI Container Groups. For local and standard this must be a single reference. For ElasticSAN there can be many.
        """
        return pulumi.get(self, "assignments")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="poolType")
    def pool_type(self) -> 'outputs.PoolTypeResponse':
        """
        Type of the Pool: ephemeralDisk, azureDisk, or elasticsan.
        """
        return pulumi.get(self, "pool_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="reclaimPolicy")
    def reclaim_policy(self) -> Optional[str]:
        """
        ReclaimPolicy defines what happens to the backend storage when StoragePool is deleted
        """
        return pulumi.get(self, "reclaim_policy")

    @property
    @pulumi.getter
    def resources(self) -> Optional['outputs.ResourcesResponse']:
        """
        Resources represent the resources the pool should have.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.ResourceOperationalStatusResponse':
        """
        The operational status of the resource
        """
        return pulumi.get(self, "status")

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
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        List of availability zones that resources can be created in.
        """
        return pulumi.get(self, "zones")


class AwaitableGetPoolResult(GetPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPoolResult(
            assignments=self.assignments,
            id=self.id,
            location=self.location,
            name=self.name,
            pool_type=self.pool_type,
            provisioning_state=self.provisioning_state,
            reclaim_policy=self.reclaim_policy,
            resources=self.resources,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            zones=self.zones)


def get_pool(pool_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPoolResult:
    """
    Get a Pool
    Azure REST API version: 2023-07-01-preview.


    :param str pool_name: Pool Object
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['poolName'] = pool_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerstorage:getPool', __args__, opts=opts, typ=GetPoolResult).value

    return AwaitableGetPoolResult(
        assignments=pulumi.get(__ret__, 'assignments'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        pool_type=pulumi.get(__ret__, 'pool_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        reclaim_policy=pulumi.get(__ret__, 'reclaim_policy'),
        resources=pulumi.get(__ret__, 'resources'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        zones=pulumi.get(__ret__, 'zones'))


@_utilities.lift_output_func(get_pool)
def get_pool_output(pool_name: Optional[pulumi.Input[str]] = None,
                    resource_group_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPoolResult]:
    """
    Get a Pool
    Azure REST API version: 2023-07-01-preview.


    :param str pool_name: Pool Object
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
