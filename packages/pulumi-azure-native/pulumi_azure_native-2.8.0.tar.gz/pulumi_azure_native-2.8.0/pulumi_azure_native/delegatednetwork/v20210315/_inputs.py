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
    'ControllerDetailsArgs',
    'OrchestratorIdentityArgs',
    'SubnetDetailsArgs',
]

@pulumi.input_type
class ControllerDetailsArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        controller details
        :param pulumi.Input[str] id: controller arm resource id
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        controller arm resource id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class OrchestratorIdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input['ResourceIdentityType']] = None):
        """
        :param pulumi.Input['ResourceIdentityType'] type: The type of identity used for orchestrator cluster. Type 'SystemAssigned' will use an implicitly created identity orchestrator clusters
        """
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['ResourceIdentityType']]:
        """
        The type of identity used for orchestrator cluster. Type 'SystemAssigned' will use an implicitly created identity orchestrator clusters
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['ResourceIdentityType']]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class SubnetDetailsArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        Properties of orchestrator
        :param pulumi.Input[str] id: subnet arm resource id
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        subnet arm resource id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


