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
    'GetWorkspaceSharedKeysResult',
    'AwaitableGetWorkspaceSharedKeysResult',
    'get_workspace_shared_keys',
    'get_workspace_shared_keys_output',
]

@pulumi.output_type
class GetWorkspaceSharedKeysResult:
    """
    The shared keys for a workspace.
    """
    def __init__(__self__, primary_shared_key=None, secondary_shared_key=None):
        if primary_shared_key and not isinstance(primary_shared_key, str):
            raise TypeError("Expected argument 'primary_shared_key' to be a str")
        pulumi.set(__self__, "primary_shared_key", primary_shared_key)
        if secondary_shared_key and not isinstance(secondary_shared_key, str):
            raise TypeError("Expected argument 'secondary_shared_key' to be a str")
        pulumi.set(__self__, "secondary_shared_key", secondary_shared_key)

    @property
    @pulumi.getter(name="primarySharedKey")
    def primary_shared_key(self) -> Optional[str]:
        """
        The primary shared key of a workspace.
        """
        return pulumi.get(self, "primary_shared_key")

    @property
    @pulumi.getter(name="secondarySharedKey")
    def secondary_shared_key(self) -> Optional[str]:
        """
        The secondary shared key of a workspace.
        """
        return pulumi.get(self, "secondary_shared_key")


class AwaitableGetWorkspaceSharedKeysResult(GetWorkspaceSharedKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceSharedKeysResult(
            primary_shared_key=self.primary_shared_key,
            secondary_shared_key=self.secondary_shared_key)


def get_workspace_shared_keys(resource_group_name: Optional[str] = None,
                              workspace_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceSharedKeysResult:
    """
    Gets the shared keys for a workspace.


    :param str resource_group_name: The name of the resource group to get. The name is case insensitive.
    :param str workspace_name: Name of the Log Analytics Workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationalinsights/v20151101preview:getWorkspaceSharedKeys', __args__, opts=opts, typ=GetWorkspaceSharedKeysResult).value

    return AwaitableGetWorkspaceSharedKeysResult(
        primary_shared_key=pulumi.get(__ret__, 'primary_shared_key'),
        secondary_shared_key=pulumi.get(__ret__, 'secondary_shared_key'))


@_utilities.lift_output_func(get_workspace_shared_keys)
def get_workspace_shared_keys_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                     workspace_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceSharedKeysResult]:
    """
    Gets the shared keys for a workspace.


    :param str resource_group_name: The name of the resource group to get. The name is case insensitive.
    :param str workspace_name: Name of the Log Analytics Workspace.
    """
    ...
