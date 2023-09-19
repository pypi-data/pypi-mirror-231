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
    'GetStorageInsightConfigResult',
    'AwaitableGetStorageInsightConfigResult',
    'get_storage_insight_config',
    'get_storage_insight_config_output',
]

@pulumi.output_type
class GetStorageInsightConfigResult:
    """
    The top level storage insight resource container.
    """
    def __init__(__self__, containers=None, e_tag=None, id=None, name=None, status=None, storage_account=None, tables=None, tags=None, type=None):
        if containers and not isinstance(containers, list):
            raise TypeError("Expected argument 'containers' to be a list")
        pulumi.set(__self__, "containers", containers)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if storage_account and not isinstance(storage_account, dict):
            raise TypeError("Expected argument 'storage_account' to be a dict")
        pulumi.set(__self__, "storage_account", storage_account)
        if tables and not isinstance(tables, list):
            raise TypeError("Expected argument 'tables' to be a list")
        pulumi.set(__self__, "tables", tables)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def containers(self) -> Optional[Sequence[str]]:
        """
        The names of the blob containers that the workspace should read
        """
        return pulumi.get(self, "containers")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[str]:
        """
        The ETag of the storage insight.
        """
        return pulumi.get(self, "e_tag")

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
    @pulumi.getter
    def status(self) -> 'outputs.StorageInsightStatusResponse':
        """
        The status of the storage insight
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> 'outputs.StorageAccountResponse':
        """
        The storage account connection details
        """
        return pulumi.get(self, "storage_account")

    @property
    @pulumi.getter
    def tables(self) -> Optional[Sequence[str]]:
        """
        The names of the Azure tables that the workspace should read
        """
        return pulumi.get(self, "tables")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetStorageInsightConfigResult(GetStorageInsightConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStorageInsightConfigResult(
            containers=self.containers,
            e_tag=self.e_tag,
            id=self.id,
            name=self.name,
            status=self.status,
            storage_account=self.storage_account,
            tables=self.tables,
            tags=self.tags,
            type=self.type)


def get_storage_insight_config(resource_group_name: Optional[str] = None,
                               storage_insight_name: Optional[str] = None,
                               workspace_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStorageInsightConfigResult:
    """
    Gets a storage insight instance.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str storage_insight_name: Name of the storageInsightsConfigs resource
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['storageInsightName'] = storage_insight_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationalinsights/v20200801:getStorageInsightConfig', __args__, opts=opts, typ=GetStorageInsightConfigResult).value

    return AwaitableGetStorageInsightConfigResult(
        containers=pulumi.get(__ret__, 'containers'),
        e_tag=pulumi.get(__ret__, 'e_tag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        status=pulumi.get(__ret__, 'status'),
        storage_account=pulumi.get(__ret__, 'storage_account'),
        tables=pulumi.get(__ret__, 'tables'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_storage_insight_config)
def get_storage_insight_config_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                      storage_insight_name: Optional[pulumi.Input[str]] = None,
                                      workspace_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStorageInsightConfigResult]:
    """
    Gets a storage insight instance.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str storage_insight_name: Name of the storageInsightsConfigs resource
    :param str workspace_name: The name of the workspace.
    """
    ...
