# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AddressPrefixType',
    'AllowedEndpointRecordType',
    'AlwaysServe',
    'DeleteExistingNSGs',
    'EndpointMonitorStatus',
    'EndpointStatus',
    'MonitorProtocol',
    'ProfileMonitorStatus',
    'ProfileStatus',
    'SecurityConfigurationRuleDirection',
    'SecurityConfigurationRuleProtocol',
    'TrafficRoutingMethod',
    'TrafficViewEnrollmentStatus',
    'UserRuleKind',
]


class AddressPrefixType(str, Enum):
    """
    Address prefix type.
    """
    IP_PREFIX = "IPPrefix"
    SERVICE_TAG = "ServiceTag"


class AllowedEndpointRecordType(str, Enum):
    """
    The allowed type DNS record types for this profile.
    """
    DOMAIN_NAME = "DomainName"
    I_PV4_ADDRESS = "IPv4Address"
    I_PV6_ADDRESS = "IPv6Address"
    ANY = "Any"


class AlwaysServe(str, Enum):
    """
    If Always Serve is enabled, probing for endpoint health will be disabled and endpoints will be included in the traffic routing method.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class DeleteExistingNSGs(str, Enum):
    """
    Flag if need to delete existing network security groups.
    """
    FALSE = "False"
    TRUE = "True"


class EndpointMonitorStatus(str, Enum):
    """
    The monitoring status of the endpoint.
    """
    CHECKING_ENDPOINT = "CheckingEndpoint"
    ONLINE = "Online"
    DEGRADED = "Degraded"
    DISABLED = "Disabled"
    INACTIVE = "Inactive"
    STOPPED = "Stopped"


class EndpointStatus(str, Enum):
    """
    The status of the endpoint. If the endpoint is Enabled, it is probed for endpoint health and is included in the traffic routing method.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class MonitorProtocol(str, Enum):
    """
    The protocol (HTTP, HTTPS or TCP) used to probe for endpoint health.
    """
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    TCP = "TCP"


class ProfileMonitorStatus(str, Enum):
    """
    The profile-level monitoring status of the Traffic Manager profile.
    """
    CHECKING_ENDPOINTS = "CheckingEndpoints"
    ONLINE = "Online"
    DEGRADED = "Degraded"
    DISABLED = "Disabled"
    INACTIVE = "Inactive"


class ProfileStatus(str, Enum):
    """
    The status of the Traffic Manager profile.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SecurityConfigurationRuleDirection(str, Enum):
    """
    Indicates if the traffic matched against the rule in inbound or outbound.
    """
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class SecurityConfigurationRuleProtocol(str, Enum):
    """
    Network protocol this rule applies to.
    """
    TCP = "Tcp"
    UDP = "Udp"
    ICMP = "Icmp"
    ESP = "Esp"
    ANY = "Any"
    AH = "Ah"


class TrafficRoutingMethod(str, Enum):
    """
    The traffic routing method of the Traffic Manager profile.
    """
    PERFORMANCE = "Performance"
    PRIORITY = "Priority"
    WEIGHTED = "Weighted"
    GEOGRAPHIC = "Geographic"
    MULTI_VALUE = "MultiValue"
    SUBNET = "Subnet"


class TrafficViewEnrollmentStatus(str, Enum):
    """
    Indicates whether Traffic View is 'Enabled' or 'Disabled' for the Traffic Manager profile. Null, indicates 'Disabled'. Enabling this feature will increase the cost of the Traffic Manage profile.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class UserRuleKind(str, Enum):
    """
    Whether the rule is custom or default.
    """
    CUSTOM = "Custom"
    DEFAULT = "Default"
