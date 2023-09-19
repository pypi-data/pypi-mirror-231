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
    'GetLabResult',
    'AwaitableGetLabResult',
    'get_lab',
    'get_lab_output',
]

@pulumi.output_type
class GetLabResult:
    """
    Represents a lab.
    """
    def __init__(__self__, created_by_object_id=None, created_by_user_principal_name=None, created_date=None, id=None, invitation_code=None, latest_operation_result=None, location=None, max_users_in_lab=None, name=None, provisioning_state=None, tags=None, type=None, unique_identifier=None, usage_quota=None, user_access_mode=None, user_quota=None):
        if created_by_object_id and not isinstance(created_by_object_id, str):
            raise TypeError("Expected argument 'created_by_object_id' to be a str")
        pulumi.set(__self__, "created_by_object_id", created_by_object_id)
        if created_by_user_principal_name and not isinstance(created_by_user_principal_name, str):
            raise TypeError("Expected argument 'created_by_user_principal_name' to be a str")
        pulumi.set(__self__, "created_by_user_principal_name", created_by_user_principal_name)
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if invitation_code and not isinstance(invitation_code, str):
            raise TypeError("Expected argument 'invitation_code' to be a str")
        pulumi.set(__self__, "invitation_code", invitation_code)
        if latest_operation_result and not isinstance(latest_operation_result, dict):
            raise TypeError("Expected argument 'latest_operation_result' to be a dict")
        pulumi.set(__self__, "latest_operation_result", latest_operation_result)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_users_in_lab and not isinstance(max_users_in_lab, int):
            raise TypeError("Expected argument 'max_users_in_lab' to be a int")
        pulumi.set(__self__, "max_users_in_lab", max_users_in_lab)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_identifier and not isinstance(unique_identifier, str):
            raise TypeError("Expected argument 'unique_identifier' to be a str")
        pulumi.set(__self__, "unique_identifier", unique_identifier)
        if usage_quota and not isinstance(usage_quota, str):
            raise TypeError("Expected argument 'usage_quota' to be a str")
        pulumi.set(__self__, "usage_quota", usage_quota)
        if user_access_mode and not isinstance(user_access_mode, str):
            raise TypeError("Expected argument 'user_access_mode' to be a str")
        pulumi.set(__self__, "user_access_mode", user_access_mode)
        if user_quota and not isinstance(user_quota, int):
            raise TypeError("Expected argument 'user_quota' to be a int")
        pulumi.set(__self__, "user_quota", user_quota)

    @property
    @pulumi.getter(name="createdByObjectId")
    def created_by_object_id(self) -> str:
        """
        Object id of the user that created the lab.
        """
        return pulumi.get(self, "created_by_object_id")

    @property
    @pulumi.getter(name="createdByUserPrincipalName")
    def created_by_user_principal_name(self) -> str:
        """
        Lab creator name
        """
        return pulumi.get(self, "created_by_user_principal_name")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        """
        Creation date for the lab
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="invitationCode")
    def invitation_code(self) -> str:
        """
        Invitation code that users can use to join a lab.
        """
        return pulumi.get(self, "invitation_code")

    @property
    @pulumi.getter(name="latestOperationResult")
    def latest_operation_result(self) -> 'outputs.LatestOperationResultResponse':
        """
        The details of the latest operation. ex: status, error
        """
        return pulumi.get(self, "latest_operation_result")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxUsersInLab")
    def max_users_in_lab(self) -> Optional[int]:
        """
        Maximum number of users allowed in the lab.
        """
        return pulumi.get(self, "max_users_in_lab")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> Optional[str]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @property
    @pulumi.getter(name="usageQuota")
    def usage_quota(self) -> Optional[str]:
        """
        Maximum duration a user can use an environment for in the lab.
        """
        return pulumi.get(self, "usage_quota")

    @property
    @pulumi.getter(name="userAccessMode")
    def user_access_mode(self) -> Optional[str]:
        """
        Lab user access mode (open to all vs. restricted to those listed on the lab).
        """
        return pulumi.get(self, "user_access_mode")

    @property
    @pulumi.getter(name="userQuota")
    def user_quota(self) -> int:
        """
        Maximum value MaxUsersInLab can be set to, as specified by the service
        """
        return pulumi.get(self, "user_quota")


class AwaitableGetLabResult(GetLabResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLabResult(
            created_by_object_id=self.created_by_object_id,
            created_by_user_principal_name=self.created_by_user_principal_name,
            created_date=self.created_date,
            id=self.id,
            invitation_code=self.invitation_code,
            latest_operation_result=self.latest_operation_result,
            location=self.location,
            max_users_in_lab=self.max_users_in_lab,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type,
            unique_identifier=self.unique_identifier,
            usage_quota=self.usage_quota,
            user_access_mode=self.user_access_mode,
            user_quota=self.user_quota)


def get_lab(expand: Optional[str] = None,
            lab_account_name: Optional[str] = None,
            lab_name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLabResult:
    """
    Get lab


    :param str expand: Specify the $expand query. Example: 'properties($select=maxUsersInLab)'
    :param str lab_account_name: The name of the lab Account.
    :param str lab_name: The name of the lab.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['labAccountName'] = lab_account_name
    __args__['labName'] = lab_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:labservices/v20181015:getLab', __args__, opts=opts, typ=GetLabResult).value

    return AwaitableGetLabResult(
        created_by_object_id=pulumi.get(__ret__, 'created_by_object_id'),
        created_by_user_principal_name=pulumi.get(__ret__, 'created_by_user_principal_name'),
        created_date=pulumi.get(__ret__, 'created_date'),
        id=pulumi.get(__ret__, 'id'),
        invitation_code=pulumi.get(__ret__, 'invitation_code'),
        latest_operation_result=pulumi.get(__ret__, 'latest_operation_result'),
        location=pulumi.get(__ret__, 'location'),
        max_users_in_lab=pulumi.get(__ret__, 'max_users_in_lab'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        unique_identifier=pulumi.get(__ret__, 'unique_identifier'),
        usage_quota=pulumi.get(__ret__, 'usage_quota'),
        user_access_mode=pulumi.get(__ret__, 'user_access_mode'),
        user_quota=pulumi.get(__ret__, 'user_quota'))


@_utilities.lift_output_func(get_lab)
def get_lab_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                   lab_account_name: Optional[pulumi.Input[str]] = None,
                   lab_name: Optional[pulumi.Input[str]] = None,
                   resource_group_name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLabResult]:
    """
    Get lab


    :param str expand: Specify the $expand query. Example: 'properties($select=maxUsersInLab)'
    :param str lab_account_name: The name of the lab Account.
    :param str lab_name: The name of the lab.
    :param str resource_group_name: The name of the resource group.
    """
    ...
