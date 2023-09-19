# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListDatabaseKeysResult',
    'AwaitableListDatabaseKeysResult',
    'list_database_keys',
    'list_database_keys_output',
]

@pulumi.output_type
class ListDatabaseKeysResult:
    """
    The secret access keys used for authenticating connections to redis
    """
    def __init__(__self__, primary_key=None, secondary_key=None):
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> str:
        """
        The current primary key that clients can use to authenticate
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> str:
        """
        The current secondary key that clients can use to authenticate
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListDatabaseKeysResult(ListDatabaseKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDatabaseKeysResult(
            primary_key=self.primary_key,
            secondary_key=self.secondary_key)


def list_database_keys(cluster_name: Optional[str] = None,
                       database_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDatabaseKeysResult:
    """
    Retrieves the access keys for the RedisEnterprise database.


    :param str cluster_name: The name of the RedisEnterprise cluster.
    :param str database_name: The name of the database.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cache/v20230701:listDatabaseKeys', __args__, opts=opts, typ=ListDatabaseKeysResult).value

    return AwaitableListDatabaseKeysResult(
        primary_key=pulumi.get(__ret__, 'primary_key'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'))


@_utilities.lift_output_func(list_database_keys)
def list_database_keys_output(cluster_name: Optional[pulumi.Input[str]] = None,
                              database_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDatabaseKeysResult]:
    """
    Retrieves the access keys for the RedisEnterprise database.


    :param str cluster_name: The name of the RedisEnterprise cluster.
    :param str database_name: The name of the database.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
