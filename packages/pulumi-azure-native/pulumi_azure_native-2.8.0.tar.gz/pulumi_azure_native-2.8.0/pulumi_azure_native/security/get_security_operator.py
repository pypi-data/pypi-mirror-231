# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetSecurityOperatorResult',
    'AwaitableGetSecurityOperatorResult',
    'get_security_operator',
    'get_security_operator_output',
]

@pulumi.output_type
class GetSecurityOperatorResult:
    """
    Security operator under a given subscription and pricing
    """
    def __init__(__self__, id=None, identity=None, name=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetSecurityOperatorResult(GetSecurityOperatorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityOperatorResult(
            id=self.id,
            identity=self.identity,
            name=self.name,
            type=self.type)


def get_security_operator(pricing_name: Optional[str] = None,
                          security_operator_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityOperatorResult:
    """
    Get a specific security operator for the requested scope.
    Azure REST API version: 2023-01-01-preview.


    :param str pricing_name: name of the pricing configuration
    :param str security_operator_name: name of the securityOperator
    """
    __args__ = dict()
    __args__['pricingName'] = pricing_name
    __args__['securityOperatorName'] = security_operator_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security:getSecurityOperator', __args__, opts=opts, typ=GetSecurityOperatorResult).value

    return AwaitableGetSecurityOperatorResult(
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_security_operator)
def get_security_operator_output(pricing_name: Optional[pulumi.Input[str]] = None,
                                 security_operator_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityOperatorResult]:
    """
    Get a specific security operator for the requested scope.
    Azure REST API version: 2023-01-01-preview.


    :param str pricing_name: name of the pricing configuration
    :param str security_operator_name: name of the securityOperator
    """
    ...
