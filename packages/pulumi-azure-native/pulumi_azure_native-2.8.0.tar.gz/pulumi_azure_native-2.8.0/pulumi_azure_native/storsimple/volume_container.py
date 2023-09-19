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
from ._enums import *
from ._inputs import *

__all__ = ['VolumeContainerArgs', 'VolumeContainer']

@pulumi.input_type
class VolumeContainerArgs:
    def __init__(__self__, *,
                 device_name: pulumi.Input[str],
                 manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_account_credential_id: pulumi.Input[str],
                 band_width_rate_in_mbps: Optional[pulumi.Input[int]] = None,
                 bandwidth_setting_id: Optional[pulumi.Input[str]] = None,
                 encryption_key: Optional[pulumi.Input['AsymmetricEncryptedSecretArgs']] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 volume_container_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VolumeContainer resource.
        :param pulumi.Input[str] device_name: The device name
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[str] storage_account_credential_id: The path ID of storage account associated with the volume container.
        :param pulumi.Input[int] band_width_rate_in_mbps: The bandwidth-rate set on the volume container.
        :param pulumi.Input[str] bandwidth_setting_id: The ID of the bandwidth setting associated with the volume container.
        :param pulumi.Input['AsymmetricEncryptedSecretArgs'] encryption_key: The key used to encrypt data in the volume container. It is required when property 'EncryptionStatus' is "Enabled".
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        :param pulumi.Input[str] volume_container_name: The name of the volume container.
        """
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "manager_name", manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_account_credential_id", storage_account_credential_id)
        if band_width_rate_in_mbps is not None:
            pulumi.set(__self__, "band_width_rate_in_mbps", band_width_rate_in_mbps)
        if bandwidth_setting_id is not None:
            pulumi.set(__self__, "bandwidth_setting_id", bandwidth_setting_id)
        if encryption_key is not None:
            pulumi.set(__self__, "encryption_key", encryption_key)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if volume_container_name is not None:
            pulumi.set(__self__, "volume_container_name", volume_container_name)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[str]:
        """
        The device name
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter(name="managerName")
    def manager_name(self) -> pulumi.Input[str]:
        """
        The manager name
        """
        return pulumi.get(self, "manager_name")

    @manager_name.setter
    def manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "manager_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(self) -> pulumi.Input[str]:
        """
        The path ID of storage account associated with the volume container.
        """
        return pulumi.get(self, "storage_account_credential_id")

    @storage_account_credential_id.setter
    def storage_account_credential_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_credential_id", value)

    @property
    @pulumi.getter(name="bandWidthRateInMbps")
    def band_width_rate_in_mbps(self) -> Optional[pulumi.Input[int]]:
        """
        The bandwidth-rate set on the volume container.
        """
        return pulumi.get(self, "band_width_rate_in_mbps")

    @band_width_rate_in_mbps.setter
    def band_width_rate_in_mbps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "band_width_rate_in_mbps", value)

    @property
    @pulumi.getter(name="bandwidthSettingId")
    def bandwidth_setting_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the bandwidth setting associated with the volume container.
        """
        return pulumi.get(self, "bandwidth_setting_id")

    @bandwidth_setting_id.setter
    def bandwidth_setting_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bandwidth_setting_id", value)

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input['AsymmetricEncryptedSecretArgs']]:
        """
        The key used to encrypt data in the volume container. It is required when property 'EncryptionStatus' is "Enabled".
        """
        return pulumi.get(self, "encryption_key")

    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input['AsymmetricEncryptedSecretArgs']]):
        pulumi.set(self, "encryption_key", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input['Kind']]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input['Kind']]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="volumeContainerName")
    def volume_container_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the volume container.
        """
        return pulumi.get(self, "volume_container_name")

    @volume_container_name.setter
    def volume_container_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_container_name", value)


