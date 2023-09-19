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
    'GetServerGroupResult',
    'AwaitableGetServerGroupResult',
    'get_server_group',
    'get_server_group_output',
]

@pulumi.output_type
class GetServerGroupResult:
    """
    Represents a server group for create.
    """
    def __init__(__self__, administrator_login=None, availability_zone=None, backup_retention_days=None, citus_version=None, delegated_subnet_arguments=None, earliest_restore_time=None, enable_mx=None, enable_shards_on_coordinator=None, enable_zfs=None, id=None, location=None, maintenance_window=None, name=None, postgresql_version=None, private_dns_zone_arguments=None, read_replicas=None, resource_provider_type=None, server_role_groups=None, source_server_group=None, standby_availability_zone=None, state=None, system_data=None, tags=None, type=None):
        if administrator_login and not isinstance(administrator_login, str):
            raise TypeError("Expected argument 'administrator_login' to be a str")
        pulumi.set(__self__, "administrator_login", administrator_login)
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if backup_retention_days and not isinstance(backup_retention_days, int):
            raise TypeError("Expected argument 'backup_retention_days' to be a int")
        pulumi.set(__self__, "backup_retention_days", backup_retention_days)
        if citus_version and not isinstance(citus_version, str):
            raise TypeError("Expected argument 'citus_version' to be a str")
        pulumi.set(__self__, "citus_version", citus_version)
        if delegated_subnet_arguments and not isinstance(delegated_subnet_arguments, dict):
            raise TypeError("Expected argument 'delegated_subnet_arguments' to be a dict")
        pulumi.set(__self__, "delegated_subnet_arguments", delegated_subnet_arguments)
        if earliest_restore_time and not isinstance(earliest_restore_time, str):
            raise TypeError("Expected argument 'earliest_restore_time' to be a str")
        pulumi.set(__self__, "earliest_restore_time", earliest_restore_time)
        if enable_mx and not isinstance(enable_mx, bool):
            raise TypeError("Expected argument 'enable_mx' to be a bool")
        pulumi.set(__self__, "enable_mx", enable_mx)
        if enable_shards_on_coordinator and not isinstance(enable_shards_on_coordinator, bool):
            raise TypeError("Expected argument 'enable_shards_on_coordinator' to be a bool")
        pulumi.set(__self__, "enable_shards_on_coordinator", enable_shards_on_coordinator)
        if enable_zfs and not isinstance(enable_zfs, bool):
            raise TypeError("Expected argument 'enable_zfs' to be a bool")
        pulumi.set(__self__, "enable_zfs", enable_zfs)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_window and not isinstance(maintenance_window, dict):
            raise TypeError("Expected argument 'maintenance_window' to be a dict")
        pulumi.set(__self__, "maintenance_window", maintenance_window)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if postgresql_version and not isinstance(postgresql_version, str):
            raise TypeError("Expected argument 'postgresql_version' to be a str")
        pulumi.set(__self__, "postgresql_version", postgresql_version)
        if private_dns_zone_arguments and not isinstance(private_dns_zone_arguments, dict):
            raise TypeError("Expected argument 'private_dns_zone_arguments' to be a dict")
        pulumi.set(__self__, "private_dns_zone_arguments", private_dns_zone_arguments)
        if read_replicas and not isinstance(read_replicas, list):
            raise TypeError("Expected argument 'read_replicas' to be a list")
        pulumi.set(__self__, "read_replicas", read_replicas)
        if resource_provider_type and not isinstance(resource_provider_type, str):
            raise TypeError("Expected argument 'resource_provider_type' to be a str")
        pulumi.set(__self__, "resource_provider_type", resource_provider_type)
        if server_role_groups and not isinstance(server_role_groups, list):
            raise TypeError("Expected argument 'server_role_groups' to be a list")
        pulumi.set(__self__, "server_role_groups", server_role_groups)
        if source_server_group and not isinstance(source_server_group, str):
            raise TypeError("Expected argument 'source_server_group' to be a str")
        pulumi.set(__self__, "source_server_group", source_server_group)
        if standby_availability_zone and not isinstance(standby_availability_zone, str):
            raise TypeError("Expected argument 'standby_availability_zone' to be a str")
        pulumi.set(__self__, "standby_availability_zone", standby_availability_zone)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
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
        The administrator's login name of servers in server group. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        """
        Availability Zone information of the server group.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[int]:
        """
        The backup retention days for server group.
        """
        return pulumi.get(self, "backup_retention_days")

    @property
    @pulumi.getter(name="citusVersion")
    def citus_version(self) -> Optional[str]:
        """
        The Citus version of server group.
        """
        return pulumi.get(self, "citus_version")

    @property
    @pulumi.getter(name="delegatedSubnetArguments")
    def delegated_subnet_arguments(self) -> Optional['outputs.ServerGroupPropertiesResponseDelegatedSubnetArguments']:
        """
        The delegated subnet arguments for a server group.
        """
        return pulumi.get(self, "delegated_subnet_arguments")

    @property
    @pulumi.getter(name="earliestRestoreTime")
    def earliest_restore_time(self) -> str:
        """
        The earliest restore point time (ISO8601 format) for server group.
        """
        return pulumi.get(self, "earliest_restore_time")

    @property
    @pulumi.getter(name="enableMx")
    def enable_mx(self) -> Optional[bool]:
        """
        If Citus MX is enabled or not for the server group.
        """
        return pulumi.get(self, "enable_mx")

    @property
    @pulumi.getter(name="enableShardsOnCoordinator")
    def enable_shards_on_coordinator(self) -> Optional[bool]:
        """
        If shards on coordinator is enabled or not for the server group.
        """
        return pulumi.get(self, "enable_shards_on_coordinator")

    @property
    @pulumi.getter(name="enableZfs")
    def enable_zfs(self) -> Optional[bool]:
        """
        If ZFS compression is enabled or not for the server group.
        """
        return pulumi.get(self, "enable_zfs")

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
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional['outputs.MaintenanceWindowResponse']:
        """
        Maintenance window of a server group.
        """
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="postgresqlVersion")
    def postgresql_version(self) -> Optional[str]:
        """
        The PostgreSQL version of server group.
        """
        return pulumi.get(self, "postgresql_version")

    @property
    @pulumi.getter(name="privateDnsZoneArguments")
    def private_dns_zone_arguments(self) -> Optional['outputs.ServerGroupPropertiesResponsePrivateDnsZoneArguments']:
        """
        The private dns zone arguments for a server group.
        """
        return pulumi.get(self, "private_dns_zone_arguments")

    @property
    @pulumi.getter(name="readReplicas")
    def read_replicas(self) -> Sequence[str]:
        """
        The array of read replica server groups.
        """
        return pulumi.get(self, "read_replicas")

    @property
    @pulumi.getter(name="resourceProviderType")
    def resource_provider_type(self) -> str:
        """
        The resource provider type of server group.
        """
        return pulumi.get(self, "resource_provider_type")

    @property
    @pulumi.getter(name="serverRoleGroups")
    def server_role_groups(self) -> Optional[Sequence['outputs.ServerRoleGroupResponse']]:
        """
        The list of server role groups.
        """
        return pulumi.get(self, "server_role_groups")

    @property
    @pulumi.getter(name="sourceServerGroup")
    def source_server_group(self) -> str:
        """
        The source server group id for read replica server groups.
        """
        return pulumi.get(self, "source_server_group")

    @property
    @pulumi.getter(name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> Optional[str]:
        """
        Standby Availability Zone information of the server group.
        """
        return pulumi.get(self, "standby_availability_zone")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        A state of a server group that is visible to user.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource
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


class AwaitableGetServerGroupResult(GetServerGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerGroupResult(
            administrator_login=self.administrator_login,
            availability_zone=self.availability_zone,
            backup_retention_days=self.backup_retention_days,
            citus_version=self.citus_version,
            delegated_subnet_arguments=self.delegated_subnet_arguments,
            earliest_restore_time=self.earliest_restore_time,
            enable_mx=self.enable_mx,
            enable_shards_on_coordinator=self.enable_shards_on_coordinator,
            enable_zfs=self.enable_zfs,
            id=self.id,
            location=self.location,
            maintenance_window=self.maintenance_window,
            name=self.name,
            postgresql_version=self.postgresql_version,
            private_dns_zone_arguments=self.private_dns_zone_arguments,
            read_replicas=self.read_replicas,
            resource_provider_type=self.resource_provider_type,
            server_role_groups=self.server_role_groups,
            source_server_group=self.source_server_group,
            standby_availability_zone=self.standby_availability_zone,
            state=self.state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_server_group(resource_group_name: Optional[str] = None,
                     server_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerGroupResult:
    """
    Gets information about a server group.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_group_name: The name of the server group.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverGroupName'] = server_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbforpostgresql/v20201005privatepreview:getServerGroup', __args__, opts=opts, typ=GetServerGroupResult).value

    return AwaitableGetServerGroupResult(
        administrator_login=pulumi.get(__ret__, 'administrator_login'),
        availability_zone=pulumi.get(__ret__, 'availability_zone'),
        backup_retention_days=pulumi.get(__ret__, 'backup_retention_days'),
        citus_version=pulumi.get(__ret__, 'citus_version'),
        delegated_subnet_arguments=pulumi.get(__ret__, 'delegated_subnet_arguments'),
        earliest_restore_time=pulumi.get(__ret__, 'earliest_restore_time'),
        enable_mx=pulumi.get(__ret__, 'enable_mx'),
        enable_shards_on_coordinator=pulumi.get(__ret__, 'enable_shards_on_coordinator'),
        enable_zfs=pulumi.get(__ret__, 'enable_zfs'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_window=pulumi.get(__ret__, 'maintenance_window'),
        name=pulumi.get(__ret__, 'name'),
        postgresql_version=pulumi.get(__ret__, 'postgresql_version'),
        private_dns_zone_arguments=pulumi.get(__ret__, 'private_dns_zone_arguments'),
        read_replicas=pulumi.get(__ret__, 'read_replicas'),
        resource_provider_type=pulumi.get(__ret__, 'resource_provider_type'),
        server_role_groups=pulumi.get(__ret__, 'server_role_groups'),
        source_server_group=pulumi.get(__ret__, 'source_server_group'),
        standby_availability_zone=pulumi.get(__ret__, 'standby_availability_zone'),
        state=pulumi.get(__ret__, 'state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_server_group)
def get_server_group_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                            server_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerGroupResult]:
    """
    Gets information about a server group.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_group_name: The name of the server group.
    """
    ...
