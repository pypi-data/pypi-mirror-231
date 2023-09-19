# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'MachineReferenceWithHintsResponse',
    'SkuResponse',
]

@pulumi.output_type
class MachineReferenceWithHintsResponse(dict):
    """
    A machine reference with a hint of the machine's name and operating system.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "displayNameHint":
            suggest = "display_name_hint"
        elif key == "osFamilyHint":
            suggest = "os_family_hint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MachineReferenceWithHintsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MachineReferenceWithHintsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MachineReferenceWithHintsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 display_name_hint: str,
                 id: str,
                 kind: str,
                 name: str,
                 os_family_hint: str,
                 type: str):
        """
        A machine reference with a hint of the machine's name and operating system.
        :param str display_name_hint: Last known display name.
        :param str id: Resource URI.
        :param str kind: Specifies the sub-class of the reference.
               Expected value is 'ref:machinewithhints'.
        :param str name: Resource name.
        :param str os_family_hint: Last known operating system family.
        :param str type: Resource type qualifier.
        """
        pulumi.set(__self__, "display_name_hint", display_name_hint)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "kind", 'ref:machinewithhints')
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "os_family_hint", os_family_hint)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="displayNameHint")
    def display_name_hint(self) -> str:
        """
        Last known display name.
        """
        return pulumi.get(self, "display_name_hint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource URI.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Specifies the sub-class of the reference.
        Expected value is 'ref:machinewithhints'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osFamilyHint")
    def os_family_hint(self) -> str:
        """
        Last known operating system family.
        """
        return pulumi.get(self, "os_family_hint")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type qualifier.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class SkuResponse(dict):
    """
    The SKU (tier) of a workspace.
    """
    def __init__(__self__, *,
                 name: str):
        """
        The SKU (tier) of a workspace.
        :param str name: The name of the SKU.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SKU.
        """
        return pulumi.get(self, "name")


