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
    'GetMongoClusterResult',
    'AwaitableGetMongoClusterResult',
    'get_mongo_cluster',
    'get_mongo_cluster_output',
]

@pulumi.output_type
class GetMongoClusterResult:
    """
    Represents a mongo cluster resource.
    """
    def __init__(__self__, administrator_login=None, cluster_status=None, connection_string=None, earliest_restore_time=None, id=None, location=None, name=None, node_group_specs=None, provisioning_state=None, server_version=None, system_data=None, tags=None, type=None):
        if administrator_login and not isinstance(administrator_login, str):
            raise TypeError("Expected argument 'administrator_login' to be a str")
        pulumi.set(__self__, "administrator_login", administrator_login)
        if cluster_status and not isinstance(cluster_status, str):
            raise TypeError("Expected argument 'cluster_status' to be a str")
        pulumi.set(__self__, "cluster_status", cluster_status)
        if connection_string and not isinstance(connection_string, str):
            raise TypeError("Expected argument 'connection_string' to be a str")
        pulumi.set(__self__, "connection_string", connection_string)
        if earliest_restore_time and not isinstance(earliest_restore_time, str):
            raise TypeError("Expected argument 'earliest_restore_time' to be a str")
        pulumi.set(__self__, "earliest_restore_time", earliest_restore_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_group_specs and not isinstance(node_group_specs, list):
            raise TypeError("Expected argument 'node_group_specs' to be a list")
        pulumi.set(__self__, "node_group_specs", node_group_specs)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if server_version and not isinstance(server_version, str):
            raise TypeError("Expected argument 'server_version' to be a str")
        pulumi.set(__self__, "server_version", server_version)
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
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[str]:
        """
        The administrator's login for the mongo cluster.
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="clusterStatus")
    def cluster_status(self) -> str:
        """
        A status of the mongo cluster.
        """
        return pulumi.get(self, "cluster_status")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> str:
        """
        The default mongo connection string for the cluster.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="earliestRestoreTime")
    def earliest_restore_time(self) -> str:
        """
        Earliest restore timestamp in UTC ISO8601 format.
        """
        return pulumi.get(self, "earliest_restore_time")

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
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeGroupSpecs")
    def node_group_specs(self) -> Optional[Sequence['outputs.NodeGroupSpecResponse']]:
        """
        The list of node group specs in the cluster.
        """
        return pulumi.get(self, "node_group_specs")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        A provisioning state of the mongo cluster.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[str]:
        """
        The Mongo DB server version. Defaults to the latest available version if not specified.
        """
        return pulumi.get(self, "server_version")

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


class AwaitableGetMongoClusterResult(GetMongoClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMongoClusterResult(
            administrator_login=self.administrator_login,
            cluster_status=self.cluster_status,
            connection_string=self.connection_string,
            earliest_restore_time=self.earliest_restore_time,
            id=self.id,
            location=self.location,
            name=self.name,
            node_group_specs=self.node_group_specs,
            provisioning_state=self.provisioning_state,
            server_version=self.server_version,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_mongo_cluster(mongo_cluster_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMongoClusterResult:
    """
    Gets information about a mongo cluster.
    Azure REST API version: 2023-03-15-preview.


    :param str mongo_cluster_name: The name of the mongo cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['mongoClusterName'] = mongo_cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb:getMongoCluster', __args__, opts=opts, typ=GetMongoClusterResult).value

    return AwaitableGetMongoClusterResult(
        administrator_login=pulumi.get(__ret__, 'administrator_login'),
        cluster_status=pulumi.get(__ret__, 'cluster_status'),
        connection_string=pulumi.get(__ret__, 'connection_string'),
        earliest_restore_time=pulumi.get(__ret__, 'earliest_restore_time'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        node_group_specs=pulumi.get(__ret__, 'node_group_specs'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        server_version=pulumi.get(__ret__, 'server_version'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_mongo_cluster)
def get_mongo_cluster_output(mongo_cluster_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMongoClusterResult]:
    """
    Gets information about a mongo cluster.
    Azure REST API version: 2023-03-15-preview.


    :param str mongo_cluster_name: The name of the mongo cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
