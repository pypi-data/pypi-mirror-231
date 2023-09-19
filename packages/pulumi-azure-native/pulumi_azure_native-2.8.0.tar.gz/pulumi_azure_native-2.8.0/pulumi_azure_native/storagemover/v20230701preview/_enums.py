# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CopyMode',
    'CredentialType',
    'EndpointType',
    'NfsVersion',
]


class CopyMode(str, Enum):
    """
    Strategy to use for copy.
    """
    ADDITIVE = "Additive"
    MIRROR = "Mirror"


class CredentialType(str, Enum):
    """
    The Credentials type.
    """
    AZURE_KEY_VAULT_SMB = "AzureKeyVaultSmb"


class EndpointType(str, Enum):
    """
    The Endpoint resource type.
    """
    AZURE_STORAGE_BLOB_CONTAINER = "AzureStorageBlobContainer"
    NFS_MOUNT = "NfsMount"
    AZURE_STORAGE_SMB_FILE_SHARE = "AzureStorageSmbFileShare"
    SMB_MOUNT = "SmbMount"


class NfsVersion(str, Enum):
    """
    The NFS protocol version.
    """
    NF_SAUTO = "NFSauto"
    NF_SV3 = "NFSv3"
    NF_SV4 = "NFSv4"
