# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EncryptionKeySource',
    'KeySource',
    'ManagedServiceIdentityType',
    'PrivateLinkServiceConnectionStatus',
    'PublicNetworkAccess',
    'RequiredNsgRules',
]


class EncryptionKeySource(str, Enum):
    """
    The encryption keySource (provider). Possible values (case-insensitive):  Microsoft.Keyvault
    """
    MICROSOFT_KEYVAULT = "Microsoft.Keyvault"


class KeySource(str, Enum):
    """
    The encryption keySource (provider). Possible values (case-insensitive):  Default, Microsoft.Keyvault
    """
    DEFAULT = "Default"
    MICROSOFT_KEYVAULT = "Microsoft.Keyvault"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class PrivateLinkServiceConnectionStatus(str, Enum):
    """
    The status of a private endpoint connection
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class PublicNetworkAccess(str, Enum):
    """
    The network access type for accessing workspace. Set value to disabled to access workspace only via private link.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RequiredNsgRules(str, Enum):
    """
    Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint. Supported values are 'AllRules' and 'NoAzureDatabricksRules'. 'NoAzureServiceRules' value is for internal use only.
    """
    ALL_RULES = "AllRules"
    NO_AZURE_DATABRICKS_RULES = "NoAzureDatabricksRules"
    NO_AZURE_SERVICE_RULES = "NoAzureServiceRules"
