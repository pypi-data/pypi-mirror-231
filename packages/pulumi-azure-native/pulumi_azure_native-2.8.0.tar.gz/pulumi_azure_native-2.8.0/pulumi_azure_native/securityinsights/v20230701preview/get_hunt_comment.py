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
    'GetHuntCommentResult',
    'AwaitableGetHuntCommentResult',
    'get_hunt_comment',
    'get_hunt_comment_output',
]

@pulumi.output_type
class GetHuntCommentResult:
    """
    Represents a Hunt Comment in Azure Security Insights
    """
    def __init__(__self__, etag=None, id=None, message=None, name=None, system_data=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if message and not isinstance(message, str):
            raise TypeError("Expected argument 'message' to be a str")
        pulumi.set(__self__, "message", message)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        The message for the comment
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

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


class AwaitableGetHuntCommentResult(GetHuntCommentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHuntCommentResult(
            etag=self.etag,
            id=self.id,
            message=self.message,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_hunt_comment(hunt_comment_id: Optional[str] = None,
                     hunt_id: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     workspace_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHuntCommentResult:
    """
    Gets a hunt comment


    :param str hunt_comment_id: The hunt comment id (GUID)
    :param str hunt_id: The hunt id (GUID)
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['huntCommentId'] = hunt_comment_id
    __args__['huntId'] = hunt_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20230701preview:getHuntComment', __args__, opts=opts, typ=GetHuntCommentResult).value

    return AwaitableGetHuntCommentResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        message=pulumi.get(__ret__, 'message'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_hunt_comment)
def get_hunt_comment_output(hunt_comment_id: Optional[pulumi.Input[str]] = None,
                            hunt_id: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            workspace_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHuntCommentResult]:
    """
    Gets a hunt comment


    :param str hunt_comment_id: The hunt comment id (GUID)
    :param str hunt_id: The hunt id (GUID)
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
