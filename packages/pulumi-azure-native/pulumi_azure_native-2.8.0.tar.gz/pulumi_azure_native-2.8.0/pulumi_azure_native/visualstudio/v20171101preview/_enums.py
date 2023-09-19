# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccountResourceRequestOperationType',
]


class AccountResourceRequestOperationType(str, Enum):
    """
    The type of the operation.
    """
    UNKNOWN = "unknown"
    CREATE = "create"
    UPDATE = "update"
    LINK = "link"
