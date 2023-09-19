# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AdministrativeCredentialsArgs',
    'BareMetalMachineConfigurationDataArgs',
    'BgpPeerArgs',
    'CniBgpConfigurationArgs',
    'CommunityAdvertisementArgs',
    'ExtendedLocationArgs',
    'ManagedResourceGroupConfigurationArgs',
    'RackDefinitionArgs',
    'ServicePrincipalInformationArgs',
    'StorageApplianceConfigurationDataArgs',
    'ValidationThresholdArgs',
]

@pulumi.input_type
class AdministrativeCredentialsArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        :param pulumi.Input[str] password: The password of the administrator of the device used during initialization.
        :param pulumi.Input[str] username: The username of the administrator of the device used during initialization.
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password of the administrator of the device used during initialization.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The username of the administrator of the device used during initialization.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class BareMetalMachineConfigurationDataArgs:
    def __init__(__self__, *,
                 bmc_credentials: pulumi.Input['AdministrativeCredentialsArgs'],
                 bmc_mac_address: pulumi.Input[str],
                 boot_mac_address: pulumi.Input[str],
                 rack_slot: pulumi.Input[float],
                 serial_number: pulumi.Input[str],
                 machine_details: Optional[pulumi.Input[str]] = None,
                 machine_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['AdministrativeCredentialsArgs'] bmc_credentials: The credentials of the baseboard management controller on this bare metal machine.
        :param pulumi.Input[str] bmc_mac_address: The MAC address of the BMC for this machine.
        :param pulumi.Input[str] boot_mac_address: The MAC address associated with the PXE NIC card.
        :param pulumi.Input[float] rack_slot: The slot the physical machine is in the rack based on the BOM configuration.
        :param pulumi.Input[str] serial_number: The serial number of the machine. Hardware suppliers may use an alternate value. For example, service tag.
        :param pulumi.Input[str] machine_details: The free-form additional information about the machine, e.g. an asset tag.
        :param pulumi.Input[str] machine_name: The user-provided name for the bare metal machine created from this specification.
               If not provided, the machine name will be generated programmatically.
        """
        pulumi.set(__self__, "bmc_credentials", bmc_credentials)
        pulumi.set(__self__, "bmc_mac_address", bmc_mac_address)
        pulumi.set(__self__, "boot_mac_address", boot_mac_address)
        pulumi.set(__self__, "rack_slot", rack_slot)
        pulumi.set(__self__, "serial_number", serial_number)
        if machine_details is not None:
            pulumi.set(__self__, "machine_details", machine_details)
        if machine_name is not None:
            pulumi.set(__self__, "machine_name", machine_name)

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
        The MAC address of the BMC for this machine.
        """
        return pulumi.get(self, "bmc_mac_address")

    @bmc_mac_address.setter
    def bmc_mac_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "bmc_mac_address", value)

    @property
    @pulumi.getter(name="bootMacAddress")
    def boot_mac_address(self) -> pulumi.Input[str]:
        """
        The MAC address associated with the PXE NIC card.
        """
        return pulumi.get(self, "boot_mac_address")

    @boot_mac_address.setter
    def boot_mac_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "boot_mac_address", value)

    @property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> pulumi.Input[float]:
        """
        The slot the physical machine is in the rack based on the BOM configuration.
        """
        return pulumi.get(self, "rack_slot")

    @rack_slot.setter
    def rack_slot(self, value: pulumi.Input[float]):
        pulumi.set(self, "rack_slot", value)

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Input[str]:
        """
        The serial number of the machine. Hardware suppliers may use an alternate value. For example, service tag.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: pulumi.Input[str]):
        pulumi.set(self, "serial_number", value)

    @property
    @pulumi.getter(name="machineDetails")
    def machine_details(self) -> Optional[pulumi.Input[str]]:
        """
        The free-form additional information about the machine, e.g. an asset tag.
        """
        return pulumi.get(self, "machine_details")

    @machine_details.setter
    def machine_details(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "machine_details", value)

    @property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user-provided name for the bare metal machine created from this specification.
        If not provided, the machine name will be generated programmatically.
        """
        return pulumi.get(self, "machine_name")

    @machine_name.setter
    def machine_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "machine_name", value)


