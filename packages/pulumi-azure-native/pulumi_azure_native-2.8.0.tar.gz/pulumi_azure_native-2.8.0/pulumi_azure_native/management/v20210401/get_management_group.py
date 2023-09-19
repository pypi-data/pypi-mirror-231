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
    'GetManagementGroupResult',
    'AwaitableGetManagementGroupResult',
    'get_management_group',
    'get_management_group_output',
]

@pulumi.output_type
class GetManagementGroupResult:
    """
    The management group details.
    """
    def __init__(__self__, children=None, details=None, display_name=None, id=None, name=None, tenant_id=None, type=None):
        if children and not isinstance(children, list):
            raise TypeError("Expected argument 'children' to be a list")
        pulumi.set(__self__, "children", children)
        if details and not isinstance(details, dict):
            raise TypeError("Expected argument 'details' to be a dict")
        pulumi.set(__self__, "details", details)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def children(self) -> Optional[Sequence['outputs.ManagementGroupChildInfoResponse']]:
        """
        The list of children.
        """
        return pulumi.get(self, "children")

    @property
    @pulumi.getter
    def details(self) -> Optional['outputs.ManagementGroupDetailsResponse']:
        """
        The details of a management group.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The friendly name of the management group.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The fully qualified ID for the management group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the management group. For example, 00000000-0000-0000-0000-000000000000
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.  For example, Microsoft.Management/managementGroups
        """
        return pulumi.get(self, "type")


class AwaitableGetManagementGroupResult(GetManagementGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagementGroupResult(
            children=self.children,
            details=self.details,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            tenant_id=self.tenant_id,
            type=self.type)


def get_management_group(expand: Optional[str] = None,
                         filter: Optional[str] = None,
                         group_id: Optional[str] = None,
                         recurse: Optional[bool] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagementGroupResult:
    """
    Get the details of the management group.


    :param str expand: The $expand=children query string parameter allows clients to request inclusion of children in the response payload.  $expand=path includes the path from the root group to the current group.  $expand=ancestors includes the ancestor Ids of the current group.
    :param str filter: A filter which allows the exclusion of subscriptions from results (i.e. '$filter=children.childType ne Subscription')
    :param str group_id: Management Group ID.
    :param bool recurse: The $recurse=true query string parameter allows clients to request inclusion of entire hierarchy in the response payload. Note that  $expand=children must be passed up if $recurse is set to true.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['filter'] = filter
    __args__['groupId'] = group_id
    __args__['recurse'] = recurse
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:management/v20210401:getManagementGroup', __args__, opts=opts, typ=GetManagementGroupResult).value

    return AwaitableGetManagementGroupResult(
        children=pulumi.get(__ret__, 'children'),
        details=pulumi.get(__ret__, 'details'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_management_group)
def get_management_group_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                                filter: Optional[pulumi.Input[Optional[str]]] = None,
                                group_id: Optional[pulumi.Input[str]] = None,
                                recurse: Optional[pulumi.Input[Optional[bool]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagementGroupResult]:
    """
    Get the details of the management group.


    :param str expand: The $expand=children query string parameter allows clients to request inclusion of children in the response payload.  $expand=path includes the path from the root group to the current group.  $expand=ancestors includes the ancestor Ids of the current group.
    :param str filter: A filter which allows the exclusion of subscriptions from results (i.e. '$filter=children.childType ne Subscription')
    :param str group_id: Management Group ID.
    :param bool recurse: The $recurse=true query string parameter allows clients to request inclusion of entire hierarchy in the response payload. Note that  $expand=children must be passed up if $recurse is set to true.
    """
    ...
