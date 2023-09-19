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
    'GetWorkspaceGroupResult',
    'AwaitableGetWorkspaceGroupResult',
    'get_workspace_group',
    'get_workspace_group_output',
]

@pulumi.output_type
class GetWorkspaceGroupResult:
    """
    Contract details.
    """
    def __init__(__self__, built_in=None, description=None, display_name=None, external_id=None, id=None, name=None, type=None):
        if built_in and not isinstance(built_in, bool):
            raise TypeError("Expected argument 'built_in' to be a bool")
        pulumi.set(__self__, "built_in", built_in)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_id and not isinstance(external_id, str):
            raise TypeError("Expected argument 'external_id' to be a str")
        pulumi.set(__self__, "external_id", external_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="builtIn")
    def built_in(self) -> bool:
        """
        true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.
        """
        return pulumi.get(self, "built_in")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Group description. Can contain HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Group name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[str]:
        """
        For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.
        """
        return pulumi.get(self, "external_id")

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
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceGroupResult(GetWorkspaceGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceGroupResult(
            built_in=self.built_in,
            description=self.description,
            display_name=self.display_name,
            external_id=self.external_id,
            id=self.id,
            name=self.name,
            type=self.type)


def get_workspace_group(group_id: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        service_name: Optional[str] = None,
                        workspace_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceGroupResult:
    """
    Gets the details of the group specified by its identifier.


    :param str group_id: Group identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    __args__ = dict()
    __args__['groupId'] = group_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20220901preview:getWorkspaceGroup', __args__, opts=opts, typ=GetWorkspaceGroupResult).value

    return AwaitableGetWorkspaceGroupResult(
        built_in=pulumi.get(__ret__, 'built_in'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        external_id=pulumi.get(__ret__, 'external_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workspace_group)
def get_workspace_group_output(group_id: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               service_name: Optional[pulumi.Input[str]] = None,
                               workspace_id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceGroupResult]:
    """
    Gets the details of the group specified by its identifier.


    :param str group_id: Group identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    ...
