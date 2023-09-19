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
    'InputLinuxParametersResponse',
    'InputPatchConfigurationResponse',
    'InputWindowsParametersResponse',
    'MaintenanceOverridePropertiesResponse',
    'SystemDataResponse',
    'TaskPropertiesResponse',
]

@pulumi.output_type
class InputLinuxParametersResponse(dict):
    """
    Input properties for patching a Linux machine.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "classificationsToInclude":
            suggest = "classifications_to_include"
        elif key == "packageNameMasksToExclude":
            suggest = "package_name_masks_to_exclude"
        elif key == "packageNameMasksToInclude":
            suggest = "package_name_masks_to_include"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InputLinuxParametersResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InputLinuxParametersResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InputLinuxParametersResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 classifications_to_include: Optional[Sequence[str]] = None,
                 package_name_masks_to_exclude: Optional[Sequence[str]] = None,
                 package_name_masks_to_include: Optional[Sequence[str]] = None):
        """
        Input properties for patching a Linux machine.
        :param Sequence[str] classifications_to_include: Classification category of patches to be patched
        :param Sequence[str] package_name_masks_to_exclude: Package names to be excluded for patching.
        :param Sequence[str] package_name_masks_to_include: Package names to be included for patching.
        """
        if classifications_to_include is not None:
            pulumi.set(__self__, "classifications_to_include", classifications_to_include)
        if package_name_masks_to_exclude is not None:
            pulumi.set(__self__, "package_name_masks_to_exclude", package_name_masks_to_exclude)
        if package_name_masks_to_include is not None:
            pulumi.set(__self__, "package_name_masks_to_include", package_name_masks_to_include)

    @property
    @pulumi.getter(name="classificationsToInclude")
    def classifications_to_include(self) -> Optional[Sequence[str]]:
        """
        Classification category of patches to be patched
        """
        return pulumi.get(self, "classifications_to_include")

    @property
    @pulumi.getter(name="packageNameMasksToExclude")
    def package_name_masks_to_exclude(self) -> Optional[Sequence[str]]:
        """
        Package names to be excluded for patching.
        """
        return pulumi.get(self, "package_name_masks_to_exclude")

    @property
    @pulumi.getter(name="packageNameMasksToInclude")
    def package_name_masks_to_include(self) -> Optional[Sequence[str]]:
        """
        Package names to be included for patching.
        """
        return pulumi.get(self, "package_name_masks_to_include")


@pulumi.output_type
class InputPatchConfigurationResponse(dict):
    """
    Input configuration for a patch run
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "linuxParameters":
            suggest = "linux_parameters"
        elif key == "postTasks":
            suggest = "post_tasks"
        elif key == "preTasks":
            suggest = "pre_tasks"
        elif key == "rebootSetting":
            suggest = "reboot_setting"
        elif key == "windowsParameters":
            suggest = "windows_parameters"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InputPatchConfigurationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InputPatchConfigurationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InputPatchConfigurationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 linux_parameters: Optional['outputs.InputLinuxParametersResponse'] = None,
                 post_tasks: Optional[Sequence['outputs.TaskPropertiesResponse']] = None,
                 pre_tasks: Optional[Sequence['outputs.TaskPropertiesResponse']] = None,
                 reboot_setting: Optional[str] = None,
                 windows_parameters: Optional['outputs.InputWindowsParametersResponse'] = None):
        """
        Input configuration for a patch run
        :param 'InputLinuxParametersResponse' linux_parameters: Input parameters specific to patching Linux machine. For Windows machines, do not pass this property.
        :param Sequence['TaskPropertiesResponse'] post_tasks: List of post tasks. e.g. [{'source' :'runbook', 'taskScope': 'Resource', 'parameters': { 'arg1': 'value1'}}]
        :param Sequence['TaskPropertiesResponse'] pre_tasks: List of pre tasks. e.g. [{'source' :'runbook', 'taskScope': 'Global', 'parameters': { 'arg1': 'value1'}}]
        :param str reboot_setting: Possible reboot preference as defined by the user based on which it would be decided to reboot the machine or not after the patch operation is completed.
        :param 'InputWindowsParametersResponse' windows_parameters: Input parameters specific to patching a Windows machine. For Linux machines, do not pass this property.
        """
        if linux_parameters is not None:
            pulumi.set(__self__, "linux_parameters", linux_parameters)
        if post_tasks is not None:
            pulumi.set(__self__, "post_tasks", post_tasks)
        if pre_tasks is not None:
            pulumi.set(__self__, "pre_tasks", pre_tasks)
        if reboot_setting is None:
            reboot_setting = 'IfRequired'
        if reboot_setting is not None:
            pulumi.set(__self__, "reboot_setting", reboot_setting)
        if windows_parameters is not None:
            pulumi.set(__self__, "windows_parameters", windows_parameters)

    @property
    @pulumi.getter(name="linuxParameters")
    def linux_parameters(self) -> Optional['outputs.InputLinuxParametersResponse']:
        """
        Input parameters specific to patching Linux machine. For Windows machines, do not pass this property.
        """
        return pulumi.get(self, "linux_parameters")

    @property
    @pulumi.getter(name="postTasks")
    def post_tasks(self) -> Optional[Sequence['outputs.TaskPropertiesResponse']]:
        """
        List of post tasks. e.g. [{'source' :'runbook', 'taskScope': 'Resource', 'parameters': { 'arg1': 'value1'}}]
        """
        return pulumi.get(self, "post_tasks")

    @property
    @pulumi.getter(name="preTasks")
    def pre_tasks(self) -> Optional[Sequence['outputs.TaskPropertiesResponse']]:
        """
        List of pre tasks. e.g. [{'source' :'runbook', 'taskScope': 'Global', 'parameters': { 'arg1': 'value1'}}]
        """
        return pulumi.get(self, "pre_tasks")

    @property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[str]:
        """
        Possible reboot preference as defined by the user based on which it would be decided to reboot the machine or not after the patch operation is completed.
        """
        return pulumi.get(self, "reboot_setting")

    @property
    @pulumi.getter(name="windowsParameters")
    def windows_parameters(self) -> Optional['outputs.InputWindowsParametersResponse']:
        """
        Input parameters specific to patching a Windows machine. For Linux machines, do not pass this property.
        """
        return pulumi.get(self, "windows_parameters")


