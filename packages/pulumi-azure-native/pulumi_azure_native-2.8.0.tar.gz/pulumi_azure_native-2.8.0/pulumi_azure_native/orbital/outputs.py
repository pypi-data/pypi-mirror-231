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

__all__ = [
    'AuthorizedGroundstationResponse',
    'AvailableContactsResponse',
    'AvailableContactsResponseSpacecraft',
    'ContactProfileLinkChannelResponse',
    'ContactProfileLinkResponse',
    'ContactProfileThirdPartyConfigurationResponse',
    'ContactProfilesPropertiesResponseNetworkConfiguration',
    'ContactsPropertiesResponseAntennaConfiguration',
    'ContactsPropertiesResponseContactProfile',
    'EndPointResponse',
    'SpacecraftLinkResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class AuthorizedGroundstationResponse(dict):
    """
    Authorized groundstation.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "expirationDate":
            suggest = "expiration_date"
        elif key == "groundStation":
            suggest = "ground_station"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AuthorizedGroundstationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AuthorizedGroundstationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AuthorizedGroundstationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 expiration_date: str,
                 ground_station: str):
        """
        Authorized groundstation.
        :param str expiration_date: Date of authorization expiration.
        :param str ground_station: Groundstation name.
        """
        pulumi.set(__self__, "expiration_date", expiration_date)
        pulumi.set(__self__, "ground_station", ground_station)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> str:
        """
        Date of authorization expiration.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter(name="groundStation")
    def ground_station(self) -> str:
        """
        Groundstation name.
        """
        return pulumi.get(self, "ground_station")


@pulumi.output_type
class AvailableContactsResponse(dict):
    """
    Customer retrieves list of Available Contacts for a spacecraft resource. Later, one of the available contact can be selected to create a contact.
    """
    def __init__(__self__, *,
                 end_azimuth_degrees: float,
                 end_elevation_degrees: float,
                 ground_station_name: str,
                 maximum_elevation_degrees: float,
                 rx_end_time: str,
                 rx_start_time: str,
                 start_azimuth_degrees: float,
                 start_elevation_degrees: float,
                 tx_end_time: str,
                 tx_start_time: str,
                 spacecraft: Optional['outputs.AvailableContactsResponseSpacecraft'] = None):
        """
        Customer retrieves list of Available Contacts for a spacecraft resource. Later, one of the available contact can be selected to create a contact.
        :param float end_azimuth_degrees: Azimuth of the antenna at the end of the contact in decimal degrees.
        :param float end_elevation_degrees: Spacecraft elevation above the horizon at contact end.
        :param str ground_station_name: Name of Azure Ground Station.
        :param float maximum_elevation_degrees: Maximum elevation of the antenna during the contact in decimal degrees.
        :param str rx_end_time: Time to lost receiving a signal (ISO 8601 UTC standard).
        :param str rx_start_time: Earliest time to receive a signal (ISO 8601 UTC standard).
        :param float start_azimuth_degrees: Azimuth of the antenna at the start of the contact in decimal degrees.
        :param float start_elevation_degrees: Spacecraft elevation above the horizon at contact start.
        :param str tx_end_time: Time at which antenna transmit will be disabled (ISO 8601 UTC standard).
        :param str tx_start_time: Time at which antenna transmit will be enabled (ISO 8601 UTC standard).
        :param 'AvailableContactsResponseSpacecraft' spacecraft: The reference to the spacecraft resource.
        """
        pulumi.set(__self__, "end_azimuth_degrees", end_azimuth_degrees)
        pulumi.set(__self__, "end_elevation_degrees", end_elevation_degrees)
        pulumi.set(__self__, "ground_station_name", ground_station_name)
        pulumi.set(__self__, "maximum_elevation_degrees", maximum_elevation_degrees)
        pulumi.set(__self__, "rx_end_time", rx_end_time)
        pulumi.set(__self__, "rx_start_time", rx_start_time)
        pulumi.set(__self__, "start_azimuth_degrees", start_azimuth_degrees)
        pulumi.set(__self__, "start_elevation_degrees", start_elevation_degrees)
        pulumi.set(__self__, "tx_end_time", tx_end_time)
        pulumi.set(__self__, "tx_start_time", tx_start_time)
        if spacecraft is not None:
            pulumi.set(__self__, "spacecraft", spacecraft)

    @property
    @pulumi.getter(name="endAzimuthDegrees")
    def end_azimuth_degrees(self) -> float:
        """
        Azimuth of the antenna at the end of the contact in decimal degrees.
        """
        return pulumi.get(self, "end_azimuth_degrees")

    @property
    @pulumi.getter(name="endElevationDegrees")
    def end_elevation_degrees(self) -> float:
        """
        Spacecraft elevation above the horizon at contact end.
        """
        return pulumi.get(self, "end_elevation_degrees")

    @property
    @pulumi.getter(name="groundStationName")
    def ground_station_name(self) -> str:
        """
        Name of Azure Ground Station.
        """
        return pulumi.get(self, "ground_station_name")

    @property
    @pulumi.getter(name="maximumElevationDegrees")
    def maximum_elevation_degrees(self) -> float:
        """
        Maximum elevation of the antenna during the contact in decimal degrees.
        """
        return pulumi.get(self, "maximum_elevation_degrees")

    @property
    @pulumi.getter(name="rxEndTime")
    def rx_end_time(self) -> str:
        """
        Time to lost receiving a signal (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "rx_end_time")

    @property
    @pulumi.getter(name="rxStartTime")
    def rx_start_time(self) -> str:
        """
        Earliest time to receive a signal (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "rx_start_time")

    @property
    @pulumi.getter(name="startAzimuthDegrees")
    def start_azimuth_degrees(self) -> float:
        """
        Azimuth of the antenna at the start of the contact in decimal degrees.
        """
        return pulumi.get(self, "start_azimuth_degrees")

    @property
    @pulumi.getter(name="startElevationDegrees")
    def start_elevation_degrees(self) -> float:
        """
        Spacecraft elevation above the horizon at contact start.
        """
        return pulumi.get(self, "start_elevation_degrees")

    @property
    @pulumi.getter(name="txEndTime")
    def tx_end_time(self) -> str:
        """
        Time at which antenna transmit will be disabled (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "tx_end_time")

    @property
    @pulumi.getter(name="txStartTime")
    def tx_start_time(self) -> str:
        """
        Time at which antenna transmit will be enabled (ISO 8601 UTC standard).
        """
        return pulumi.get(self, "tx_start_time")

    @property
    @pulumi.getter
    def spacecraft(self) -> Optional['outputs.AvailableContactsResponseSpacecraft']:
        """
        The reference to the spacecraft resource.
        """
        return pulumi.get(self, "spacecraft")


@pulumi.output_type
class AvailableContactsResponseSpacecraft(dict):
    """
    The reference to the spacecraft resource.
    """
    def __init__(__self__, *,
                 id: str):
        """
        The reference to the spacecraft resource.
        :param str id: Resource ID.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class ContactProfileLinkChannelResponse(dict):
    """
    Contact Profile Link Channel.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bandwidthMHz":
            suggest = "bandwidth_m_hz"
        elif key == "centerFrequencyMHz":
            suggest = "center_frequency_m_hz"
        elif key == "endPoint":
            suggest = "end_point"
        elif key == "decodingConfiguration":
            suggest = "decoding_configuration"
        elif key == "demodulationConfiguration":
            suggest = "demodulation_configuration"
        elif key == "encodingConfiguration":
            suggest = "encoding_configuration"
        elif key == "modulationConfiguration":
            suggest = "modulation_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContactProfileLinkChannelResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContactProfileLinkChannelResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContactProfileLinkChannelResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bandwidth_m_hz: float,
                 center_frequency_m_hz: float,
                 end_point: 'outputs.EndPointResponse',
                 name: str,
                 decoding_configuration: Optional[str] = None,
                 demodulation_configuration: Optional[str] = None,
                 encoding_configuration: Optional[str] = None,
                 modulation_configuration: Optional[str] = None):
        """
        Contact Profile Link Channel.
        :param float bandwidth_m_hz: Bandwidth in MHz.
        :param float center_frequency_m_hz: Center Frequency in MHz.
        :param 'EndPointResponse' end_point: Customer end point to store and retrieve data during a contact with the spacecraft.
        :param str name: Channel name.
        :param str decoding_configuration: Currently unused.
        :param str demodulation_configuration: Copy of the modem configuration file such as Kratos QRadio or Kratos QuantumRx. Only valid for downlink directions. If provided, the modem connects to the customer endpoint and sends demodulated data instead of a VITA.49 stream.
        :param str encoding_configuration: Currently unused.
        :param str modulation_configuration: Copy of the modem configuration file such as Kratos QRadio. Only valid for uplink directions. If provided, the modem connects to the customer endpoint and accepts commands from the customer instead of a VITA.49 stream.
        """
        pulumi.set(__self__, "bandwidth_m_hz", bandwidth_m_hz)
        pulumi.set(__self__, "center_frequency_m_hz", center_frequency_m_hz)
        pulumi.set(__self__, "end_point", end_point)
        pulumi.set(__self__, "name", name)
        if decoding_configuration is not None:
            pulumi.set(__self__, "decoding_configuration", decoding_configuration)
        if demodulation_configuration is not None:
            pulumi.set(__self__, "demodulation_configuration", demodulation_configuration)
        if encoding_configuration is not None:
            pulumi.set(__self__, "encoding_configuration", encoding_configuration)
        if modulation_configuration is not None:
            pulumi.set(__self__, "modulation_configuration", modulation_configuration)

    @property
    @pulumi.getter(name="bandwidthMHz")
    def bandwidth_m_hz(self) -> float:
        """
        Bandwidth in MHz.
        """
        return pulumi.get(self, "bandwidth_m_hz")

    @property
    @pulumi.getter(name="centerFrequencyMHz")
    def center_frequency_m_hz(self) -> float:
        """
        Center Frequency in MHz.
        """
        return pulumi.get(self, "center_frequency_m_hz")

    @property
    @pulumi.getter(name="endPoint")
    def end_point(self) -> 'outputs.EndPointResponse':
        """
        Customer end point to store and retrieve data during a contact with the spacecraft.
        """
        return pulumi.get(self, "end_point")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Channel name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="decodingConfiguration")
    def decoding_configuration(self) -> Optional[str]:
        """
        Currently unused.
        """
        return pulumi.get(self, "decoding_configuration")

    @property
    @pulumi.getter(name="demodulationConfiguration")
    def demodulation_configuration(self) -> Optional[str]:
        """
        Copy of the modem configuration file such as Kratos QRadio or Kratos QuantumRx. Only valid for downlink directions. If provided, the modem connects to the customer endpoint and sends demodulated data instead of a VITA.49 stream.
        """
        return pulumi.get(self, "demodulation_configuration")

    @property
    @pulumi.getter(name="encodingConfiguration")
    def encoding_configuration(self) -> Optional[str]:
        """
        Currently unused.
        """
        return pulumi.get(self, "encoding_configuration")

    @property
    @pulumi.getter(name="modulationConfiguration")
    def modulation_configuration(self) -> Optional[str]:
        """
        Copy of the modem configuration file such as Kratos QRadio. Only valid for uplink directions. If provided, the modem connects to the customer endpoint and accepts commands from the customer instead of a VITA.49 stream.
        """
        return pulumi.get(self, "modulation_configuration")


@pulumi.output_type
class ContactProfileLinkResponse(dict):
    """
    Contact Profile Link.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "eirpdBW":
            suggest = "eirpd_bw"
        elif key == "gainOverTemperature":
            suggest = "gain_over_temperature"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContactProfileLinkResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContactProfileLinkResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContactProfileLinkResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 channels: Sequence['outputs.ContactProfileLinkChannelResponse'],
                 direction: str,
                 name: str,
                 polarization: str,
                 eirpd_bw: Optional[float] = None,
                 gain_over_temperature: Optional[float] = None):
        """
        Contact Profile Link.
        :param Sequence['ContactProfileLinkChannelResponse'] channels: Contact Profile Link Channel.
        :param str direction: Direction (Uplink or Downlink).
        :param str name: Link name.
        :param str polarization: Polarization. e.g. (RHCP, LHCP).
        :param float eirpd_bw: Effective Isotropic Radiated Power (EIRP) in dBW. It is the required EIRP by the customer. Not used yet.
        :param float gain_over_temperature: Gain to noise temperature in db/K. It is the required G/T by the customer. Not used yet.
        """
        pulumi.set(__self__, "channels", channels)
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "polarization", polarization)
        if eirpd_bw is not None:
            pulumi.set(__self__, "eirpd_bw", eirpd_bw)
        if gain_over_temperature is not None:
            pulumi.set(__self__, "gain_over_temperature", gain_over_temperature)

    @property
    @pulumi.getter
    def channels(self) -> Sequence['outputs.ContactProfileLinkChannelResponse']:
        """
        Contact Profile Link Channel.
        """
        return pulumi.get(self, "channels")

    @property
    @pulumi.getter
    def direction(self) -> str:
        """
        Direction (Uplink or Downlink).
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Link name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def polarization(self) -> str:
        """
        Polarization. e.g. (RHCP, LHCP).
        """
        return pulumi.get(self, "polarization")

    @property
    @pulumi.getter(name="eirpdBW")
    def eirpd_bw(self) -> Optional[float]:
        """
        Effective Isotropic Radiated Power (EIRP) in dBW. It is the required EIRP by the customer. Not used yet.
        """
        return pulumi.get(self, "eirpd_bw")

    @property
    @pulumi.getter(name="gainOverTemperature")
    def gain_over_temperature(self) -> Optional[float]:
        """
        Gain to noise temperature in db/K. It is the required G/T by the customer. Not used yet.
        """
        return pulumi.get(self, "gain_over_temperature")


@pulumi.output_type
class ContactProfileThirdPartyConfigurationResponse(dict):
    """
    Contact Profile third-party partner configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "missionConfiguration":
            suggest = "mission_configuration"
        elif key == "providerName":
            suggest = "provider_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContactProfileThirdPartyConfigurationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContactProfileThirdPartyConfigurationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContactProfileThirdPartyConfigurationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 mission_configuration: str,
                 provider_name: str):
        """
        Contact Profile third-party partner configuration.
        :param str mission_configuration: Name of string referencing the configuration describing contact set-up for a particular mission. Expected values are those which have been created in collaboration with the partner network.
        :param str provider_name: Name of the third-party provider.
        """
        pulumi.set(__self__, "mission_configuration", mission_configuration)
        pulumi.set(__self__, "provider_name", provider_name)

    @property
    @pulumi.getter(name="missionConfiguration")
    def mission_configuration(self) -> str:
        """
        Name of string referencing the configuration describing contact set-up for a particular mission. Expected values are those which have been created in collaboration with the partner network.
        """
        return pulumi.get(self, "mission_configuration")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> str:
        """
        Name of the third-party provider.
        """
        return pulumi.get(self, "provider_name")


