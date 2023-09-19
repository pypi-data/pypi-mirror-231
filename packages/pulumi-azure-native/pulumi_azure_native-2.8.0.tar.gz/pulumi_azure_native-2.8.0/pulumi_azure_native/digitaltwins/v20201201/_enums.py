# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'PrivateLinkServiceConnectionStatus',
]


class PrivateLinkServiceConnectionStatus(str, Enum):
    """
    The status of a private endpoint connection.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"
