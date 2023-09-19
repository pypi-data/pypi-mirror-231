# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccessType',
    'TpmAttestationAuthenticationType',
]


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccessType(str, Enum):
    """
    Controls whether traffic from the public network is allowed to access the Attestation Provider APIs.
    """
    ENABLED = "Enabled"
    """
    Enables public network connectivity to the Attestation Provider REST APIs.
    """
    DISABLED = "Disabled"
    """
    Disables public network connectivity to the Attestation Provider REST APIs.
    """


class TpmAttestationAuthenticationType(str, Enum):
    """
    The setting that controls whether authentication is enabled or disabled for TPM Attestation REST APIs.
    """
    ENABLED = "Enabled"
    """
    Enables the requirement of authentication for TPM Attestation REST APIs.
    """
    DISABLED = "Disabled"
    """
    Disables the requirement of authentication for TPM Attestation REST APIs.
    """
