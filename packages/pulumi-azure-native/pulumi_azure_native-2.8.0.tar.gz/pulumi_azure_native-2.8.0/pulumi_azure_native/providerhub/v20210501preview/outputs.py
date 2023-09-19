# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'OperationsDefinitionResponseDisplay',
]

@pulumi.output_type
class OperationsDefinitionResponseDisplay(dict):
    """
    Display information of the operation.
    """
    def __init__(__self__, *,
                 description: str,
                 operation: str,
                 provider: str,
                 resource: str):
        """
        Display information of the operation.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "operation", operation)
        pulumi.set(__self__, "provider", provider)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def operation(self) -> str:
        return pulumi.get(self, "operation")

    @property
    @pulumi.getter
    def provider(self) -> str:
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter
    def resource(self) -> str:
        return pulumi.get(self, "resource")


