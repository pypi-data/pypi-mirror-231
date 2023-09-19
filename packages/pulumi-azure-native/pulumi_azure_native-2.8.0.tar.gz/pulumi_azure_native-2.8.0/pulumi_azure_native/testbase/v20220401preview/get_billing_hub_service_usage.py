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
    'GetBillingHubServiceUsageResult',
    'AwaitableGetBillingHubServiceUsageResult',
    'get_billing_hub_service_usage',
    'get_billing_hub_service_usage_output',
]

@pulumi.output_type
class GetBillingHubServiceUsageResult:
    def __init__(__self__, next_request=None, package_usage_entries=None, total_charges=None, total_used_billable_hours=None, total_used_free_hours=None):
        if next_request and not isinstance(next_request, dict):
            raise TypeError("Expected argument 'next_request' to be a dict")
        pulumi.set(__self__, "next_request", next_request)
        if package_usage_entries and not isinstance(package_usage_entries, list):
            raise TypeError("Expected argument 'package_usage_entries' to be a list")
        pulumi.set(__self__, "package_usage_entries", package_usage_entries)
        if total_charges and not isinstance(total_charges, float):
            raise TypeError("Expected argument 'total_charges' to be a float")
        pulumi.set(__self__, "total_charges", total_charges)
        if total_used_billable_hours and not isinstance(total_used_billable_hours, float):
            raise TypeError("Expected argument 'total_used_billable_hours' to be a float")
        pulumi.set(__self__, "total_used_billable_hours", total_used_billable_hours)
        if total_used_free_hours and not isinstance(total_used_free_hours, float):
            raise TypeError("Expected argument 'total_used_free_hours' to be a float")
        pulumi.set(__self__, "total_used_free_hours", total_used_free_hours)

    @property
    @pulumi.getter(name="nextRequest")
    def next_request(self) -> Optional['outputs.BillingHubGetUsageRequestResponse']:
        return pulumi.get(self, "next_request")

    @property
    @pulumi.getter(name="packageUsageEntries")
    def package_usage_entries(self) -> Optional[Sequence['outputs.BillingHubPackageUsageResponse']]:
        return pulumi.get(self, "package_usage_entries")

    @property
    @pulumi.getter(name="totalCharges")
    def total_charges(self) -> Optional[float]:
        return pulumi.get(self, "total_charges")

    @property
    @pulumi.getter(name="totalUsedBillableHours")
    def total_used_billable_hours(self) -> Optional[float]:
        return pulumi.get(self, "total_used_billable_hours")

    @property
    @pulumi.getter(name="totalUsedFreeHours")
    def total_used_free_hours(self) -> Optional[float]:
        return pulumi.get(self, "total_used_free_hours")


class AwaitableGetBillingHubServiceUsageResult(GetBillingHubServiceUsageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBillingHubServiceUsageResult(
            next_request=self.next_request,
            package_usage_entries=self.package_usage_entries,
            total_charges=self.total_charges,
            total_used_billable_hours=self.total_used_billable_hours,
            total_used_free_hours=self.total_used_free_hours)


def get_billing_hub_service_usage(end_time_stamp: Optional[str] = None,
                                  page_index: Optional[int] = None,
                                  page_size: Optional[int] = None,
                                  resource_group_name: Optional[str] = None,
                                  start_time_stamp: Optional[str] = None,
                                  test_base_account_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBillingHubServiceUsageResult:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: The name of the resource group that contains the resource.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    __args__ = dict()
    __args__['endTimeStamp'] = end_time_stamp
    __args__['pageIndex'] = page_index
    __args__['pageSize'] = page_size
    __args__['resourceGroupName'] = resource_group_name
    __args__['startTimeStamp'] = start_time_stamp
    __args__['testBaseAccountName'] = test_base_account_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:testbase/v20220401preview:getBillingHubServiceUsage', __args__, opts=opts, typ=GetBillingHubServiceUsageResult).value

    return AwaitableGetBillingHubServiceUsageResult(
        next_request=pulumi.get(__ret__, 'next_request'),
        package_usage_entries=pulumi.get(__ret__, 'package_usage_entries'),
        total_charges=pulumi.get(__ret__, 'total_charges'),
        total_used_billable_hours=pulumi.get(__ret__, 'total_used_billable_hours'),
        total_used_free_hours=pulumi.get(__ret__, 'total_used_free_hours'))


@_utilities.lift_output_func(get_billing_hub_service_usage)
def get_billing_hub_service_usage_output(end_time_stamp: Optional[pulumi.Input[str]] = None,
                                         page_index: Optional[pulumi.Input[Optional[int]]] = None,
                                         page_size: Optional[pulumi.Input[Optional[int]]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         start_time_stamp: Optional[pulumi.Input[str]] = None,
                                         test_base_account_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBillingHubServiceUsageResult]:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: The name of the resource group that contains the resource.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    ...
