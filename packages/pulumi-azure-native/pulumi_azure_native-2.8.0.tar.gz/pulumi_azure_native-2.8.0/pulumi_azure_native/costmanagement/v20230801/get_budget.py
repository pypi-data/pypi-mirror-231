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
    'GetBudgetResult',
    'AwaitableGetBudgetResult',
    'get_budget',
    'get_budget_output',
]

@pulumi.output_type
class GetBudgetResult:
    """
    A budget resource.
    """
    def __init__(__self__, amount=None, category=None, current_spend=None, e_tag=None, filter=None, forecast_spend=None, id=None, name=None, notifications=None, time_grain=None, time_period=None, type=None):
        if amount and not isinstance(amount, float):
            raise TypeError("Expected argument 'amount' to be a float")
        pulumi.set(__self__, "amount", amount)
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if current_spend and not isinstance(current_spend, dict):
            raise TypeError("Expected argument 'current_spend' to be a dict")
        pulumi.set(__self__, "current_spend", current_spend)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if forecast_spend and not isinstance(forecast_spend, dict):
            raise TypeError("Expected argument 'forecast_spend' to be a dict")
        pulumi.set(__self__, "forecast_spend", forecast_spend)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notifications and not isinstance(notifications, dict):
            raise TypeError("Expected argument 'notifications' to be a dict")
        pulumi.set(__self__, "notifications", notifications)
        if time_grain and not isinstance(time_grain, str):
            raise TypeError("Expected argument 'time_grain' to be a str")
        pulumi.set(__self__, "time_grain", time_grain)
        if time_period and not isinstance(time_period, dict):
            raise TypeError("Expected argument 'time_period' to be a dict")
        pulumi.set(__self__, "time_period", time_period)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def amount(self) -> Optional[float]:
        """
        The total amount of cost to track with the budget.

         Supported for CategoryType(s): Cost.

         Required for CategoryType(s): Cost.
        """
        return pulumi.get(self, "amount")

    @property
    @pulumi.getter
    def category(self) -> str:
        """
        The category of the budget.
        - 'Cost' defines a Budget.
        - 'ReservationUtilization' defines a Reservation Utilization Alert Rule.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="currentSpend")
    def current_spend(self) -> 'outputs.CurrentSpendResponse':
        """
        The current amount of cost which is being tracked for a budget.

         Supported for CategoryType(s): Cost.
        """
        return pulumi.get(self, "current_spend")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[str]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.BudgetFilterResponse']:
        """
        May be used to filter budgets by user-specified dimensions and/or tags.

         Supported for CategoryType(s): Cost, ReservationUtilization.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter(name="forecastSpend")
    def forecast_spend(self) -> 'outputs.ForecastSpendResponse':
        """
        The forecasted cost which is being tracked for a budget.

         Supported for CategoryType(s): Cost.
        """
        return pulumi.get(self, "forecast_spend")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notifications(self) -> Optional[Mapping[str, 'outputs.NotificationResponse']]:
        """
        Dictionary of notifications associated with the budget.

         Supported for CategoryType(s): Cost, ReservationUtilization.

        - Constraints for **CategoryType: Cost** - Budget can have up to 5 notifications with thresholdType: Actual and 5 notifications with thresholdType: Forecasted.
        - Constraints for **CategoryType: ReservationUtilization** - Only one notification allowed. thresholdType is not applicable.
        """
        return pulumi.get(self, "notifications")

    @property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> str:
        """
        The time covered by a budget. Tracking of the amount will be reset based on the time grain.

        Supported for CategoryType(s): Cost, ReservationUtilization.

         Supported timeGrainTypes for **CategoryType: Cost**

        - Monthly
        - Quarterly
        - Annually
        - BillingMonth*
        - BillingQuarter*
        - BillingAnnual*

          *only supported for Web Direct customers.

         Supported timeGrainTypes for **CategoryType: ReservationUtilization**
        - Last7Days
        - Last30Days

         Required for CategoryType(s): Cost, ReservationUtilization.
        """
        return pulumi.get(self, "time_grain")

    @property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> 'outputs.BudgetTimePeriodResponse':
        """
        The time period that defines the active period of the budget. The budget will evaluate data on or after the startDate and will expire on the endDate.

         Supported for CategoryType(s): Cost, ReservationUtilization.

         Required for CategoryType(s): Cost, ReservationUtilization.
        """
        return pulumi.get(self, "time_period")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetBudgetResult(GetBudgetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBudgetResult(
            amount=self.amount,
            category=self.category,
            current_spend=self.current_spend,
            e_tag=self.e_tag,
            filter=self.filter,
            forecast_spend=self.forecast_spend,
            id=self.id,
            name=self.name,
            notifications=self.notifications,
            time_grain=self.time_grain,
            time_period=self.time_period,
            type=self.type)


def get_budget(budget_name: Optional[str] = None,
               scope: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBudgetResult:
    """
    Gets the budget for the scope by budget name.


    :param str budget_name: Budget Name.
    :param str scope: The scope associated with budget operations.
           
            Supported scopes for **CategoryType: Cost**
           
            Azure RBAC Scopes:
           - '/subscriptions/{subscriptionId}/' for subscription scope
           - '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope
           - '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope
           
            EA (Enterprise Agreement) Scopes:
           
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope
           
            MCA (Modern Customer Agreement) Scopes:
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' for customer scope (CSP only)
           
            Supported scopes for **CategoryType: ReservationUtilization**
           
            EA (Enterprise Agreement) Scopes:
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account Scope
           
           MCA (Modern Customer Agreement) Scopes:
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope (non-CSP only)
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' for customer scope (CSP only)
    """
    __args__ = dict()
    __args__['budgetName'] = budget_name
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:costmanagement/v20230801:getBudget', __args__, opts=opts, typ=GetBudgetResult).value

    return AwaitableGetBudgetResult(
        amount=pulumi.get(__ret__, 'amount'),
        category=pulumi.get(__ret__, 'category'),
        current_spend=pulumi.get(__ret__, 'current_spend'),
        e_tag=pulumi.get(__ret__, 'e_tag'),
        filter=pulumi.get(__ret__, 'filter'),
        forecast_spend=pulumi.get(__ret__, 'forecast_spend'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        notifications=pulumi.get(__ret__, 'notifications'),
        time_grain=pulumi.get(__ret__, 'time_grain'),
        time_period=pulumi.get(__ret__, 'time_period'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_budget)
def get_budget_output(budget_name: Optional[pulumi.Input[str]] = None,
                      scope: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBudgetResult]:
    """
    Gets the budget for the scope by budget name.


    :param str budget_name: Budget Name.
    :param str scope: The scope associated with budget operations.
           
            Supported scopes for **CategoryType: Cost**
           
            Azure RBAC Scopes:
           - '/subscriptions/{subscriptionId}/' for subscription scope
           - '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope
           - '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope
           
            EA (Enterprise Agreement) Scopes:
           
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope
           
            MCA (Modern Customer Agreement) Scopes:
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' for customer scope (CSP only)
           
            Supported scopes for **CategoryType: ReservationUtilization**
           
            EA (Enterprise Agreement) Scopes:
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account Scope
           
           MCA (Modern Customer Agreement) Scopes:
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope (non-CSP only)
           - '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' for customer scope (CSP only)
    """
    ...