class VolumeContainer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 band_width_rate_in_mbps: Optional[pulumi.Input[int]] = None,
                 bandwidth_setting_id: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 encryption_key: Optional[pulumi.Input[pulumi.InputType['AsymmetricEncryptedSecretArgs']]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_credential_id: Optional[pulumi.Input[str]] = None,
                 volume_container_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The volume container.
        Azure REST API version: 2017-06-01. Prior API version in Azure Native 1.x: 2017-06-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] band_width_rate_in_mbps: The bandwidth-rate set on the volume container.
        :param pulumi.Input[str] bandwidth_setting_id: The ID of the bandwidth setting associated with the volume container.
        :param pulumi.Input[str] device_name: The device name
        :param pulumi.Input[pulumi.InputType['AsymmetricEncryptedSecretArgs']] encryption_key: The key used to encrypt data in the volume container. It is required when property 'EncryptionStatus' is "Enabled".
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[str] storage_account_credential_id: The path ID of storage account associated with the volume container.
        :param pulumi.Input[str] volume_container_name: The name of the volume container.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeContainerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The volume container.
        Azure REST API version: 2017-06-01. Prior API version in Azure Native 1.x: 2017-06-01

        :param str resource_name: The name of the resource.
        :param VolumeContainerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeContainerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 band_width_rate_in_mbps: Optional[pulumi.Input[int]] = None,
                 bandwidth_setting_id: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 encryption_key: Optional[pulumi.Input[pulumi.InputType['AsymmetricEncryptedSecretArgs']]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_credential_id: Optional[pulumi.Input[str]] = None,
                 volume_container_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeContainerArgs.__new__(VolumeContainerArgs)

            __props__.__dict__["band_width_rate_in_mbps"] = band_width_rate_in_mbps
            __props__.__dict__["bandwidth_setting_id"] = bandwidth_setting_id
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__.__dict__["device_name"] = device_name
            __props__.__dict__["encryption_key"] = encryption_key
            __props__.__dict__["kind"] = kind
            if manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'manager_name'")
            __props__.__dict__["manager_name"] = manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_account_credential_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_credential_id'")
            __props__.__dict__["storage_account_credential_id"] = storage_account_credential_id
            __props__.__dict__["volume_container_name"] = volume_container_name
            __props__.__dict__["encryption_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["owner_ship_status"] = None
            __props__.__dict__["total_cloud_storage_usage_in_bytes"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["volume_count"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storsimple/v20170601:VolumeContainer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VolumeContainer, __self__).__init__(
            'azure-native:storsimple:VolumeContainer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VolumeContainer':
        """
        Get an existing VolumeContainer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VolumeContainerArgs.__new__(VolumeContainerArgs)

        __props__.__dict__["band_width_rate_in_mbps"] = None
        __props__.__dict__["bandwidth_setting_id"] = None
        __props__.__dict__["encryption_key"] = None
        __props__.__dict__["encryption_status"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["owner_ship_status"] = None
        __props__.__dict__["storage_account_credential_id"] = None
        __props__.__dict__["total_cloud_storage_usage_in_bytes"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["volume_count"] = None
        return VolumeContainer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bandWidthRateInMbps")
    def band_width_rate_in_mbps(self) -> pulumi.Output[Optional[int]]:
        """
        The bandwidth-rate set on the volume container.
        """
        return pulumi.get(self, "band_width_rate_in_mbps")

    @property
    @pulumi.getter(name="bandwidthSettingId")
    def bandwidth_setting_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the bandwidth setting associated with the volume container.
        """
        return pulumi.get(self, "bandwidth_setting_id")

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> pulumi.Output[Optional['outputs.AsymmetricEncryptedSecretResponse']]:
        """
        The key used to encrypt data in the volume container. It is required when property 'EncryptionStatus' is "Enabled".
        """
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter(name="encryptionStatus")
    def encryption_status(self) -> pulumi.Output[str]:
        """
        The flag to denote whether encryption is enabled or not.
        """
        return pulumi.get(self, "encryption_status")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerShipStatus")
    def owner_ship_status(self) -> pulumi.Output[str]:
        """
        The owner ship status of the volume container. Only when the status is "NotOwned", the delete operation on the volume container is permitted.
        """
        return pulumi.get(self, "owner_ship_status")

    @property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(self) -> pulumi.Output[str]:
        """
        The path ID of storage account associated with the volume container.
        """
        return pulumi.get(self, "storage_account_credential_id")

    @property
    @pulumi.getter(name="totalCloudStorageUsageInBytes")
    def total_cloud_storage_usage_in_bytes(self) -> pulumi.Output[float]:
        """
        The total cloud storage for the volume container.
        """
        return pulumi.get(self, "total_cloud_storage_usage_in_bytes")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeCount")
    def volume_count(self) -> pulumi.Output[int]:
        """
        The number of volumes in the volume Container.
        """
        return pulumi.get(self, "volume_count")

