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
    'GetScheduledActionByScopeResult',
    'AwaitableGetScheduledActionByScopeResult',
    'get_scheduled_action_by_scope',
    'get_scheduled_action_by_scope_output',
]

@pulumi.output_type
class GetScheduledActionByScopeResult:
    """
    Scheduled action definition.
    """
    def __init__(__self__, display_name=None, e_tag=None, file_destination=None, id=None, kind=None, name=None, notification=None, notification_email=None, schedule=None, scope=None, status=None, system_data=None, type=None, view_id=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if file_destination and not isinstance(file_destination, dict):
            raise TypeError("Expected argument 'file_destination' to be a dict")
        pulumi.set(__self__, "file_destination", file_destination)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notification and not isinstance(notification, dict):
            raise TypeError("Expected argument 'notification' to be a dict")
        pulumi.set(__self__, "notification", notification)
        if notification_email and not isinstance(notification_email, str):
            raise TypeError("Expected argument 'notification_email' to be a str")
        pulumi.set(__self__, "notification_email", notification_email)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if view_id and not isinstance(view_id, str):
            raise TypeError("Expected argument 'view_id' to be a str")
        pulumi.set(__self__, "view_id", view_id)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Scheduled action name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> str:
        """
        Resource Etag. For update calls, eTag is optional and can be specified to achieve optimistic concurrency. Fetch the resource's eTag by doing a 'GET' call first and then including the latest eTag as part of the request body or 'If-Match' header while performing the update. For create calls, eTag is not required.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="fileDestination")
    def file_destination(self) -> Optional['outputs.FileDestinationResponse']:
        """
        Destination format of the view data. This is optional.
        """
        return pulumi.get(self, "file_destination")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of the scheduled action.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notification(self) -> 'outputs.NotificationPropertiesResponse':
        """
        Notification properties based on scheduled action kind.
        """
        return pulumi.get(self, "notification")

    @property
    @pulumi.getter(name="notificationEmail")
    def notification_email(self) -> Optional[str]:
        """
        Email address of the point of contact that should get the unsubscribe requests and notification emails.
        """
        return pulumi.get(self, "notification_email")

    @property
    @pulumi.getter
    def schedule(self) -> 'outputs.SchedulePropertiesResponse':
        """
        Schedule of the scheduled action.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        """
        For private scheduled action(Create or Update), scope will be empty.<br /> For shared scheduled action(Create or Update By Scope), Cost Management scope can be 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for ExternalSubscription scope.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the scheduled action.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Kind of the scheduled action.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="viewId")
    def view_id(self) -> str:
        """
        Cost analysis viewId used for scheduled action. For example, '/providers/Microsoft.CostManagement/views/swaggerExample'
        """
        return pulumi.get(self, "view_id")


class AwaitableGetScheduledActionByScopeResult(GetScheduledActionByScopeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduledActionByScopeResult(
            display_name=self.display_name,
            e_tag=self.e_tag,
            file_destination=self.file_destination,
            id=self.id,
            kind=self.kind,
            name=self.name,
            notification=self.notification,
            notification_email=self.notification_email,
            schedule=self.schedule,
            scope=self.scope,
            status=self.status,
            system_data=self.system_data,
            type=self.type,
            view_id=self.view_id)


def get_scheduled_action_by_scope(name: Optional[str] = None,
                                  scope: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduledActionByScopeResult:
    """
    Get the shared scheduled action from the given scope by name.


    :param str name: Scheduled action name.
    :param str scope: The scope associated with scheduled action operations. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for External Billing Account scope and 'providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for External Subscription scope. Note: Insight Alerts are only available on subscription scope.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:costmanagement/v20230301:getScheduledActionByScope', __args__, opts=opts, typ=GetScheduledActionByScopeResult).value

    return AwaitableGetScheduledActionByScopeResult(
        display_name=pulumi.get(__ret__, 'display_name'),
        e_tag=pulumi.get(__ret__, 'e_tag'),
        file_destination=pulumi.get(__ret__, 'file_destination'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        notification=pulumi.get(__ret__, 'notification'),
        notification_email=pulumi.get(__ret__, 'notification_email'),
        schedule=pulumi.get(__ret__, 'schedule'),
        scope=pulumi.get(__ret__, 'scope'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        view_id=pulumi.get(__ret__, 'view_id'))


@_utilities.lift_output_func(get_scheduled_action_by_scope)
def get_scheduled_action_by_scope_output(name: Optional[pulumi.Input[str]] = None,
                                         scope: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduledActionByScopeResult]:
    """
    Get the shared scheduled action from the given scope by name.


    :param str name: Scheduled action name.
    :param str scope: The scope associated with scheduled action operations. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for External Billing Account scope and 'providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for External Subscription scope. Note: Insight Alerts are only available on subscription scope.
    """
    ...
