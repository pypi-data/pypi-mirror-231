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
    'GetIncidentCommentResult',
    'AwaitableGetIncidentCommentResult',
    'get_incident_comment',
    'get_incident_comment_output',
]

@pulumi.output_type
class GetIncidentCommentResult:
    """
    Represents an incident comment
    """
    def __init__(__self__, author=None, created_time_utc=None, etag=None, id=None, last_modified_time_utc=None, message=None, name=None, system_data=None, type=None):
        if author and not isinstance(author, dict):
            raise TypeError("Expected argument 'author' to be a dict")
        pulumi.set(__self__, "author", author)
        if created_time_utc and not isinstance(created_time_utc, str):
            raise TypeError("Expected argument 'created_time_utc' to be a str")
        pulumi.set(__self__, "created_time_utc", created_time_utc)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_time_utc and not isinstance(last_modified_time_utc, str):
            raise TypeError("Expected argument 'last_modified_time_utc' to be a str")
        pulumi.set(__self__, "last_modified_time_utc", last_modified_time_utc)
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
    def author(self) -> 'outputs.ClientInfoResponse':
        """
        Describes the client that created the comment
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> str:
        """
        The time the comment was created
        """
        return pulumi.get(self, "created_time_utc")

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
        Azure resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> str:
        """
        The time the comment was updated
        """
        return pulumi.get(self, "last_modified_time_utc")

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        The comment message
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name
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
        Azure resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetIncidentCommentResult(GetIncidentCommentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIncidentCommentResult(
            author=self.author,
            created_time_utc=self.created_time_utc,
            etag=self.etag,
            id=self.id,
            last_modified_time_utc=self.last_modified_time_utc,
            message=self.message,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_incident_comment(incident_comment_id: Optional[str] = None,
                         incident_id: Optional[str] = None,
                         operational_insights_resource_provider: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         workspace_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIncidentCommentResult:
    """
    Gets an incident comment.


    :param str incident_comment_id: Incident comment ID
    :param str incident_id: Incident ID
    :param str operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['incidentCommentId'] = incident_comment_id
    __args__['incidentId'] = incident_id
    __args__['operationalInsightsResourceProvider'] = operational_insights_resource_provider
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20210301preview:getIncidentComment', __args__, opts=opts, typ=GetIncidentCommentResult).value

    return AwaitableGetIncidentCommentResult(
        author=pulumi.get(__ret__, 'author'),
        created_time_utc=pulumi.get(__ret__, 'created_time_utc'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        last_modified_time_utc=pulumi.get(__ret__, 'last_modified_time_utc'),
        message=pulumi.get(__ret__, 'message'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_incident_comment)
def get_incident_comment_output(incident_comment_id: Optional[pulumi.Input[str]] = None,
                                incident_id: Optional[pulumi.Input[str]] = None,
                                operational_insights_resource_provider: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                workspace_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIncidentCommentResult]:
    """
    Gets an incident comment.


    :param str incident_comment_id: Incident comment ID
    :param str incident_id: Incident ID
    :param str operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
