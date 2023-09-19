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
    'GetVirtualMachineInstanceResult',
    'AwaitableGetVirtualMachineInstanceResult',
    'get_virtual_machine_instance',
    'get_virtual_machine_instance_output',
]

@pulumi.output_type
class GetVirtualMachineInstanceResult:
    """
    Define the virtualMachineInstance.
    """
    def __init__(__self__, availability_sets=None, extended_location=None, hardware_profile=None, id=None, infrastructure_profile=None, name=None, network_profile=None, os_profile=None, power_state=None, provisioning_state=None, storage_profile=None, system_data=None, type=None):
        if availability_sets and not isinstance(availability_sets, list):
            raise TypeError("Expected argument 'availability_sets' to be a list")
        pulumi.set(__self__, "availability_sets", availability_sets)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if hardware_profile and not isinstance(hardware_profile, dict):
            raise TypeError("Expected argument 'hardware_profile' to be a dict")
        pulumi.set(__self__, "hardware_profile", hardware_profile)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if infrastructure_profile and not isinstance(infrastructure_profile, dict):
            raise TypeError("Expected argument 'infrastructure_profile' to be a dict")
        pulumi.set(__self__, "infrastructure_profile", infrastructure_profile)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if os_profile and not isinstance(os_profile, dict):
            raise TypeError("Expected argument 'os_profile' to be a dict")
        pulumi.set(__self__, "os_profile", os_profile)
        if power_state and not isinstance(power_state, str):
            raise TypeError("Expected argument 'power_state' to be a str")
        pulumi.set(__self__, "power_state", power_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if storage_profile and not isinstance(storage_profile, dict):
            raise TypeError("Expected argument 'storage_profile' to be a dict")
        pulumi.set(__self__, "storage_profile", storage_profile)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="availabilitySets")
    def availability_sets(self) -> Optional[Sequence['outputs.VirtualMachineInstancePropertiesResponseAvailabilitySets']]:
        """
        Availability Sets in vm.
        """
        return pulumi.get(self, "availability_sets")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        Gets or sets the extended location.
        """
        return pulumi.get(self, "extended_location")

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
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="infrastructureProfile")
    def infrastructure_profile(self) -> Optional['outputs.InfrastructureProfileResponse']:
        """
        Gets the infrastructure profile.
        """
        return pulumi.get(self, "infrastructure_profile")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
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
    def os_profile(self) -> Optional['outputs.OsProfileForVMInstanceResponse']:
        """
        OS properties.
        """
        return pulumi.get(self, "os_profile")

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
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetVirtualMachineInstanceResult(GetVirtualMachineInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineInstanceResult(
            availability_sets=self.availability_sets,
            extended_location=self.extended_location,
            hardware_profile=self.hardware_profile,
            id=self.id,
            infrastructure_profile=self.infrastructure_profile,
            name=self.name,
            network_profile=self.network_profile,
            os_profile=self.os_profile,
            power_state=self.power_state,
            provisioning_state=self.provisioning_state,
            storage_profile=self.storage_profile,
            system_data=self.system_data,
            type=self.type)


def get_virtual_machine_instance(resource_uri: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineInstanceResult:
    """
    Retrieves information about a virtual machine instance.
    Azure REST API version: 2023-04-01-preview.


    :param str resource_uri: The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
    """
    __args__ = dict()
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:scvmm:getVirtualMachineInstance', __args__, opts=opts, typ=GetVirtualMachineInstanceResult).value

    return AwaitableGetVirtualMachineInstanceResult(
        availability_sets=pulumi.get(__ret__, 'availability_sets'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        hardware_profile=pulumi.get(__ret__, 'hardware_profile'),
        id=pulumi.get(__ret__, 'id'),
        infrastructure_profile=pulumi.get(__ret__, 'infrastructure_profile'),
        name=pulumi.get(__ret__, 'name'),
        network_profile=pulumi.get(__ret__, 'network_profile'),
        os_profile=pulumi.get(__ret__, 'os_profile'),
        power_state=pulumi.get(__ret__, 'power_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        storage_profile=pulumi.get(__ret__, 'storage_profile'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_virtual_machine_instance)
def get_virtual_machine_instance_output(resource_uri: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineInstanceResult]:
    """
    Retrieves information about a virtual machine instance.
    Azure REST API version: 2023-04-01-preview.


    :param str resource_uri: The fully qualified Azure Resource manager identifier of the Hybrid Compute machine resource to be extended.
    """
    ...
