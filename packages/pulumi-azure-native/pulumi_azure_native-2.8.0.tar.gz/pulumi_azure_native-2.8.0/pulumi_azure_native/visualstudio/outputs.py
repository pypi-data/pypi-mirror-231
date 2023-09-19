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
    'ExtensionResourcePlanResponse',
]

@pulumi.output_type
class ExtensionResourcePlanResponse(dict):
    """
    Plan data for an extension resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "promotionCode":
            suggest = "promotion_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExtensionResourcePlanResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExtensionResourcePlanResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExtensionResourcePlanResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: Optional[str] = None,
                 product: Optional[str] = None,
                 promotion_code: Optional[str] = None,
                 publisher: Optional[str] = None,
                 version: Optional[str] = None):
        """
        Plan data for an extension resource.
        :param str name: Name of the plan.
        :param str product: Product name.
        :param str promotion_code: Optional: the promotion code associated with the plan.
        :param str publisher: Name of the extension publisher.
        :param str version: A string that uniquely identifies the plan version.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if product is not None:
            pulumi.set(__self__, "product", product)
        if promotion_code is not None:
            pulumi.set(__self__, "promotion_code", promotion_code)
        if publisher is not None:
            pulumi.set(__self__, "publisher", publisher)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the plan.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def product(self) -> Optional[str]:
        """
        Product name.
        """
        return pulumi.get(self, "product")

    @property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[str]:
        """
        Optional: the promotion code associated with the plan.
        """
        return pulumi.get(self, "promotion_code")

    @property
    @pulumi.getter
    def publisher(self) -> Optional[str]:
        """
        Name of the extension publisher.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        A string that uniquely identifies the plan version.
        """
        return pulumi.get(self, "version")


