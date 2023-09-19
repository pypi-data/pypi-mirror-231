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
from ._enums import *

__all__ = [
    'AdvancedScheduleMonthlyOccurrenceResponse',
    'AdvancedScheduleResponse',
    'AzureQueryPropertiesResponse',
    'ErrorResponseResponse',
    'LinuxPropertiesResponse',
    'NonAzureQueryPropertiesResponse',
    'SUCSchedulePropertiesResponse',
    'SoftwareUpdateConfigurationTasksResponse',
    'TagSettingsPropertiesResponse',
    'TargetPropertiesResponse',
    'TaskPropertiesResponse',
    'UpdateConfigurationResponse',
    'WindowsPropertiesResponse',
]

@pulumi.output_type
class AdvancedScheduleMonthlyOccurrenceResponse(dict):
    """
    The properties of the create advanced schedule monthly occurrence.
    """
    def __init__(__self__, *,
                 day: Optional[str] = None,
                 occurrence: Optional[int] = None):
        """
        The properties of the create advanced schedule monthly occurrence.
        :param str day: Day of the occurrence. Must be one of monday, tuesday, wednesday, thursday, friday, saturday, sunday.
        :param int occurrence: Occurrence of the week within the month. Must be between 1 and 5
        """
        if day is not None:
            pulumi.set(__self__, "day", day)
        if occurrence is not None:
            pulumi.set(__self__, "occurrence", occurrence)

    @property
    @pulumi.getter
    def day(self) -> Optional[str]:
        """
        Day of the occurrence. Must be one of monday, tuesday, wednesday, thursday, friday, saturday, sunday.
        """
        return pulumi.get(self, "day")

    @property
    @pulumi.getter
    def occurrence(self) -> Optional[int]:
        """
        Occurrence of the week within the month. Must be between 1 and 5
        """
        return pulumi.get(self, "occurrence")


