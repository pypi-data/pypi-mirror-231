# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'ResourceSelectorResponse',
    'SelectorResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class ResourceSelectorResponse(dict):
    """
    The resource selector to filter policies by resource properties.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 selectors: Optional[Sequence['outputs.SelectorResponse']] = None):
        """
        The resource selector to filter policies by resource properties.
        :param str name: The name of the resource selector.
        :param Sequence['SelectorResponse'] selectors: The list of the selector expressions.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if selectors is not None:
            pulumi.set(__self__, "selectors", selectors)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource selector.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def selectors(self) -> Optional[Sequence['outputs.SelectorResponse']]:
        """
        The list of the selector expressions.
        """
        return pulumi.get(self, "selectors")


@pulumi.output_type
class SelectorResponse(dict):
    """
    The selector expression.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "in":
            suggest = "in_"
        elif key == "notIn":
            suggest = "not_in"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SelectorResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SelectorResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SelectorResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 in_: Optional[Sequence[str]] = None,
                 kind: Optional[str] = None,
                 not_in: Optional[Sequence[str]] = None):
        """
        The selector expression.
        :param Sequence[str] in_: The list of values to filter in.
        :param str kind: The selector kind.
        :param Sequence[str] not_in: The list of values to filter out.
        """
        if in_ is not None:
            pulumi.set(__self__, "in_", in_)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if not_in is not None:
            pulumi.set(__self__, "not_in", not_in)

    @property
    @pulumi.getter(name="in")
    def in_(self) -> Optional[Sequence[str]]:
        """
        The list of values to filter in.
        """
        return pulumi.get(self, "in_")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The selector kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="notIn")
    def not_in(self) -> Optional[Sequence[str]]:
        """
        The list of values to filter out.
        """
        return pulumi.get(self, "not_in")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


