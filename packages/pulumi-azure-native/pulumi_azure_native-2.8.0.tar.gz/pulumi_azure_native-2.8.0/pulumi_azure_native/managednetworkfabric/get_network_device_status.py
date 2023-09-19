# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetNetworkDeviceStatusResult',
    'AwaitableGetNetworkDeviceStatusResult',
    'get_network_device_status',
    'get_network_device_status_output',
]

@pulumi.output_type
class GetNetworkDeviceStatusResult:
    """
    Get Device status response properties.
    """
    def __init__(__self__, operational_status=None, power_cycle_state=None, serial_number=None):
        if operational_status and not isinstance(operational_status, str):
            raise TypeError("Expected argument 'operational_status' to be a str")
        pulumi.set(__self__, "operational_status", operational_status)
        if power_cycle_state and not isinstance(power_cycle_state, str):
            raise TypeError("Expected argument 'power_cycle_state' to be a str")
        pulumi.set(__self__, "power_cycle_state", power_cycle_state)
        if serial_number and not isinstance(serial_number, str):
            raise TypeError("Expected argument 'serial_number' to be a str")
        pulumi.set(__self__, "serial_number", serial_number)

    @property
    @pulumi.getter(name="operationalStatus")
    def operational_status(self) -> str:
        """
        Primary or Secondary power end.
        """
        return pulumi.get(self, "operational_status")

    @property
    @pulumi.getter(name="powerCycleState")
    def power_cycle_state(self) -> str:
        """
        On or Off power cycle state.
        """
        return pulumi.get(self, "power_cycle_state")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> str:
        """
        The serial number of the device
        """
        return pulumi.get(self, "serial_number")


class AwaitableGetNetworkDeviceStatusResult(GetNetworkDeviceStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkDeviceStatusResult(
            operational_status=self.operational_status,
            power_cycle_state=self.power_cycle_state,
            serial_number=self.serial_number)


def get_network_device_status(network_device_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkDeviceStatusResult:
    """
    Get the running status of the Network Device.
    Azure REST API version: 2023-02-01-preview.


    :param str network_device_name: Name of the NetworkDevice.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['networkDeviceName'] = network_device_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric:getNetworkDeviceStatus', __args__, opts=opts, typ=GetNetworkDeviceStatusResult).value

    return AwaitableGetNetworkDeviceStatusResult(
        operational_status=pulumi.get(__ret__, 'operational_status'),
        power_cycle_state=pulumi.get(__ret__, 'power_cycle_state'),
        serial_number=pulumi.get(__ret__, 'serial_number'))


@_utilities.lift_output_func(get_network_device_status)
def get_network_device_status_output(network_device_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkDeviceStatusResult]:
    """
    Get the running status of the Network Device.
    Azure REST API version: 2023-02-01-preview.


    :param str network_device_name: Name of the NetworkDevice.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
