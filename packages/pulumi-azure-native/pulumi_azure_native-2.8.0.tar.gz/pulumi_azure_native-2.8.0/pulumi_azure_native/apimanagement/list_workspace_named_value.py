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
    'ListWorkspaceNamedValueResult',
    'AwaitableListWorkspaceNamedValueResult',
    'list_workspace_named_value',
    'list_workspace_named_value_output',
]

@pulumi.output_type
class ListWorkspaceNamedValueResult:
    """
    Client or app secret used in IdentityProviders, Aad, OpenID or OAuth.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        This is secret value of the NamedValue entity.
        """
        return pulumi.get(self, "value")


class AwaitableListWorkspaceNamedValueResult(ListWorkspaceNamedValueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWorkspaceNamedValueResult(
            value=self.value)


def list_workspace_named_value(named_value_id: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               service_name: Optional[str] = None,
                               workspace_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWorkspaceNamedValueResult:
    """
    Gets the secret of the named value specified by its identifier.
    Azure REST API version: 2022-09-01-preview.


    :param str named_value_id: Identifier of the NamedValue.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    __args__ = dict()
    __args__['namedValueId'] = named_value_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement:listWorkspaceNamedValue', __args__, opts=opts, typ=ListWorkspaceNamedValueResult).value

    return AwaitableListWorkspaceNamedValueResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_workspace_named_value)
def list_workspace_named_value_output(named_value_id: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      service_name: Optional[pulumi.Input[str]] = None,
                                      workspace_id: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWorkspaceNamedValueResult]:
    """
    Gets the secret of the named value specified by its identifier.
    Azure REST API version: 2022-09-01-preview.


    :param str named_value_id: Identifier of the NamedValue.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    ...
