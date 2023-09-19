# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Action',
    'EncryptionType',
    'SkuName',
    'SkuTier',
    'StorageTargetType',
    'VolumeCreateOption',
]


class Action(str, Enum):
    """
    The action of virtual network rule.
    """
    ALLOW = "Allow"


class EncryptionType(str, Enum):
    """
    Type of encryption
    """
    ENCRYPTION_AT_REST_WITH_PLATFORM_KEY = "EncryptionAtRestWithPlatformKey"
    """
    Volume is encrypted at rest with Platform managed key. It is the default encryption type.
    """


class SkuName(str, Enum):
    """
    The sku name.
    """
    PREMIUM_LRS = "Premium_LRS"
    """
    Premium locally redundant storage
    """
    PREMIUM_ZRS = "Premium_ZRS"
    """
    Premium zone redundant storage
    """


class SkuTier(str, Enum):
    """
    The sku tier.
    """
    PREMIUM = "Premium"
    """
    Premium Tier
    """


class StorageTargetType(str, Enum):
    """
    Type of storage target
    """
    ISCSI = "Iscsi"
    NONE = "None"


class VolumeCreateOption(str, Enum):
    """
    This enumerates the possible sources of a volume creation.
    """
    NONE = "None"
