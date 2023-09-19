# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Distro',
    'Provider',
    'ResourceIdentityType',
]


class Distro(str, Enum):
    """
    Represents a supported Fabric/Infra. (AKSEdge etc...).
    """
    AKS_EDGE = "AKSEdge"


class Provider(str, Enum):
    """
    Information about the connected appliance.
    """
    VM_WARE = "VMWare"
    HCI = "HCI"
    SCVMM = "SCVMM"


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"
