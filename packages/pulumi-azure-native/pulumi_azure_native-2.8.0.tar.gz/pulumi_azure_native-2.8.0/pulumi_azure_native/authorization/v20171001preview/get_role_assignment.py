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
    'GetRoleAssignmentResult',
    'AwaitableGetRoleAssignmentResult',
    'get_role_assignment',
    'get_role_assignment_output',
]

@pulumi.output_type
class GetRoleAssignmentResult:
    """
    Role Assignments
    """
    def __init__(__self__, can_delegate=None, id=None, name=None, principal_id=None, role_definition_id=None, scope=None, type=None):
        if can_delegate and not isinstance(can_delegate, bool):
            raise TypeError("Expected argument 'can_delegate' to be a bool")
        pulumi.set(__self__, "can_delegate", can_delegate)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if principal_id and not isinstance(principal_id, str):
            raise TypeError("Expected argument 'principal_id' to be a str")
        pulumi.set(__self__, "principal_id", principal_id)
        if role_definition_id and not isinstance(role_definition_id, str):
            raise TypeError("Expected argument 'role_definition_id' to be a str")
        pulumi.set(__self__, "role_definition_id", role_definition_id)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="canDelegate")
    def can_delegate(self) -> Optional[bool]:
        """
        The Delegation flag for the role assignment
        """
        return pulumi.get(self, "can_delegate")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The role assignment ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The role assignment name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[str]:
        """
        The principal ID.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[str]:
        """
        The role definition ID.
        """
        return pulumi.get(self, "role_definition_id")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        """
        The role assignment scope.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The role assignment type.
        """
        return pulumi.get(self, "type")


class AwaitableGetRoleAssignmentResult(GetRoleAssignmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleAssignmentResult(
            can_delegate=self.can_delegate,
            id=self.id,
            name=self.name,
            principal_id=self.principal_id,
            role_definition_id=self.role_definition_id,
            scope=self.scope,
            type=self.type)


def get_role_assignment(role_assignment_name: Optional[str] = None,
                        scope: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleAssignmentResult:
    """
    Get the specified role assignment.


    :param str role_assignment_name: The name of the role assignment to get.
    :param str scope: The scope of the role assignment.
    """
    __args__ = dict()
    __args__['roleAssignmentName'] = role_assignment_name
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:authorization/v20171001preview:getRoleAssignment', __args__, opts=opts, typ=GetRoleAssignmentResult).value

    return AwaitableGetRoleAssignmentResult(
        can_delegate=pulumi.get(__ret__, 'can_delegate'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        principal_id=pulumi.get(__ret__, 'principal_id'),
        role_definition_id=pulumi.get(__ret__, 'role_definition_id'),
        scope=pulumi.get(__ret__, 'scope'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_role_assignment)
def get_role_assignment_output(role_assignment_name: Optional[pulumi.Input[str]] = None,
                               scope: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleAssignmentResult]:
    """
    Get the specified role assignment.


    :param str role_assignment_name: The name of the role assignment to get.
    :param str scope: The scope of the role assignment.
    """
    ...
