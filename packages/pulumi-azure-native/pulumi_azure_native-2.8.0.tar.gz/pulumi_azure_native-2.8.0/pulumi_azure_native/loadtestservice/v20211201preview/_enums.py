# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'SystemAssignedServiceIdentityType',
]


class SystemAssignedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (either system assigned, or none).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