@pulumi.output_type
class AdvancedScheduleResponse(dict):
    """
    The properties of the create Advanced Schedule.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "monthDays":
            suggest = "month_days"
        elif key == "monthlyOccurrences":
            suggest = "monthly_occurrences"
        elif key == "weekDays":
            suggest = "week_days"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AdvancedScheduleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AdvancedScheduleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AdvancedScheduleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 month_days: Optional[Sequence[int]] = None,
                 monthly_occurrences: Optional[Sequence['outputs.AdvancedScheduleMonthlyOccurrenceResponse']] = None,
                 week_days: Optional[Sequence[str]] = None):
        """
        The properties of the create Advanced Schedule.
        :param Sequence[int] month_days: Days of the month that the job should execute on. Must be between 1 and 31.
        :param Sequence['AdvancedScheduleMonthlyOccurrenceResponse'] monthly_occurrences: Occurrences of days within a month.
        :param Sequence[str] week_days: Days of the week that the job should execute on.
        """
        if month_days is not None:
            pulumi.set(__self__, "month_days", month_days)
        if monthly_occurrences is not None:
            pulumi.set(__self__, "monthly_occurrences", monthly_occurrences)
        if week_days is not None:
            pulumi.set(__self__, "week_days", week_days)

    @property
    @pulumi.getter(name="monthDays")
    def month_days(self) -> Optional[Sequence[int]]:
        """
        Days of the month that the job should execute on. Must be between 1 and 31.
        """
        return pulumi.get(self, "month_days")

    @property
    @pulumi.getter(name="monthlyOccurrences")
    def monthly_occurrences(self) -> Optional[Sequence['outputs.AdvancedScheduleMonthlyOccurrenceResponse']]:
        """
        Occurrences of days within a month.
        """
        return pulumi.get(self, "monthly_occurrences")

    @property
    @pulumi.getter(name="weekDays")
    def week_days(self) -> Optional[Sequence[str]]:
        """
        Days of the week that the job should execute on.
        """
        return pulumi.get(self, "week_days")


@pulumi.output_type
class AzureQueryPropertiesResponse(dict):
    """
    Azure query for the update configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "tagSettings":
            suggest = "tag_settings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AzureQueryPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AzureQueryPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AzureQueryPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 locations: Optional[Sequence[str]] = None,
                 scope: Optional[Sequence[str]] = None,
                 tag_settings: Optional['outputs.TagSettingsPropertiesResponse'] = None):
        """
        Azure query for the update configuration.
        :param Sequence[str] locations: List of locations to scope the query to.
        :param Sequence[str] scope: List of Subscription or Resource Group ARM Ids.
        :param 'TagSettingsPropertiesResponse' tag_settings: Tag settings for the VM.
        """
        if locations is not None:
            pulumi.set(__self__, "locations", locations)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if tag_settings is not None:
            pulumi.set(__self__, "tag_settings", tag_settings)

    @property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[str]]:
        """
        List of locations to scope the query to.
        """
        return pulumi.get(self, "locations")

    @property
    @pulumi.getter
    def scope(self) -> Optional[Sequence[str]]:
        """
        List of Subscription or Resource Group ARM Ids.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="tagSettings")
    def tag_settings(self) -> Optional['outputs.TagSettingsPropertiesResponse']:
        """
        Tag settings for the VM.
        """
        return pulumi.get(self, "tag_settings")


@pulumi.output_type
class ErrorResponseResponse(dict):
    """
    Error response of an operation failure
    """
    def __init__(__self__, *,
                 code: Optional[str] = None,
                 message: Optional[str] = None):
        """
        Error response of an operation failure
        :param str code: Error code
        :param str message: Error message indicating why the operation failed.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def code(self) -> Optional[str]:
        """
        Error code
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        Error message indicating why the operation failed.
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class LinuxPropertiesResponse(dict):
    """
    Linux specific update configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "excludedPackageNameMasks":
            suggest = "excluded_package_name_masks"
        elif key == "includedPackageClassifications":
            suggest = "included_package_classifications"
        elif key == "includedPackageNameMasks":
            suggest = "included_package_name_masks"
        elif key == "rebootSetting":
            suggest = "reboot_setting"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LinuxPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LinuxPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LinuxPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 excluded_package_name_masks: Optional[Sequence[str]] = None,
                 included_package_classifications: Optional[str] = None,
                 included_package_name_masks: Optional[Sequence[str]] = None,
                 reboot_setting: Optional[str] = None):
        """
        Linux specific update configuration.
        :param Sequence[str] excluded_package_name_masks: packages excluded from the software update configuration.
        :param str included_package_classifications: Update classifications included in the software update configuration.
        :param Sequence[str] included_package_name_masks: packages included from the software update configuration.
        :param str reboot_setting: Reboot setting for the software update configuration.
        """
        if excluded_package_name_masks is not None:
            pulumi.set(__self__, "excluded_package_name_masks", excluded_package_name_masks)
        if included_package_classifications is not None:
            pulumi.set(__self__, "included_package_classifications", included_package_classifications)
        if included_package_name_masks is not None:
            pulumi.set(__self__, "included_package_name_masks", included_package_name_masks)
        if reboot_setting is not None:
            pulumi.set(__self__, "reboot_setting", reboot_setting)

    @property
    @pulumi.getter(name="excludedPackageNameMasks")
    def excluded_package_name_masks(self) -> Optional[Sequence[str]]:
        """
        packages excluded from the software update configuration.
        """
        return pulumi.get(self, "excluded_package_name_masks")

    @property
    @pulumi.getter(name="includedPackageClassifications")
    def included_package_classifications(self) -> Optional[str]:
        """
        Update classifications included in the software update configuration.
        """
        return pulumi.get(self, "included_package_classifications")

    @property
    @pulumi.getter(name="includedPackageNameMasks")
    def included_package_name_masks(self) -> Optional[Sequence[str]]:
        """
        packages included from the software update configuration.
        """
        return pulumi.get(self, "included_package_name_masks")

    @property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[str]:
        """
        Reboot setting for the software update configuration.
        """
        return pulumi.get(self, "reboot_setting")


