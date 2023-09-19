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
    'CreatorPropertiesArgs',
    'MapsAccountPropertiesArgs',
    'SkuArgs',
]

@pulumi.input_type
class CreatorPropertiesArgs:
    def __init__(__self__, *,
                 storage_units: pulumi.Input[int]):
        """
        Creator resource properties
        :param pulumi.Input[int] storage_units: The storage units to be allocated. Integer values from 1 to 100, inclusive.
        """
        pulumi.set(__self__, "storage_units", storage_units)

    @property
    @pulumi.getter(name="storageUnits")
    def storage_units(self) -> pulumi.Input[int]:
        """
        The storage units to be allocated. Integer values from 1 to 100, inclusive.
        """
        return pulumi.get(self, "storage_units")

    @storage_units.setter
    def storage_units(self, value: pulumi.Input[int]):
        pulumi.set(self, "storage_units", value)


@pulumi.input_type
class MapsAccountPropertiesArgs:
    def __init__(__self__, *,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None):
        """
        Additional Map account properties
        :param pulumi.Input[bool] disable_local_auth: Allows toggle functionality on Azure Policy to disable Azure Maps local authentication support. This will disable Shared Keys authentication from any usage.
        """
        if disable_local_auth is None:
            disable_local_auth = False
        if disable_local_auth is not None:
            pulumi.set(__self__, "disable_local_auth", disable_local_auth)

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Allows toggle functionality on Azure Policy to disable Azure Maps local authentication support. This will disable Shared Keys authentication from any usage.
        """
        return pulumi.get(self, "disable_local_auth")

    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_local_auth", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'Name']]):
        """
        The SKU of the Maps Account.
        :param pulumi.Input[Union[str, 'Name']] name: The name of the SKU, in standard format (such as S0).
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'Name']]:
        """
        The name of the SKU, in standard format (such as S0).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'Name']]):
        pulumi.set(self, "name", value)


