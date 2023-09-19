# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Role',
    'ValidationState',
]


class Role(str, Enum):
    """
    The role of the contact.
    """
    NOC = "Noc"
    POLICY = "Policy"
    TECHNICAL = "Technical"
    SERVICE = "Service"
    ESCALATION = "Escalation"
    OTHER = "Other"


class ValidationState(str, Enum):
    """
    The validation state of the ASN associated with the peer.
    """
    NONE = "None"
    PENDING = "Pending"
    APPROVED = "Approved"
    FAILED = "Failed"
