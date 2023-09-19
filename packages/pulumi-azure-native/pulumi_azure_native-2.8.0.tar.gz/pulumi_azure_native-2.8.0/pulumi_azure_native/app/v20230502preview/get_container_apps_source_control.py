# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetContainerAppsSourceControlResult',
    'AwaitableGetContainerAppsSourceControlResult',
    'get_container_apps_source_control',
    'get_container_apps_source_control_output',
]

@pulumi.output_type
class GetContainerAppsSourceControlResult:
    """
    Container App SourceControl.
    """
    def __init__(__self__, branch=None, github_action_configuration=None, id=None, name=None, operation_state=None, repo_url=None, system_data=None, type=None):
        if branch and not isinstance(branch, str):
            raise TypeError("Expected argument 'branch' to be a str")
        pulumi.set(__self__, "branch", branch)
        if github_action_configuration and not isinstance(github_action_configuration, dict):
            raise TypeError("Expected argument 'github_action_configuration' to be a dict")
        pulumi.set(__self__, "github_action_configuration", github_action_configuration)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if operation_state and not isinstance(operation_state, str):
            raise TypeError("Expected argument 'operation_state' to be a str")
        pulumi.set(__self__, "operation_state", operation_state)
        if repo_url and not isinstance(repo_url, str):
            raise TypeError("Expected argument 'repo_url' to be a str")
        pulumi.set(__self__, "repo_url", repo_url)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def branch(self) -> Optional[str]:
        """
        The branch which will trigger the auto deployment
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="githubActionConfiguration")
    def github_action_configuration(self) -> Optional['outputs.GithubActionConfigurationResponse']:
        """
        Container App Revision Template with all possible settings and the
        defaults if user did not provide them. The defaults are populated
        as they were at the creation time
        """
        return pulumi.get(self, "github_action_configuration")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationState")
    def operation_state(self) -> str:
        """
        Current provisioning State of the operation
        """
        return pulumi.get(self, "operation_state")

    @property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> Optional[str]:
        """
        The repo url which will be integrated to ContainerApp.
        """
        return pulumi.get(self, "repo_url")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetContainerAppsSourceControlResult(GetContainerAppsSourceControlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerAppsSourceControlResult(
            branch=self.branch,
            github_action_configuration=self.github_action_configuration,
            id=self.id,
            name=self.name,
            operation_state=self.operation_state,
            repo_url=self.repo_url,
            system_data=self.system_data,
            type=self.type)


def get_container_apps_source_control(container_app_name: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      source_control_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerAppsSourceControlResult:
    """
    Container App SourceControl.


    :param str container_app_name: Name of the Container App.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str source_control_name: Name of the Container App SourceControl.
    """
    __args__ = dict()
    __args__['containerAppName'] = container_app_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['sourceControlName'] = source_control_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20230502preview:getContainerAppsSourceControl', __args__, opts=opts, typ=GetContainerAppsSourceControlResult).value

    return AwaitableGetContainerAppsSourceControlResult(
        branch=pulumi.get(__ret__, 'branch'),
        github_action_configuration=pulumi.get(__ret__, 'github_action_configuration'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        operation_state=pulumi.get(__ret__, 'operation_state'),
        repo_url=pulumi.get(__ret__, 'repo_url'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_container_apps_source_control)
def get_container_apps_source_control_output(container_app_name: Optional[pulumi.Input[str]] = None,
                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                             source_control_name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerAppsSourceControlResult]:
    """
    Container App SourceControl.


    :param str container_app_name: Name of the Container App.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str source_control_name: Name of the Container App SourceControl.
    """
    ...
