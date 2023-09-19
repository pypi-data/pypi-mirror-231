# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'B2CResourceSKUArgs',
]

@pulumi.input_type
class B2CResourceSKUArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[Union[str, 'B2CResourceSKUName']]] = None,
                 tier: Optional[pulumi.Input[Union[str, 'B2CResourceSKUTier']]] = None):
        """
        SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling).
        :param pulumi.Input[Union[str, 'B2CResourceSKUName']] name: The name of the SKU for the tenant.
        :param pulumi.Input[Union[str, 'B2CResourceSKUTier']] tier: The tier of the tenant.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[str, 'B2CResourceSKUName']]]:
        """
        The name of the SKU for the tenant.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[str, 'B2CResourceSKUName']]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[str, 'B2CResourceSKUTier']]]:
        """
        The tier of the tenant.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[str, 'B2CResourceSKUTier']]]):
        pulumi.set(self, "tier", value)


