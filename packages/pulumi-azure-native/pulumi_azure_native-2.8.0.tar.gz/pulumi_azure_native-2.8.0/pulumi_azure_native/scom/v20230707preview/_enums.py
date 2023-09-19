# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'HybridLicenseType',
    'ManagedIdentityType',
]


class HybridLicenseType(str, Enum):
    """
    Specifies that the image or disk that is being used was licensed on-premises. <br><br> For more information, see [Azure Hybrid Use Benefit for Windows Server](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
    """
    NONE = "None"
    AZURE_HYBRID_BENEFIT = "AzureHybridBenefit"


class ManagedIdentityType(str, Enum):
    """
    The identity type
    """
    NONE = "None"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED = "SystemAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
