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
from ._inputs import *

__all__ = ['BareMetalMachineArgs', 'BareMetalMachine']

@pulumi.input_type
class BareMetalMachineArgs:
    def __init__(__self__, *,
                 bmc_connection_string: pulumi.Input[str],
                 bmc_credentials: pulumi.Input['AdministrativeCredentialsArgs'],
                 bmc_mac_address: pulumi.Input[str],
                 boot_mac_address: pulumi.Input[str],
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 machine_details: pulumi.Input[str],
                 machine_name: pulumi.Input[str],
                 machine_sku_id: pulumi.Input[str],
                 rack_id: pulumi.Input[str],
                 rack_slot: pulumi.Input[float],
                 resource_group_name: pulumi.Input[str],
                 serial_number: pulumi.Input[str],
                 bare_metal_machine_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a BareMetalMachine resource.
        :param pulumi.Input[str] bmc_connection_string: The connection string for the baseboard management controller including IP address and protocol.
        :param pulumi.Input['AdministrativeCredentialsArgs'] bmc_credentials: The credentials of the baseboard management controller on this bare metal machine.
        :param pulumi.Input[str] bmc_mac_address: The MAC address of the BMC device.
        :param pulumi.Input[str] boot_mac_address: The MAC address of a NIC connected to the PXE network.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[str] machine_details: The custom details provided by the customer.
        :param pulumi.Input[str] machine_name: The OS-level hostname assigned to this machine.
        :param pulumi.Input[str] machine_sku_id: The unique internal identifier of the bare metal machine SKU.
        :param pulumi.Input[str] rack_id: The resource ID of the rack where this bare metal machine resides.
        :param pulumi.Input[float] rack_slot: The rack slot in which this bare metal machine is located, ordered from the bottom up i.e. the lowest slot is 1.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] serial_number: The serial number of the bare metal machine.
        :param pulumi.Input[str] bare_metal_machine_name: The name of the bare metal machine.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "bmc_connection_string", bmc_connection_string)
        pulumi.set(__self__, "bmc_credentials", bmc_credentials)
        pulumi.set(__self__, "bmc_mac_address", bmc_mac_address)
        pulumi.set(__self__, "boot_mac_address", boot_mac_address)
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "machine_details", machine_details)
        pulumi.set(__self__, "machine_name", machine_name)
        pulumi.set(__self__, "machine_sku_id", machine_sku_id)
        pulumi.set(__self__, "rack_id", rack_id)
        pulumi.set(__self__, "rack_slot", rack_slot)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "serial_number", serial_number)
        if bare_metal_machine_name is not None:
            pulumi.set(__self__, "bare_metal_machine_name", bare_metal_machine_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="bmcConnectionString")
    def bmc_connection_string(self) -> pulumi.Input[str]:
        """
        The connection string for the baseboard management controller including IP address and protocol.
        """
        return pulumi.get(self, "bmc_connection_string")

    @bmc_connection_string.setter
    def bmc_connection_string(self, value: pulumi.Input[str]):
        pulumi.set(self, "bmc_connection_string", value)

    @property
    @pulumi.getter(name="bmcCredentials")
    def bmc_credentials(self) -> pulumi.Input['AdministrativeCredentialsArgs']:
        """
        The credentials of the baseboard management controller on this bare metal machine.
        """
        return pulumi.get(self, "bmc_credentials")

    @bmc_credentials.setter
    def bmc_credentials(self, value: pulumi.Input['AdministrativeCredentialsArgs']):
        pulumi.set(self, "bmc_credentials", value)

    @property
    @pulumi.getter(name="bmcMacAddress")
    def bmc_mac_address(self) -> pulumi.Input[str]:
        """
        The MAC address of the BMC device.
        """
        return pulumi.get(self, "bmc_mac_address")

    @bmc_mac_address.setter
    def bmc_mac_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "bmc_mac_address", value)

    @property
    @pulumi.getter(name="bootMacAddress")
    def boot_mac_address(self) -> pulumi.Input[str]:
        """
        The MAC address of a NIC connected to the PXE network.
        """
        return pulumi.get(self, "boot_mac_address")

    @boot_mac_address.setter
    def boot_mac_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "boot_mac_address", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="machineDetails")
    def machine_details(self) -> pulumi.Input[str]:
        """
        The custom details provided by the customer.
        """
        return pulumi.get(self, "machine_details")

    @machine_details.setter
    def machine_details(self, value: pulumi.Input[str]):
        pulumi.set(self, "machine_details", value)

    @property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> pulumi.Input[str]:
        """
        The OS-level hostname assigned to this machine.
        """
        return pulumi.get(self, "machine_name")

    @machine_name.setter
    def machine_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "machine_name", value)

    @property
    @pulumi.getter(name="machineSkuId")
    def machine_sku_id(self) -> pulumi.Input[str]:
        """
        The unique internal identifier of the bare metal machine SKU.
        """
        return pulumi.get(self, "machine_sku_id")

    @machine_sku_id.setter
    def machine_sku_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "machine_sku_id", value)

    @property
    @pulumi.getter(name="rackId")
    def rack_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the rack where this bare metal machine resides.
        """
        return pulumi.get(self, "rack_id")

    @rack_id.setter
    def rack_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rack_id", value)

    @property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> pulumi.Input[float]:
        """
        The rack slot in which this bare metal machine is located, ordered from the bottom up i.e. the lowest slot is 1.
        """
        return pulumi.get(self, "rack_slot")

    @rack_slot.setter
    def rack_slot(self, value: pulumi.Input[float]):
        pulumi.set(self, "rack_slot", value)

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
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Input[str]:
        """
        The serial number of the bare metal machine.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: pulumi.Input[str]):
        pulumi.set(self, "serial_number", value)

    @property
    @pulumi.getter(name="bareMetalMachineName")
    def bare_metal_machine_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the bare metal machine.
        """
        return pulumi.get(self, "bare_metal_machine_name")

    @bare_metal_machine_name.setter
    def bare_metal_machine_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bare_metal_machine_name", value)

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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class BareMetalMachine(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bare_metal_machine_name: Optional[pulumi.Input[str]] = None,
                 bmc_connection_string: Optional[pulumi.Input[str]] = None,
                 bmc_credentials: Optional[pulumi.Input[pulumi.InputType['AdministrativeCredentialsArgs']]] = None,
                 bmc_mac_address: Optional[pulumi.Input[str]] = None,
                 boot_mac_address: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 machine_details: Optional[pulumi.Input[str]] = None,
                 machine_name: Optional[pulumi.Input[str]] = None,
                 machine_sku_id: Optional[pulumi.Input[str]] = None,
                 rack_id: Optional[pulumi.Input[str]] = None,
                 rack_slot: Optional[pulumi.Input[float]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a BareMetalMachine resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bare_metal_machine_name: The name of the bare metal machine.
        :param pulumi.Input[str] bmc_connection_string: The connection string for the baseboard management controller including IP address and protocol.
        :param pulumi.Input[pulumi.InputType['AdministrativeCredentialsArgs']] bmc_credentials: The credentials of the baseboard management controller on this bare metal machine.
        :param pulumi.Input[str] bmc_mac_address: The MAC address of the BMC device.
        :param pulumi.Input[str] boot_mac_address: The MAC address of a NIC connected to the PXE network.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] machine_details: The custom details provided by the customer.
        :param pulumi.Input[str] machine_name: The OS-level hostname assigned to this machine.
        :param pulumi.Input[str] machine_sku_id: The unique internal identifier of the bare metal machine SKU.
        :param pulumi.Input[str] rack_id: The resource ID of the rack where this bare metal machine resides.
        :param pulumi.Input[float] rack_slot: The rack slot in which this bare metal machine is located, ordered from the bottom up i.e. the lowest slot is 1.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] serial_number: The serial number of the bare metal machine.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BareMetalMachineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a BareMetalMachine resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param BareMetalMachineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BareMetalMachineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bare_metal_machine_name: Optional[pulumi.Input[str]] = None,
                 bmc_connection_string: Optional[pulumi.Input[str]] = None,
                 bmc_credentials: Optional[pulumi.Input[pulumi.InputType['AdministrativeCredentialsArgs']]] = None,
                 bmc_mac_address: Optional[pulumi.Input[str]] = None,
                 boot_mac_address: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 machine_details: Optional[pulumi.Input[str]] = None,
                 machine_name: Optional[pulumi.Input[str]] = None,
                 machine_sku_id: Optional[pulumi.Input[str]] = None,
                 rack_id: Optional[pulumi.Input[str]] = None,
                 rack_slot: Optional[pulumi.Input[float]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BareMetalMachineArgs.__new__(BareMetalMachineArgs)

            __props__.__dict__["bare_metal_machine_name"] = bare_metal_machine_name
            if bmc_connection_string is None and not opts.urn:
                raise TypeError("Missing required property 'bmc_connection_string'")
            __props__.__dict__["bmc_connection_string"] = bmc_connection_string
            if bmc_credentials is None and not opts.urn:
                raise TypeError("Missing required property 'bmc_credentials'")
            __props__.__dict__["bmc_credentials"] = bmc_credentials
            if bmc_mac_address is None and not opts.urn:
                raise TypeError("Missing required property 'bmc_mac_address'")
            __props__.__dict__["bmc_mac_address"] = bmc_mac_address
            if boot_mac_address is None and not opts.urn:
                raise TypeError("Missing required property 'boot_mac_address'")
            __props__.__dict__["boot_mac_address"] = boot_mac_address
            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            if machine_details is None and not opts.urn:
                raise TypeError("Missing required property 'machine_details'")
            __props__.__dict__["machine_details"] = machine_details
            if machine_name is None and not opts.urn:
                raise TypeError("Missing required property 'machine_name'")
            __props__.__dict__["machine_name"] = machine_name
            if machine_sku_id is None and not opts.urn:
                raise TypeError("Missing required property 'machine_sku_id'")
            __props__.__dict__["machine_sku_id"] = machine_sku_id
            if rack_id is None and not opts.urn:
                raise TypeError("Missing required property 'rack_id'")
            __props__.__dict__["rack_id"] = rack_id
            if rack_slot is None and not opts.urn:
                raise TypeError("Missing required property 'rack_slot'")
            __props__.__dict__["rack_slot"] = rack_slot
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if serial_number is None and not opts.urn:
                raise TypeError("Missing required property 'serial_number'")
            __props__.__dict__["serial_number"] = serial_number
            __props__.__dict__["tags"] = tags
            __props__.__dict__["associated_resource_ids"] = None
            __props__.__dict__["cluster_id"] = None
            __props__.__dict__["cordon_status"] = None
            __props__.__dict__["detailed_status"] = None
            __props__.__dict__["detailed_status_message"] = None
            __props__.__dict__["hardware_inventory"] = None
            __props__.__dict__["hardware_validation_status"] = None
            __props__.__dict__["hybrid_aks_clusters_associated_ids"] = None
            __props__.__dict__["kubernetes_node_name"] = None
            __props__.__dict__["kubernetes_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["oam_ipv4_address"] = None
            __props__.__dict__["oam_ipv6_address"] = None
            __props__.__dict__["os_image"] = None
            __props__.__dict__["power_state"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["ready_state"] = None
            __props__.__dict__["service_tag"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["virtual_machines_associated_ids"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkcloud:BareMetalMachine"), pulumi.Alias(type_="azure-native:networkcloud/v20221212preview:BareMetalMachine"), pulumi.Alias(type_="azure-native:networkcloud/v20230501preview:BareMetalMachine")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BareMetalMachine, __self__).__init__(
            'azure-native:networkcloud/v20230701:BareMetalMachine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BareMetalMachine':
        """
        Get an existing BareMetalMachine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BareMetalMachineArgs.__new__(BareMetalMachineArgs)

        __props__.__dict__["associated_resource_ids"] = None
        __props__.__dict__["bmc_connection_string"] = None
        __props__.__dict__["bmc_credentials"] = None
        __props__.__dict__["bmc_mac_address"] = None
        __props__.__dict__["boot_mac_address"] = None
        __props__.__dict__["cluster_id"] = None
        __props__.__dict__["cordon_status"] = None
        __props__.__dict__["detailed_status"] = None
        __props__.__dict__["detailed_status_message"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["hardware_inventory"] = None
        __props__.__dict__["hardware_validation_status"] = None
        __props__.__dict__["hybrid_aks_clusters_associated_ids"] = None
        __props__.__dict__["kubernetes_node_name"] = None
        __props__.__dict__["kubernetes_version"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["machine_details"] = None
        __props__.__dict__["machine_name"] = None
        __props__.__dict__["machine_sku_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["oam_ipv4_address"] = None
        __props__.__dict__["oam_ipv6_address"] = None
        __props__.__dict__["os_image"] = None
        __props__.__dict__["power_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rack_id"] = None
        __props__.__dict__["rack_slot"] = None
        __props__.__dict__["ready_state"] = None
        __props__.__dict__["serial_number"] = None
        __props__.__dict__["service_tag"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_machines_associated_ids"] = None
        return BareMetalMachine(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associatedResourceIds")
    def associated_resource_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of resource IDs for the other Microsoft.NetworkCloud resources that have attached this network.
        """
        return pulumi.get(self, "associated_resource_ids")

    @property
    @pulumi.getter(name="bmcConnectionString")
    def bmc_connection_string(self) -> pulumi.Output[str]:
        """
        The connection string for the baseboard management controller including IP address and protocol.
        """
        return pulumi.get(self, "bmc_connection_string")

    @property
    @pulumi.getter(name="bmcCredentials")
    def bmc_credentials(self) -> pulumi.Output['outputs.AdministrativeCredentialsResponse']:
        """
        The credentials of the baseboard management controller on this bare metal machine.
        """
        return pulumi.get(self, "bmc_credentials")

    @property
    @pulumi.getter(name="bmcMacAddress")
    def bmc_mac_address(self) -> pulumi.Output[str]:
        """
        The MAC address of the BMC device.
        """
        return pulumi.get(self, "bmc_mac_address")

    @property
    @pulumi.getter(name="bootMacAddress")
    def boot_mac_address(self) -> pulumi.Output[str]:
        """
        The MAC address of a NIC connected to the PXE network.
        """
        return pulumi.get(self, "boot_mac_address")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the cluster this bare metal machine is associated with.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="cordonStatus")
    def cordon_status(self) -> pulumi.Output[str]:
        """
        The cordon status of the bare metal machine.
        """
        return pulumi.get(self, "cordon_status")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[str]:
        """
        The more detailed status of the bare metal machine.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[str]:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hardwareInventory")
    def hardware_inventory(self) -> pulumi.Output['outputs.HardwareInventoryResponse']:
        """
        The hardware inventory, including information acquired from the model/sku information and from the ironic inspector.
        """
        return pulumi.get(self, "hardware_inventory")

    @property
    @pulumi.getter(name="hardwareValidationStatus")
    def hardware_validation_status(self) -> pulumi.Output['outputs.HardwareValidationStatusResponse']:
        """
        The details of the latest hardware validation performed for this bare metal machine.
        """
        return pulumi.get(self, "hardware_validation_status")

    @property
    @pulumi.getter(name="hybridAksClustersAssociatedIds")
    def hybrid_aks_clusters_associated_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Field Deprecated. These fields will be empty/omitted. The list of the resource IDs for the HybridAksClusters that have nodes hosted on this bare metal machine.
        """
        return pulumi.get(self, "hybrid_aks_clusters_associated_ids")

    @property
    @pulumi.getter(name="kubernetesNodeName")
    def kubernetes_node_name(self) -> pulumi.Output[str]:
        """
        The name of this machine represented by the host object in the Cluster's Kubernetes control plane.
        """
        return pulumi.get(self, "kubernetes_node_name")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> pulumi.Output[str]:
        """
        The version of Kubernetes running on this machine.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="machineDetails")
    def machine_details(self) -> pulumi.Output[str]:
        """
        The custom details provided by the customer.
        """
        return pulumi.get(self, "machine_details")

    @property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> pulumi.Output[str]:
        """
        The OS-level hostname assigned to this machine.
        """
        return pulumi.get(self, "machine_name")

    @property
    @pulumi.getter(name="machineSkuId")
    def machine_sku_id(self) -> pulumi.Output[str]:
        """
        The unique internal identifier of the bare metal machine SKU.
        """
        return pulumi.get(self, "machine_sku_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oamIpv4Address")
    def oam_ipv4_address(self) -> pulumi.Output[str]:
        """
        The IPv4 address that is assigned to the bare metal machine during the cluster deployment.
        """
        return pulumi.get(self, "oam_ipv4_address")

    @property
    @pulumi.getter(name="oamIpv6Address")
    def oam_ipv6_address(self) -> pulumi.Output[str]:
        """
        The IPv6 address that is assigned to the bare metal machine during the cluster deployment.
        """
        return pulumi.get(self, "oam_ipv6_address")

    @property
    @pulumi.getter(name="osImage")
    def os_image(self) -> pulumi.Output[str]:
        """
        The image that is currently provisioned to the OS disk.
        """
        return pulumi.get(self, "os_image")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> pulumi.Output[str]:
        """
        The power state derived from the baseboard management controller.
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the bare metal machine.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rackId")
    def rack_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the rack where this bare metal machine resides.
        """
        return pulumi.get(self, "rack_id")

    @property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> pulumi.Output[float]:
        """
        The rack slot in which this bare metal machine is located, ordered from the bottom up i.e. the lowest slot is 1.
        """
        return pulumi.get(self, "rack_slot")

    @property
    @pulumi.getter(name="readyState")
    def ready_state(self) -> pulumi.Output[str]:
        """
        The indicator of whether the bare metal machine is ready to receive workloads.
        """
        return pulumi.get(self, "ready_state")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[str]:
        """
        The serial number of the bare metal machine.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter(name="serviceTag")
    def service_tag(self) -> pulumi.Output[str]:
        """
        The discovered value of the machine's service tag.
        """
        return pulumi.get(self, "service_tag")

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

    @property
    @pulumi.getter(name="virtualMachinesAssociatedIds")
    def virtual_machines_associated_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Field Deprecated. These fields will be empty/omitted. The list of the resource IDs for the VirtualMachines that are hosted on this bare metal machine.
        """
        return pulumi.get(self, "virtual_machines_associated_ids")

