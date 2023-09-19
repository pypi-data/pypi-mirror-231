# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DaysOfWeek',
    'DirectoryType',
    'JsonWebKeyEncryptionAlgorithm',
    'OSType',
    'PrivateIPAllocationMethod',
    'PrivateLink',
    'PrivateLinkServiceConnectionStatus',
    'ResourceIdentityType',
    'ResourceProviderConnection',
    'Tier',
]


class DaysOfWeek(str, Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class DirectoryType(str, Enum):
    """
    The directory type.
    """
    ACTIVE_DIRECTORY = "ActiveDirectory"


class JsonWebKeyEncryptionAlgorithm(str, Enum):
    """
    Algorithm identifier for encryption, default RSA-OAEP.
    """
    RS_A_OAEP = "RSA-OAEP"
    RS_A_OAE_P_256 = "RSA-OAEP-256"
    RSA1_5 = "RSA1_5"


class OSType(str, Enum):
    """
    The type of operating system.
    """
    WINDOWS = "Windows"
    LINUX = "Linux"


class PrivateIPAllocationMethod(str, Enum):
    """
    The method that private IP address is allocated.
    """
    DYNAMIC = "dynamic"
    STATIC = "static"


class PrivateLink(str, Enum):
    """
    Indicates whether or not private link is enabled.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class PrivateLinkServiceConnectionStatus(str, Enum):
    """
    The concrete private link service connection.
    """
    APPROVED = "Approved"
    REJECTED = "Rejected"
    PENDING = "Pending"
    REMOVED = "Removed"


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the cluster. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user assigned identities.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class ResourceProviderConnection(str, Enum):
    """
    The direction for the resource provider connection.
    """
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class Tier(str, Enum):
    """
    The cluster tier.
    """
    STANDARD = "Standard"
    PREMIUM = "Premium"