@pulumi.input_type
class BgpPeerArgs:
    def __init__(__self__, *,
                 as_number: pulumi.Input[float],
                 peer_ip: pulumi.Input[str],
                 password: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[float] as_number: The ASN (Autonomous System Number) of the BGP peer.
        :param pulumi.Input[str] peer_ip: The IPv4 or IPv6 address to peer with the associated CNI Network. The IP version type will drive a peering with the same version type from the Default CNI Network. For example, IPv4 to IPv4 or IPv6 to IPv6.
        :param pulumi.Input[str] password: The password for this peering neighbor. It defaults to no password if not specified.
        """
        pulumi.set(__self__, "as_number", as_number)
        pulumi.set(__self__, "peer_ip", peer_ip)
        if password is not None:
            pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter(name="asNumber")
    def as_number(self) -> pulumi.Input[float]:
        """
        The ASN (Autonomous System Number) of the BGP peer.
        """
        return pulumi.get(self, "as_number")

    @as_number.setter
    def as_number(self, value: pulumi.Input[float]):
        pulumi.set(self, "as_number", value)

    @property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> pulumi.Input[str]:
        """
        The IPv4 or IPv6 address to peer with the associated CNI Network. The IP version type will drive a peering with the same version type from the Default CNI Network. For example, IPv4 to IPv4 or IPv6 to IPv6.
        """
        return pulumi.get(self, "peer_ip")

    @peer_ip.setter
    def peer_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_ip", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for this peering neighbor. It defaults to no password if not specified.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)


@pulumi.input_type
class CniBgpConfigurationArgs:
    def __init__(__self__, *,
                 bgp_peers: Optional[pulumi.Input[Sequence[pulumi.Input['BgpPeerArgs']]]] = None,
                 community_advertisements: Optional[pulumi.Input[Sequence[pulumi.Input['CommunityAdvertisementArgs']]]] = None,
                 node_mesh_password: Optional[pulumi.Input[str]] = None,
                 service_external_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_load_balancer_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['BgpPeerArgs']]] bgp_peers: The list of BgpPeer entities that the Hybrid AKS cluster will peer with in addition to peering that occurs automatically with the switch fabric.
        :param pulumi.Input[Sequence[pulumi.Input['CommunityAdvertisementArgs']]] community_advertisements: The list of prefix community advertisement properties. Each prefix community specifies a prefix, and the
               communities that should be associated with that prefix when it is announced.
        :param pulumi.Input[str] node_mesh_password: The password of the Calico node mesh. It defaults to a randomly-generated string when not provided.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] service_external_prefixes: The subnet blocks in CIDR format for Kubernetes service external IPs to be advertised over BGP.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] service_load_balancer_prefixes: The subnet blocks in CIDR format for Kubernetes load balancers. Load balancer IPs will only be advertised if they
               are within one of these blocks.
        """
        if bgp_peers is not None:
            pulumi.set(__self__, "bgp_peers", bgp_peers)
        if community_advertisements is not None:
            pulumi.set(__self__, "community_advertisements", community_advertisements)
        if node_mesh_password is not None:
            pulumi.set(__self__, "node_mesh_password", node_mesh_password)
        if service_external_prefixes is not None:
            pulumi.set(__self__, "service_external_prefixes", service_external_prefixes)
        if service_load_balancer_prefixes is not None:
            pulumi.set(__self__, "service_load_balancer_prefixes", service_load_balancer_prefixes)

    @property
    @pulumi.getter(name="bgpPeers")
    def bgp_peers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BgpPeerArgs']]]]:
        """
        The list of BgpPeer entities that the Hybrid AKS cluster will peer with in addition to peering that occurs automatically with the switch fabric.
        """
        return pulumi.get(self, "bgp_peers")

    @bgp_peers.setter
    def bgp_peers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BgpPeerArgs']]]]):
        pulumi.set(self, "bgp_peers", value)

    @property
    @pulumi.getter(name="communityAdvertisements")
    def community_advertisements(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CommunityAdvertisementArgs']]]]:
        """
        The list of prefix community advertisement properties. Each prefix community specifies a prefix, and the
        communities that should be associated with that prefix when it is announced.
        """
        return pulumi.get(self, "community_advertisements")

    @community_advertisements.setter
    def community_advertisements(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CommunityAdvertisementArgs']]]]):
        pulumi.set(self, "community_advertisements", value)

    @property
    @pulumi.getter(name="nodeMeshPassword")
    def node_mesh_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the Calico node mesh. It defaults to a randomly-generated string when not provided.
        """
        return pulumi.get(self, "node_mesh_password")

    @node_mesh_password.setter
    def node_mesh_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_mesh_password", value)

    @property
    @pulumi.getter(name="serviceExternalPrefixes")
    def service_external_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The subnet blocks in CIDR format for Kubernetes service external IPs to be advertised over BGP.
        """
        return pulumi.get(self, "service_external_prefixes")

    @service_external_prefixes.setter
    def service_external_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "service_external_prefixes", value)

    @property
    @pulumi.getter(name="serviceLoadBalancerPrefixes")
    def service_load_balancer_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The subnet blocks in CIDR format for Kubernetes load balancers. Load balancer IPs will only be advertised if they
        are within one of these blocks.
        """
        return pulumi.get(self, "service_load_balancer_prefixes")

    @service_load_balancer_prefixes.setter
    def service_load_balancer_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "service_load_balancer_prefixes", value)


@pulumi.input_type
class CommunityAdvertisementArgs:
    def __init__(__self__, *,
                 communities: pulumi.Input[Sequence[pulumi.Input[str]]],
                 subnet_prefix: pulumi.Input[str]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] communities: The list of community strings to announce with this prefix.
        :param pulumi.Input[str] subnet_prefix: The subnet in CIDR format for which properties should be advertised.
        """
        pulumi.set(__self__, "communities", communities)
        pulumi.set(__self__, "subnet_prefix", subnet_prefix)

    @property
    @pulumi.getter
    def communities(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of community strings to announce with this prefix.
        """
        return pulumi.get(self, "communities")

    @communities.setter
    def communities(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "communities", value)

    @property
    @pulumi.getter(name="subnetPrefix")
    def subnet_prefix(self) -> pulumi.Input[str]:
        """
        The subnet in CIDR format for which properties should be advertised.
        """
        return pulumi.get(self, "subnet_prefix")

    @subnet_prefix.setter
    def subnet_prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_prefix", value)


@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The resource ID of the extended location on which the resource will be created.
        :param pulumi.Input[str] type: The extended location type, for example, CustomLocation.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The resource ID of the extended location on which the resource will be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The extended location type, for example, CustomLocation.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class ManagedResourceGroupConfigurationArgs:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] location: The location of the managed resource group. If not specified, the location of the parent resource is chosen.
        :param pulumi.Input[str] name: The name for the managed resource group. If not specified, the unique name is automatically generated.
        """
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the managed resource group. If not specified, the location of the parent resource is chosen.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for the managed resource group. If not specified, the unique name is automatically generated.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class RackDefinitionArgs:
    def __init__(__self__, *,
                 network_rack_id: pulumi.Input[str],
                 rack_serial_number: pulumi.Input[str],
                 rack_sku_id: pulumi.Input[str],
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 bare_metal_machine_configuration_data: Optional[pulumi.Input[Sequence[pulumi.Input['BareMetalMachineConfigurationDataArgs']]]] = None,
                 rack_location: Optional[pulumi.Input[str]] = None,
                 storage_appliance_configuration_data: Optional[pulumi.Input[Sequence[pulumi.Input['StorageApplianceConfigurationDataArgs']]]] = None):
        """
        :param pulumi.Input[str] network_rack_id: The resource ID of the network rack that matches this rack definition.
        :param pulumi.Input[str] rack_serial_number: The unique identifier for the rack within Network Cloud cluster. An alternate unique alphanumeric value other than a serial number may be provided if desired.
        :param pulumi.Input[str] rack_sku_id: The resource ID of the sku for the rack being added.
        :param pulumi.Input[str] availability_zone: The zone name used for this rack when created.
        :param pulumi.Input[Sequence[pulumi.Input['BareMetalMachineConfigurationDataArgs']]] bare_metal_machine_configuration_data: The unordered list of bare metal machine configuration.
        :param pulumi.Input[str] rack_location: The free-form description of the rack's location.
        :param pulumi.Input[Sequence[pulumi.Input['StorageApplianceConfigurationDataArgs']]] storage_appliance_configuration_data: The list of storage appliance configuration data for this rack.
        """
        pulumi.set(__self__, "network_rack_id", network_rack_id)
        pulumi.set(__self__, "rack_serial_number", rack_serial_number)
        pulumi.set(__self__, "rack_sku_id", rack_sku_id)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if bare_metal_machine_configuration_data is not None:
            pulumi.set(__self__, "bare_metal_machine_configuration_data", bare_metal_machine_configuration_data)
        if rack_location is not None:
            pulumi.set(__self__, "rack_location", rack_location)
        if storage_appliance_configuration_data is not None:
            pulumi.set(__self__, "storage_appliance_configuration_data", storage_appliance_configuration_data)

    @property
    @pulumi.getter(name="networkRackId")
    def network_rack_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the network rack that matches this rack definition.
        """
        return pulumi.get(self, "network_rack_id")

    @network_rack_id.setter
    def network_rack_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_rack_id", value)

    @property
    @pulumi.getter(name="rackSerialNumber")
    def rack_serial_number(self) -> pulumi.Input[str]:
        """
        The unique identifier for the rack within Network Cloud cluster. An alternate unique alphanumeric value other than a serial number may be provided if desired.
        """
        return pulumi.get(self, "rack_serial_number")

    @rack_serial_number.setter
    def rack_serial_number(self, value: pulumi.Input[str]):
        pulumi.set(self, "rack_serial_number", value)

    @property
    @pulumi.getter(name="rackSkuId")
    def rack_sku_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the sku for the rack being added.
        """
        return pulumi.get(self, "rack_sku_id")

    @rack_sku_id.setter
    def rack_sku_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rack_sku_id", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The zone name used for this rack when created.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="bareMetalMachineConfigurationData")
    def bare_metal_machine_configuration_data(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BareMetalMachineConfigurationDataArgs']]]]:
        """
        The unordered list of bare metal machine configuration.
        """
        return pulumi.get(self, "bare_metal_machine_configuration_data")

    @bare_metal_machine_configuration_data.setter
    def bare_metal_machine_configuration_data(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BareMetalMachineConfigurationDataArgs']]]]):
        pulumi.set(self, "bare_metal_machine_configuration_data", value)

    @property
    @pulumi.getter(name="rackLocation")
    def rack_location(self) -> Optional[pulumi.Input[str]]:
        """
        The free-form description of the rack's location.
        """
        return pulumi.get(self, "rack_location")

    @rack_location.setter
    def rack_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rack_location", value)

    @property
    @pulumi.getter(name="storageApplianceConfigurationData")
    def storage_appliance_configuration_data(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StorageApplianceConfigurationDataArgs']]]]:
        """
        The list of storage appliance configuration data for this rack.
        """
        return pulumi.get(self, "storage_appliance_configuration_data")

    @storage_appliance_configuration_data.setter
    def storage_appliance_configuration_data(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StorageApplianceConfigurationDataArgs']]]]):
        pulumi.set(self, "storage_appliance_configuration_data", value)


@pulumi.input_type
class ServicePrincipalInformationArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 password: pulumi.Input[str],
                 principal_id: pulumi.Input[str],
                 tenant_id: pulumi.Input[str]):
        """
        :param pulumi.Input[str] application_id: The application ID, also known as client ID, of the service principal.
        :param pulumi.Input[str] password: The password of the service principal.
        :param pulumi.Input[str] principal_id: The principal ID, also known as the object ID, of the service principal.
        :param pulumi.Input[str] tenant_id: The tenant ID, also known as the directory ID, of the tenant in which the service principal is created.
        """
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        """
        The application ID, also known as client ID, of the service principal.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password of the service principal.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[str]:
        """
        The principal ID, also known as the object ID, of the service principal.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[str]:
        """
        The tenant ID, also known as the directory ID, of the tenant in which the service principal is created.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class StorageApplianceConfigurationDataArgs:
    def __init__(__self__, *,
                 admin_credentials: pulumi.Input['AdministrativeCredentialsArgs'],
                 rack_slot: pulumi.Input[float],
                 serial_number: pulumi.Input[str],
                 storage_appliance_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['AdministrativeCredentialsArgs'] admin_credentials: The credentials of the administrative interface on this storage appliance.
        :param pulumi.Input[float] rack_slot: The slot that storage appliance is in the rack based on the BOM configuration.
        :param pulumi.Input[str] serial_number: The serial number of the appliance.
        :param pulumi.Input[str] storage_appliance_name: The user-provided name for the storage appliance that will be created from this specification.
        """
        pulumi.set(__self__, "admin_credentials", admin_credentials)
        pulumi.set(__self__, "rack_slot", rack_slot)
        pulumi.set(__self__, "serial_number", serial_number)
        if storage_appliance_name is not None:
            pulumi.set(__self__, "storage_appliance_name", storage_appliance_name)

    @property
    @pulumi.getter(name="adminCredentials")
    def admin_credentials(self) -> pulumi.Input['AdministrativeCredentialsArgs']:
        """
        The credentials of the administrative interface on this storage appliance.
        """
        return pulumi.get(self, "admin_credentials")

    @admin_credentials.setter
    def admin_credentials(self, value: pulumi.Input['AdministrativeCredentialsArgs']):
        pulumi.set(self, "admin_credentials", value)

    @property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> pulumi.Input[float]:
        """
        The slot that storage appliance is in the rack based on the BOM configuration.
        """
        return pulumi.get(self, "rack_slot")

    @rack_slot.setter
    def rack_slot(self, value: pulumi.Input[float]):
        pulumi.set(self, "rack_slot", value)

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Input[str]:
        """
        The serial number of the appliance.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: pulumi.Input[str]):
        pulumi.set(self, "serial_number", value)

    @property
    @pulumi.getter(name="storageApplianceName")
    def storage_appliance_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user-provided name for the storage appliance that will be created from this specification.
        """
        return pulumi.get(self, "storage_appliance_name")

    @storage_appliance_name.setter
    def storage_appliance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_appliance_name", value)


@pulumi.input_type
class ValidationThresholdArgs:
    def __init__(__self__, *,
                 grouping: pulumi.Input[Union[str, 'ValidationThresholdGrouping']],
                 type: pulumi.Input[Union[str, 'ValidationThresholdType']],
                 value: pulumi.Input[float]):
        """
        :param pulumi.Input[Union[str, 'ValidationThresholdGrouping']] grouping: Selection of how the type evaluation is applied to the cluster calculation.
        :param pulumi.Input[Union[str, 'ValidationThresholdType']] type: Selection of how the threshold should be evaluated.
        :param pulumi.Input[float] value: The numeric threshold value.
        """
        pulumi.set(__self__, "grouping", grouping)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def grouping(self) -> pulumi.Input[Union[str, 'ValidationThresholdGrouping']]:
        """
        Selection of how the type evaluation is applied to the cluster calculation.
        """
        return pulumi.get(self, "grouping")

    @grouping.setter
    def grouping(self, value: pulumi.Input[Union[str, 'ValidationThresholdGrouping']]):
        pulumi.set(self, "grouping", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ValidationThresholdType']]:
        """
        Selection of how the threshold should be evaluated.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ValidationThresholdType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[float]:
        """
        The numeric threshold value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[float]):
        pulumi.set(self, "value", value)


