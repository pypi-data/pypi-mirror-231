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
    'GetAccessPolicyAssignmentResult',
    'AwaitableGetAccessPolicyAssignmentResult',
    'get_access_policy_assignment',
    'get_access_policy_assignment_output',
]

@pulumi.output_type
class GetAccessPolicyAssignmentResult:
    """
    Response to an operation on access policy assignment
    """
    def __init__(__self__, access_policy_name=None, id=None, name=None, object_id=None, object_id_alias=None, provisioning_state=None, type=None):
        if access_policy_name and not isinstance(access_policy_name, str):
            raise TypeError("Expected argument 'access_policy_name' to be a str")
        pulumi.set(__self__, "access_policy_name", access_policy_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        pulumi.set(__self__, "object_id", object_id)
        if object_id_alias and not isinstance(object_id_alias, str):
            raise TypeError("Expected argument 'object_id_alias' to be a str")
        pulumi.set(__self__, "object_id_alias", object_id_alias)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accessPolicyName")
    def access_policy_name(self) -> str:
        """
        The name of the access policy that is being assigned
        """
        return pulumi.get(self, "access_policy_name")

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
    @pulumi.getter(name="objectId")
    def object_id(self) -> str:
        """
        Object Id to assign access policy to
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="objectIdAlias")
    def object_id_alias(self) -> str:
        """
        User friendly name for object id. Also represents username for token based authentication
        """
        return pulumi.get(self, "object_id_alias")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of an access policy assignment set
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAccessPolicyAssignmentResult(GetAccessPolicyAssignmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessPolicyAssignmentResult(
            access_policy_name=self.access_policy_name,
            id=self.id,
            name=self.name,
            object_id=self.object_id,
            object_id_alias=self.object_id_alias,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_access_policy_assignment(access_policy_assignment_name: Optional[str] = None,
                                 cache_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessPolicyAssignmentResult:
    """
    Gets the list of assignments for an access policy of a redis cache
    Azure REST API version: 2023-05-01-preview.


    :param str access_policy_assignment_name: The name of the access policy assignment.
    :param str cache_name: The name of the Redis cache.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accessPolicyAssignmentName'] = access_policy_assignment_name
    __args__['cacheName'] = cache_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cache:getAccessPolicyAssignment', __args__, opts=opts, typ=GetAccessPolicyAssignmentResult).value

    return AwaitableGetAccessPolicyAssignmentResult(
        access_policy_name=pulumi.get(__ret__, 'access_policy_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        object_id=pulumi.get(__ret__, 'object_id'),
        object_id_alias=pulumi.get(__ret__, 'object_id_alias'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_access_policy_assignment)
def get_access_policy_assignment_output(access_policy_assignment_name: Optional[pulumi.Input[str]] = None,
                                        cache_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessPolicyAssignmentResult]:
    """
    Gets the list of assignments for an access policy of a redis cache
    Azure REST API version: 2023-05-01-preview.


    :param str access_policy_assignment_name: The name of the access policy assignment.
    :param str cache_name: The name of the Redis cache.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
