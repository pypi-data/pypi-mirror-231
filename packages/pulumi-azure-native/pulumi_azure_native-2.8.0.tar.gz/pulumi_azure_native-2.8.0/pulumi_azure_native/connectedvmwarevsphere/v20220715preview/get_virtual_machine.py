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
    'GetVirtualMachineResult',
    'AwaitableGetVirtualMachineResult',
    'get_virtual_machine',
    'get_virtual_machine_output',
]

@pulumi.output_type
class GetVirtualMachineResult:
    """
    Define the virtualMachine.
    """
    def __init__(__self__, custom_resource_name=None, extended_location=None, firmware_type=None, folder_path=None, guest_agent_profile=None, hardware_profile=None, id=None, identity=None, instance_uuid=None, inventory_item_id=None, kind=None, location=None, mo_name=None, mo_ref_id=None, name=None, network_profile=None, os_profile=None, placement_profile=None, power_state=None, provisioning_state=None, resource_pool_id=None, security_profile=None, smbios_uuid=None, statuses=None, storage_profile=None, system_data=None, tags=None, template_id=None, type=None, uuid=None, v_center_id=None, vm_id=None):
        if custom_resource_name and not isinstance(custom_resource_name, str):
            raise TypeError("Expected argument 'custom_resource_name' to be a str")
        pulumi.set(__self__, "custom_resource_name", custom_resource_name)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if firmware_type and not isinstance(firmware_type, str):
            raise TypeError("Expected argument 'firmware_type' to be a str")
        pulumi.set(__self__, "firmware_type", firmware_type)
        if folder_path and not isinstance(folder_path, str):
            raise TypeError("Expected argument 'folder_path' to be a str")
        pulumi.set(__self__, "folder_path", folder_path)
        if guest_agent_profile and not isinstance(guest_agent_profile, dict):
            raise TypeError("Expected argument 'guest_agent_profile' to be a dict")
        pulumi.set(__self__, "guest_agent_profile", guest_agent_profile)
        if hardware_profile and not isinstance(hardware_profile, dict):
            raise TypeError("Expected argument 'hardware_profile' to be a dict")
        pulumi.set(__self__, "hardware_profile", hardware_profile)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if instance_uuid and not isinstance(instance_uuid, str):
            raise TypeError("Expected argument 'instance_uuid' to be a str")
        pulumi.set(__self__, "instance_uuid", instance_uuid)
        if inventory_item_id and not isinstance(inventory_item_id, str):
            raise TypeError("Expected argument 'inventory_item_id' to be a str")
        pulumi.set(__self__, "inventory_item_id", inventory_item_id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mo_name and not isinstance(mo_name, str):
            raise TypeError("Expected argument 'mo_name' to be a str")
        pulumi.set(__self__, "mo_name", mo_name)
        if mo_ref_id and not isinstance(mo_ref_id, str):
            raise TypeError("Expected argument 'mo_ref_id' to be a str")
        pulumi.set(__self__, "mo_ref_id", mo_ref_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if os_profile and not isinstance(os_profile, dict):
            raise TypeError("Expected argument 'os_profile' to be a dict")
        pulumi.set(__self__, "os_profile", os_profile)
        if placement_profile and not isinstance(placement_profile, dict):
            raise TypeError("Expected argument 'placement_profile' to be a dict")
        pulumi.set(__self__, "placement_profile", placement_profile)
        if power_state and not isinstance(power_state, str):
            raise TypeError("Expected argument 'power_state' to be a str")
        pulumi.set(__self__, "power_state", power_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_pool_id and not isinstance(resource_pool_id, str):
            raise TypeError("Expected argument 'resource_pool_id' to be a str")
        pulumi.set(__self__, "resource_pool_id", resource_pool_id)
        if security_profile and not isinstance(security_profile, dict):
            raise TypeError("Expected argument 'security_profile' to be a dict")
        pulumi.set(__self__, "security_profile", security_profile)
        if smbios_uuid and not isinstance(smbios_uuid, str):
            raise TypeError("Expected argument 'smbios_uuid' to be a str")
        pulumi.set(__self__, "smbios_uuid", smbios_uuid)
        if statuses and not isinstance(statuses, list):
            raise TypeError("Expected argument 'statuses' to be a list")
        pulumi.set(__self__, "statuses", statuses)
        if storage_profile and not isinstance(storage_profile, dict):
            raise TypeError("Expected argument 'storage_profile' to be a dict")
        pulumi.set(__self__, "storage_profile", storage_profile)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if template_id and not isinstance(template_id, str):
            raise TypeError("Expected argument 'template_id' to be a str")
        pulumi.set(__self__, "template_id", template_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if v_center_id and not isinstance(v_center_id, str):
            raise TypeError("Expected argument 'v_center_id' to be a str")
        pulumi.set(__self__, "v_center_id", v_center_id)
        if vm_id and not isinstance(vm_id, str):
            raise TypeError("Expected argument 'vm_id' to be a str")
        pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> str:
        """
        Gets the name of the corresponding resource in Kubernetes.
        """
        return pulumi.get(self, "custom_resource_name")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        Gets or sets the extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> Optional[str]:
        """
        Firmware type
        """
        return pulumi.get(self, "firmware_type")

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> str:
        """
        Gets or sets the folder path of the vm.
        """
        return pulumi.get(self, "folder_path")

    @property
    @pulumi.getter(name="guestAgentProfile")
    def guest_agent_profile(self) -> Optional['outputs.GuestAgentProfileResponse']:
        """
        Guest agent status properties.
        """
        return pulumi.get(self, "guest_agent_profile")

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional['outputs.HardwareProfileResponse']:
        """
        Hardware properties.
        """
        return pulumi.get(self, "hardware_profile")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Gets or sets the Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="instanceUuid")
    def instance_uuid(self) -> str:
        """
        Gets or sets the instance uuid of the vm.
        """
        return pulumi.get(self, "instance_uuid")

    @property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[str]:
        """
        Gets or sets the inventory Item ID for the virtual machine.
        """
        return pulumi.get(self, "inventory_item_id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="moName")
    def mo_name(self) -> str:
        """
        Gets or sets the vCenter Managed Object name for the virtual machine.
        """
        return pulumi.get(self, "mo_name")

    @property
    @pulumi.getter(name="moRefId")
    def mo_ref_id(self) -> Optional[str]:
        """
        Gets or sets the vCenter MoRef (Managed Object Reference) ID for the virtual machine.
        """
        return pulumi.get(self, "mo_ref_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets or sets the name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional['outputs.NetworkProfileResponse']:
        """
        Network properties.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional['outputs.OsProfileResponse']:
        """
        OS properties.
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter(name="placementProfile")
    def placement_profile(self) -> Optional['outputs.PlacementProfileResponse']:
        """
        Placement properties.
        """
        return pulumi.get(self, "placement_profile")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> str:
        """
        Gets the power state of the virtual machine.
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourcePoolId")
    def resource_pool_id(self) -> Optional[str]:
        """
        Gets or sets the ARM Id of the resourcePool resource on which this virtual machine will
        deploy.
        """
        return pulumi.get(self, "resource_pool_id")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional['outputs.SecurityProfileResponse']:
        """
        Gets the security profile.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter(name="smbiosUuid")
    def smbios_uuid(self) -> Optional[str]:
        """
        Gets or sets the SMBIOS UUID of the vm.
        """
        return pulumi.get(self, "smbios_uuid")

    @property
    @pulumi.getter
    def statuses(self) -> Sequence['outputs.ResourceStatusResponse']:
        """
        The resource status information.
        """
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional['outputs.StorageProfileResponse']:
        """
        Storage properties.
        """
        return pulumi.get(self, "storage_profile")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Gets or sets the Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[str]:
        """
        Gets or sets the ARM Id of the template resource to deploy the virtual machine.
        """
        return pulumi.get(self, "template_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets or sets the type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        Gets or sets a unique identifier for this resource.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter(name="vCenterId")
    def v_center_id(self) -> Optional[str]:
        """
        Gets or sets the ARM Id of the vCenter resource in which this resource pool resides.
        """
        return pulumi.get(self, "v_center_id")

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> str:
        """
        Gets or sets a unique identifier for the vm resource.
        """
        return pulumi.get(self, "vm_id")


class AwaitableGetVirtualMachineResult(GetVirtualMachineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineResult(
            custom_resource_name=self.custom_resource_name,
            extended_location=self.extended_location,
            firmware_type=self.firmware_type,
            folder_path=self.folder_path,
            guest_agent_profile=self.guest_agent_profile,
            hardware_profile=self.hardware_profile,
            id=self.id,
            identity=self.identity,
            instance_uuid=self.instance_uuid,
            inventory_item_id=self.inventory_item_id,
            kind=self.kind,
            location=self.location,
            mo_name=self.mo_name,
            mo_ref_id=self.mo_ref_id,
            name=self.name,
            network_profile=self.network_profile,
            os_profile=self.os_profile,
            placement_profile=self.placement_profile,
            power_state=self.power_state,
            provisioning_state=self.provisioning_state,
            resource_pool_id=self.resource_pool_id,
            security_profile=self.security_profile,
            smbios_uuid=self.smbios_uuid,
            statuses=self.statuses,
            storage_profile=self.storage_profile,
            system_data=self.system_data,
            tags=self.tags,
            template_id=self.template_id,
            type=self.type,
            uuid=self.uuid,
            v_center_id=self.v_center_id,
            vm_id=self.vm_id)


def get_virtual_machine(resource_group_name: Optional[str] = None,
                        virtual_machine_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineResult:
    """
    Implements virtual machine GET method.


    :param str resource_group_name: The Resource Group Name.
    :param str virtual_machine_name: Name of the virtual machine resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualMachineName'] = virtual_machine_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:connectedvmwarevsphere/v20220715preview:getVirtualMachine', __args__, opts=opts, typ=GetVirtualMachineResult).value

    return AwaitableGetVirtualMachineResult(
        custom_resource_name=pulumi.get(__ret__, 'custom_resource_name'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        firmware_type=pulumi.get(__ret__, 'firmware_type'),
        folder_path=pulumi.get(__ret__, 'folder_path'),
        guest_agent_profile=pulumi.get(__ret__, 'guest_agent_profile'),
        hardware_profile=pulumi.get(__ret__, 'hardware_profile'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        instance_uuid=pulumi.get(__ret__, 'instance_uuid'),
        inventory_item_id=pulumi.get(__ret__, 'inventory_item_id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        mo_name=pulumi.get(__ret__, 'mo_name'),
        mo_ref_id=pulumi.get(__ret__, 'mo_ref_id'),
        name=pulumi.get(__ret__, 'name'),
        network_profile=pulumi.get(__ret__, 'network_profile'),
        os_profile=pulumi.get(__ret__, 'os_profile'),
        placement_profile=pulumi.get(__ret__, 'placement_profile'),
        power_state=pulumi.get(__ret__, 'power_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_pool_id=pulumi.get(__ret__, 'resource_pool_id'),
        security_profile=pulumi.get(__ret__, 'security_profile'),
        smbios_uuid=pulumi.get(__ret__, 'smbios_uuid'),
        statuses=pulumi.get(__ret__, 'statuses'),
        storage_profile=pulumi.get(__ret__, 'storage_profile'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        template_id=pulumi.get(__ret__, 'template_id'),
        type=pulumi.get(__ret__, 'type'),
        uuid=pulumi.get(__ret__, 'uuid'),
        v_center_id=pulumi.get(__ret__, 'v_center_id'),
        vm_id=pulumi.get(__ret__, 'vm_id'))


@_utilities.lift_output_func(get_virtual_machine)
def get_virtual_machine_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                               virtual_machine_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineResult]:
    """
    Implements virtual machine GET method.


    :param str resource_group_name: The Resource Group Name.
    :param str virtual_machine_name: Name of the virtual machine resource.
    """
    ...
