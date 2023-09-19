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
    'GetProjectKeysResult',
    'AwaitableGetProjectKeysResult',
    'get_project_keys',
    'get_project_keys_output',
]

@pulumi.output_type
class GetProjectKeysResult:
    """
    ID and Key for Migration Project.
    """
    def __init__(__self__, workspace_id=None, workspace_key=None):
        if workspace_id and not isinstance(workspace_id, str):
            raise TypeError("Expected argument 'workspace_id' to be a str")
        pulumi.set(__self__, "workspace_id", workspace_id)
        if workspace_key and not isinstance(workspace_key, str):
            raise TypeError("Expected argument 'workspace_key' to be a str")
        pulumi.set(__self__, "workspace_key", workspace_key)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> str:
        """
        ID of Migration Project.
        """
        return pulumi.get(self, "workspace_id")

    @property
    @pulumi.getter(name="workspaceKey")
    def workspace_key(self) -> str:
        """
        Key of Migration Project.
        """
        return pulumi.get(self, "workspace_key")


class AwaitableGetProjectKeysResult(GetProjectKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectKeysResult(
            workspace_id=self.workspace_id,
            workspace_key=self.workspace_key)


def get_project_keys(project_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectKeysResult:
    """
    Gets the Log Analytics Workspace ID and Primary Key for the specified project.


    :param str project_name: Name of the Azure Migrate project.
    :param str resource_group_name: Name of the Azure Resource Group that project is part of.
    """
    __args__ = dict()
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:migrate/v20180202:getProjectKeys', __args__, opts=opts, typ=GetProjectKeysResult).value

    return AwaitableGetProjectKeysResult(
        workspace_id=pulumi.get(__ret__, 'workspace_id'),
        workspace_key=pulumi.get(__ret__, 'workspace_key'))


@_utilities.lift_output_func(get_project_keys)
def get_project_keys_output(project_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectKeysResult]:
    """
    Gets the Log Analytics Workspace ID and Primary Key for the specified project.


    :param str project_name: Name of the Azure Migrate project.
    :param str resource_group_name: Name of the Azure Resource Group that project is part of.
    """
    ...