@pulumi.output_type
class NonAzureQueryPropertiesResponse(dict):
    """
    Non Azure query for the update configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "functionAlias":
            suggest = "function_alias"
        elif key == "workspaceId":
            suggest = "workspace_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NonAzureQueryPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NonAzureQueryPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NonAzureQueryPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 function_alias: Optional[str] = None,
                 workspace_id: Optional[str] = None):
        """
        Non Azure query for the update configuration.
        :param str function_alias: Log Analytics Saved Search name.
        :param str workspace_id: Workspace Id for Log Analytics in which the saved Search is resided.
        """
        if function_alias is not None:
            pulumi.set(__self__, "function_alias", function_alias)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="functionAlias")
    def function_alias(self) -> Optional[str]:
        """
        Log Analytics Saved Search name.
        """
        return pulumi.get(self, "function_alias")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[str]:
        """
        Workspace Id for Log Analytics in which the saved Search is resided.
        """
        return pulumi.get(self, "workspace_id")


@pulumi.output_type
class SUCSchedulePropertiesResponse(dict):
    """
    Definition of schedule parameters.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "startTimeOffsetMinutes":
            suggest = "start_time_offset_minutes"
        elif key == "advancedSchedule":
            suggest = "advanced_schedule"
        elif key == "creationTime":
            suggest = "creation_time"
        elif key == "expiryTime":
            suggest = "expiry_time"
        elif key == "expiryTimeOffsetMinutes":
            suggest = "expiry_time_offset_minutes"
        elif key == "isEnabled":
            suggest = "is_enabled"
        elif key == "lastModifiedTime":
            suggest = "last_modified_time"
        elif key == "nextRun":
            suggest = "next_run"
        elif key == "nextRunOffsetMinutes":
            suggest = "next_run_offset_minutes"
        elif key == "startTime":
            suggest = "start_time"
        elif key == "timeZone":
            suggest = "time_zone"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SUCSchedulePropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SUCSchedulePropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SUCSchedulePropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 start_time_offset_minutes: float,
                 advanced_schedule: Optional['outputs.AdvancedScheduleResponse'] = None,
                 creation_time: Optional[str] = None,
                 description: Optional[str] = None,
                 expiry_time: Optional[str] = None,
                 expiry_time_offset_minutes: Optional[float] = None,
                 frequency: Optional[str] = None,
                 interval: Optional[float] = None,
                 is_enabled: Optional[bool] = None,
                 last_modified_time: Optional[str] = None,
                 next_run: Optional[str] = None,
                 next_run_offset_minutes: Optional[float] = None,
                 start_time: Optional[str] = None,
                 time_zone: Optional[str] = None):
        """
        Definition of schedule parameters.
        :param float start_time_offset_minutes: Gets the start time's offset in minutes.
        :param 'AdvancedScheduleResponse' advanced_schedule: Gets or sets the advanced schedule.
        :param str creation_time: Gets or sets the creation time.
        :param str description: Gets or sets the description.
        :param str expiry_time: Gets or sets the end time of the schedule.
        :param float expiry_time_offset_minutes: Gets or sets the expiry time's offset in minutes.
        :param str frequency: Gets or sets the frequency of the schedule.
        :param float interval: Gets or sets the interval of the schedule.
        :param bool is_enabled: Gets or sets a value indicating whether this schedule is enabled.
        :param str last_modified_time: Gets or sets the last modified time.
        :param str next_run: Gets or sets the next run time of the schedule.
        :param float next_run_offset_minutes: Gets or sets the next run time's offset in minutes.
        :param str start_time: Gets or sets the start time of the schedule.
        :param str time_zone: Gets or sets the time zone of the schedule.
        """
        pulumi.set(__self__, "start_time_offset_minutes", start_time_offset_minutes)
        if advanced_schedule is not None:
            pulumi.set(__self__, "advanced_schedule", advanced_schedule)
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expiry_time is not None:
            pulumi.set(__self__, "expiry_time", expiry_time)
        if expiry_time_offset_minutes is not None:
            pulumi.set(__self__, "expiry_time_offset_minutes", expiry_time_offset_minutes)
        if frequency is not None:
            pulumi.set(__self__, "frequency", frequency)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if is_enabled is None:
            is_enabled = False
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)
        if last_modified_time is not None:
            pulumi.set(__self__, "last_modified_time", last_modified_time)
        if next_run is not None:
            pulumi.set(__self__, "next_run", next_run)
        if next_run_offset_minutes is not None:
            pulumi.set(__self__, "next_run_offset_minutes", next_run_offset_minutes)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="startTimeOffsetMinutes")
    def start_time_offset_minutes(self) -> float:
        """
        Gets the start time's offset in minutes.
        """
        return pulumi.get(self, "start_time_offset_minutes")

    @property
    @pulumi.getter(name="advancedSchedule")
    def advanced_schedule(self) -> Optional['outputs.AdvancedScheduleResponse']:
        """
        Gets or sets the advanced schedule.
        """
        return pulumi.get(self, "advanced_schedule")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        Gets or sets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[str]:
        """
        Gets or sets the end time of the schedule.
        """
        return pulumi.get(self, "expiry_time")

    @property
    @pulumi.getter(name="expiryTimeOffsetMinutes")
    def expiry_time_offset_minutes(self) -> Optional[float]:
        """
        Gets or sets the expiry time's offset in minutes.
        """
        return pulumi.get(self, "expiry_time_offset_minutes")

    @property
    @pulumi.getter
    def frequency(self) -> Optional[str]:
        """
        Gets or sets the frequency of the schedule.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def interval(self) -> Optional[float]:
        """
        Gets or sets the interval of the schedule.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[bool]:
        """
        Gets or sets a value indicating whether this schedule is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[str]:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="nextRun")
    def next_run(self) -> Optional[str]:
        """
        Gets or sets the next run time of the schedule.
        """
        return pulumi.get(self, "next_run")

    @property
    @pulumi.getter(name="nextRunOffsetMinutes")
    def next_run_offset_minutes(self) -> Optional[float]:
        """
        Gets or sets the next run time's offset in minutes.
        """
        return pulumi.get(self, "next_run_offset_minutes")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        Gets or sets the start time of the schedule.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[str]:
        """
        Gets or sets the time zone of the schedule.
        """
        return pulumi.get(self, "time_zone")


@pulumi.output_type
class SoftwareUpdateConfigurationTasksResponse(dict):
    """
    Task properties of the software update configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "postTask":
            suggest = "post_task"
        elif key == "preTask":
            suggest = "pre_task"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SoftwareUpdateConfigurationTasksResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SoftwareUpdateConfigurationTasksResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SoftwareUpdateConfigurationTasksResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 post_task: Optional['outputs.TaskPropertiesResponse'] = None,
                 pre_task: Optional['outputs.TaskPropertiesResponse'] = None):
        """
        Task properties of the software update configuration.
        :param 'TaskPropertiesResponse' post_task: Post task properties.
        :param 'TaskPropertiesResponse' pre_task: Pre task properties.
        """
        if post_task is not None:
            pulumi.set(__self__, "post_task", post_task)
        if pre_task is not None:
            pulumi.set(__self__, "pre_task", pre_task)

    @property
    @pulumi.getter(name="postTask")
    def post_task(self) -> Optional['outputs.TaskPropertiesResponse']:
        """
        Post task properties.
        """
        return pulumi.get(self, "post_task")

    @property
    @pulumi.getter(name="preTask")
    def pre_task(self) -> Optional['outputs.TaskPropertiesResponse']:
        """
        Pre task properties.
        """
        return pulumi.get(self, "pre_task")


