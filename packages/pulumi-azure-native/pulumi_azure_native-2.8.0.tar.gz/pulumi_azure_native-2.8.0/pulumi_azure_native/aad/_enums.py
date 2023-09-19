# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ChannelBinding',
    'ExternalAccess',
    'FilteredSync',
    'KerberosArmoring',
    'KerberosRc4Encryption',
    'LdapSigning',
    'Ldaps',
    'NotifyDcAdmins',
    'NotifyGlobalAdmins',
    'NtlmV1',
    'Status',
    'SyncKerberosPasswords',
    'SyncNtlmPasswords',
    'SyncOnPremPasswords',
    'SyncScope',
    'TlsV1',
]


class ChannelBinding(str, Enum):
    """
    A flag to determine whether or not ChannelBinding is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ExternalAccess(str, Enum):
    """
    A flag to determine whether or not Secure LDAP access over the internet is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class FilteredSync(str, Enum):
    """
    Enabled or Disabled flag to turn on Group-based filtered sync
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class KerberosArmoring(str, Enum):
    """
    A flag to determine whether or not KerberosArmoring is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class KerberosRc4Encryption(str, Enum):
    """
    A flag to determine whether or not KerberosRc4Encryption is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class LdapSigning(str, Enum):
    """
    A flag to determine whether or not LdapSigning is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class Ldaps(str, Enum):
    """
    A flag to determine whether or not Secure LDAP is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class NotifyDcAdmins(str, Enum):
    """
    Should domain controller admins be notified
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class NotifyGlobalAdmins(str, Enum):
    """
    Should global admins be notified
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class NtlmV1(str, Enum):
    """
    A flag to determine whether or not NtlmV1 is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class Status(str, Enum):
    """
    Status for individual validator after running diagnostics.
    """
    NONE = "None"
    RUNNING = "Running"
    OK = "OK"
    FAILURE = "Failure"
    WARNING = "Warning"
    SKIPPED = "Skipped"


class SyncKerberosPasswords(str, Enum):
    """
    A flag to determine whether or not SyncKerberosPasswords is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SyncNtlmPasswords(str, Enum):
    """
    A flag to determine whether or not SyncNtlmPasswords is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SyncOnPremPasswords(str, Enum):
    """
    A flag to determine whether or not SyncOnPremPasswords is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SyncScope(str, Enum):
    """
    All or CloudOnly, All users in AAD are synced to AAD DS domain or only users actively syncing in the cloud
    """
    ALL = "All"
    CLOUD_ONLY = "CloudOnly"


class TlsV1(str, Enum):
    """
    A flag to determine whether or not TlsV1 is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
