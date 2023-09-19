# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'OsType',
    'SupportType',
]


class OsType(str, Enum):
    """
    Type of OS for which the key is requested.
    """
    WINDOWS7 = "Windows7"
    WINDOWS_SERVER2008 = "WindowsServer2008"
    WINDOWS_SERVER2008_R2 = "WindowsServer2008R2"


class SupportType(str, Enum):
    """
    Type of support
    """
    SUPPLEMENTAL_SERVICING = "SupplementalServicing"
    PREMIUM_ASSURANCE = "PremiumAssurance"
