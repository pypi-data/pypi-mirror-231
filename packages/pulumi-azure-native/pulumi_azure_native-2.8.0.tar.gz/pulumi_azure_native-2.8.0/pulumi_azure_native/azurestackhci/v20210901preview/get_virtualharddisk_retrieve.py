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
    'GetVirtualharddiskRetrieveResult',
    'AwaitableGetVirtualharddiskRetrieveResult',
    'get_virtualharddisk_retrieve',
    'get_virtualharddisk_retrieve_output',
]

@pulumi.output_type
class GetVirtualharddiskRetrieveResult:
    """
    The virtual hard disk resource definition.
    """
    def __init__(__self__, block_size_bytes=None, container_id=None, disk_file_format=None, disk_size_bytes=None, dynamic=None, extended_location=None, hyper_v_generation=None, id=None, location=None, logical_sector_bytes=None, name=None, physical_sector_bytes=None, provisioning_state=None, resource_name=None, status=None, system_data=None, tags=None, type=None):
        if block_size_bytes and not isinstance(block_size_bytes, int):
            raise TypeError("Expected argument 'block_size_bytes' to be a int")
        pulumi.set(__self__, "block_size_bytes", block_size_bytes)
        if container_id and not isinstance(container_id, str):
            raise TypeError("Expected argument 'container_id' to be a str")
        pulumi.set(__self__, "container_id", container_id)
        if disk_file_format and not isinstance(disk_file_format, str):
            raise TypeError("Expected argument 'disk_file_format' to be a str")
        pulumi.set(__self__, "disk_file_format", disk_file_format)
        if disk_size_bytes and not isinstance(disk_size_bytes, float):
            raise TypeError("Expected argument 'disk_size_bytes' to be a float")
        pulumi.set(__self__, "disk_size_bytes", disk_size_bytes)
        if dynamic and not isinstance(dynamic, bool):
            raise TypeError("Expected argument 'dynamic' to be a bool")
        pulumi.set(__self__, "dynamic", dynamic)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if hyper_v_generation and not isinstance(hyper_v_generation, str):
            raise TypeError("Expected argument 'hyper_v_generation' to be a str")
        pulumi.set(__self__, "hyper_v_generation", hyper_v_generation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if logical_sector_bytes and not isinstance(logical_sector_bytes, int):
            raise TypeError("Expected argument 'logical_sector_bytes' to be a int")
        pulumi.set(__self__, "logical_sector_bytes", logical_sector_bytes)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if physical_sector_bytes and not isinstance(physical_sector_bytes, int):
            raise TypeError("Expected argument 'physical_sector_bytes' to be a int")
        pulumi.set(__self__, "physical_sector_bytes", physical_sector_bytes)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_name and not isinstance(resource_name, str):
            raise TypeError("Expected argument 'resource_name' to be a str")
        pulumi.set(__self__, "resource_name", resource_name)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
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
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> Optional[int]:
        return pulumi.get(self, "block_size_bytes")

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[str]:
        """
        Storage ContainerID of the storage container to be used for VHD
        """
        return pulumi.get(self, "container_id")

    @property
    @pulumi.getter(name="diskFileFormat")
    def disk_file_format(self) -> Optional[str]:
        """
        The format of the actual VHD file [vhd, vhdx]
        """
        return pulumi.get(self, "disk_file_format")

    @property
    @pulumi.getter(name="diskSizeBytes")
    def disk_size_bytes(self) -> Optional[float]:
        """
        diskSizeBytes - size of the disk in GB
        """
        return pulumi.get(self, "disk_size_bytes")

    @property
    @pulumi.getter
    def dynamic(self) -> Optional[bool]:
        """
        Boolean for enabling dynamic sizing on the virtual hard disk
        """
        return pulumi.get(self, "dynamic")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> Optional[str]:
        """
        The hypervisor generation of the Virtual Machine [V1, V2]
        """
        return pulumi.get(self, "hyper_v_generation")

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
    @pulumi.getter(name="logicalSectorBytes")
    def logical_sector_bytes(self) -> Optional[int]:
        return pulumi.get(self, "logical_sector_bytes")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="physicalSectorBytes")
    def physical_sector_bytes(self) -> Optional[int]:
        return pulumi.get(self, "physical_sector_bytes")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[str]:
        """
        name of the object to be used in moc
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.VirtualHardDiskStatusResponse':
        """
        VirtualHardDiskStatus defines the observed state of virtualharddisks
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
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


class AwaitableGetVirtualharddiskRetrieveResult(GetVirtualharddiskRetrieveResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualharddiskRetrieveResult(
            block_size_bytes=self.block_size_bytes,
            container_id=self.container_id,
            disk_file_format=self.disk_file_format,
            disk_size_bytes=self.disk_size_bytes,
            dynamic=self.dynamic,
            extended_location=self.extended_location,
            hyper_v_generation=self.hyper_v_generation,
            id=self.id,
            location=self.location,
            logical_sector_bytes=self.logical_sector_bytes,
            name=self.name,
            physical_sector_bytes=self.physical_sector_bytes,
            provisioning_state=self.provisioning_state,
            resource_name=self.resource_name,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_virtualharddisk_retrieve(resource_group_name: Optional[str] = None,
                                 virtualharddisks_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualharddiskRetrieveResult:
    """
    Gets virtualharddisks by resource name


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualharddisksName'] = virtualharddisks_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20210901preview:getVirtualharddiskRetrieve', __args__, opts=opts, typ=GetVirtualharddiskRetrieveResult).value

    return AwaitableGetVirtualharddiskRetrieveResult(
        block_size_bytes=pulumi.get(__ret__, 'block_size_bytes'),
        container_id=pulumi.get(__ret__, 'container_id'),
        disk_file_format=pulumi.get(__ret__, 'disk_file_format'),
        disk_size_bytes=pulumi.get(__ret__, 'disk_size_bytes'),
        dynamic=pulumi.get(__ret__, 'dynamic'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        hyper_v_generation=pulumi.get(__ret__, 'hyper_v_generation'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        logical_sector_bytes=pulumi.get(__ret__, 'logical_sector_bytes'),
        name=pulumi.get(__ret__, 'name'),
        physical_sector_bytes=pulumi.get(__ret__, 'physical_sector_bytes'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_name=pulumi.get(__ret__, 'resource_name'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_virtualharddisk_retrieve)
def get_virtualharddisk_retrieve_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                        virtualharddisks_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualharddiskRetrieveResult]:
    """
    Gets virtualharddisks by resource name


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
