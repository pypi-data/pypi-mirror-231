# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'DatabasePropertiesGeoReplicationArgs',
    'EnterpriseSkuArgs',
    'LinkedDatabaseArgs',
    'ModuleArgs',
    'PersistenceArgs',
    'PrivateLinkServiceConnectionStateArgs',
]

@pulumi.input_type
class DatabasePropertiesGeoReplicationArgs:
    def __init__(__self__, *,
                 group_nickname: Optional[pulumi.Input[str]] = None,
                 linked_databases: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatabaseArgs']]]] = None):
        """
        Optional set of properties to configure geo replication for this database.
        :param pulumi.Input[str] group_nickname: Name for the group of linked database resources
        :param pulumi.Input[Sequence[pulumi.Input['LinkedDatabaseArgs']]] linked_databases: List of database resources to link with this database
        """
        if group_nickname is not None:
            pulumi.set(__self__, "group_nickname", group_nickname)
        if linked_databases is not None:
            pulumi.set(__self__, "linked_databases", linked_databases)

    @property
    @pulumi.getter(name="groupNickname")
    def group_nickname(self) -> Optional[pulumi.Input[str]]:
        """
        Name for the group of linked database resources
        """
        return pulumi.get(self, "group_nickname")

    @group_nickname.setter
    def group_nickname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_nickname", value)

    @property
    @pulumi.getter(name="linkedDatabases")
    def linked_databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatabaseArgs']]]]:
        """
        List of database resources to link with this database
        """
        return pulumi.get(self, "linked_databases")

    @linked_databases.setter
    def linked_databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatabaseArgs']]]]):
        pulumi.set(self, "linked_databases", value)


@pulumi.input_type
class EnterpriseSkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'SkuName']],
                 capacity: Optional[pulumi.Input[int]] = None):
        """
        SKU parameters supplied to the create RedisEnterprise operation.
        :param pulumi.Input[Union[str, 'SkuName']] name: The type of RedisEnterprise cluster to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)
        :param pulumi.Input[int] capacity: The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'SkuName']]:
        """
        The type of RedisEnterprise cluster to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'SkuName']]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)


@pulumi.input_type
class LinkedDatabaseArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        Specifies details of a linked database resource.
        :param pulumi.Input[str] id: Resource ID of a database resource to link with this database.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID of a database resource to link with this database.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class ModuleArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 args: Optional[pulumi.Input[str]] = None):
        """
        Specifies configuration of a redis module
        :param pulumi.Input[str] name: The name of the module, e.g. 'RedisBloom', 'RediSearch', 'RedisTimeSeries'
        :param pulumi.Input[str] args: Configuration options for the module, e.g. 'ERROR_RATE 0.01 INITIAL_SIZE 400'.
        """
        pulumi.set(__self__, "name", name)
        if args is not None:
            pulumi.set(__self__, "args", args)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the module, e.g. 'RedisBloom', 'RediSearch', 'RedisTimeSeries'
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[str]]:
        """
        Configuration options for the module, e.g. 'ERROR_RATE 0.01 INITIAL_SIZE 400'.
        """
        return pulumi.get(self, "args")

    @args.setter
    def args(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "args", value)


@pulumi.input_type
class PersistenceArgs:
    def __init__(__self__, *,
                 aof_enabled: Optional[pulumi.Input[bool]] = None,
                 aof_frequency: Optional[pulumi.Input[Union[str, 'AofFrequency']]] = None,
                 rdb_enabled: Optional[pulumi.Input[bool]] = None,
                 rdb_frequency: Optional[pulumi.Input[Union[str, 'RdbFrequency']]] = None):
        """
        Persistence-related configuration for the RedisEnterprise database
        :param pulumi.Input[bool] aof_enabled: Sets whether AOF is enabled.
        :param pulumi.Input[Union[str, 'AofFrequency']] aof_frequency: Sets the frequency at which data is written to disk.
        :param pulumi.Input[bool] rdb_enabled: Sets whether RDB is enabled.
        :param pulumi.Input[Union[str, 'RdbFrequency']] rdb_frequency: Sets the frequency at which a snapshot of the database is created.
        """
        if aof_enabled is not None:
            pulumi.set(__self__, "aof_enabled", aof_enabled)
        if aof_frequency is not None:
            pulumi.set(__self__, "aof_frequency", aof_frequency)
        if rdb_enabled is not None:
            pulumi.set(__self__, "rdb_enabled", rdb_enabled)
        if rdb_frequency is not None:
            pulumi.set(__self__, "rdb_frequency", rdb_frequency)

    @property
    @pulumi.getter(name="aofEnabled")
    def aof_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Sets whether AOF is enabled.
        """
        return pulumi.get(self, "aof_enabled")

    @aof_enabled.setter
    def aof_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "aof_enabled", value)

    @property
    @pulumi.getter(name="aofFrequency")
    def aof_frequency(self) -> Optional[pulumi.Input[Union[str, 'AofFrequency']]]:
        """
        Sets the frequency at which data is written to disk.
        """
        return pulumi.get(self, "aof_frequency")

    @aof_frequency.setter
    def aof_frequency(self, value: Optional[pulumi.Input[Union[str, 'AofFrequency']]]):
        pulumi.set(self, "aof_frequency", value)

    @property
    @pulumi.getter(name="rdbEnabled")
    def rdb_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Sets whether RDB is enabled.
        """
        return pulumi.get(self, "rdb_enabled")

    @rdb_enabled.setter
    def rdb_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "rdb_enabled", value)

    @property
    @pulumi.getter(name="rdbFrequency")
    def rdb_frequency(self) -> Optional[pulumi.Input[Union[str, 'RdbFrequency']]]:
        """
        Sets the frequency at which a snapshot of the database is created.
        """
        return pulumi.get(self, "rdb_frequency")

    @rdb_frequency.setter
    def rdb_frequency(self, value: Optional[pulumi.Input[Union[str, 'RdbFrequency']]]):
        pulumi.set(self, "rdb_frequency", value)


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param pulumi.Input[str] description: The reason for approval/rejection of the connection.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[str]]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


