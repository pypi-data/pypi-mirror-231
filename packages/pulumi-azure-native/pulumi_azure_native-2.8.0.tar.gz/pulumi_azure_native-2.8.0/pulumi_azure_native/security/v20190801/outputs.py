# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AdditionalWorkspacesPropertiesResponse',
    'AllowlistCustomAlertRuleResponse',
    'DenylistCustomAlertRuleResponse',
    'RecommendationConfigurationPropertiesResponse',
    'SystemDataResponse',
    'ThresholdCustomAlertRuleResponse',
    'TimeWindowCustomAlertRuleResponse',
    'UserDefinedResourcesPropertiesResponse',
]

@pulumi.output_type
class AdditionalWorkspacesPropertiesResponse(dict):
    """
    Properties of the additional workspaces.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataTypes":
            suggest = "data_types"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AdditionalWorkspacesPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AdditionalWorkspacesPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AdditionalWorkspacesPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 data_types: Optional[Sequence[str]] = None,
                 type: Optional[str] = None,
                 workspace: Optional[str] = None):
        """
        Properties of the additional workspaces.
        :param Sequence[str] data_types: List of data types sent to workspace
        :param str type: Workspace type.
        :param str workspace: Workspace resource id
        """
        if data_types is not None:
            pulumi.set(__self__, "data_types", data_types)
        if type is None:
            type = 'Sentinel'
        if type is not None:
            pulumi.set(__self__, "type", type)
        if workspace is not None:
            pulumi.set(__self__, "workspace", workspace)

    @property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> Optional[Sequence[str]]:
        """
        List of data types sent to workspace
        """
        return pulumi.get(self, "data_types")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Workspace type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def workspace(self) -> Optional[str]:
        """
        Workspace resource id
        """
        return pulumi.get(self, "workspace")


@pulumi.output_type
class AllowlistCustomAlertRuleResponse(dict):
    """
    A custom alert rule that checks if a value (depends on the custom alert type) is allowed.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowlistValues":
            suggest = "allowlist_values"
        elif key == "displayName":
            suggest = "display_name"
        elif key == "isEnabled":
            suggest = "is_enabled"
        elif key == "ruleType":
            suggest = "rule_type"
        elif key == "valueType":
            suggest = "value_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AllowlistCustomAlertRuleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AllowlistCustomAlertRuleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AllowlistCustomAlertRuleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowlist_values: Sequence[str],
                 description: str,
                 display_name: str,
                 is_enabled: bool,
                 rule_type: str,
                 value_type: str):
        """
        A custom alert rule that checks if a value (depends on the custom alert type) is allowed.
        :param Sequence[str] allowlist_values: The values to allow. The format of the values depends on the rule type.
        :param str description: The description of the custom alert.
        :param str display_name: The display name of the custom alert.
        :param bool is_enabled: Status of the custom alert.
        :param str rule_type: The type of the custom alert rule.
               Expected value is 'AllowlistCustomAlertRule'.
        :param str value_type: The value type of the items in the list.
        """
        pulumi.set(__self__, "allowlist_values", allowlist_values)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "is_enabled", is_enabled)
        pulumi.set(__self__, "rule_type", 'AllowlistCustomAlertRule')
        pulumi.set(__self__, "value_type", value_type)

    @property
    @pulumi.getter(name="allowlistValues")
    def allowlist_values(self) -> Sequence[str]:
        """
        The values to allow. The format of the values depends on the rule type.
        """
        return pulumi.get(self, "allowlist_values")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the custom alert.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the custom alert.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> bool:
        """
        Status of the custom alert.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> str:
        """
        The type of the custom alert rule.
        Expected value is 'AllowlistCustomAlertRule'.
        """
        return pulumi.get(self, "rule_type")

    @property
    @pulumi.getter(name="valueType")
    def value_type(self) -> str:
        """
        The value type of the items in the list.
        """
        return pulumi.get(self, "value_type")


@pulumi.output_type
class DenylistCustomAlertRuleResponse(dict):
    """
    A custom alert rule that checks if a value (depends on the custom alert type) is denied.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "denylistValues":
            suggest = "denylist_values"
        elif key == "displayName":
            suggest = "display_name"
        elif key == "isEnabled":
            suggest = "is_enabled"
        elif key == "ruleType":
            suggest = "rule_type"
        elif key == "valueType":
            suggest = "value_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DenylistCustomAlertRuleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DenylistCustomAlertRuleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DenylistCustomAlertRuleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 denylist_values: Sequence[str],
                 description: str,
                 display_name: str,
                 is_enabled: bool,
                 rule_type: str,
                 value_type: str):
        """
        A custom alert rule that checks if a value (depends on the custom alert type) is denied.
        :param Sequence[str] denylist_values: The values to deny. The format of the values depends on the rule type.
        :param str description: The description of the custom alert.
        :param str display_name: The display name of the custom alert.
        :param bool is_enabled: Status of the custom alert.
        :param str rule_type: The type of the custom alert rule.
               Expected value is 'DenylistCustomAlertRule'.
        :param str value_type: The value type of the items in the list.
        """
        pulumi.set(__self__, "denylist_values", denylist_values)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "is_enabled", is_enabled)
        pulumi.set(__self__, "rule_type", 'DenylistCustomAlertRule')
        pulumi.set(__self__, "value_type", value_type)

    @property
    @pulumi.getter(name="denylistValues")
    def denylist_values(self) -> Sequence[str]:
        """
        The values to deny. The format of the values depends on the rule type.
        """
        return pulumi.get(self, "denylist_values")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the custom alert.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the custom alert.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> bool:
        """
        Status of the custom alert.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> str:
        """
        The type of the custom alert rule.
        Expected value is 'DenylistCustomAlertRule'.
        """
        return pulumi.get(self, "rule_type")

    @property
    @pulumi.getter(name="valueType")
    def value_type(self) -> str:
        """
        The value type of the items in the list.
        """
        return pulumi.get(self, "value_type")


@pulumi.output_type
class RecommendationConfigurationPropertiesResponse(dict):
    """
    The type of IoT Security recommendation.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "recommendationType":
            suggest = "recommendation_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecommendationConfigurationPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecommendationConfigurationPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecommendationConfigurationPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 recommendation_type: str,
                 status: str):
        """
        The type of IoT Security recommendation.
        :param str recommendation_type: The type of IoT Security recommendation.
        :param str status: Recommendation status. When the recommendation status is disabled recommendations are not generated.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "recommendation_type", recommendation_type)
        if status is None:
            status = 'Enabled'
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recommendationType")
    def recommendation_type(self) -> str:
        """
        The type of IoT Security recommendation.
        """
        return pulumi.get(self, "recommendation_type")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Recommendation status. When the recommendation status is disabled recommendations are not generated.
        """
        return pulumi.get(self, "status")


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
class ThresholdCustomAlertRuleResponse(dict):
    """
    A custom alert rule that checks if a value (depends on the custom alert type) is within the given range.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "displayName":
            suggest = "display_name"
        elif key == "isEnabled":
            suggest = "is_enabled"
        elif key == "maxThreshold":
            suggest = "max_threshold"
        elif key == "minThreshold":
            suggest = "min_threshold"
        elif key == "ruleType":
            suggest = "rule_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ThresholdCustomAlertRuleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ThresholdCustomAlertRuleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ThresholdCustomAlertRuleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: str,
                 display_name: str,
                 is_enabled: bool,
                 max_threshold: int,
                 min_threshold: int,
                 rule_type: str):
        """
        A custom alert rule that checks if a value (depends on the custom alert type) is within the given range.
        :param str description: The description of the custom alert.
        :param str display_name: The display name of the custom alert.
        :param bool is_enabled: Status of the custom alert.
        :param int max_threshold: The maximum threshold.
        :param int min_threshold: The minimum threshold.
        :param str rule_type: The type of the custom alert rule.
               Expected value is 'ThresholdCustomAlertRule'.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "is_enabled", is_enabled)
        pulumi.set(__self__, "max_threshold", max_threshold)
        pulumi.set(__self__, "min_threshold", min_threshold)
        pulumi.set(__self__, "rule_type", 'ThresholdCustomAlertRule')

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the custom alert.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the custom alert.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> bool:
        """
        Status of the custom alert.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="maxThreshold")
    def max_threshold(self) -> int:
        """
        The maximum threshold.
        """
        return pulumi.get(self, "max_threshold")

    @property
    @pulumi.getter(name="minThreshold")
    def min_threshold(self) -> int:
        """
        The minimum threshold.
        """
        return pulumi.get(self, "min_threshold")

    @property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> str:
        """
        The type of the custom alert rule.
        Expected value is 'ThresholdCustomAlertRule'.
        """
        return pulumi.get(self, "rule_type")


@pulumi.output_type
class TimeWindowCustomAlertRuleResponse(dict):
    """
    A custom alert rule that checks if the number of activities (depends on the custom alert type) in a time window is within the given range.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "displayName":
            suggest = "display_name"
        elif key == "isEnabled":
            suggest = "is_enabled"
        elif key == "maxThreshold":
            suggest = "max_threshold"
        elif key == "minThreshold":
            suggest = "min_threshold"
        elif key == "ruleType":
            suggest = "rule_type"
        elif key == "timeWindowSize":
            suggest = "time_window_size"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TimeWindowCustomAlertRuleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TimeWindowCustomAlertRuleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TimeWindowCustomAlertRuleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: str,
                 display_name: str,
                 is_enabled: bool,
                 max_threshold: int,
                 min_threshold: int,
                 rule_type: str,
                 time_window_size: str):
        """
        A custom alert rule that checks if the number of activities (depends on the custom alert type) in a time window is within the given range.
        :param str description: The description of the custom alert.
        :param str display_name: The display name of the custom alert.
        :param bool is_enabled: Status of the custom alert.
        :param int max_threshold: The maximum threshold.
        :param int min_threshold: The minimum threshold.
        :param str rule_type: The type of the custom alert rule.
               Expected value is 'TimeWindowCustomAlertRule'.
        :param str time_window_size: The time window size in iso8601 format.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "is_enabled", is_enabled)
        pulumi.set(__self__, "max_threshold", max_threshold)
        pulumi.set(__self__, "min_threshold", min_threshold)
        pulumi.set(__self__, "rule_type", 'TimeWindowCustomAlertRule')
        pulumi.set(__self__, "time_window_size", time_window_size)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the custom alert.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the custom alert.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> bool:
        """
        Status of the custom alert.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="maxThreshold")
    def max_threshold(self) -> int:
        """
        The maximum threshold.
        """
        return pulumi.get(self, "max_threshold")

    @property
    @pulumi.getter(name="minThreshold")
    def min_threshold(self) -> int:
        """
        The minimum threshold.
        """
        return pulumi.get(self, "min_threshold")

    @property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> str:
        """
        The type of the custom alert rule.
        Expected value is 'TimeWindowCustomAlertRule'.
        """
        return pulumi.get(self, "rule_type")

    @property
    @pulumi.getter(name="timeWindowSize")
    def time_window_size(self) -> str:
        """
        The time window size in iso8601 format.
        """
        return pulumi.get(self, "time_window_size")


