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

__all__ = ['VirtualHardDiskArgs', 'VirtualHardDisk']

@pulumi.input_type
class VirtualHardDiskArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 block_size_bytes: Optional[pulumi.Input[int]] = None,
                 container_id: Optional[pulumi.Input[str]] = None,
                 disk_file_format: Optional[pulumi.Input[Union[str, 'DiskFileFormat']]] = None,
                 disk_size_gb: Optional[pulumi.Input[float]] = None,
                 dynamic: Optional[pulumi.Input[bool]] = None,
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 hyper_v_generation: Optional[pulumi.Input[Union[str, 'HyperVGeneration']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logical_sector_bytes: Optional[pulumi.Input[int]] = None,
                 physical_sector_bytes: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hard_disk_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualHardDisk resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] container_id: Storage ContainerID of the storage container to be used for VHD
        :param pulumi.Input[Union[str, 'DiskFileFormat']] disk_file_format: The format of the actual VHD file [vhd, vhdx]
        :param pulumi.Input[float] disk_size_gb: Size of the disk in GB
        :param pulumi.Input[bool] dynamic: Boolean for enabling dynamic sizing on the virtual hard disk
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extendedLocation of the resource.
        :param pulumi.Input[Union[str, 'HyperVGeneration']] hyper_v_generation: The hypervisor generation of the Virtual Machine [V1, V2]
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] virtual_hard_disk_name: Name of the virtual hard disk
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if block_size_bytes is not None:
            pulumi.set(__self__, "block_size_bytes", block_size_bytes)
        if container_id is not None:
            pulumi.set(__self__, "container_id", container_id)
        if disk_file_format is not None:
            pulumi.set(__self__, "disk_file_format", disk_file_format)
        if disk_size_gb is not None:
            pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if dynamic is not None:
            pulumi.set(__self__, "dynamic", dynamic)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if hyper_v_generation is not None:
            pulumi.set(__self__, "hyper_v_generation", hyper_v_generation)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if logical_sector_bytes is not None:
            pulumi.set(__self__, "logical_sector_bytes", logical_sector_bytes)
        if physical_sector_bytes is not None:
            pulumi.set(__self__, "physical_sector_bytes", physical_sector_bytes)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_hard_disk_name is not None:
            pulumi.set(__self__, "virtual_hard_disk_name", virtual_hard_disk_name)

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
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "block_size_bytes")

    @block_size_bytes.setter
    def block_size_bytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "block_size_bytes", value)

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[str]]:
        """
        Storage ContainerID of the storage container to be used for VHD
        """
        return pulumi.get(self, "container_id")

    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_id", value)

    @property
    @pulumi.getter(name="diskFileFormat")
    def disk_file_format(self) -> Optional[pulumi.Input[Union[str, 'DiskFileFormat']]]:
        """
        The format of the actual VHD file [vhd, vhdx]
        """
        return pulumi.get(self, "disk_file_format")

    @disk_file_format.setter
    def disk_file_format(self, value: Optional[pulumi.Input[Union[str, 'DiskFileFormat']]]):
        pulumi.set(self, "disk_file_format", value)

    @property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[float]]:
        """
        Size of the disk in GB
        """
        return pulumi.get(self, "disk_size_gb")

    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "disk_size_gb", value)

    @property
    @pulumi.getter
    def dynamic(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean for enabling dynamic sizing on the virtual hard disk
        """
        return pulumi.get(self, "dynamic")

    @dynamic.setter
    def dynamic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dynamic", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> Optional[pulumi.Input[Union[str, 'HyperVGeneration']]]:
        """
        The hypervisor generation of the Virtual Machine [V1, V2]
        """
        return pulumi.get(self, "hyper_v_generation")

    @hyper_v_generation.setter
    def hyper_v_generation(self, value: Optional[pulumi.Input[Union[str, 'HyperVGeneration']]]):
        pulumi.set(self, "hyper_v_generation", value)

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
    @pulumi.getter(name="logicalSectorBytes")
    def logical_sector_bytes(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "logical_sector_bytes")

    @logical_sector_bytes.setter
    def logical_sector_bytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "logical_sector_bytes", value)

    @property
    @pulumi.getter(name="physicalSectorBytes")
    def physical_sector_bytes(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "physical_sector_bytes")

    @physical_sector_bytes.setter
    def physical_sector_bytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "physical_sector_bytes", value)

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
    @pulumi.getter(name="virtualHardDiskName")
    def virtual_hard_disk_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the virtual hard disk
        """
        return pulumi.get(self, "virtual_hard_disk_name")

    @virtual_hard_disk_name.setter
    def virtual_hard_disk_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_hard_disk_name", value)


class VirtualHardDisk(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 block_size_bytes: Optional[pulumi.Input[int]] = None,
                 container_id: Optional[pulumi.Input[str]] = None,
                 disk_file_format: Optional[pulumi.Input[Union[str, 'DiskFileFormat']]] = None,
                 disk_size_gb: Optional[pulumi.Input[float]] = None,
                 dynamic: Optional[pulumi.Input[bool]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 hyper_v_generation: Optional[pulumi.Input[Union[str, 'HyperVGeneration']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logical_sector_bytes: Optional[pulumi.Input[int]] = None,
                 physical_sector_bytes: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hard_disk_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The virtual hard disk resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_id: Storage ContainerID of the storage container to be used for VHD
        :param pulumi.Input[Union[str, 'DiskFileFormat']] disk_file_format: The format of the actual VHD file [vhd, vhdx]
        :param pulumi.Input[float] disk_size_gb: Size of the disk in GB
        :param pulumi.Input[bool] dynamic: Boolean for enabling dynamic sizing on the virtual hard disk
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extendedLocation of the resource.
        :param pulumi.Input[Union[str, 'HyperVGeneration']] hyper_v_generation: The hypervisor generation of the Virtual Machine [V1, V2]
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] virtual_hard_disk_name: Name of the virtual hard disk
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualHardDiskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The virtual hard disk resource definition.

        :param str resource_name: The name of the resource.
        :param VirtualHardDiskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualHardDiskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 block_size_bytes: Optional[pulumi.Input[int]] = None,
                 container_id: Optional[pulumi.Input[str]] = None,
                 disk_file_format: Optional[pulumi.Input[Union[str, 'DiskFileFormat']]] = None,
                 disk_size_gb: Optional[pulumi.Input[float]] = None,
                 dynamic: Optional[pulumi.Input[bool]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 hyper_v_generation: Optional[pulumi.Input[Union[str, 'HyperVGeneration']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logical_sector_bytes: Optional[pulumi.Input[int]] = None,
                 physical_sector_bytes: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hard_disk_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualHardDiskArgs.__new__(VirtualHardDiskArgs)

            __props__.__dict__["block_size_bytes"] = block_size_bytes
            __props__.__dict__["container_id"] = container_id
            __props__.__dict__["disk_file_format"] = disk_file_format
            __props__.__dict__["disk_size_gb"] = disk_size_gb
            __props__.__dict__["dynamic"] = dynamic
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["hyper_v_generation"] = hyper_v_generation
            __props__.__dict__["location"] = location
            __props__.__dict__["logical_sector_bytes"] = logical_sector_bytes
            __props__.__dict__["physical_sector_bytes"] = physical_sector_bytes
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_hard_disk_name"] = virtual_hard_disk_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci:VirtualHardDisk"), pulumi.Alias(type_="azure-native:azurestackhci/v20210701preview:VirtualHardDisk"), pulumi.Alias(type_="azure-native:azurestackhci/v20210901preview:VirtualHardDisk"), pulumi.Alias(type_="azure-native:azurestackhci/v20230701preview:VirtualHardDisk")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualHardDisk, __self__).__init__(
            'azure-native:azurestackhci/v20221215preview:VirtualHardDisk',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualHardDisk':
        """
        Get an existing VirtualHardDisk resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualHardDiskArgs.__new__(VirtualHardDiskArgs)

        __props__.__dict__["block_size_bytes"] = None
        __props__.__dict__["container_id"] = None
        __props__.__dict__["disk_file_format"] = None
        __props__.__dict__["disk_size_gb"] = None
        __props__.__dict__["dynamic"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["hyper_v_generation"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["logical_sector_bytes"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["physical_sector_bytes"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return VirtualHardDisk(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "block_size_bytes")

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> pulumi.Output[Optional[str]]:
        """
        Storage ContainerID of the storage container to be used for VHD
        """
        return pulumi.get(self, "container_id")

    @property
    @pulumi.getter(name="diskFileFormat")
    def disk_file_format(self) -> pulumi.Output[Optional[str]]:
        """
        The format of the actual VHD file [vhd, vhdx]
        """
        return pulumi.get(self, "disk_file_format")

    @property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> pulumi.Output[Optional[float]]:
        """
        Size of the disk in GB
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter
    def dynamic(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean for enabling dynamic sizing on the virtual hard disk
        """
        return pulumi.get(self, "dynamic")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> pulumi.Output[Optional[str]]:
        """
        The hypervisor generation of the Virtual Machine [V1, V2]
        """
        return pulumi.get(self, "hyper_v_generation")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logicalSectorBytes")
    def logical_sector_bytes(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "logical_sector_bytes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="physicalSectorBytes")
    def physical_sector_bytes(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "physical_sector_bytes")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the virtual hard disk.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.VirtualHardDiskStatusResponse']:
        """
        The observed state of virtual hard disks
        """
        return pulumi.get(self, "status")

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
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

