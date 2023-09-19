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
    'GetReadWriteDatabaseResult',
    'AwaitableGetReadWriteDatabaseResult',
    'get_read_write_database',
    'get_read_write_database_output',
]

@pulumi.output_type
class GetReadWriteDatabaseResult:
    """
    Class representing a read write database.
    """
    def __init__(__self__, hot_cache_period=None, id=None, is_followed=None, kind=None, location=None, name=None, provisioning_state=None, soft_delete_period=None, statistics=None, system_data=None, type=None):
        if hot_cache_period and not isinstance(hot_cache_period, str):
            raise TypeError("Expected argument 'hot_cache_period' to be a str")
        pulumi.set(__self__, "hot_cache_period", hot_cache_period)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_followed and not isinstance(is_followed, bool):
            raise TypeError("Expected argument 'is_followed' to be a bool")
        pulumi.set(__self__, "is_followed", is_followed)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if soft_delete_period and not isinstance(soft_delete_period, str):
            raise TypeError("Expected argument 'soft_delete_period' to be a str")
        pulumi.set(__self__, "soft_delete_period", soft_delete_period)
        if statistics and not isinstance(statistics, dict):
            raise TypeError("Expected argument 'statistics' to be a dict")
        pulumi.set(__self__, "statistics", statistics)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="hotCachePeriod")
    def hot_cache_period(self) -> Optional[str]:
        """
        The time the data should be kept in cache for fast queries in TimeSpan.
        """
        return pulumi.get(self, "hot_cache_period")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isFollowed")
    def is_followed(self) -> bool:
        """
        Indicates whether the database is followed.
        """
        return pulumi.get(self, "is_followed")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of the database
        Expected value is 'ReadWrite'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
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
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="softDeletePeriod")
    def soft_delete_period(self) -> Optional[str]:
        """
        The time the data should be kept before it stops being accessible to queries in TimeSpan.
        """
        return pulumi.get(self, "soft_delete_period")

    @property
    @pulumi.getter
    def statistics(self) -> 'outputs.DatabaseStatisticsResponse':
        """
        The statistics of the database.
        """
        return pulumi.get(self, "statistics")

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


class AwaitableGetReadWriteDatabaseResult(GetReadWriteDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReadWriteDatabaseResult(
            hot_cache_period=self.hot_cache_period,
            id=self.id,
            is_followed=self.is_followed,
            kind=self.kind,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            soft_delete_period=self.soft_delete_period,
            statistics=self.statistics,
            system_data=self.system_data,
            type=self.type)


def get_read_write_database(database_name: Optional[str] = None,
                            kusto_pool_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            workspace_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReadWriteDatabaseResult:
    """
    Returns a database.
    Azure REST API version: 2021-06-01-preview.


    :param str database_name: The name of the database in the Kusto pool.
    :param str kusto_pool_name: The name of the Kusto pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['kustoPoolName'] = kusto_pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:synapse:getReadWriteDatabase', __args__, opts=opts, typ=GetReadWriteDatabaseResult).value

    return AwaitableGetReadWriteDatabaseResult(
        hot_cache_period=pulumi.get(__ret__, 'hot_cache_period'),
        id=pulumi.get(__ret__, 'id'),
        is_followed=pulumi.get(__ret__, 'is_followed'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        soft_delete_period=pulumi.get(__ret__, 'soft_delete_period'),
        statistics=pulumi.get(__ret__, 'statistics'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_read_write_database)
def get_read_write_database_output(database_name: Optional[pulumi.Input[str]] = None,
                                   kusto_pool_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   workspace_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReadWriteDatabaseResult]:
    """
    Returns a database.
    Azure REST API version: 2021-06-01-preview.


    :param str database_name: The name of the database in the Kusto pool.
    :param str kusto_pool_name: The name of the Kusto pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
