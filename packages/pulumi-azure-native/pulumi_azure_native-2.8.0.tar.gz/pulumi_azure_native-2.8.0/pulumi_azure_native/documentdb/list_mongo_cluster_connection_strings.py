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
    'ListMongoClusterConnectionStringsResult',
    'AwaitableListMongoClusterConnectionStringsResult',
    'list_mongo_cluster_connection_strings',
    'list_mongo_cluster_connection_strings_output',
]

@pulumi.output_type
class ListMongoClusterConnectionStringsResult:
    """
    The connection strings for the given mongo cluster.
    """
    def __init__(__self__, connection_strings=None):
        if connection_strings and not isinstance(connection_strings, list):
            raise TypeError("Expected argument 'connection_strings' to be a list")
        pulumi.set(__self__, "connection_strings", connection_strings)

    @property
    @pulumi.getter(name="connectionStrings")
    def connection_strings(self) -> Sequence['outputs.ConnectionStringResponse']:
        """
        An array that contains the connection strings for a mongo cluster.
        """
        return pulumi.get(self, "connection_strings")


class AwaitableListMongoClusterConnectionStringsResult(ListMongoClusterConnectionStringsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListMongoClusterConnectionStringsResult(
            connection_strings=self.connection_strings)


def list_mongo_cluster_connection_strings(mongo_cluster_name: Optional[str] = None,
                                          resource_group_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListMongoClusterConnectionStringsResult:
    """
    List mongo cluster connection strings. This includes the default connection string using SCRAM-SHA-256, as well as other connection strings supported by the cluster.
    Azure REST API version: 2023-03-15-preview.


    :param str mongo_cluster_name: The name of the mongo cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['mongoClusterName'] = mongo_cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb:listMongoClusterConnectionStrings', __args__, opts=opts, typ=ListMongoClusterConnectionStringsResult).value

    return AwaitableListMongoClusterConnectionStringsResult(
        connection_strings=pulumi.get(__ret__, 'connection_strings'))


@_utilities.lift_output_func(list_mongo_cluster_connection_strings)
def list_mongo_cluster_connection_strings_output(mongo_cluster_name: Optional[pulumi.Input[str]] = None,
                                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListMongoClusterConnectionStringsResult]:
    """
    List mongo cluster connection strings. This includes the default connection string using SCRAM-SHA-256, as well as other connection strings supported by the cluster.
    Azure REST API version: 2023-03-15-preview.


    :param str mongo_cluster_name: The name of the mongo cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
