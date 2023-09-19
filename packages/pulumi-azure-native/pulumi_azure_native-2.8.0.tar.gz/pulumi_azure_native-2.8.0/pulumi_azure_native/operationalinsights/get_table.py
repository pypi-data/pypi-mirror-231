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
    'GetTableResult',
    'AwaitableGetTableResult',
    'get_table',
    'get_table_output',
]

@pulumi.output_type
class GetTableResult:
    """
    Workspace data table definition.
    """
    def __init__(__self__, archive_retention_in_days=None, id=None, last_plan_modified_date=None, name=None, plan=None, provisioning_state=None, restored_logs=None, result_statistics=None, retention_in_days=None, retention_in_days_as_default=None, schema=None, search_results=None, system_data=None, total_retention_in_days=None, total_retention_in_days_as_default=None, type=None):
        if archive_retention_in_days and not isinstance(archive_retention_in_days, int):
            raise TypeError("Expected argument 'archive_retention_in_days' to be a int")
        pulumi.set(__self__, "archive_retention_in_days", archive_retention_in_days)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_plan_modified_date and not isinstance(last_plan_modified_date, str):
            raise TypeError("Expected argument 'last_plan_modified_date' to be a str")
        pulumi.set(__self__, "last_plan_modified_date", last_plan_modified_date)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        pulumi.set(__self__, "plan", plan)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if restored_logs and not isinstance(restored_logs, dict):
            raise TypeError("Expected argument 'restored_logs' to be a dict")
        pulumi.set(__self__, "restored_logs", restored_logs)
        if result_statistics and not isinstance(result_statistics, dict):
            raise TypeError("Expected argument 'result_statistics' to be a dict")
        pulumi.set(__self__, "result_statistics", result_statistics)
        if retention_in_days and not isinstance(retention_in_days, int):
            raise TypeError("Expected argument 'retention_in_days' to be a int")
        pulumi.set(__self__, "retention_in_days", retention_in_days)
        if retention_in_days_as_default and not isinstance(retention_in_days_as_default, bool):
            raise TypeError("Expected argument 'retention_in_days_as_default' to be a bool")
        pulumi.set(__self__, "retention_in_days_as_default", retention_in_days_as_default)
        if schema and not isinstance(schema, dict):
            raise TypeError("Expected argument 'schema' to be a dict")
        pulumi.set(__self__, "schema", schema)
        if search_results and not isinstance(search_results, dict):
            raise TypeError("Expected argument 'search_results' to be a dict")
        pulumi.set(__self__, "search_results", search_results)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if total_retention_in_days and not isinstance(total_retention_in_days, int):
            raise TypeError("Expected argument 'total_retention_in_days' to be a int")
        pulumi.set(__self__, "total_retention_in_days", total_retention_in_days)
        if total_retention_in_days_as_default and not isinstance(total_retention_in_days_as_default, bool):
            raise TypeError("Expected argument 'total_retention_in_days_as_default' to be a bool")
        pulumi.set(__self__, "total_retention_in_days_as_default", total_retention_in_days_as_default)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="archiveRetentionInDays")
    def archive_retention_in_days(self) -> int:
        """
        The table data archive retention in days. Calculated as (totalRetentionInDays-retentionInDays)
        """
        return pulumi.get(self, "archive_retention_in_days")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastPlanModifiedDate")
    def last_plan_modified_date(self) -> str:
        """
        The timestamp that table plan was last modified (UTC).
        """
        return pulumi.get(self, "last_plan_modified_date")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> Optional[str]:
        """
        Instruct the system how to handle and charge the logs ingested to this table.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Table's current provisioning state. If set to 'updating', indicates a resource lock due to ongoing operation, forbidding any update to the table until the ongoing operation is concluded.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="restoredLogs")
    def restored_logs(self) -> Optional['outputs.RestoredLogsResponse']:
        """
        Parameters of the restore operation that initiated this table.
        """
        return pulumi.get(self, "restored_logs")

    @property
    @pulumi.getter(name="resultStatistics")
    def result_statistics(self) -> 'outputs.ResultStatisticsResponse':
        """
        Search job execution statistics.
        """
        return pulumi.get(self, "result_statistics")

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[int]:
        """
        The table retention in days, between 4 and 730. Setting this property to -1 will default to the workspace retention.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter(name="retentionInDaysAsDefault")
    def retention_in_days_as_default(self) -> bool:
        """
        True - Value originates from workspace retention in days, False - Customer specific.
        """
        return pulumi.get(self, "retention_in_days_as_default")

    @property
    @pulumi.getter
    def schema(self) -> Optional['outputs.SchemaResponse']:
        """
        Table schema.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="searchResults")
    def search_results(self) -> Optional['outputs.SearchResultsResponse']:
        """
        Parameters of the search job that initiated this table.
        """
        return pulumi.get(self, "search_results")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="totalRetentionInDays")
    def total_retention_in_days(self) -> Optional[int]:
        """
        The table total retention in days, between 4 and 2556. Setting this property to -1 will default to table retention.
        """
        return pulumi.get(self, "total_retention_in_days")

    @property
    @pulumi.getter(name="totalRetentionInDaysAsDefault")
    def total_retention_in_days_as_default(self) -> bool:
        """
        True - Value originates from retention in days, False - Customer specific.
        """
        return pulumi.get(self, "total_retention_in_days_as_default")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetTableResult(GetTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTableResult(
            archive_retention_in_days=self.archive_retention_in_days,
            id=self.id,
            last_plan_modified_date=self.last_plan_modified_date,
            name=self.name,
            plan=self.plan,
            provisioning_state=self.provisioning_state,
            restored_logs=self.restored_logs,
            result_statistics=self.result_statistics,
            retention_in_days=self.retention_in_days,
            retention_in_days_as_default=self.retention_in_days_as_default,
            schema=self.schema,
            search_results=self.search_results,
            system_data=self.system_data,
            total_retention_in_days=self.total_retention_in_days,
            total_retention_in_days_as_default=self.total_retention_in_days_as_default,
            type=self.type)


def get_table(resource_group_name: Optional[str] = None,
              table_name: Optional[str] = None,
              workspace_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTableResult:
    """
    Gets a Log Analytics workspace table.
    Azure REST API version: 2022-10-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str table_name: The name of the table.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['tableName'] = table_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationalinsights:getTable', __args__, opts=opts, typ=GetTableResult).value

    return AwaitableGetTableResult(
        archive_retention_in_days=pulumi.get(__ret__, 'archive_retention_in_days'),
        id=pulumi.get(__ret__, 'id'),
        last_plan_modified_date=pulumi.get(__ret__, 'last_plan_modified_date'),
        name=pulumi.get(__ret__, 'name'),
        plan=pulumi.get(__ret__, 'plan'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        restored_logs=pulumi.get(__ret__, 'restored_logs'),
        result_statistics=pulumi.get(__ret__, 'result_statistics'),
        retention_in_days=pulumi.get(__ret__, 'retention_in_days'),
        retention_in_days_as_default=pulumi.get(__ret__, 'retention_in_days_as_default'),
        schema=pulumi.get(__ret__, 'schema'),
        search_results=pulumi.get(__ret__, 'search_results'),
        system_data=pulumi.get(__ret__, 'system_data'),
        total_retention_in_days=pulumi.get(__ret__, 'total_retention_in_days'),
        total_retention_in_days_as_default=pulumi.get(__ret__, 'total_retention_in_days_as_default'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_table)
def get_table_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                     table_name: Optional[pulumi.Input[str]] = None,
                     workspace_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTableResult]:
    """
    Gets a Log Analytics workspace table.
    Azure REST API version: 2022-10-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str table_name: The name of the table.
    :param str workspace_name: The name of the workspace.
    """
    ...
