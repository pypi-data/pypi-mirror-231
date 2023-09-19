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
from ._enums import *

__all__ = ['LabArgs', 'Lab']

@pulumi.input_type
class LabArgs:
    def __init__(__self__, *,
                 lab_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_users_in_lab: Optional[pulumi.Input[int]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unique_identifier: Optional[pulumi.Input[str]] = None,
                 usage_quota: Optional[pulumi.Input[str]] = None,
                 user_access_mode: Optional[pulumi.Input[Union[str, 'LabUserAccessMode']]] = None):
        """
        The set of arguments for constructing a Lab resource.
        :param pulumi.Input[str] lab_account_name: The name of the lab Account.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[int] max_users_in_lab: Maximum number of users allowed in the lab.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] unique_identifier: The unique immutable identifier of a resource (Guid).
        :param pulumi.Input[str] usage_quota: Maximum duration a user can use an environment for in the lab.
        :param pulumi.Input[Union[str, 'LabUserAccessMode']] user_access_mode: Lab user access mode (open to all vs. restricted to those listed on the lab).
        """
        pulumi.set(__self__, "lab_account_name", lab_account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if lab_name is not None:
            pulumi.set(__self__, "lab_name", lab_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if max_users_in_lab is not None:
            pulumi.set(__self__, "max_users_in_lab", max_users_in_lab)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if unique_identifier is not None:
            pulumi.set(__self__, "unique_identifier", unique_identifier)
        if usage_quota is not None:
            pulumi.set(__self__, "usage_quota", usage_quota)
        if user_access_mode is not None:
            pulumi.set(__self__, "user_access_mode", user_access_mode)

    @property
    @pulumi.getter(name="labAccountName")
    def lab_account_name(self) -> pulumi.Input[str]:
        """
        The name of the lab Account.
        """
        return pulumi.get(self, "lab_account_name")

    @lab_account_name.setter
    def lab_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "lab_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="labName")
    def lab_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the lab.
        """
        return pulumi.get(self, "lab_name")

    @lab_name.setter
    def lab_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lab_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="maxUsersInLab")
    def max_users_in_lab(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum number of users allowed in the lab.
        """
        return pulumi.get(self, "max_users_in_lab")

    @max_users_in_lab.setter
    def max_users_in_lab(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_users_in_lab", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @unique_identifier.setter
    def unique_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unique_identifier", value)

    @property
    @pulumi.getter(name="usageQuota")
    def usage_quota(self) -> Optional[pulumi.Input[str]]:
        """
        Maximum duration a user can use an environment for in the lab.
        """
        return pulumi.get(self, "usage_quota")

    @usage_quota.setter
    def usage_quota(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "usage_quota", value)

    @property
    @pulumi.getter(name="userAccessMode")
    def user_access_mode(self) -> Optional[pulumi.Input[Union[str, 'LabUserAccessMode']]]:
        """
        Lab user access mode (open to all vs. restricted to those listed on the lab).
        """
        return pulumi.get(self, "user_access_mode")

    @user_access_mode.setter
    def user_access_mode(self, value: Optional[pulumi.Input[Union[str, 'LabUserAccessMode']]]):
        pulumi.set(self, "user_access_mode", value)


class Lab(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 lab_account_name: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_users_in_lab: Optional[pulumi.Input[int]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unique_identifier: Optional[pulumi.Input[str]] = None,
                 usage_quota: Optional[pulumi.Input[str]] = None,
                 user_access_mode: Optional[pulumi.Input[Union[str, 'LabUserAccessMode']]] = None,
                 __props__=None):
        """
        Represents a lab.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] lab_account_name: The name of the lab Account.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[int] max_users_in_lab: Maximum number of users allowed in the lab.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] unique_identifier: The unique immutable identifier of a resource (Guid).
        :param pulumi.Input[str] usage_quota: Maximum duration a user can use an environment for in the lab.
        :param pulumi.Input[Union[str, 'LabUserAccessMode']] user_access_mode: Lab user access mode (open to all vs. restricted to those listed on the lab).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LabArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a lab.

        :param str resource_name: The name of the resource.
        :param LabArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LabArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 lab_account_name: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_users_in_lab: Optional[pulumi.Input[int]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 unique_identifier: Optional[pulumi.Input[str]] = None,
                 usage_quota: Optional[pulumi.Input[str]] = None,
                 user_access_mode: Optional[pulumi.Input[Union[str, 'LabUserAccessMode']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LabArgs.__new__(LabArgs)

            if lab_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'lab_account_name'")
            __props__.__dict__["lab_account_name"] = lab_account_name
            __props__.__dict__["lab_name"] = lab_name
            __props__.__dict__["location"] = location
            __props__.__dict__["max_users_in_lab"] = max_users_in_lab
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["unique_identifier"] = unique_identifier
            __props__.__dict__["usage_quota"] = usage_quota
            __props__.__dict__["user_access_mode"] = user_access_mode
            __props__.__dict__["created_by_object_id"] = None
            __props__.__dict__["created_by_user_principal_name"] = None
            __props__.__dict__["created_date"] = None
            __props__.__dict__["invitation_code"] = None
            __props__.__dict__["latest_operation_result"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["user_quota"] = None
        super(Lab, __self__).__init__(
            'azure-native:labservices/v20181015:Lab',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Lab':
        """
        Get an existing Lab resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LabArgs.__new__(LabArgs)

        __props__.__dict__["created_by_object_id"] = None
        __props__.__dict__["created_by_user_principal_name"] = None
        __props__.__dict__["created_date"] = None
        __props__.__dict__["invitation_code"] = None
        __props__.__dict__["latest_operation_result"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["max_users_in_lab"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["unique_identifier"] = None
        __props__.__dict__["usage_quota"] = None
        __props__.__dict__["user_access_mode"] = None
        __props__.__dict__["user_quota"] = None
        return Lab(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdByObjectId")
    def created_by_object_id(self) -> pulumi.Output[str]:
        """
        Object id of the user that created the lab.
        """
        return pulumi.get(self, "created_by_object_id")

    @property
    @pulumi.getter(name="createdByUserPrincipalName")
    def created_by_user_principal_name(self) -> pulumi.Output[str]:
        """
        Lab creator name
        """
        return pulumi.get(self, "created_by_user_principal_name")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        Creation date for the lab
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="invitationCode")
    def invitation_code(self) -> pulumi.Output[str]:
        """
        Invitation code that users can use to join a lab.
        """
        return pulumi.get(self, "invitation_code")

    @property
    @pulumi.getter(name="latestOperationResult")
    def latest_operation_result(self) -> pulumi.Output['outputs.LatestOperationResultResponse']:
        """
        The details of the latest operation. ex: status, error
        """
        return pulumi.get(self, "latest_operation_result")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxUsersInLab")
    def max_users_in_lab(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum number of users allowed in the lab.
        """
        return pulumi.get(self, "max_users_in_lab")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @property
    @pulumi.getter(name="usageQuota")
    def usage_quota(self) -> pulumi.Output[Optional[str]]:
        """
        Maximum duration a user can use an environment for in the lab.
        """
        return pulumi.get(self, "usage_quota")

    @property
    @pulumi.getter(name="userAccessMode")
    def user_access_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Lab user access mode (open to all vs. restricted to those listed on the lab).
        """
        return pulumi.get(self, "user_access_mode")

    @property
    @pulumi.getter(name="userQuota")
    def user_quota(self) -> pulumi.Output[int]:
        """
        Maximum value MaxUsersInLab can be set to, as specified by the service
        """
        return pulumi.get(self, "user_quota")