@pulumi.output_type
class TagSettingsPropertiesResponse(dict):
    """
    Tag filter information for the VM.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "filterOperator":
            suggest = "filter_operator"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TagSettingsPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TagSettingsPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TagSettingsPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 filter_operator: Optional[str] = None,
                 tags: Optional[Mapping[str, Sequence[str]]] = None):
        """
        Tag filter information for the VM.
        :param str filter_operator: Filter VMs by Any or All specified tags.
        :param Mapping[str, Sequence[str]] tags: Dictionary of tags with its list of values.
        """
        if filter_operator is not None:
            pulumi.set(__self__, "filter_operator", filter_operator)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="filterOperator")
    def filter_operator(self) -> Optional[str]:
        """
        Filter VMs by Any or All specified tags.
        """
        return pulumi.get(self, "filter_operator")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Sequence[str]]]:
        """
        Dictionary of tags with its list of values.
        """
        return pulumi.get(self, "tags")


@pulumi.output_type
class TargetPropertiesResponse(dict):
    """
    Group specific to the update configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "azureQueries":
            suggest = "azure_queries"
        elif key == "nonAzureQueries":
            suggest = "non_azure_queries"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TargetPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TargetPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TargetPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 azure_queries: Optional[Sequence['outputs.AzureQueryPropertiesResponse']] = None,
                 non_azure_queries: Optional[Sequence['outputs.NonAzureQueryPropertiesResponse']] = None):
        """
        Group specific to the update configuration.
        :param Sequence['AzureQueryPropertiesResponse'] azure_queries: List of Azure queries in the software update configuration.
        :param Sequence['NonAzureQueryPropertiesResponse'] non_azure_queries: List of non Azure queries in the software update configuration.
        """
        if azure_queries is not None:
            pulumi.set(__self__, "azure_queries", azure_queries)
        if non_azure_queries is not None:
            pulumi.set(__self__, "non_azure_queries", non_azure_queries)

    @property
    @pulumi.getter(name="azureQueries")
    def azure_queries(self) -> Optional[Sequence['outputs.AzureQueryPropertiesResponse']]:
        """
        List of Azure queries in the software update configuration.
        """
        return pulumi.get(self, "azure_queries")

    @property
    @pulumi.getter(name="nonAzureQueries")
    def non_azure_queries(self) -> Optional[Sequence['outputs.NonAzureQueryPropertiesResponse']]:
        """
        List of non Azure queries in the software update configuration.
        """
        return pulumi.get(self, "non_azure_queries")


