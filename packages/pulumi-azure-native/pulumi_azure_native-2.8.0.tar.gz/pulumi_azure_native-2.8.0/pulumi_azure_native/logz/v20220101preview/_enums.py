# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ManagedIdentityTypes',
    'MarketplaceSubscriptionStatus',
    'MonitoringStatus',
    'TagAction',
]


class ManagedIdentityTypes(str, Enum):
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class MarketplaceSubscriptionStatus(str, Enum):
    """
    Flag specifying the Marketplace Subscription Status of the resource. If payment is not made in time, the resource will go in Suspended state.
    """
    ACTIVE = "Active"
    SUSPENDED = "Suspended"


class MonitoringStatus(str, Enum):
    """
    Flag specifying if the resource monitoring is enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TagAction(str, Enum):
    """
    Valid actions for a filtering tag. Exclusion takes priority over inclusion.
    """
    INCLUDE = "Include"
    EXCLUDE = "Exclude"
