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
    'GetApiIssueCommentResult',
    'AwaitableGetApiIssueCommentResult',
    'get_api_issue_comment',
    'get_api_issue_comment_output',
]

@pulumi.output_type
class GetApiIssueCommentResult:
    """
    Issue Comment Contract details.
    """
    def __init__(__self__, created_date=None, id=None, name=None, text=None, type=None, user_id=None):
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if text and not isinstance(text, str):
            raise TypeError("Expected argument 'text' to be a str")
        pulumi.set(__self__, "text", text)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[str]:
        """
        Date and time when the comment was created.
        """
        return pulumi.get(self, "created_date")

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
    def text(self) -> str:
        """
        Comment text.
        """
        return pulumi.get(self, "text")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        A resource identifier for the user who left the comment.
        """
        return pulumi.get(self, "user_id")


class AwaitableGetApiIssueCommentResult(GetApiIssueCommentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiIssueCommentResult(
            created_date=self.created_date,
            id=self.id,
            name=self.name,
            text=self.text,
            type=self.type,
            user_id=self.user_id)


def get_api_issue_comment(api_id: Optional[str] = None,
                          comment_id: Optional[str] = None,
                          issue_id: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          service_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiIssueCommentResult:
    """
    Gets the details of the issue Comment for an API specified by its identifier.
    Azure REST API version: 2022-08-01.


    :param str api_id: API identifier. Must be unique in the current API Management service instance.
    :param str comment_id: Comment identifier within an Issue. Must be unique in the current Issue.
    :param str issue_id: Issue identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['commentId'] = comment_id
    __args__['issueId'] = issue_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement:getApiIssueComment', __args__, opts=opts, typ=GetApiIssueCommentResult).value

    return AwaitableGetApiIssueCommentResult(
        created_date=pulumi.get(__ret__, 'created_date'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        text=pulumi.get(__ret__, 'text'),
        type=pulumi.get(__ret__, 'type'),
        user_id=pulumi.get(__ret__, 'user_id'))


@_utilities.lift_output_func(get_api_issue_comment)
def get_api_issue_comment_output(api_id: Optional[pulumi.Input[str]] = None,
                                 comment_id: Optional[pulumi.Input[str]] = None,
                                 issue_id: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 service_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiIssueCommentResult]:
    """
    Gets the details of the issue Comment for an API specified by its identifier.
    Azure REST API version: 2022-08-01.


    :param str api_id: API identifier. Must be unique in the current API Management service instance.
    :param str comment_id: Comment identifier within an Issue. Must be unique in the current Issue.
    :param str issue_id: Issue identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