@pulumi.output_type
class UserDefinedResourcesPropertiesResponse(dict):
    """
    Properties of the IoT Security solution's user defined resources.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "querySubscriptions":
            suggest = "query_subscriptions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserDefinedResourcesPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserDefinedResourcesPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserDefinedResourcesPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 query: str,
                 query_subscriptions: Sequence[str]):
        """
        Properties of the IoT Security solution's user defined resources.
        :param str query: Azure Resource Graph query which represents the security solution's user defined resources. Required to start with "where type != "Microsoft.Devices/IotHubs""
        :param Sequence[str] query_subscriptions: List of Azure subscription ids on which the user defined resources query should be executed.
        """
        pulumi.set(__self__, "query", query)
        pulumi.set(__self__, "query_subscriptions", query_subscriptions)

    @property
    @pulumi.getter
    def query(self) -> str:
        """
        Azure Resource Graph query which represents the security solution's user defined resources. Required to start with "where type != "Microsoft.Devices/IotHubs""
        """
        return pulumi.get(self, "query")

    @property
    @pulumi.getter(name="querySubscriptions")
    def query_subscriptions(self) -> Sequence[str]:
        """
        List of Azure subscription ids on which the user defined resources query should be executed.
        """
        return pulumi.get(self, "query_subscriptions")


