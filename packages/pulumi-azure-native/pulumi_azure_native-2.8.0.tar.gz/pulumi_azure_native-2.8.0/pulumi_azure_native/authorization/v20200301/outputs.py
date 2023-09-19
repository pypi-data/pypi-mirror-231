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
    'IdentityResponse',
    'ParameterValuesValueResponse',
    'PolicySkuResponse',
]

@pulumi.output_type
class IdentityResponse(dict):
    """
    Identity for the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        Identity for the resource.
        :param str principal_id: The principal ID of the resource identity.
        :param str tenant_id: The tenant ID of the resource identity.
        :param str type: The identity type. This is the only required field when adding a system assigned identity to a resource.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of the resource identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of the resource identity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The identity type. This is the only required field when adding a system assigned identity to a resource.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ParameterValuesValueResponse(dict):
    """
    The value of a parameter.
    """
    def __init__(__self__, *,
                 value: Optional[Any] = None):
        """
        The value of a parameter.
        :param Any value: The value of the parameter.
        """
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        """
        The value of the parameter.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class PolicySkuResponse(dict):
    """
    The policy sku. This property is optional, obsolete, and will be ignored.
    """
    def __init__(__self__, *,
                 name: str,
                 tier: Optional[str] = None):
        """
        The policy sku. This property is optional, obsolete, and will be ignored.
        :param str name: The name of the policy sku. Possible values are A0 and A1.
        :param str tier: The policy sku tier. Possible values are Free and Standard.
        """
        pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy sku. Possible values are A0 and A1.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        The policy sku tier. Possible values are Free and Standard.
        """
        return pulumi.get(self, "tier")