@pulumi.output_type
class TaskPropertiesResponse(dict):
    """
    Task properties of the software update configuration.
    """
    def __init__(__self__, *,
                 parameters: Optional[Mapping[str, str]] = None,
                 source: Optional[str] = None):
        """
        Task properties of the software update configuration.
        :param Mapping[str, str] parameters: Gets or sets the parameters of the task.
        :param str source: Gets or sets the name of the runbook.
        """
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if source is not None:
            pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, str]]:
        """
        Gets or sets the parameters of the task.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def source(self) -> Optional[str]:
        """
        Gets or sets the name of the runbook.
        """
        return pulumi.get(self, "source")


@pulumi.output_type
class UpdateConfigurationResponse(dict):
    """
    Update specific properties of the software update configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "operatingSystem":
            suggest = "operating_system"
        elif key == "azureVirtualMachines":
            suggest = "azure_virtual_machines"
        elif key == "nonAzureComputerNames":
            suggest = "non_azure_computer_names"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UpdateConfigurationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UpdateConfigurationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UpdateConfigurationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 operating_system: str,
                 azure_virtual_machines: Optional[Sequence[str]] = None,
                 duration: Optional[str] = None,
                 linux: Optional['outputs.LinuxPropertiesResponse'] = None,
                 non_azure_computer_names: Optional[Sequence[str]] = None,
                 targets: Optional['outputs.TargetPropertiesResponse'] = None,
                 windows: Optional['outputs.WindowsPropertiesResponse'] = None):
        """
        Update specific properties of the software update configuration.
        :param str operating_system: operating system of target machines
        :param Sequence[str] azure_virtual_machines: List of azure resource Ids for azure virtual machines targeted by the software update configuration.
        :param str duration: Maximum time allowed for the software update configuration run. Duration needs to be specified using the format PT[n]H[n]M[n]S as per ISO8601
        :param 'LinuxPropertiesResponse' linux: Linux specific update configuration.
        :param Sequence[str] non_azure_computer_names: List of names of non-azure machines targeted by the software update configuration.
        :param 'TargetPropertiesResponse' targets: Group targets for the software update configuration.
        :param 'WindowsPropertiesResponse' windows: Windows specific update configuration.
        """
        pulumi.set(__self__, "operating_system", operating_system)
        if azure_virtual_machines is not None:
            pulumi.set(__self__, "azure_virtual_machines", azure_virtual_machines)
        if duration is not None:
            pulumi.set(__self__, "duration", duration)
        if linux is not None:
            pulumi.set(__self__, "linux", linux)
        if non_azure_computer_names is not None:
            pulumi.set(__self__, "non_azure_computer_names", non_azure_computer_names)
        if targets is not None:
            pulumi.set(__self__, "targets", targets)
        if windows is not None:
            pulumi.set(__self__, "windows", windows)

    @property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> str:
        """
        operating system of target machines
        """
        return pulumi.get(self, "operating_system")

    @property
    @pulumi.getter(name="azureVirtualMachines")
    def azure_virtual_machines(self) -> Optional[Sequence[str]]:
        """
        List of azure resource Ids for azure virtual machines targeted by the software update configuration.
        """
        return pulumi.get(self, "azure_virtual_machines")

    @property
    @pulumi.getter
    def duration(self) -> Optional[str]:
        """
        Maximum time allowed for the software update configuration run. Duration needs to be specified using the format PT[n]H[n]M[n]S as per ISO8601
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def linux(self) -> Optional['outputs.LinuxPropertiesResponse']:
        """
        Linux specific update configuration.
        """
        return pulumi.get(self, "linux")

    @property
    @pulumi.getter(name="nonAzureComputerNames")
    def non_azure_computer_names(self) -> Optional[Sequence[str]]:
        """
        List of names of non-azure machines targeted by the software update configuration.
        """
        return pulumi.get(self, "non_azure_computer_names")

    @property
    @pulumi.getter
    def targets(self) -> Optional['outputs.TargetPropertiesResponse']:
        """
        Group targets for the software update configuration.
        """
        return pulumi.get(self, "targets")

    @property
    @pulumi.getter
    def windows(self) -> Optional['outputs.WindowsPropertiesResponse']:
        """
        Windows specific update configuration.
        """
        return pulumi.get(self, "windows")


@pulumi.output_type
class WindowsPropertiesResponse(dict):
    """
    Windows specific update configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "excludedKbNumbers":
            suggest = "excluded_kb_numbers"
        elif key == "includedKbNumbers":
            suggest = "included_kb_numbers"
        elif key == "includedUpdateClassifications":
            suggest = "included_update_classifications"
        elif key == "rebootSetting":
            suggest = "reboot_setting"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WindowsPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WindowsPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WindowsPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 excluded_kb_numbers: Optional[Sequence[str]] = None,
                 included_kb_numbers: Optional[Sequence[str]] = None,
                 included_update_classifications: Optional[str] = None,
                 reboot_setting: Optional[str] = None):
        """
        Windows specific update configuration.
        :param Sequence[str] excluded_kb_numbers: KB numbers excluded from the software update configuration.
        :param Sequence[str] included_kb_numbers: KB numbers included from the software update configuration.
        :param str included_update_classifications: Update classification included in the software update configuration. A comma separated string with required values
        :param str reboot_setting: Reboot setting for the software update configuration.
        """
        if excluded_kb_numbers is not None:
            pulumi.set(__self__, "excluded_kb_numbers", excluded_kb_numbers)
        if included_kb_numbers is not None:
            pulumi.set(__self__, "included_kb_numbers", included_kb_numbers)
        if included_update_classifications is not None:
            pulumi.set(__self__, "included_update_classifications", included_update_classifications)
        if reboot_setting is not None:
            pulumi.set(__self__, "reboot_setting", reboot_setting)

    @property
    @pulumi.getter(name="excludedKbNumbers")
    def excluded_kb_numbers(self) -> Optional[Sequence[str]]:
        """
        KB numbers excluded from the software update configuration.
        """
        return pulumi.get(self, "excluded_kb_numbers")

    @property
    @pulumi.getter(name="includedKbNumbers")
    def included_kb_numbers(self) -> Optional[Sequence[str]]:
        """
        KB numbers included from the software update configuration.
        """
        return pulumi.get(self, "included_kb_numbers")

    @property
    @pulumi.getter(name="includedUpdateClassifications")
    def included_update_classifications(self) -> Optional[str]:
        """
        Update classification included in the software update configuration. A comma separated string with required values
        """
        return pulumi.get(self, "included_update_classifications")

    @property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[str]:
        """
        Reboot setting for the software update configuration.
        """
        return pulumi.get(self, "reboot_setting")


