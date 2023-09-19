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
    'GetManagedInstanceLongTermRetentionPolicyResult',
    'AwaitableGetManagedInstanceLongTermRetentionPolicyResult',
    'get_managed_instance_long_term_retention_policy',
    'get_managed_instance_long_term_retention_policy_output',
]

@pulumi.output_type
class GetManagedInstanceLongTermRetentionPolicyResult:
    """
    A long term retention policy.
    """
    def __init__(__self__, id=None, monthly_retention=None, name=None, type=None, week_of_year=None, weekly_retention=None, yearly_retention=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if monthly_retention and not isinstance(monthly_retention, str):
            raise TypeError("Expected argument 'monthly_retention' to be a str")
        pulumi.set(__self__, "monthly_retention", monthly_retention)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if week_of_year and not isinstance(week_of_year, int):
            raise TypeError("Expected argument 'week_of_year' to be a int")
        pulumi.set(__self__, "week_of_year", week_of_year)
        if weekly_retention and not isinstance(weekly_retention, str):
            raise TypeError("Expected argument 'weekly_retention' to be a str")
        pulumi.set(__self__, "weekly_retention", weekly_retention)
        if yearly_retention and not isinstance(yearly_retention, str):
            raise TypeError("Expected argument 'yearly_retention' to be a str")
        pulumi.set(__self__, "yearly_retention", yearly_retention)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="monthlyRetention")
    def monthly_retention(self) -> Optional[str]:
        """
        The monthly retention policy for an LTR backup in an ISO 8601 format.
        """
        return pulumi.get(self, "monthly_retention")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="weekOfYear")
    def week_of_year(self) -> Optional[int]:
        """
        The week of year to take the yearly backup in an ISO 8601 format.
        """
        return pulumi.get(self, "week_of_year")

    @property
    @pulumi.getter(name="weeklyRetention")
    def weekly_retention(self) -> Optional[str]:
        """
        The weekly retention policy for an LTR backup in an ISO 8601 format.
        """
        return pulumi.get(self, "weekly_retention")

    @property
    @pulumi.getter(name="yearlyRetention")
    def yearly_retention(self) -> Optional[str]:
        """
        The yearly retention policy for an LTR backup in an ISO 8601 format.
        """
        return pulumi.get(self, "yearly_retention")


class AwaitableGetManagedInstanceLongTermRetentionPolicyResult(GetManagedInstanceLongTermRetentionPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstanceLongTermRetentionPolicyResult(
            id=self.id,
            monthly_retention=self.monthly_retention,
            name=self.name,
            type=self.type,
            week_of_year=self.week_of_year,
            weekly_retention=self.weekly_retention,
            yearly_retention=self.yearly_retention)


def get_managed_instance_long_term_retention_policy(database_name: Optional[str] = None,
                                                    managed_instance_name: Optional[str] = None,
                                                    policy_name: Optional[str] = None,
                                                    resource_group_name: Optional[str] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstanceLongTermRetentionPolicyResult:
    """
    Gets a managed database's long term retention policy.
    Azure REST API version: 2022-11-01-preview.


    :param str database_name: The name of the database.
    :param str managed_instance_name: The name of the managed instance.
    :param str policy_name: The policy name. Should always be Default.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['managedInstanceName'] = managed_instance_name
    __args__['policyName'] = policy_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql:getManagedInstanceLongTermRetentionPolicy', __args__, opts=opts, typ=GetManagedInstanceLongTermRetentionPolicyResult).value

    return AwaitableGetManagedInstanceLongTermRetentionPolicyResult(
        id=pulumi.get(__ret__, 'id'),
        monthly_retention=pulumi.get(__ret__, 'monthly_retention'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'),
        week_of_year=pulumi.get(__ret__, 'week_of_year'),
        weekly_retention=pulumi.get(__ret__, 'weekly_retention'),
        yearly_retention=pulumi.get(__ret__, 'yearly_retention'))


@_utilities.lift_output_func(get_managed_instance_long_term_retention_policy)
def get_managed_instance_long_term_retention_policy_output(database_name: Optional[pulumi.Input[str]] = None,
                                                           managed_instance_name: Optional[pulumi.Input[str]] = None,
                                                           policy_name: Optional[pulumi.Input[str]] = None,
                                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstanceLongTermRetentionPolicyResult]:
    """
    Gets a managed database's long term retention policy.
    Azure REST API version: 2022-11-01-preview.


    :param str database_name: The name of the database.
    :param str managed_instance_name: The name of the managed instance.
    :param str policy_name: The policy name. Should always be Default.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    ...
