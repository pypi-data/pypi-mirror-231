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
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
    'get_user_output',
]

@pulumi.output_type
class GetUserResult:
    """
    The User registered to a lab
    """
    def __init__(__self__, email=None, family_name=None, given_name=None, id=None, latest_operation_result=None, location=None, name=None, provisioning_state=None, tags=None, tenant_id=None, total_usage=None, type=None, unique_identifier=None):
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if family_name and not isinstance(family_name, str):
            raise TypeError("Expected argument 'family_name' to be a str")
        pulumi.set(__self__, "family_name", family_name)
        if given_name and not isinstance(given_name, str):
            raise TypeError("Expected argument 'given_name' to be a str")
        pulumi.set(__self__, "given_name", given_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if latest_operation_result and not isinstance(latest_operation_result, dict):
            raise TypeError("Expected argument 'latest_operation_result' to be a dict")
        pulumi.set(__self__, "latest_operation_result", latest_operation_result)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if total_usage and not isinstance(total_usage, str):
            raise TypeError("Expected argument 'total_usage' to be a str")
        pulumi.set(__self__, "total_usage", total_usage)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_identifier and not isinstance(unique_identifier, str):
            raise TypeError("Expected argument 'unique_identifier' to be a str")
        pulumi.set(__self__, "unique_identifier", unique_identifier)

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The user email address, as it was specified during registration.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="familyName")
    def family_name(self) -> str:
        """
        The user family name, as it was specified during registration.
        """
        return pulumi.get(self, "family_name")

    @property
    @pulumi.getter(name="givenName")
    def given_name(self) -> str:
        """
        The user given name, as it was specified during registration.
        """
        return pulumi.get(self, "given_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

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
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The user tenant ID, as it was specified during registration.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="totalUsage")
    def total_usage(self) -> str:
        """
        How long the user has used his VMs in this lab
        """
        return pulumi.get(self, "total_usage")

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


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            email=self.email,
            family_name=self.family_name,
            given_name=self.given_name,
            id=self.id,
            latest_operation_result=self.latest_operation_result,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            tenant_id=self.tenant_id,
            total_usage=self.total_usage,
            type=self.type,
            unique_identifier=self.unique_identifier)


def get_user(expand: Optional[str] = None,
             lab_account_name: Optional[str] = None,
             lab_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             user_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    Get user


    :param str expand: Specify the $expand query. Example: 'properties($select=email)'
    :param str lab_account_name: The name of the lab Account.
    :param str lab_name: The name of the lab.
    :param str resource_group_name: The name of the resource group.
    :param str user_name: The name of the user.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['labAccountName'] = lab_account_name
    __args__['labName'] = lab_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:labservices/v20181015:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        email=pulumi.get(__ret__, 'email'),
        family_name=pulumi.get(__ret__, 'family_name'),
        given_name=pulumi.get(__ret__, 'given_name'),
        id=pulumi.get(__ret__, 'id'),
        latest_operation_result=pulumi.get(__ret__, 'latest_operation_result'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        tags=pulumi.get(__ret__, 'tags'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        total_usage=pulumi.get(__ret__, 'total_usage'),
        type=pulumi.get(__ret__, 'type'),
        unique_identifier=pulumi.get(__ret__, 'unique_identifier'))


@_utilities.lift_output_func(get_user)
def get_user_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                    lab_account_name: Optional[pulumi.Input[str]] = None,
                    lab_name: Optional[pulumi.Input[str]] = None,
                    resource_group_name: Optional[pulumi.Input[str]] = None,
                    user_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserResult]:
    """
    Get user


    :param str expand: Specify the $expand query. Example: 'properties($select=email)'
    :param str lab_account_name: The name of the lab Account.
    :param str lab_name: The name of the lab.
    :param str resource_group_name: The name of the resource group.
    :param str user_name: The name of the user.
    """
    ...