@pulumi.output_type
class ContactProfilesPropertiesResponseNetworkConfiguration(dict):
    """
    Network configuration of customer virtual network.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetId":
            suggest = "subnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContactProfilesPropertiesResponseNetworkConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContactProfilesPropertiesResponseNetworkConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContactProfilesPropertiesResponseNetworkConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_id: str):
        """
        Network configuration of customer virtual network.
        :param str subnet_id: ARM resource identifier of the subnet delegated to the Microsoft.Orbital/orbitalGateways. Needs to be at least a class C subnet, and should not have any IP created in it.
        """
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        ARM resource identifier of the subnet delegated to the Microsoft.Orbital/orbitalGateways. Needs to be at least a class C subnet, and should not have any IP created in it.
        """
        return pulumi.get(self, "subnet_id")


@pulumi.output_type
class ContactsPropertiesResponseAntennaConfiguration(dict):
    """
    The configuration associated with the allocated antenna.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "destinationIp":
            suggest = "destination_ip"
        elif key == "sourceIps":
            suggest = "source_ips"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContactsPropertiesResponseAntennaConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContactsPropertiesResponseAntennaConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContactsPropertiesResponseAntennaConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 destination_ip: Optional[str] = None,
                 source_ips: Optional[Sequence[str]] = None):
        """
        The configuration associated with the allocated antenna.
        :param str destination_ip: The destination IP a packet can be sent to. This would for example be the TCP endpoint you would send data to.
        :param Sequence[str] source_ips: List of Source IP
        """
        if destination_ip is not None:
            pulumi.set(__self__, "destination_ip", destination_ip)
        if source_ips is not None:
            pulumi.set(__self__, "source_ips", source_ips)

    @property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> Optional[str]:
        """
        The destination IP a packet can be sent to. This would for example be the TCP endpoint you would send data to.
        """
        return pulumi.get(self, "destination_ip")

    @property
    @pulumi.getter(name="sourceIps")
    def source_ips(self) -> Optional[Sequence[str]]:
        """
        List of Source IP
        """
        return pulumi.get(self, "source_ips")


@pulumi.output_type
class ContactsPropertiesResponseContactProfile(dict):
    """
    The reference to the contact profile resource.
    """
    def __init__(__self__, *,
                 id: str):
        """
        The reference to the contact profile resource.
        :param str id: Resource ID.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class EndPointResponse(dict):
    """
    Customer end point to store and retrieve data during a contact with the spacecraft.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endPointName":
            suggest = "end_point_name"
        elif key == "ipAddress":
            suggest = "ip_address"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndPointResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndPointResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndPointResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 end_point_name: str,
                 ip_address: str,
                 port: str,
                 protocol: str):
        """
        Customer end point to store and retrieve data during a contact with the spacecraft.
        :param str end_point_name: Name of an end point.
        :param str ip_address: IP Address (IPv4).
        :param str port: TCP port to listen on to receive data.
        :param str protocol: Protocol either UDP or TCP.
        """
        pulumi.set(__self__, "end_point_name", end_point_name)
        pulumi.set(__self__, "ip_address", ip_address)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="endPointName")
    def end_point_name(self) -> str:
        """
        Name of an end point.
        """
        return pulumi.get(self, "end_point_name")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        IP Address (IPv4).
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def port(self) -> str:
        """
        TCP port to listen on to receive data.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Protocol either UDP or TCP.
        """
        return pulumi.get(self, "protocol")


@pulumi.output_type
class SpacecraftLinkResponse(dict):
    """
    List of authorized spacecraft links per ground station and the expiration date of the authorization.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bandwidthMHz":
            suggest = "bandwidth_m_hz"
        elif key == "centerFrequencyMHz":
            suggest = "center_frequency_m_hz"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SpacecraftLinkResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SpacecraftLinkResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SpacecraftLinkResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 authorizations: Sequence['outputs.AuthorizedGroundstationResponse'],
                 bandwidth_m_hz: float,
                 center_frequency_m_hz: float,
                 direction: str,
                 name: str,
                 polarization: str):
        """
        List of authorized spacecraft links per ground station and the expiration date of the authorization.
        :param Sequence['AuthorizedGroundstationResponse'] authorizations: Authorized Ground Stations
        :param float bandwidth_m_hz: Bandwidth in MHz.
        :param float center_frequency_m_hz: Center Frequency in MHz.
        :param str direction: Direction (Uplink or Downlink).
        :param str name: Link name.
        :param str polarization: Polarization. e.g. (RHCP, LHCP).
        """
        pulumi.set(__self__, "authorizations", authorizations)
        pulumi.set(__self__, "bandwidth_m_hz", bandwidth_m_hz)
        pulumi.set(__self__, "center_frequency_m_hz", center_frequency_m_hz)
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "polarization", polarization)

    @property
    @pulumi.getter
    def authorizations(self) -> Sequence['outputs.AuthorizedGroundstationResponse']:
        """
        Authorized Ground Stations
        """
        return pulumi.get(self, "authorizations")

    @property
    @pulumi.getter(name="bandwidthMHz")
    def bandwidth_m_hz(self) -> float:
        """
        Bandwidth in MHz.
        """
        return pulumi.get(self, "bandwidth_m_hz")

    @property
    @pulumi.getter(name="centerFrequencyMHz")
    def center_frequency_m_hz(self) -> float:
        """
        Center Frequency in MHz.
        """
        return pulumi.get(self, "center_frequency_m_hz")

    @property
    @pulumi.getter
    def direction(self) -> str:
        """
        Direction (Uplink or Downlink).
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Link name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def polarization(self) -> str:
        """
        Polarization. e.g. (RHCP, LHCP).
        """
        return pulumi.get(self, "polarization")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


