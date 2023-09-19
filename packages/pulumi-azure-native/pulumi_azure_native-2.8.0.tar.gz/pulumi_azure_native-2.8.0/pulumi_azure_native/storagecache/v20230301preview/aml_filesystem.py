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

__all__ = ['AmlFilesystemArgs', 'AmlFilesystem']

@pulumi.input_type
class AmlFilesystemArgs:
    def __init__(__self__, *,
                 filesystem_subnet: pulumi.Input[str],
                 maintenance_window: pulumi.Input['AmlFilesystemMaintenanceWindowArgs'],
                 resource_group_name: pulumi.Input[str],
                 storage_capacity_ti_b: pulumi.Input[float],
                 aml_filesystem_name: Optional[pulumi.Input[str]] = None,
                 encryption_settings: Optional[pulumi.Input['AmlFilesystemEncryptionSettingsArgs']] = None,
                 hsm: Optional[pulumi.Input['AmlFilesystemHsmArgs']] = None,
                 identity: Optional[pulumi.Input['AmlFilesystemIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuNameArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AmlFilesystem resource.
        :param pulumi.Input[str] filesystem_subnet: Subnet used for managing the AML file system and for client-facing operations. This subnet should have at least a /24 subnet mask within the VNET's address space.
        :param pulumi.Input['AmlFilesystemMaintenanceWindowArgs'] maintenance_window: Start time of a 30-minute weekly maintenance window.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[float] storage_capacity_ti_b: The size of the AML file system, in TiB. This might be rounded up.
        :param pulumi.Input[str] aml_filesystem_name: Name for the AML file system. Allows alphanumerics, underscores, and hyphens. Start and end with alphanumeric.
        :param pulumi.Input['AmlFilesystemEncryptionSettingsArgs'] encryption_settings: Specifies encryption settings of the AML file system.
        :param pulumi.Input['AmlFilesystemHsmArgs'] hsm: Hydration and archive settings and status
        :param pulumi.Input['AmlFilesystemIdentityArgs'] identity: The managed identity used by the AML file system, if configured.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['SkuNameArgs'] sku: SKU for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: Availability zones for resources. This field should only contain a single element in the array.
        """
        pulumi.set(__self__, "filesystem_subnet", filesystem_subnet)
        pulumi.set(__self__, "maintenance_window", maintenance_window)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_capacity_ti_b", storage_capacity_ti_b)
        if aml_filesystem_name is not None:
            pulumi.set(__self__, "aml_filesystem_name", aml_filesystem_name)
        if encryption_settings is not None:
            pulumi.set(__self__, "encryption_settings", encryption_settings)
        if hsm is not None:
            pulumi.set(__self__, "hsm", hsm)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="filesystemSubnet")
    def filesystem_subnet(self) -> pulumi.Input[str]:
        """
        Subnet used for managing the AML file system and for client-facing operations. This subnet should have at least a /24 subnet mask within the VNET's address space.
        """
        return pulumi.get(self, "filesystem_subnet")

    @filesystem_subnet.setter
    def filesystem_subnet(self, value: pulumi.Input[str]):
        pulumi.set(self, "filesystem_subnet", value)

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Input['AmlFilesystemMaintenanceWindowArgs']:
        """
        Start time of a 30-minute weekly maintenance window.
        """
        return pulumi.get(self, "maintenance_window")

    @maintenance_window.setter
    def maintenance_window(self, value: pulumi.Input['AmlFilesystemMaintenanceWindowArgs']):
        pulumi.set(self, "maintenance_window", value)

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
    @pulumi.getter(name="storageCapacityTiB")
    def storage_capacity_ti_b(self) -> pulumi.Input[float]:
        """
        The size of the AML file system, in TiB. This might be rounded up.
        """
        return pulumi.get(self, "storage_capacity_ti_b")

    @storage_capacity_ti_b.setter
    def storage_capacity_ti_b(self, value: pulumi.Input[float]):
        pulumi.set(self, "storage_capacity_ti_b", value)

    @property
    @pulumi.getter(name="amlFilesystemName")
    def aml_filesystem_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for the AML file system. Allows alphanumerics, underscores, and hyphens. Start and end with alphanumeric.
        """
        return pulumi.get(self, "aml_filesystem_name")

    @aml_filesystem_name.setter
    def aml_filesystem_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aml_filesystem_name", value)

    @property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional[pulumi.Input['AmlFilesystemEncryptionSettingsArgs']]:
        """
        Specifies encryption settings of the AML file system.
        """
        return pulumi.get(self, "encryption_settings")

    @encryption_settings.setter
    def encryption_settings(self, value: Optional[pulumi.Input['AmlFilesystemEncryptionSettingsArgs']]):
        pulumi.set(self, "encryption_settings", value)

    @property
    @pulumi.getter
    def hsm(self) -> Optional[pulumi.Input['AmlFilesystemHsmArgs']]:
        """
        Hydration and archive settings and status
        """
        return pulumi.get(self, "hsm")

    @hsm.setter
    def hsm(self, value: Optional[pulumi.Input['AmlFilesystemHsmArgs']]):
        pulumi.set(self, "hsm", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['AmlFilesystemIdentityArgs']]:
        """
        The managed identity used by the AML file system, if configured.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['AmlFilesystemIdentityArgs']]):
        pulumi.set(self, "identity", value)

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
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuNameArgs']]:
        """
        SKU for the resource.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuNameArgs']]):
        pulumi.set(self, "sku", value)

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

    @property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Availability zones for resources. This field should only contain a single element in the array.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


class AmlFilesystem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aml_filesystem_name: Optional[pulumi.Input[str]] = None,
                 encryption_settings: Optional[pulumi.Input[pulumi.InputType['AmlFilesystemEncryptionSettingsArgs']]] = None,
                 filesystem_subnet: Optional[pulumi.Input[str]] = None,
                 hsm: Optional[pulumi.Input[pulumi.InputType['AmlFilesystemHsmArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['AmlFilesystemIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['AmlFilesystemMaintenanceWindowArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuNameArgs']]] = None,
                 storage_capacity_ti_b: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        An AML file system instance. Follows Azure Resource Manager standards: https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/resource-api-reference.md

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aml_filesystem_name: Name for the AML file system. Allows alphanumerics, underscores, and hyphens. Start and end with alphanumeric.
        :param pulumi.Input[pulumi.InputType['AmlFilesystemEncryptionSettingsArgs']] encryption_settings: Specifies encryption settings of the AML file system.
        :param pulumi.Input[str] filesystem_subnet: Subnet used for managing the AML file system and for client-facing operations. This subnet should have at least a /24 subnet mask within the VNET's address space.
        :param pulumi.Input[pulumi.InputType['AmlFilesystemHsmArgs']] hsm: Hydration and archive settings and status
        :param pulumi.Input[pulumi.InputType['AmlFilesystemIdentityArgs']] identity: The managed identity used by the AML file system, if configured.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['AmlFilesystemMaintenanceWindowArgs']] maintenance_window: Start time of a 30-minute weekly maintenance window.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SkuNameArgs']] sku: SKU for the resource.
        :param pulumi.Input[float] storage_capacity_ti_b: The size of the AML file system, in TiB. This might be rounded up.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: Availability zones for resources. This field should only contain a single element in the array.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AmlFilesystemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An AML file system instance. Follows Azure Resource Manager standards: https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/resource-api-reference.md

        :param str resource_name: The name of the resource.
        :param AmlFilesystemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AmlFilesystemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aml_filesystem_name: Optional[pulumi.Input[str]] = None,
                 encryption_settings: Optional[pulumi.Input[pulumi.InputType['AmlFilesystemEncryptionSettingsArgs']]] = None,
                 filesystem_subnet: Optional[pulumi.Input[str]] = None,
                 hsm: Optional[pulumi.Input[pulumi.InputType['AmlFilesystemHsmArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['AmlFilesystemIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['AmlFilesystemMaintenanceWindowArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuNameArgs']]] = None,
                 storage_capacity_ti_b: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AmlFilesystemArgs.__new__(AmlFilesystemArgs)

            __props__.__dict__["aml_filesystem_name"] = aml_filesystem_name
            __props__.__dict__["encryption_settings"] = encryption_settings
            if filesystem_subnet is None and not opts.urn:
                raise TypeError("Missing required property 'filesystem_subnet'")
            __props__.__dict__["filesystem_subnet"] = filesystem_subnet
            __props__.__dict__["hsm"] = hsm
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if maintenance_window is None and not opts.urn:
                raise TypeError("Missing required property 'maintenance_window'")
            __props__.__dict__["maintenance_window"] = maintenance_window
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            if storage_capacity_ti_b is None and not opts.urn:
                raise TypeError("Missing required property 'storage_capacity_ti_b'")
            __props__.__dict__["storage_capacity_ti_b"] = storage_capacity_ti_b
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zones"] = zones
            __props__.__dict__["health"] = None
            __props__.__dict__["lustre_version"] = None
            __props__.__dict__["mgs_address"] = None
            __props__.__dict__["mount_command"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["throughput_provisioned_m_bps"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storagecache/v20230301preview:amlFilesystem"), pulumi.Alias(type_="azure-native:storagecache:AmlFilesystem"), pulumi.Alias(type_="azure-native:storagecache:amlFilesystem"), pulumi.Alias(type_="azure-native:storagecache/v20230501:AmlFilesystem"), pulumi.Alias(type_="azure-native:storagecache/v20230501:amlFilesystem")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AmlFilesystem, __self__).__init__(
            'azure-native:storagecache/v20230301preview:AmlFilesystem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AmlFilesystem':
        """
        Get an existing AmlFilesystem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AmlFilesystemArgs.__new__(AmlFilesystemArgs)

        __props__.__dict__["encryption_settings"] = None
        __props__.__dict__["filesystem_subnet"] = None
        __props__.__dict__["health"] = None
        __props__.__dict__["hsm"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["lustre_version"] = None
        __props__.__dict__["maintenance_window"] = None
        __props__.__dict__["mgs_address"] = None
        __props__.__dict__["mount_command"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["storage_capacity_ti_b"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["throughput_provisioned_m_bps"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["zones"] = None
        return AmlFilesystem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> pulumi.Output[Optional['outputs.AmlFilesystemEncryptionSettingsResponse']]:
        """
        Specifies encryption settings of the AML file system.
        """
        return pulumi.get(self, "encryption_settings")

    @property
    @pulumi.getter(name="filesystemSubnet")
    def filesystem_subnet(self) -> pulumi.Output[str]:
        """
        Subnet used for managing the AML file system and for client-facing operations. This subnet should have at least a /24 subnet mask within the VNET's address space.
        """
        return pulumi.get(self, "filesystem_subnet")

    @property
    @pulumi.getter
    def health(self) -> pulumi.Output['outputs.AmlFilesystemHealthResponse']:
        """
        Health of the AML file system.
        """
        return pulumi.get(self, "health")

    @property
    @pulumi.getter
    def hsm(self) -> pulumi.Output[Optional['outputs.AmlFilesystemResponseHsm']]:
        """
        Hydration and archive settings and status
        """
        return pulumi.get(self, "hsm")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.AmlFilesystemIdentityResponse']]:
        """
        The managed identity used by the AML file system, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="lustreVersion")
    def lustre_version(self) -> pulumi.Output[str]:
        """
        The version of Lustre running in the AML file system
        """
        return pulumi.get(self, "lustre_version")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output['outputs.AmlFilesystemResponseMaintenanceWindow']:
        """
        Start time of a 30-minute weekly maintenance window.
        """
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter(name="mgsAddress")
    def mgs_address(self) -> pulumi.Output[str]:
        """
        The IPv4 address used by clients to mount the AML file system's Lustre Management Service (MGS).
        """
        return pulumi.get(self, "mgs_address")

    @property
    @pulumi.getter(name="mountCommand")
    def mount_command(self) -> pulumi.Output[str]:
        """
        Recommended command to mount the AML file system
        """
        return pulumi.get(self, "mount_command")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        ARM provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuNameResponse']]:
        """
        SKU for the resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="storageCapacityTiB")
    def storage_capacity_ti_b(self) -> pulumi.Output[float]:
        """
        The size of the AML file system, in TiB. This might be rounded up.
        """
        return pulumi.get(self, "storage_capacity_ti_b")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
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
    @pulumi.getter(name="throughputProvisionedMBps")
    def throughput_provisioned_m_bps(self) -> pulumi.Output[int]:
        """
        Throughput provisioned in MB per sec, calculated as storageCapacityTiB * per-unit storage throughput
        """
        return pulumi.get(self, "throughput_provisioned_m_bps")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Availability zones for resources. This field should only contain a single element in the array.
        """
        return pulumi.get(self, "zones")

