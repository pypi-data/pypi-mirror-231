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
    'ConnectedClusterIdentityArgs',
]

@pulumi.input_type
class ConnectedClusterIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input['ResourceIdentityType']):
        """
        Identity for the connected cluster.
        :param pulumi.Input['ResourceIdentityType'] type: The type of identity used for the connected cluster. The type 'SystemAssigned, includes a system created identity. The type 'None' means no identity is assigned to the connected cluster.
        """
        if type is None:
            type = 'SystemAssigned'
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['ResourceIdentityType']:
        """
        The type of identity used for the connected cluster. The type 'SystemAssigned, includes a system created identity. The type 'None' means no identity is assigned to the connected cluster.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['ResourceIdentityType']):
        pulumi.set(self, "type", value)


