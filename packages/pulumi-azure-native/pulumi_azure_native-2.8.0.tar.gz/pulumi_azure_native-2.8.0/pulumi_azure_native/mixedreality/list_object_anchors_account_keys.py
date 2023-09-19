# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ListObjectAnchorsAccountKeysResult',
    'AwaitableListObjectAnchorsAccountKeysResult',
    'list_object_anchors_account_keys',
    'list_object_anchors_account_keys_output',
]

@pulumi.output_type
class ListObjectAnchorsAccountKeysResult:
    """
    Developer Keys of account
    """
    def __init__(__self__, primary_key=None, secondary_key=None):
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> str:
        """
        value of primary key.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> str:
        """
        value of secondary key.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListObjectAnchorsAccountKeysResult(ListObjectAnchorsAccountKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListObjectAnchorsAccountKeysResult(
            primary_key=self.primary_key,
            secondary_key=self.secondary_key)


def list_object_anchors_account_keys(account_name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListObjectAnchorsAccountKeysResult:
    """
    List Both of the 2 Keys of an object anchors Account
    Azure REST API version: 2021-03-01-preview.


    :param str account_name: Name of an Mixed Reality Account.
    :param str resource_group_name: Name of an Azure resource group.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:mixedreality:listObjectAnchorsAccountKeys', __args__, opts=opts, typ=ListObjectAnchorsAccountKeysResult).value

    return AwaitableListObjectAnchorsAccountKeysResult(
        primary_key=pulumi.get(__ret__, 'primary_key'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'))


@_utilities.lift_output_func(list_object_anchors_account_keys)
def list_object_anchors_account_keys_output(account_name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListObjectAnchorsAccountKeysResult]:
    """
    List Both of the 2 Keys of an object anchors Account
    Azure REST API version: 2021-03-01-preview.


    :param str account_name: Name of an Mixed Reality Account.
    :param str resource_group_name: Name of an Azure resource group.
    """
    ...
