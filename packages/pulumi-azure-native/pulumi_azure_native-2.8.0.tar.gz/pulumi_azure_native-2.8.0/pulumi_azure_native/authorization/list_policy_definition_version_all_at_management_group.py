# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'ListPolicyDefinitionVersionAllAtManagementGroupResult',
    'AwaitableListPolicyDefinitionVersionAllAtManagementGroupResult',
    'list_policy_definition_version_all_at_management_group',
    'list_policy_definition_version_all_at_management_group_output',
]

@pulumi.output_type
class ListPolicyDefinitionVersionAllAtManagementGroupResult:
    """
    List of policy definition versions.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The URL to use for getting the next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.PolicyDefinitionVersionResponse']]:
        """
        An array of policy definitions versions.
        """
        return pulumi.get(self, "value")


class AwaitableListPolicyDefinitionVersionAllAtManagementGroupResult(ListPolicyDefinitionVersionAllAtManagementGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListPolicyDefinitionVersionAllAtManagementGroupResult(
            next_link=self.next_link,
            value=self.value)


def list_policy_definition_version_all_at_management_group(management_group_name: Optional[str] = None,
                                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListPolicyDefinitionVersionAllAtManagementGroupResult:
    """
    This operation lists all the policy definition versions for all policy definitions at the management group scope.
    Azure REST API version: 2023-04-01.


    :param str management_group_name: The name of the management group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['managementGroupName'] = management_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:authorization:listPolicyDefinitionVersionAllAtManagementGroup', __args__, opts=opts, typ=ListPolicyDefinitionVersionAllAtManagementGroupResult).value

    return AwaitableListPolicyDefinitionVersionAllAtManagementGroupResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_policy_definition_version_all_at_management_group)
def list_policy_definition_version_all_at_management_group_output(management_group_name: Optional[pulumi.Input[str]] = None,
                                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListPolicyDefinitionVersionAllAtManagementGroupResult]:
    """
    This operation lists all the policy definition versions for all policy definitions at the management group scope.
    Azure REST API version: 2023-04-01.


    :param str management_group_name: The name of the management group. The name is case insensitive.
    """
    ...
