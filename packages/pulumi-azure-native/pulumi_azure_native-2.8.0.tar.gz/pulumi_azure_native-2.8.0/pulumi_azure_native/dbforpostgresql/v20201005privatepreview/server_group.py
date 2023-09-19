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
from ._enums import *
from ._inputs import *

__all__ = ['ServerGroupArgs', 'ServerGroup']

@pulumi.input_type
class ServerGroupArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 backup_retention_days: Optional[pulumi.Input[int]] = None,
                 citus_version: Optional[pulumi.Input[Union[str, 'CitusVersion']]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 delegated_subnet_arguments: Optional[pulumi.Input['ServerGroupPropertiesDelegatedSubnetArgumentsArgs']] = None,
                 enable_mx: Optional[pulumi.Input[bool]] = None,
                 enable_shards_on_coordinator: Optional[pulumi.Input[bool]] = None,
                 enable_zfs: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input['MaintenanceWindowArgs']] = None,
                 point_in_time_utc: Optional[pulumi.Input[str]] = None,
                 postgresql_version: Optional[pulumi.Input[Union[str, 'PostgreSQLVersion']]] = None,
                 private_dns_zone_arguments: Optional[pulumi.Input['ServerGroupPropertiesPrivateDnsZoneArgumentsArgs']] = None,
                 server_group_name: Optional[pulumi.Input[str]] = None,
                 server_role_groups: Optional[pulumi.Input[Sequence[pulumi.Input['ServerRoleGroupArgs']]]] = None,
                 source_location: Optional[pulumi.Input[str]] = None,
                 source_resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_server_group_name: Optional[pulumi.Input[str]] = None,
                 source_subscription_id: Optional[pulumi.Input[str]] = None,
                 standby_availability_zone: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ServerGroup resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] administrator_login: The administrator's login name of servers in server group. Can only be specified when the server is being created (and is required for creation).
        :param pulumi.Input[str] administrator_login_password: The password of the administrator login.
        :param pulumi.Input[str] availability_zone: Availability Zone information of the server group.
        :param pulumi.Input[int] backup_retention_days: The backup retention days for server group.
        :param pulumi.Input[Union[str, 'CitusVersion']] citus_version: The Citus version of server group.
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: The mode to create a new server group.
        :param pulumi.Input['ServerGroupPropertiesDelegatedSubnetArgumentsArgs'] delegated_subnet_arguments: The delegated subnet arguments for a server group.
        :param pulumi.Input[bool] enable_mx: If Citus MX is enabled or not for the server group.
        :param pulumi.Input[bool] enable_shards_on_coordinator: If shards on coordinator is enabled or not for the server group.
        :param pulumi.Input[bool] enable_zfs: If ZFS compression is enabled or not for the server group.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['MaintenanceWindowArgs'] maintenance_window: Maintenance window of a server group.
        :param pulumi.Input[str] point_in_time_utc: Restore point creation time (ISO8601 format), specifying the time to restore from. It's required when 'createMode' is 'PointInTimeRestore'
        :param pulumi.Input[Union[str, 'PostgreSQLVersion']] postgresql_version: The PostgreSQL version of server group.
        :param pulumi.Input['ServerGroupPropertiesPrivateDnsZoneArgumentsArgs'] private_dns_zone_arguments: The private dns zone arguments for a server group.
        :param pulumi.Input[str] server_group_name: The name of the server group.
        :param pulumi.Input[Sequence[pulumi.Input['ServerRoleGroupArgs']]] server_role_groups: The list of server role groups.
        :param pulumi.Input[str] source_location: The source server group location to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        :param pulumi.Input[str] source_resource_group_name: The source resource group name to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        :param pulumi.Input[str] source_server_group_name: The source server group name to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        :param pulumi.Input[str] source_subscription_id: The source subscription id to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        :param pulumi.Input[str] standby_availability_zone: Standby Availability Zone information of the server group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if administrator_login is not None:
            pulumi.set(__self__, "administrator_login", administrator_login)
        if administrator_login_password is not None:
            pulumi.set(__self__, "administrator_login_password", administrator_login_password)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if backup_retention_days is not None:
            pulumi.set(__self__, "backup_retention_days", backup_retention_days)
        if citus_version is not None:
            pulumi.set(__self__, "citus_version", citus_version)
        if create_mode is not None:
            pulumi.set(__self__, "create_mode", create_mode)
        if delegated_subnet_arguments is not None:
            pulumi.set(__self__, "delegated_subnet_arguments", delegated_subnet_arguments)
        if enable_mx is not None:
            pulumi.set(__self__, "enable_mx", enable_mx)
        if enable_shards_on_coordinator is not None:
            pulumi.set(__self__, "enable_shards_on_coordinator", enable_shards_on_coordinator)
        if enable_zfs is not None:
            pulumi.set(__self__, "enable_zfs", enable_zfs)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if maintenance_window is not None:
            pulumi.set(__self__, "maintenance_window", maintenance_window)
        if point_in_time_utc is not None:
            pulumi.set(__self__, "point_in_time_utc", point_in_time_utc)
        if postgresql_version is not None:
            pulumi.set(__self__, "postgresql_version", postgresql_version)
        if private_dns_zone_arguments is not None:
            pulumi.set(__self__, "private_dns_zone_arguments", private_dns_zone_arguments)
        if server_group_name is not None:
            pulumi.set(__self__, "server_group_name", server_group_name)
        if server_role_groups is not None:
            pulumi.set(__self__, "server_role_groups", server_role_groups)
        if source_location is not None:
            pulumi.set(__self__, "source_location", source_location)
        if source_resource_group_name is not None:
            pulumi.set(__self__, "source_resource_group_name", source_resource_group_name)
        if source_server_group_name is not None:
            pulumi.set(__self__, "source_server_group_name", source_server_group_name)
        if source_subscription_id is not None:
            pulumi.set(__self__, "source_subscription_id", source_subscription_id)
        if standby_availability_zone is not None:
            pulumi.set(__self__, "standby_availability_zone", standby_availability_zone)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[pulumi.Input[str]]:
        """
        The administrator's login name of servers in server group. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @administrator_login.setter
    def administrator_login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_login", value)

    @property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the administrator login.
        """
        return pulumi.get(self, "administrator_login_password")

    @administrator_login_password.setter
    def administrator_login_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_login_password", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Availability Zone information of the server group.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[pulumi.Input[int]]:
        """
        The backup retention days for server group.
        """
        return pulumi.get(self, "backup_retention_days")

    @backup_retention_days.setter
    def backup_retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "backup_retention_days", value)

    @property
    @pulumi.getter(name="citusVersion")
    def citus_version(self) -> Optional[pulumi.Input[Union[str, 'CitusVersion']]]:
        """
        The Citus version of server group.
        """
        return pulumi.get(self, "citus_version")

    @citus_version.setter
    def citus_version(self, value: Optional[pulumi.Input[Union[str, 'CitusVersion']]]):
        pulumi.set(self, "citus_version", value)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[str, 'CreateMode']]]:
        """
        The mode to create a new server group.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[str, 'CreateMode']]]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="delegatedSubnetArguments")
    def delegated_subnet_arguments(self) -> Optional[pulumi.Input['ServerGroupPropertiesDelegatedSubnetArgumentsArgs']]:
        """
        The delegated subnet arguments for a server group.
        """
        return pulumi.get(self, "delegated_subnet_arguments")

    @delegated_subnet_arguments.setter
    def delegated_subnet_arguments(self, value: Optional[pulumi.Input['ServerGroupPropertiesDelegatedSubnetArgumentsArgs']]):
        pulumi.set(self, "delegated_subnet_arguments", value)

    @property
    @pulumi.getter(name="enableMx")
    def enable_mx(self) -> Optional[pulumi.Input[bool]]:
        """
        If Citus MX is enabled or not for the server group.
        """
        return pulumi.get(self, "enable_mx")

    @enable_mx.setter
    def enable_mx(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_mx", value)

    @property
    @pulumi.getter(name="enableShardsOnCoordinator")
    def enable_shards_on_coordinator(self) -> Optional[pulumi.Input[bool]]:
        """
        If shards on coordinator is enabled or not for the server group.
        """
        return pulumi.get(self, "enable_shards_on_coordinator")

    @enable_shards_on_coordinator.setter
    def enable_shards_on_coordinator(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_shards_on_coordinator", value)

    @property
    @pulumi.getter(name="enableZfs")
    def enable_zfs(self) -> Optional[pulumi.Input[bool]]:
        """
        If ZFS compression is enabled or not for the server group.
        """
        return pulumi.get(self, "enable_zfs")

    @enable_zfs.setter
    def enable_zfs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_zfs", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input['MaintenanceWindowArgs']]:
        """
        Maintenance window of a server group.
        """
        return pulumi.get(self, "maintenance_window")

    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input['MaintenanceWindowArgs']]):
        pulumi.set(self, "maintenance_window", value)

    @property
    @pulumi.getter(name="pointInTimeUTC")
    def point_in_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Restore point creation time (ISO8601 format), specifying the time to restore from. It's required when 'createMode' is 'PointInTimeRestore'
        """
        return pulumi.get(self, "point_in_time_utc")

    @point_in_time_utc.setter
    def point_in_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "point_in_time_utc", value)

    @property
    @pulumi.getter(name="postgresqlVersion")
    def postgresql_version(self) -> Optional[pulumi.Input[Union[str, 'PostgreSQLVersion']]]:
        """
        The PostgreSQL version of server group.
        """
        return pulumi.get(self, "postgresql_version")

    @postgresql_version.setter
    def postgresql_version(self, value: Optional[pulumi.Input[Union[str, 'PostgreSQLVersion']]]):
        pulumi.set(self, "postgresql_version", value)

    @property
    @pulumi.getter(name="privateDnsZoneArguments")
    def private_dns_zone_arguments(self) -> Optional[pulumi.Input['ServerGroupPropertiesPrivateDnsZoneArgumentsArgs']]:
        """
        The private dns zone arguments for a server group.
        """
        return pulumi.get(self, "private_dns_zone_arguments")

    @private_dns_zone_arguments.setter
    def private_dns_zone_arguments(self, value: Optional[pulumi.Input['ServerGroupPropertiesPrivateDnsZoneArgumentsArgs']]):
        pulumi.set(self, "private_dns_zone_arguments", value)

    @property
    @pulumi.getter(name="serverGroupName")
    def server_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the server group.
        """
        return pulumi.get(self, "server_group_name")

    @server_group_name.setter
    def server_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_group_name", value)

    @property
    @pulumi.getter(name="serverRoleGroups")
    def server_role_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerRoleGroupArgs']]]]:
        """
        The list of server role groups.
        """
        return pulumi.get(self, "server_role_groups")

    @server_role_groups.setter
    def server_role_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerRoleGroupArgs']]]]):
        pulumi.set(self, "server_role_groups", value)

    @property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[pulumi.Input[str]]:
        """
        The source server group location to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        """
        return pulumi.get(self, "source_location")

    @source_location.setter
    def source_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_location", value)

    @property
    @pulumi.getter(name="sourceResourceGroupName")
    def source_resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The source resource group name to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        """
        return pulumi.get(self, "source_resource_group_name")

    @source_resource_group_name.setter
    def source_resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_group_name", value)

    @property
    @pulumi.getter(name="sourceServerGroupName")
    def source_server_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The source server group name to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        """
        return pulumi.get(self, "source_server_group_name")

    @source_server_group_name.setter
    def source_server_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_server_group_name", value)

    @property
    @pulumi.getter(name="sourceSubscriptionId")
    def source_subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The source subscription id to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        """
        return pulumi.get(self, "source_subscription_id")

    @source_subscription_id.setter
    def source_subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_subscription_id", value)

    @property
    @pulumi.getter(name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Standby Availability Zone information of the server group.
        """
        return pulumi.get(self, "standby_availability_zone")

    @standby_availability_zone.setter
    def standby_availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "standby_availability_zone", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ServerGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 backup_retention_days: Optional[pulumi.Input[int]] = None,
                 citus_version: Optional[pulumi.Input[Union[str, 'CitusVersion']]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 delegated_subnet_arguments: Optional[pulumi.Input[pulumi.InputType['ServerGroupPropertiesDelegatedSubnetArgumentsArgs']]] = None,
                 enable_mx: Optional[pulumi.Input[bool]] = None,
                 enable_shards_on_coordinator: Optional[pulumi.Input[bool]] = None,
                 enable_zfs: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['MaintenanceWindowArgs']]] = None,
                 point_in_time_utc: Optional[pulumi.Input[str]] = None,
                 postgresql_version: Optional[pulumi.Input[Union[str, 'PostgreSQLVersion']]] = None,
                 private_dns_zone_arguments: Optional[pulumi.Input[pulumi.InputType['ServerGroupPropertiesPrivateDnsZoneArgumentsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_group_name: Optional[pulumi.Input[str]] = None,
                 server_role_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerRoleGroupArgs']]]]] = None,
                 source_location: Optional[pulumi.Input[str]] = None,
                 source_resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_server_group_name: Optional[pulumi.Input[str]] = None,
                 source_subscription_id: Optional[pulumi.Input[str]] = None,
                 standby_availability_zone: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents a server group for create.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administrator_login: The administrator's login name of servers in server group. Can only be specified when the server is being created (and is required for creation).
        :param pulumi.Input[str] administrator_login_password: The password of the administrator login.
        :param pulumi.Input[str] availability_zone: Availability Zone information of the server group.
        :param pulumi.Input[int] backup_retention_days: The backup retention days for server group.
        :param pulumi.Input[Union[str, 'CitusVersion']] citus_version: The Citus version of server group.
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: The mode to create a new server group.
        :param pulumi.Input[pulumi.InputType['ServerGroupPropertiesDelegatedSubnetArgumentsArgs']] delegated_subnet_arguments: The delegated subnet arguments for a server group.
        :param pulumi.Input[bool] enable_mx: If Citus MX is enabled or not for the server group.
        :param pulumi.Input[bool] enable_shards_on_coordinator: If shards on coordinator is enabled or not for the server group.
        :param pulumi.Input[bool] enable_zfs: If ZFS compression is enabled or not for the server group.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['MaintenanceWindowArgs']] maintenance_window: Maintenance window of a server group.
        :param pulumi.Input[str] point_in_time_utc: Restore point creation time (ISO8601 format), specifying the time to restore from. It's required when 'createMode' is 'PointInTimeRestore'
        :param pulumi.Input[Union[str, 'PostgreSQLVersion']] postgresql_version: The PostgreSQL version of server group.
        :param pulumi.Input[pulumi.InputType['ServerGroupPropertiesPrivateDnsZoneArgumentsArgs']] private_dns_zone_arguments: The private dns zone arguments for a server group.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] server_group_name: The name of the server group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerRoleGroupArgs']]]] server_role_groups: The list of server role groups.
        :param pulumi.Input[str] source_location: The source server group location to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        :param pulumi.Input[str] source_resource_group_name: The source resource group name to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        :param pulumi.Input[str] source_server_group_name: The source server group name to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        :param pulumi.Input[str] source_subscription_id: The source subscription id to restore from. It's required when 'createMode' is 'PointInTimeRestore' or 'ReadReplica'
        :param pulumi.Input[str] standby_availability_zone: Standby Availability Zone information of the server group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a server group for create.

        :param str resource_name: The name of the resource.
        :param ServerGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 backup_retention_days: Optional[pulumi.Input[int]] = None,
                 citus_version: Optional[pulumi.Input[Union[str, 'CitusVersion']]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 delegated_subnet_arguments: Optional[pulumi.Input[pulumi.InputType['ServerGroupPropertiesDelegatedSubnetArgumentsArgs']]] = None,
                 enable_mx: Optional[pulumi.Input[bool]] = None,
                 enable_shards_on_coordinator: Optional[pulumi.Input[bool]] = None,
                 enable_zfs: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['MaintenanceWindowArgs']]] = None,
                 point_in_time_utc: Optional[pulumi.Input[str]] = None,
                 postgresql_version: Optional[pulumi.Input[Union[str, 'PostgreSQLVersion']]] = None,
                 private_dns_zone_arguments: Optional[pulumi.Input[pulumi.InputType['ServerGroupPropertiesPrivateDnsZoneArgumentsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_group_name: Optional[pulumi.Input[str]] = None,
                 server_role_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerRoleGroupArgs']]]]] = None,
                 source_location: Optional[pulumi.Input[str]] = None,
                 source_resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_server_group_name: Optional[pulumi.Input[str]] = None,
                 source_subscription_id: Optional[pulumi.Input[str]] = None,
                 standby_availability_zone: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerGroupArgs.__new__(ServerGroupArgs)

            __props__.__dict__["administrator_login"] = administrator_login
            __props__.__dict__["administrator_login_password"] = administrator_login_password
            __props__.__dict__["availability_zone"] = availability_zone
            __props__.__dict__["backup_retention_days"] = backup_retention_days
            __props__.__dict__["citus_version"] = citus_version
            __props__.__dict__["create_mode"] = create_mode
            __props__.__dict__["delegated_subnet_arguments"] = delegated_subnet_arguments
            __props__.__dict__["enable_mx"] = enable_mx
            __props__.__dict__["enable_shards_on_coordinator"] = enable_shards_on_coordinator
            __props__.__dict__["enable_zfs"] = enable_zfs
            __props__.__dict__["location"] = location
            __props__.__dict__["maintenance_window"] = maintenance_window
            __props__.__dict__["point_in_time_utc"] = point_in_time_utc
            __props__.__dict__["postgresql_version"] = postgresql_version
            __props__.__dict__["private_dns_zone_arguments"] = private_dns_zone_arguments
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["server_group_name"] = server_group_name
            __props__.__dict__["server_role_groups"] = server_role_groups
            __props__.__dict__["source_location"] = source_location
            __props__.__dict__["source_resource_group_name"] = source_resource_group_name
            __props__.__dict__["source_server_group_name"] = source_server_group_name
            __props__.__dict__["source_subscription_id"] = source_subscription_id
            __props__.__dict__["standby_availability_zone"] = standby_availability_zone
            __props__.__dict__["tags"] = tags
            __props__.__dict__["earliest_restore_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["read_replicas"] = None
            __props__.__dict__["resource_provider_type"] = None
            __props__.__dict__["source_server_group"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:dbforpostgresql:ServerGroup"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20221108:ServerGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerGroup, __self__).__init__(
            'azure-native:dbforpostgresql/v20201005privatepreview:ServerGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerGroup':
        """
        Get an existing ServerGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerGroupArgs.__new__(ServerGroupArgs)

        __props__.__dict__["administrator_login"] = None
        __props__.__dict__["availability_zone"] = None
        __props__.__dict__["backup_retention_days"] = None
        __props__.__dict__["citus_version"] = None
        __props__.__dict__["delegated_subnet_arguments"] = None
        __props__.__dict__["earliest_restore_time"] = None
        __props__.__dict__["enable_mx"] = None
        __props__.__dict__["enable_shards_on_coordinator"] = None
        __props__.__dict__["enable_zfs"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["maintenance_window"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["postgresql_version"] = None
        __props__.__dict__["private_dns_zone_arguments"] = None
        __props__.__dict__["read_replicas"] = None
        __props__.__dict__["resource_provider_type"] = None
        __props__.__dict__["server_role_groups"] = None
        __props__.__dict__["source_server_group"] = None
        __props__.__dict__["standby_availability_zone"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ServerGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Output[Optional[str]]:
        """
        The administrator's login name of servers in server group. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[Optional[str]]:
        """
        Availability Zone information of the server group.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> pulumi.Output[Optional[int]]:
        """
        The backup retention days for server group.
        """
        return pulumi.get(self, "backup_retention_days")

    @property
    @pulumi.getter(name="citusVersion")
    def citus_version(self) -> pulumi.Output[Optional[str]]:
        """
        The Citus version of server group.
        """
        return pulumi.get(self, "citus_version")

    @property
    @pulumi.getter(name="delegatedSubnetArguments")
    def delegated_subnet_arguments(self) -> pulumi.Output[Optional['outputs.ServerGroupPropertiesResponseDelegatedSubnetArguments']]:
        """
        The delegated subnet arguments for a server group.
        """
        return pulumi.get(self, "delegated_subnet_arguments")

    @property
    @pulumi.getter(name="earliestRestoreTime")
    def earliest_restore_time(self) -> pulumi.Output[str]:
        """
        The earliest restore point time (ISO8601 format) for server group.
        """
        return pulumi.get(self, "earliest_restore_time")

    @property
    @pulumi.getter(name="enableMx")
    def enable_mx(self) -> pulumi.Output[Optional[bool]]:
        """
        If Citus MX is enabled or not for the server group.
        """
        return pulumi.get(self, "enable_mx")

    @property
    @pulumi.getter(name="enableShardsOnCoordinator")
    def enable_shards_on_coordinator(self) -> pulumi.Output[Optional[bool]]:
        """
        If shards on coordinator is enabled or not for the server group.
        """
        return pulumi.get(self, "enable_shards_on_coordinator")

    @property
    @pulumi.getter(name="enableZfs")
    def enable_zfs(self) -> pulumi.Output[Optional[bool]]:
        """
        If ZFS compression is enabled or not for the server group.
        """
        return pulumi.get(self, "enable_zfs")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[Optional['outputs.MaintenanceWindowResponse']]:
        """
        Maintenance window of a server group.
        """
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="postgresqlVersion")
    def postgresql_version(self) -> pulumi.Output[Optional[str]]:
        """
        The PostgreSQL version of server group.
        """
        return pulumi.get(self, "postgresql_version")

    @property
    @pulumi.getter(name="privateDnsZoneArguments")
    def private_dns_zone_arguments(self) -> pulumi.Output[Optional['outputs.ServerGroupPropertiesResponsePrivateDnsZoneArguments']]:
        """
        The private dns zone arguments for a server group.
        """
        return pulumi.get(self, "private_dns_zone_arguments")

    @property
    @pulumi.getter(name="readReplicas")
    def read_replicas(self) -> pulumi.Output[Sequence[str]]:
        """
        The array of read replica server groups.
        """
        return pulumi.get(self, "read_replicas")

    @property
    @pulumi.getter(name="resourceProviderType")
    def resource_provider_type(self) -> pulumi.Output[str]:
        """
        The resource provider type of server group.
        """
        return pulumi.get(self, "resource_provider_type")

    @property
    @pulumi.getter(name="serverRoleGroups")
    def server_role_groups(self) -> pulumi.Output[Optional[Sequence['outputs.ServerRoleGroupResponse']]]:
        """
        The list of server role groups.
        """
        return pulumi.get(self, "server_role_groups")

    @property
    @pulumi.getter(name="sourceServerGroup")
    def source_server_group(self) -> pulumi.Output[str]:
        """
        The source server group id for read replica server groups.
        """
        return pulumi.get(self, "source_server_group")

    @property
    @pulumi.getter(name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> pulumi.Output[Optional[str]]:
        """
        Standby Availability Zone information of the server group.
        """
        return pulumi.get(self, "standby_availability_zone")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        A state of a server group that is visible to user.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to this resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

