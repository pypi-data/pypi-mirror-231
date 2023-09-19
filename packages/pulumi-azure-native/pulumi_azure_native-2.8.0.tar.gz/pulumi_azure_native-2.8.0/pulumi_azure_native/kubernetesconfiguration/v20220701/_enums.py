# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AKSIdentityType',
    'LevelType',
    'ResourceIdentityType',
]


class AKSIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class LevelType(str, Enum):
    """
    Level of the status.
    """
    ERROR = "Error"
    WARNING = "Warning"
    INFORMATION = "Information"


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
