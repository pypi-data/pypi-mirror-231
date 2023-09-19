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
    'SkuArgs',
    'StorageAccountParametersArgs',
]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str]):
        """
        The SKU of a container registry.
        :param pulumi.Input[str] name: The SKU name of the container registry. Required for registry creation. Allowed value: Basic.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The SKU name of the container registry. Required for registry creation. Allowed value: Basic.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class StorageAccountParametersArgs:
    def __init__(__self__, *,
                 access_key: pulumi.Input[str],
                 name: pulumi.Input[str]):
        """
        The parameters of a storage account for a container registry.
        :param pulumi.Input[str] access_key: The access key to the storage account.
        :param pulumi.Input[str] name: The name of the storage account.
        """
        pulumi.set(__self__, "access_key", access_key)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Input[str]:
        """
        The access key to the storage account.
        """
        return pulumi.get(self, "access_key")

    @access_key.setter
    def access_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_key", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the storage account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


