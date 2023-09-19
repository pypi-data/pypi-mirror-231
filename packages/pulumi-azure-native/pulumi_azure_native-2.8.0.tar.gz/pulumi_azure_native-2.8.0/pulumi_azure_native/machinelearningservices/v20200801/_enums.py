# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EncryptionStatus',
    'PrivateEndpointServiceConnectionStatus',
    'ResourceIdentityType',
]


class EncryptionStatus(str, Enum):
    """
    Indicates whether or not the encryption is enabled for the workspace.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"
    TIMEOUT = "Timeout"


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"