@pulumi.output_type
class InputWindowsParametersResponse(dict):
    """
    Input properties for patching a Windows machine.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "classificationsToInclude":
            suggest = "classifications_to_include"
        elif key == "excludeKbsRequiringReboot":
            suggest = "exclude_kbs_requiring_reboot"
        elif key == "kbNumbersToExclude":
            suggest = "kb_numbers_to_exclude"
        elif key == "kbNumbersToInclude":
            suggest = "kb_numbers_to_include"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InputWindowsParametersResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InputWindowsParametersResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InputWindowsParametersResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 classifications_to_include: Optional[Sequence[str]] = None,
                 exclude_kbs_requiring_reboot: Optional[bool] = None,
                 kb_numbers_to_exclude: Optional[Sequence[str]] = None,
                 kb_numbers_to_include: Optional[Sequence[str]] = None):
        """
        Input properties for patching a Windows machine.
        :param Sequence[str] classifications_to_include: Classification category of patches to be patched
        :param bool exclude_kbs_requiring_reboot: Exclude patches which need reboot
        :param Sequence[str] kb_numbers_to_exclude: Windows KBID to be excluded for patching.
        :param Sequence[str] kb_numbers_to_include: Windows KBID to be included for patching.
        """
        if classifications_to_include is not None:
            pulumi.set(__self__, "classifications_to_include", classifications_to_include)
        if exclude_kbs_requiring_reboot is not None:
            pulumi.set(__self__, "exclude_kbs_requiring_reboot", exclude_kbs_requiring_reboot)
        if kb_numbers_to_exclude is not None:
            pulumi.set(__self__, "kb_numbers_to_exclude", kb_numbers_to_exclude)
        if kb_numbers_to_include is not None:
            pulumi.set(__self__, "kb_numbers_to_include", kb_numbers_to_include)

    @property
    @pulumi.getter(name="classificationsToInclude")
    def classifications_to_include(self) -> Optional[Sequence[str]]:
        """
        Classification category of patches to be patched
        """
        return pulumi.get(self, "classifications_to_include")

    @property
    @pulumi.getter(name="excludeKbsRequiringReboot")
    def exclude_kbs_requiring_reboot(self) -> Optional[bool]:
        """
        Exclude patches which need reboot
        """
        return pulumi.get(self, "exclude_kbs_requiring_reboot")

    @property
    @pulumi.getter(name="kbNumbersToExclude")
    def kb_numbers_to_exclude(self) -> Optional[Sequence[str]]:
        """
        Windows KBID to be excluded for patching.
        """
        return pulumi.get(self, "kb_numbers_to_exclude")

    @property
    @pulumi.getter(name="kbNumbersToInclude")
    def kb_numbers_to_include(self) -> Optional[Sequence[str]]:
        """
        Windows KBID to be included for patching.
        """
        return pulumi.get(self, "kb_numbers_to_include")


@pulumi.output_type
class MaintenanceOverridePropertiesResponse(dict):
    """
    Definition of a MaintenanceOverrideProperties
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endDateTime":
            suggest = "end_date_time"
        elif key == "overrideProperties":
            suggest = "override_properties"
        elif key == "startDateTime":
            suggest = "start_date_time"
        elif key == "timeZone":
            suggest = "time_zone"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MaintenanceOverridePropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MaintenanceOverridePropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MaintenanceOverridePropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 end_date_time: Optional[str] = None,
                 override_properties: Optional[Mapping[str, str]] = None,
                 start_date_time: Optional[str] = None,
                 time_zone: Optional[str] = None):
        """
        Definition of a MaintenanceOverrideProperties
        :param str end_date_time: Effective end date of the maintenance override window in YYYY-MM-DD hh:mm format. The window will be created in the time zone provided and adjusted to daylight savings according to that time zone. Expiration date must be set to a future date. If not provided, it will be set to the maximum datetime 9999-12-31 23:59:59.
        :param Mapping[str, str] override_properties: Gets or sets overrideProperties of the maintenanceConfiguration
        :param str start_date_time: Effective start date of the maintenance override window in YYYY-MM-DD hh:mm format. The start date can be set to either the current date or future date. The window will be created in the time zone provided and adjusted to daylight savings according to that time zone.
        :param str time_zone: Name of the timezone. List of timezones can be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. Example: Pacific Standard Time, UTC, W. Europe Standard Time, Korea Standard Time, Cen. Australia Standard Time.
        """
        if end_date_time is not None:
            pulumi.set(__self__, "end_date_time", end_date_time)
        if override_properties is not None:
            pulumi.set(__self__, "override_properties", override_properties)
        if start_date_time is not None:
            pulumi.set(__self__, "start_date_time", start_date_time)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="endDateTime")
    def end_date_time(self) -> Optional[str]:
        """
        Effective end date of the maintenance override window in YYYY-MM-DD hh:mm format. The window will be created in the time zone provided and adjusted to daylight savings according to that time zone. Expiration date must be set to a future date. If not provided, it will be set to the maximum datetime 9999-12-31 23:59:59.
        """
        return pulumi.get(self, "end_date_time")

    @property
    @pulumi.getter(name="overrideProperties")
    def override_properties(self) -> Optional[Mapping[str, str]]:
        """
        Gets or sets overrideProperties of the maintenanceConfiguration
        """
        return pulumi.get(self, "override_properties")

    @property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> Optional[str]:
        """
        Effective start date of the maintenance override window in YYYY-MM-DD hh:mm format. The start date can be set to either the current date or future date. The window will be created in the time zone provided and adjusted to daylight savings according to that time zone.
        """
        return pulumi.get(self, "start_date_time")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[str]:
        """
        Name of the timezone. List of timezones can be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. Example: Pacific Standard Time, UTC, W. Europe Standard Time, Korea Standard Time, Cen. Australia Standard Time.
        """
        return pulumi.get(self, "time_zone")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


@pulumi.output_type
class TaskPropertiesResponse(dict):
    """
    Task properties of the software update configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "taskScope":
            suggest = "task_scope"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TaskPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TaskPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TaskPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 parameters: Optional[Mapping[str, str]] = None,
                 source: Optional[str] = None,
                 task_scope: Optional[str] = None):
        """
        Task properties of the software update configuration.
        :param Mapping[str, str] parameters: Gets or sets the parameters of the task.
        :param str source: Gets or sets the name of the runbook.
        :param str task_scope: Global Task execute once when schedule trigger. Resource task execute for each VM.
        """
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if task_scope is None:
            task_scope = 'Global'
        if task_scope is not None:
            pulumi.set(__self__, "task_scope", task_scope)

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

    @property
    @pulumi.getter(name="taskScope")
    def task_scope(self) -> Optional[str]:
        """
        Global Task execute once when schedule trigger. Resource task execute for each VM.
        """
        return pulumi.get(self, "task_scope")


