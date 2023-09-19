# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EncryptionConfigType',
    'EncryptionIdentityType',
    'EncryptionState',
    'FirewallAllowAzureIpsState',
    'FirewallState',
    'TierType',
    'TrustedIdProviderState',
]


class EncryptionConfigType(str, Enum):
    """
    The type of encryption configuration being used. Currently the only supported types are 'UserManaged' and 'ServiceManaged'.
    """
    USER_MANAGED = "UserManaged"
    SERVICE_MANAGED = "ServiceManaged"


class EncryptionIdentityType(str, Enum):
    """
    The type of encryption being used. Currently the only supported type is 'SystemAssigned'.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"


class EncryptionState(str, Enum):
    """
    The current state of encryption for this Data Lake Store account.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class FirewallAllowAzureIpsState(str, Enum):
    """
    The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class FirewallState(str, Enum):
    """
    The current state of the IP address firewall for this Data Lake Store account.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TierType(str, Enum):
    """
    The commitment tier to use for next month.
    """
    CONSUMPTION = "Consumption"
    COMMITMENT_1_TB = "Commitment_1TB"
    COMMITMENT_10_TB = "Commitment_10TB"
    COMMITMENT_100_TB = "Commitment_100TB"
    COMMITMENT_500_TB = "Commitment_500TB"
    COMMITMENT_1_PB = "Commitment_1PB"
    COMMITMENT_5_PB = "Commitment_5PB"


class TrustedIdProviderState(str, Enum):
    """
    The current state of the trusted identity provider feature for this Data Lake Store account.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
