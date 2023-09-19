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
    'GetManagedInstanceResult',
    'AwaitableGetManagedInstanceResult',
    'get_managed_instance',
    'get_managed_instance_output',
]

@pulumi.output_type
class GetManagedInstanceResult:
    """
    An Azure SQL managed instance.
    """
    def __init__(__self__, administrator_login=None, administrators=None, collation=None, current_backup_storage_redundancy=None, dns_zone=None, fully_qualified_domain_name=None, id=None, identity=None, instance_pool_id=None, key_id=None, license_type=None, location=None, maintenance_configuration_id=None, minimal_tls_version=None, name=None, primary_user_assigned_identity_id=None, private_endpoint_connections=None, provisioning_state=None, proxy_override=None, public_data_endpoint_enabled=None, requested_backup_storage_redundancy=None, service_principal=None, sku=None, state=None, storage_size_in_gb=None, subnet_id=None, tags=None, timezone_id=None, type=None, v_cores=None, zone_redundant=None):
        if administrator_login and not isinstance(administrator_login, str):
            raise TypeError("Expected argument 'administrator_login' to be a str")
        pulumi.set(__self__, "administrator_login", administrator_login)
        if administrators and not isinstance(administrators, dict):
            raise TypeError("Expected argument 'administrators' to be a dict")
        pulumi.set(__self__, "administrators", administrators)
        if collation and not isinstance(collation, str):
            raise TypeError("Expected argument 'collation' to be a str")
        pulumi.set(__self__, "collation", collation)
        if current_backup_storage_redundancy and not isinstance(current_backup_storage_redundancy, str):
            raise TypeError("Expected argument 'current_backup_storage_redundancy' to be a str")
        pulumi.set(__self__, "current_backup_storage_redundancy", current_backup_storage_redundancy)
        if dns_zone and not isinstance(dns_zone, str):
            raise TypeError("Expected argument 'dns_zone' to be a str")
        pulumi.set(__self__, "dns_zone", dns_zone)
        if fully_qualified_domain_name and not isinstance(fully_qualified_domain_name, str):
            raise TypeError("Expected argument 'fully_qualified_domain_name' to be a str")
        pulumi.set(__self__, "fully_qualified_domain_name", fully_qualified_domain_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if instance_pool_id and not isinstance(instance_pool_id, str):
            raise TypeError("Expected argument 'instance_pool_id' to be a str")
        pulumi.set(__self__, "instance_pool_id", instance_pool_id)
        if key_id and not isinstance(key_id, str):
            raise TypeError("Expected argument 'key_id' to be a str")
        pulumi.set(__self__, "key_id", key_id)
        if license_type and not isinstance(license_type, str):
            raise TypeError("Expected argument 'license_type' to be a str")
        pulumi.set(__self__, "license_type", license_type)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_configuration_id and not isinstance(maintenance_configuration_id, str):
            raise TypeError("Expected argument 'maintenance_configuration_id' to be a str")
        pulumi.set(__self__, "maintenance_configuration_id", maintenance_configuration_id)
        if minimal_tls_version and not isinstance(minimal_tls_version, str):
            raise TypeError("Expected argument 'minimal_tls_version' to be a str")
        pulumi.set(__self__, "minimal_tls_version", minimal_tls_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if primary_user_assigned_identity_id and not isinstance(primary_user_assigned_identity_id, str):
            raise TypeError("Expected argument 'primary_user_assigned_identity_id' to be a str")
        pulumi.set(__self__, "primary_user_assigned_identity_id", primary_user_assigned_identity_id)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if proxy_override and not isinstance(proxy_override, str):
            raise TypeError("Expected argument 'proxy_override' to be a str")
        pulumi.set(__self__, "proxy_override", proxy_override)
        if public_data_endpoint_enabled and not isinstance(public_data_endpoint_enabled, bool):
            raise TypeError("Expected argument 'public_data_endpoint_enabled' to be a bool")
        pulumi.set(__self__, "public_data_endpoint_enabled", public_data_endpoint_enabled)
        if requested_backup_storage_redundancy and not isinstance(requested_backup_storage_redundancy, str):
            raise TypeError("Expected argument 'requested_backup_storage_redundancy' to be a str")
        pulumi.set(__self__, "requested_backup_storage_redundancy", requested_backup_storage_redundancy)
        if service_principal and not isinstance(service_principal, dict):
            raise TypeError("Expected argument 'service_principal' to be a dict")
        pulumi.set(__self__, "service_principal", service_principal)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_size_in_gb and not isinstance(storage_size_in_gb, int):
            raise TypeError("Expected argument 'storage_size_in_gb' to be a int")
        pulumi.set(__self__, "storage_size_in_gb", storage_size_in_gb)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if timezone_id and not isinstance(timezone_id, str):
            raise TypeError("Expected argument 'timezone_id' to be a str")
        pulumi.set(__self__, "timezone_id", timezone_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if v_cores and not isinstance(v_cores, int):
            raise TypeError("Expected argument 'v_cores' to be a int")
        pulumi.set(__self__, "v_cores", v_cores)
        if zone_redundant and not isinstance(zone_redundant, bool):
            raise TypeError("Expected argument 'zone_redundant' to be a bool")
        pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[str]:
        """
        Administrator username for the managed instance. Can only be specified when the managed instance is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter
    def administrators(self) -> Optional['outputs.ManagedInstanceExternalAdministratorResponse']:
        """
        The Azure Active Directory administrator of the server.
        """
        return pulumi.get(self, "administrators")

    @property
    @pulumi.getter
    def collation(self) -> Optional[str]:
        """
        Collation of the managed instance.
        """
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter(name="currentBackupStorageRedundancy")
    def current_backup_storage_redundancy(self) -> str:
        """
        The storage account type used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage)
        """
        return pulumi.get(self, "current_backup_storage_redundancy")

    @property
    @pulumi.getter(name="dnsZone")
    def dns_zone(self) -> str:
        """
        The Dns Zone that the managed instance is in.
        """
        return pulumi.get(self, "dns_zone")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> str:
        """
        The fully qualified domain name of the managed instance.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ResourceIdentityResponse']:
        """
        The Azure Active Directory identity of the managed instance.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="instancePoolId")
    def instance_pool_id(self) -> Optional[str]:
        """
        The Id of the instance pool this managed server belongs to.
        """
        return pulumi.get(self, "instance_pool_id")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[str]:
        """
        A CMK URI of the key to use for encryption.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[str]:
        """
        The license type. Possible values are 'LicenseIncluded' (regular price inclusive of a new SQL license) and 'BasePrice' (discounted AHB price for bringing your own SQL licenses).
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(self) -> Optional[str]:
        """
        Specifies maintenance configuration id to apply to this managed instance.
        """
        return pulumi.get(self, "maintenance_configuration_id")

    @property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[str]:
        """
        Minimal TLS version. Allowed values: 'None', '1.0', '1.1', '1.2'
        """
        return pulumi.get(self, "minimal_tls_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[str]:
        """
        The resource id of a user assigned identity to be used by default.
        """
        return pulumi.get(self, "primary_user_assigned_identity_id")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.ManagedInstancePecPropertyResponse']:
        """
        List of private endpoint connections on a managed instance.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="proxyOverride")
    def proxy_override(self) -> Optional[str]:
        """
        Connection type used for connecting to the instance.
        """
        return pulumi.get(self, "proxy_override")

    @property
    @pulumi.getter(name="publicDataEndpointEnabled")
    def public_data_endpoint_enabled(self) -> Optional[bool]:
        """
        Whether or not the public data endpoint is enabled.
        """
        return pulumi.get(self, "public_data_endpoint_enabled")

    @property
    @pulumi.getter(name="requestedBackupStorageRedundancy")
    def requested_backup_storage_redundancy(self) -> Optional[str]:
        """
        The storage account type to be used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage)
        """
        return pulumi.get(self, "requested_backup_storage_redundancy")

    @property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> Optional['outputs.ServicePrincipalResponse']:
        """
        The managed instance's service principal.
        """
        return pulumi.get(self, "service_principal")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        Managed instance SKU. Allowed values for sku.name: GP_Gen5, GP_G8IM, GP_G8IH, BC_Gen5, BC_G8IM, BC_G8IH
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the managed instance.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageSizeInGB")
    def storage_size_in_gb(self) -> Optional[int]:
        """
        Storage size in GB. Minimum value: 32. Maximum value: 16384. Increments of 32 GB allowed only. Maximum value depends on the selected hardware family and number of vCores.
        """
        return pulumi.get(self, "storage_size_in_gb")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[str]:
        """
        Subnet resource ID for the managed instance.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timezoneId")
    def timezone_id(self) -> Optional[str]:
        """
        Id of the timezone. Allowed values are timezones supported by Windows.
        Windows keeps details on supported timezones, including the id, in registry under
        KEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Time Zones.
        You can get those registry values via SQL Server by querying SELECT name AS timezone_id FROM sys.time_zone_info.
        List of Ids can also be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell.
        An example of valid timezone id is "Pacific Standard Time" or "W. Europe Standard Time".
        """
        return pulumi.get(self, "timezone_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vCores")
    def v_cores(self) -> Optional[int]:
        """
        The number of vCores. Allowed values: 8, 16, 24, 32, 40, 64, 80.
        """
        return pulumi.get(self, "v_cores")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[bool]:
        """
        Whether or not the multi-az is enabled.
        """
        return pulumi.get(self, "zone_redundant")


class AwaitableGetManagedInstanceResult(GetManagedInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstanceResult(
            administrator_login=self.administrator_login,
            administrators=self.administrators,
            collation=self.collation,
            current_backup_storage_redundancy=self.current_backup_storage_redundancy,
            dns_zone=self.dns_zone,
            fully_qualified_domain_name=self.fully_qualified_domain_name,
            id=self.id,
            identity=self.identity,
            instance_pool_id=self.instance_pool_id,
            key_id=self.key_id,
            license_type=self.license_type,
            location=self.location,
            maintenance_configuration_id=self.maintenance_configuration_id,
            minimal_tls_version=self.minimal_tls_version,
            name=self.name,
            primary_user_assigned_identity_id=self.primary_user_assigned_identity_id,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            proxy_override=self.proxy_override,
            public_data_endpoint_enabled=self.public_data_endpoint_enabled,
            requested_backup_storage_redundancy=self.requested_backup_storage_redundancy,
            service_principal=self.service_principal,
            sku=self.sku,
            state=self.state,
            storage_size_in_gb=self.storage_size_in_gb,
            subnet_id=self.subnet_id,
            tags=self.tags,
            timezone_id=self.timezone_id,
            type=self.type,
            v_cores=self.v_cores,
            zone_redundant=self.zone_redundant)


def get_managed_instance(expand: Optional[str] = None,
                         managed_instance_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstanceResult:
    """
    Gets a managed instance.
    Azure REST API version: 2021-11-01.


    :param str expand: The child resources to include in the response.
    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['managedInstanceName'] = managed_instance_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql:getManagedInstance', __args__, opts=opts, typ=GetManagedInstanceResult).value

    return AwaitableGetManagedInstanceResult(
        administrator_login=pulumi.get(__ret__, 'administrator_login'),
        administrators=pulumi.get(__ret__, 'administrators'),
        collation=pulumi.get(__ret__, 'collation'),
        current_backup_storage_redundancy=pulumi.get(__ret__, 'current_backup_storage_redundancy'),
        dns_zone=pulumi.get(__ret__, 'dns_zone'),
        fully_qualified_domain_name=pulumi.get(__ret__, 'fully_qualified_domain_name'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        instance_pool_id=pulumi.get(__ret__, 'instance_pool_id'),
        key_id=pulumi.get(__ret__, 'key_id'),
        license_type=pulumi.get(__ret__, 'license_type'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_configuration_id=pulumi.get(__ret__, 'maintenance_configuration_id'),
        minimal_tls_version=pulumi.get(__ret__, 'minimal_tls_version'),
        name=pulumi.get(__ret__, 'name'),
        primary_user_assigned_identity_id=pulumi.get(__ret__, 'primary_user_assigned_identity_id'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        proxy_override=pulumi.get(__ret__, 'proxy_override'),
        public_data_endpoint_enabled=pulumi.get(__ret__, 'public_data_endpoint_enabled'),
        requested_backup_storage_redundancy=pulumi.get(__ret__, 'requested_backup_storage_redundancy'),
        service_principal=pulumi.get(__ret__, 'service_principal'),
        sku=pulumi.get(__ret__, 'sku'),
        state=pulumi.get(__ret__, 'state'),
        storage_size_in_gb=pulumi.get(__ret__, 'storage_size_in_gb'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        tags=pulumi.get(__ret__, 'tags'),
        timezone_id=pulumi.get(__ret__, 'timezone_id'),
        type=pulumi.get(__ret__, 'type'),
        v_cores=pulumi.get(__ret__, 'v_cores'),
        zone_redundant=pulumi.get(__ret__, 'zone_redundant'))


@_utilities.lift_output_func(get_managed_instance)
def get_managed_instance_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                                managed_instance_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstanceResult]:
    """
    Gets a managed instance.
    Azure REST API version: 2021-11-01.


    :param str expand: The child resources to include in the response.
    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    ...
