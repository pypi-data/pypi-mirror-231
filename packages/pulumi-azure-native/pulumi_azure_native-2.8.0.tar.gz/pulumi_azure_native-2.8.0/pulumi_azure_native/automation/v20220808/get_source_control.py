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
    'GetSourceControlResult',
    'AwaitableGetSourceControlResult',
    'get_source_control',
    'get_source_control_output',
]

@pulumi.output_type
class GetSourceControlResult:
    """
    Definition of the source control.
    """
    def __init__(__self__, auto_sync=None, branch=None, creation_time=None, description=None, folder_path=None, id=None, last_modified_time=None, name=None, publish_runbook=None, repo_url=None, source_type=None, type=None):
        if auto_sync and not isinstance(auto_sync, bool):
            raise TypeError("Expected argument 'auto_sync' to be a bool")
        pulumi.set(__self__, "auto_sync", auto_sync)
        if branch and not isinstance(branch, str):
            raise TypeError("Expected argument 'branch' to be a str")
        pulumi.set(__self__, "branch", branch)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if folder_path and not isinstance(folder_path, str):
            raise TypeError("Expected argument 'folder_path' to be a str")
        pulumi.set(__self__, "folder_path", folder_path)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if publish_runbook and not isinstance(publish_runbook, bool):
            raise TypeError("Expected argument 'publish_runbook' to be a bool")
        pulumi.set(__self__, "publish_runbook", publish_runbook)
        if repo_url and not isinstance(repo_url, str):
            raise TypeError("Expected argument 'repo_url' to be a str")
        pulumi.set(__self__, "repo_url", repo_url)
        if source_type and not isinstance(source_type, str):
            raise TypeError("Expected argument 'source_type' to be a str")
        pulumi.set(__self__, "source_type", source_type)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoSync")
    def auto_sync(self) -> Optional[bool]:
        """
        The auto sync of the source control. Default is false.
        """
        return pulumi.get(self, "auto_sync")

    @property
    @pulumi.getter
    def branch(self) -> Optional[str]:
        """
        The repo branch of the source control. Include branch as empty string for VsoTfvc.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        The creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> Optional[str]:
        """
        The folder path of the source control.
        """
        return pulumi.get(self, "folder_path")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[str]:
        """
        The last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publishRunbook")
    def publish_runbook(self) -> Optional[bool]:
        """
        The auto publish of the source control. Default is true.
        """
        return pulumi.get(self, "publish_runbook")

    @property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> Optional[str]:
        """
        The repo url of the source control.
        """
        return pulumi.get(self, "repo_url")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[str]:
        """
        The source type. Must be one of VsoGit, VsoTfvc, GitHub.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetSourceControlResult(GetSourceControlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSourceControlResult(
            auto_sync=self.auto_sync,
            branch=self.branch,
            creation_time=self.creation_time,
            description=self.description,
            folder_path=self.folder_path,
            id=self.id,
            last_modified_time=self.last_modified_time,
            name=self.name,
            publish_runbook=self.publish_runbook,
            repo_url=self.repo_url,
            source_type=self.source_type,
            type=self.type)


def get_source_control(automation_account_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       source_control_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSourceControlResult:
    """
    Retrieve the source control identified by source control name.


    :param str automation_account_name: The name of the automation account.
    :param str resource_group_name: Name of an Azure Resource group.
    :param str source_control_name: The name of source control.
    """
    __args__ = dict()
    __args__['automationAccountName'] = automation_account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['sourceControlName'] = source_control_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:automation/v20220808:getSourceControl', __args__, opts=opts, typ=GetSourceControlResult).value

    return AwaitableGetSourceControlResult(
        auto_sync=pulumi.get(__ret__, 'auto_sync'),
        branch=pulumi.get(__ret__, 'branch'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        description=pulumi.get(__ret__, 'description'),
        folder_path=pulumi.get(__ret__, 'folder_path'),
        id=pulumi.get(__ret__, 'id'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        name=pulumi.get(__ret__, 'name'),
        publish_runbook=pulumi.get(__ret__, 'publish_runbook'),
        repo_url=pulumi.get(__ret__, 'repo_url'),
        source_type=pulumi.get(__ret__, 'source_type'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_source_control)
def get_source_control_output(automation_account_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              source_control_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSourceControlResult]:
    """
    Retrieve the source control identified by source control name.


    :param str automation_account_name: The name of the automation account.
    :param str resource_group_name: Name of an Azure Resource group.
    :param str source_control_name: The name of source control.
    """
    ...
