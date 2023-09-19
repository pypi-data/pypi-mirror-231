# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Kind',
    'ManagedServiceIdentityType',
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccess',
]


class Kind(str, Enum):
    """
    The kind of the service.
    """
    FHIR = "fhir"
    FHIR_STU3 = "fhir-Stu3"
    FHIR_R4 = "fhir-R4"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of identity being specified, currently SystemAssigned and None are allowed.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccess(str, Enum):
    """
    Control permission for data plane traffic coming from public networks while private endpoint is enabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
