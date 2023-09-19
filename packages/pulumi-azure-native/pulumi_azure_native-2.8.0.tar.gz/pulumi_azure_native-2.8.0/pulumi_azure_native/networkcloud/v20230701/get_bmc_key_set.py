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
    'GetBmcKeySetResult',
    'AwaitableGetBmcKeySetResult',
    'get_bmc_key_set',
    'get_bmc_key_set_output',
]

@pulumi.output_type
class GetBmcKeySetResult:
    def __init__(__self__, azure_group_id=None, detailed_status=None, detailed_status_message=None, expiration=None, extended_location=None, id=None, last_validation=None, location=None, name=None, privilege_level=None, provisioning_state=None, system_data=None, tags=None, type=None, user_list=None, user_list_status=None):
        if azure_group_id and not isinstance(azure_group_id, str):
            raise TypeError("Expected argument 'azure_group_id' to be a str")
        pulumi.set(__self__, "azure_group_id", azure_group_id)
        if detailed_status and not isinstance(detailed_status, str):
            raise TypeError("Expected argument 'detailed_status' to be a str")
        pulumi.set(__self__, "detailed_status", detailed_status)
        if detailed_status_message and not isinstance(detailed_status_message, str):
            raise TypeError("Expected argument 'detailed_status_message' to be a str")
        pulumi.set(__self__, "detailed_status_message", detailed_status_message)
        if expiration and not isinstance(expiration, str):
            raise TypeError("Expected argument 'expiration' to be a str")
        pulumi.set(__self__, "expiration", expiration)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_validation and not isinstance(last_validation, str):
            raise TypeError("Expected argument 'last_validation' to be a str")
        pulumi.set(__self__, "last_validation", last_validation)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if privilege_level and not isinstance(privilege_level, str):
            raise TypeError("Expected argument 'privilege_level' to be a str")
        pulumi.set(__self__, "privilege_level", privilege_level)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_list and not isinstance(user_list, list):
            raise TypeError("Expected argument 'user_list' to be a list")
        pulumi.set(__self__, "user_list", user_list)
        if user_list_status and not isinstance(user_list_status, list):
            raise TypeError("Expected argument 'user_list_status' to be a list")
        pulumi.set(__self__, "user_list_status", user_list_status)

    @property
    @pulumi.getter(name="azureGroupId")
    def azure_group_id(self) -> str:
        """
        The object ID of Azure Active Directory group that all users in the list must be in for access to be granted. Users that are not in the group will not have access.
        """
        return pulumi.get(self, "azure_group_id")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> str:
        """
        The more detailed status of the key set.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> str:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter
    def expiration(self) -> str:
        """
        The date and time after which the users in this key set will be removed from the baseboard management controllers.
        """
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastValidation")
    def last_validation(self) -> str:
        """
        The last time this key set was validated.
        """
        return pulumi.get(self, "last_validation")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privilegeLevel")
    def privilege_level(self) -> str:
        """
        The access level allowed for the users in this key set.
        """
        return pulumi.get(self, "privilege_level")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the baseboard management controller key set.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

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

    @property
    @pulumi.getter(name="userList")
    def user_list(self) -> Sequence['outputs.KeySetUserResponse']:
        """
        The unique list of permitted users.
        """
        return pulumi.get(self, "user_list")

    @property
    @pulumi.getter(name="userListStatus")
    def user_list_status(self) -> Sequence['outputs.KeySetUserStatusResponse']:
        """
        The status evaluation of each user.
        """
        return pulumi.get(self, "user_list_status")


class AwaitableGetBmcKeySetResult(GetBmcKeySetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBmcKeySetResult(
            azure_group_id=self.azure_group_id,
            detailed_status=self.detailed_status,
            detailed_status_message=self.detailed_status_message,
            expiration=self.expiration,
            extended_location=self.extended_location,
            id=self.id,
            last_validation=self.last_validation,
            location=self.location,
            name=self.name,
            privilege_level=self.privilege_level,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            user_list=self.user_list,
            user_list_status=self.user_list_status)


def get_bmc_key_set(bmc_key_set_name: Optional[str] = None,
                    cluster_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBmcKeySetResult:
    """
    Get baseboard management controller key set of the provided cluster.


    :param str bmc_key_set_name: The name of the baseboard management controller key set.
    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['bmcKeySetName'] = bmc_key_set_name
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkcloud/v20230701:getBmcKeySet', __args__, opts=opts, typ=GetBmcKeySetResult).value

    return AwaitableGetBmcKeySetResult(
        azure_group_id=pulumi.get(__ret__, 'azure_group_id'),
        detailed_status=pulumi.get(__ret__, 'detailed_status'),
        detailed_status_message=pulumi.get(__ret__, 'detailed_status_message'),
        expiration=pulumi.get(__ret__, 'expiration'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        last_validation=pulumi.get(__ret__, 'last_validation'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        privilege_level=pulumi.get(__ret__, 'privilege_level'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        user_list=pulumi.get(__ret__, 'user_list'),
        user_list_status=pulumi.get(__ret__, 'user_list_status'))


@_utilities.lift_output_func(get_bmc_key_set)
def get_bmc_key_set_output(bmc_key_set_name: Optional[pulumi.Input[str]] = None,
                           cluster_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBmcKeySetResult]:
    """
    Get baseboard management controller key set of the provided cluster.


    :param str bmc_key_set_name: The name of the baseboard management controller key set.
    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
