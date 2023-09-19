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
    'AlertDetailsOverrideArgs',
    'EntityMappingArgs',
    'FieldMappingArgs',
    'FusionScenarioExclusionPatternArgs',
    'FusionSourceSettingsArgs',
    'FusionSourceSubTypeSettingArgs',
    'FusionSubTypeSeverityFiltersItemArgs',
    'FusionSubTypeSeverityFilterArgs',
    'GroupingConfigurationArgs',
    'IncidentConfigurationArgs',
    'WatchlistUserInfoArgs',
]

@pulumi.input_type
class AlertDetailsOverrideArgs:
    def __init__(__self__, *,
                 alert_description_format: Optional[pulumi.Input[str]] = None,
                 alert_display_name_format: Optional[pulumi.Input[str]] = None,
                 alert_severity_column_name: Optional[pulumi.Input[str]] = None,
                 alert_tactics_column_name: Optional[pulumi.Input[str]] = None):
        """
        Settings for how to dynamically override alert static details
        :param pulumi.Input[str] alert_description_format: the format containing columns name(s) to override the alert description
        :param pulumi.Input[str] alert_display_name_format: the format containing columns name(s) to override the alert name
        :param pulumi.Input[str] alert_severity_column_name: the column name to take the alert severity from
        :param pulumi.Input[str] alert_tactics_column_name: the column name to take the alert tactics from
        """
        if alert_description_format is not None:
            pulumi.set(__self__, "alert_description_format", alert_description_format)
        if alert_display_name_format is not None:
            pulumi.set(__self__, "alert_display_name_format", alert_display_name_format)
        if alert_severity_column_name is not None:
            pulumi.set(__self__, "alert_severity_column_name", alert_severity_column_name)
        if alert_tactics_column_name is not None:
            pulumi.set(__self__, "alert_tactics_column_name", alert_tactics_column_name)

    @property
    @pulumi.getter(name="alertDescriptionFormat")
    def alert_description_format(self) -> Optional[pulumi.Input[str]]:
        """
        the format containing columns name(s) to override the alert description
        """
        return pulumi.get(self, "alert_description_format")

    @alert_description_format.setter
    def alert_description_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_description_format", value)

    @property
    @pulumi.getter(name="alertDisplayNameFormat")
    def alert_display_name_format(self) -> Optional[pulumi.Input[str]]:
        """
        the format containing columns name(s) to override the alert name
        """
        return pulumi.get(self, "alert_display_name_format")

    @alert_display_name_format.setter
    def alert_display_name_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_display_name_format", value)

    @property
    @pulumi.getter(name="alertSeverityColumnName")
    def alert_severity_column_name(self) -> Optional[pulumi.Input[str]]:
        """
        the column name to take the alert severity from
        """
        return pulumi.get(self, "alert_severity_column_name")

    @alert_severity_column_name.setter
    def alert_severity_column_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_severity_column_name", value)

    @property
    @pulumi.getter(name="alertTacticsColumnName")
    def alert_tactics_column_name(self) -> Optional[pulumi.Input[str]]:
        """
        the column name to take the alert tactics from
        """
        return pulumi.get(self, "alert_tactics_column_name")

    @alert_tactics_column_name.setter
    def alert_tactics_column_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_tactics_column_name", value)


@pulumi.input_type
class EntityMappingArgs:
    def __init__(__self__, *,
                 entity_type: Optional[pulumi.Input[Union[str, 'EntityMappingType']]] = None,
                 field_mappings: Optional[pulumi.Input[Sequence[pulumi.Input['FieldMappingArgs']]]] = None):
        """
        Single entity mapping for the alert rule
        :param pulumi.Input[Union[str, 'EntityMappingType']] entity_type: The V3 type of the mapped entity
        :param pulumi.Input[Sequence[pulumi.Input['FieldMappingArgs']]] field_mappings: array of field mappings for the given entity mapping
        """
        if entity_type is not None:
            pulumi.set(__self__, "entity_type", entity_type)
        if field_mappings is not None:
            pulumi.set(__self__, "field_mappings", field_mappings)

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[pulumi.Input[Union[str, 'EntityMappingType']]]:
        """
        The V3 type of the mapped entity
        """
        return pulumi.get(self, "entity_type")

    @entity_type.setter
    def entity_type(self, value: Optional[pulumi.Input[Union[str, 'EntityMappingType']]]):
        pulumi.set(self, "entity_type", value)

    @property
    @pulumi.getter(name="fieldMappings")
    def field_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FieldMappingArgs']]]]:
        """
        array of field mappings for the given entity mapping
        """
        return pulumi.get(self, "field_mappings")

    @field_mappings.setter
    def field_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FieldMappingArgs']]]]):
        pulumi.set(self, "field_mappings", value)


@pulumi.input_type
class FieldMappingArgs:
    def __init__(__self__, *,
                 column_name: Optional[pulumi.Input[str]] = None,
                 identifier: Optional[pulumi.Input[str]] = None):
        """
        A single field mapping of the mapped entity
        :param pulumi.Input[str] column_name: the column name to be mapped to the identifier
        :param pulumi.Input[str] identifier: the V3 identifier of the entity
        """
        if column_name is not None:
            pulumi.set(__self__, "column_name", column_name)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)

    @property
    @pulumi.getter(name="columnName")
    def column_name(self) -> Optional[pulumi.Input[str]]:
        """
        the column name to be mapped to the identifier
        """
        return pulumi.get(self, "column_name")

    @column_name.setter
    def column_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "column_name", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        the V3 identifier of the entity
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)


@pulumi.input_type
class FusionScenarioExclusionPatternArgs:
    def __init__(__self__, *,
                 date_added_in_utc: pulumi.Input[str],
                 exclusion_pattern: pulumi.Input[str]):
        """
        Represents a Fusion scenario exclusion patterns in Fusion detection.
        :param pulumi.Input[str] date_added_in_utc: DateTime when scenario exclusion pattern is added in UTC.
        :param pulumi.Input[str] exclusion_pattern: Scenario exclusion pattern.
        """
        pulumi.set(__self__, "date_added_in_utc", date_added_in_utc)
        pulumi.set(__self__, "exclusion_pattern", exclusion_pattern)

    @property
    @pulumi.getter(name="dateAddedInUTC")
    def date_added_in_utc(self) -> pulumi.Input[str]:
        """
        DateTime when scenario exclusion pattern is added in UTC.
        """
        return pulumi.get(self, "date_added_in_utc")

    @date_added_in_utc.setter
    def date_added_in_utc(self, value: pulumi.Input[str]):
        pulumi.set(self, "date_added_in_utc", value)

    @property
    @pulumi.getter(name="exclusionPattern")
    def exclusion_pattern(self) -> pulumi.Input[str]:
        """
        Scenario exclusion pattern.
        """
        return pulumi.get(self, "exclusion_pattern")

    @exclusion_pattern.setter
    def exclusion_pattern(self, value: pulumi.Input[str]):
        pulumi.set(self, "exclusion_pattern", value)


@pulumi.input_type
class FusionSourceSettingsArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 source_name: pulumi.Input[str],
                 source_sub_types: Optional[pulumi.Input[Sequence[pulumi.Input['FusionSourceSubTypeSettingArgs']]]] = None):
        """
        Represents a supported source signal configuration in Fusion detection.
        :param pulumi.Input[bool] enabled: Determines whether this source signal is enabled or disabled in Fusion detection.
        :param pulumi.Input[str] source_name: Name of the Fusion source signal. Refer to Fusion alert rule template for supported values.
        :param pulumi.Input[Sequence[pulumi.Input['FusionSourceSubTypeSettingArgs']]] source_sub_types: Configuration for all source subtypes under this source signal consumed in fusion detection.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "source_name", source_name)
        if source_sub_types is not None:
            pulumi.set(__self__, "source_sub_types", source_sub_types)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Determines whether this source signal is enabled or disabled in Fusion detection.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> pulumi.Input[str]:
        """
        Name of the Fusion source signal. Refer to Fusion alert rule template for supported values.
        """
        return pulumi.get(self, "source_name")

    @source_name.setter
    def source_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_name", value)

    @property
    @pulumi.getter(name="sourceSubTypes")
    def source_sub_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FusionSourceSubTypeSettingArgs']]]]:
        """
        Configuration for all source subtypes under this source signal consumed in fusion detection.
        """
        return pulumi.get(self, "source_sub_types")

    @source_sub_types.setter
    def source_sub_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FusionSourceSubTypeSettingArgs']]]]):
        pulumi.set(self, "source_sub_types", value)


@pulumi.input_type
class FusionSourceSubTypeSettingArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 severity_filters: pulumi.Input['FusionSubTypeSeverityFilterArgs'],
                 source_sub_type_name: pulumi.Input[str]):
        """
        Represents a supported source subtype configuration under a source signal in Fusion detection.
        :param pulumi.Input[bool] enabled: Determines whether this source subtype under source signal is enabled or disabled in Fusion detection.
        :param pulumi.Input['FusionSubTypeSeverityFilterArgs'] severity_filters: Severity configuration for a source subtype consumed in fusion detection.
        :param pulumi.Input[str] source_sub_type_name: The Name of the source subtype under a given source signal in Fusion detection. Refer to Fusion alert rule template for supported values.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "severity_filters", severity_filters)
        pulumi.set(__self__, "source_sub_type_name", source_sub_type_name)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Determines whether this source subtype under source signal is enabled or disabled in Fusion detection.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="severityFilters")
    def severity_filters(self) -> pulumi.Input['FusionSubTypeSeverityFilterArgs']:
        """
        Severity configuration for a source subtype consumed in fusion detection.
        """
        return pulumi.get(self, "severity_filters")

    @severity_filters.setter
    def severity_filters(self, value: pulumi.Input['FusionSubTypeSeverityFilterArgs']):
        pulumi.set(self, "severity_filters", value)

    @property
    @pulumi.getter(name="sourceSubTypeName")
    def source_sub_type_name(self) -> pulumi.Input[str]:
        """
        The Name of the source subtype under a given source signal in Fusion detection. Refer to Fusion alert rule template for supported values.
        """
        return pulumi.get(self, "source_sub_type_name")

    @source_sub_type_name.setter
    def source_sub_type_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_sub_type_name", value)


@pulumi.input_type
class FusionSubTypeSeverityFiltersItemArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 severity: pulumi.Input[Union[str, 'AlertSeverity']]):
        """
        Represents a Severity filter setting for a given source subtype consumed in Fusion detection.
        :param pulumi.Input[bool] enabled: Determines whether this severity is enabled or disabled for this source subtype consumed in Fusion detection.
        :param pulumi.Input[Union[str, 'AlertSeverity']] severity: The Severity for a given source subtype consumed in Fusion detection.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "severity", severity)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Determines whether this severity is enabled or disabled for this source subtype consumed in Fusion detection.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Input[Union[str, 'AlertSeverity']]:
        """
        The Severity for a given source subtype consumed in Fusion detection.
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: pulumi.Input[Union[str, 'AlertSeverity']]):
        pulumi.set(self, "severity", value)


@pulumi.input_type
class FusionSubTypeSeverityFilterArgs:
    def __init__(__self__, *,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input['FusionSubTypeSeverityFiltersItemArgs']]]] = None):
        """
        Represents severity configuration for a source subtype consumed in Fusion detection.
        :param pulumi.Input[Sequence[pulumi.Input['FusionSubTypeSeverityFiltersItemArgs']]] filters: Individual Severity configuration settings for a given source subtype consumed in Fusion detection.
        """
        if filters is not None:
            pulumi.set(__self__, "filters", filters)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FusionSubTypeSeverityFiltersItemArgs']]]]:
        """
        Individual Severity configuration settings for a given source subtype consumed in Fusion detection.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FusionSubTypeSeverityFiltersItemArgs']]]]):
        pulumi.set(self, "filters", value)


@pulumi.input_type
class GroupingConfigurationArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 lookback_duration: pulumi.Input[str],
                 matching_method: pulumi.Input[Union[str, 'MatchingMethod']],
                 reopen_closed_incident: pulumi.Input[bool],
                 group_by_alert_details: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AlertDetail']]]]] = None,
                 group_by_custom_details: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 group_by_entities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'EntityMappingType']]]]] = None):
        """
        Grouping configuration property bag.
        :param pulumi.Input[bool] enabled: Grouping enabled
        :param pulumi.Input[str] lookback_duration: Limit the group to alerts created within the lookback duration (in ISO 8601 duration format)
        :param pulumi.Input[Union[str, 'MatchingMethod']] matching_method: Grouping matching method. When method is Selected at least one of groupByEntities, groupByAlertDetails, groupByCustomDetails must be provided and not empty.
        :param pulumi.Input[bool] reopen_closed_incident: Re-open closed matching incidents
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AlertDetail']]]] group_by_alert_details: A list of alert details to group by (when matchingMethod is Selected)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_by_custom_details: A list of custom details keys to group by (when matchingMethod is Selected). Only keys defined in the current alert rule may be used.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'EntityMappingType']]]] group_by_entities: A list of entity types to group by (when matchingMethod is Selected). Only entities defined in the current alert rule may be used.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "lookback_duration", lookback_duration)
        pulumi.set(__self__, "matching_method", matching_method)
        pulumi.set(__self__, "reopen_closed_incident", reopen_closed_incident)
        if group_by_alert_details is not None:
            pulumi.set(__self__, "group_by_alert_details", group_by_alert_details)
        if group_by_custom_details is not None:
            pulumi.set(__self__, "group_by_custom_details", group_by_custom_details)
        if group_by_entities is not None:
            pulumi.set(__self__, "group_by_entities", group_by_entities)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Grouping enabled
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="lookbackDuration")
    def lookback_duration(self) -> pulumi.Input[str]:
        """
        Limit the group to alerts created within the lookback duration (in ISO 8601 duration format)
        """
        return pulumi.get(self, "lookback_duration")

    @lookback_duration.setter
    def lookback_duration(self, value: pulumi.Input[str]):
        pulumi.set(self, "lookback_duration", value)

    @property
    @pulumi.getter(name="matchingMethod")
    def matching_method(self) -> pulumi.Input[Union[str, 'MatchingMethod']]:
        """
        Grouping matching method. When method is Selected at least one of groupByEntities, groupByAlertDetails, groupByCustomDetails must be provided and not empty.
        """
        return pulumi.get(self, "matching_method")

    @matching_method.setter
    def matching_method(self, value: pulumi.Input[Union[str, 'MatchingMethod']]):
        pulumi.set(self, "matching_method", value)

    @property
    @pulumi.getter(name="reopenClosedIncident")
    def reopen_closed_incident(self) -> pulumi.Input[bool]:
        """
        Re-open closed matching incidents
        """
        return pulumi.get(self, "reopen_closed_incident")

    @reopen_closed_incident.setter
    def reopen_closed_incident(self, value: pulumi.Input[bool]):
        pulumi.set(self, "reopen_closed_incident", value)

    @property
    @pulumi.getter(name="groupByAlertDetails")
    def group_by_alert_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AlertDetail']]]]]:
        """
        A list of alert details to group by (when matchingMethod is Selected)
        """
        return pulumi.get(self, "group_by_alert_details")

    @group_by_alert_details.setter
    def group_by_alert_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AlertDetail']]]]]):
        pulumi.set(self, "group_by_alert_details", value)

    @property
    @pulumi.getter(name="groupByCustomDetails")
    def group_by_custom_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of custom details keys to group by (when matchingMethod is Selected). Only keys defined in the current alert rule may be used.
        """
        return pulumi.get(self, "group_by_custom_details")

    @group_by_custom_details.setter
    def group_by_custom_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_by_custom_details", value)

    @property
    @pulumi.getter(name="groupByEntities")
    def group_by_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'EntityMappingType']]]]]:
        """
        A list of entity types to group by (when matchingMethod is Selected). Only entities defined in the current alert rule may be used.
        """
        return pulumi.get(self, "group_by_entities")

    @group_by_entities.setter
    def group_by_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'EntityMappingType']]]]]):
        pulumi.set(self, "group_by_entities", value)


@pulumi.input_type
class IncidentConfigurationArgs:
    def __init__(__self__, *,
                 create_incident: pulumi.Input[bool],
                 grouping_configuration: Optional[pulumi.Input['GroupingConfigurationArgs']] = None):
        """
        Incident Configuration property bag.
        :param pulumi.Input[bool] create_incident: Create incidents from alerts triggered by this analytics rule
        :param pulumi.Input['GroupingConfigurationArgs'] grouping_configuration: Set how the alerts that are triggered by this analytics rule, are grouped into incidents
        """
        pulumi.set(__self__, "create_incident", create_incident)
        if grouping_configuration is not None:
            pulumi.set(__self__, "grouping_configuration", grouping_configuration)

    @property
    @pulumi.getter(name="createIncident")
    def create_incident(self) -> pulumi.Input[bool]:
        """
        Create incidents from alerts triggered by this analytics rule
        """
        return pulumi.get(self, "create_incident")

    @create_incident.setter
    def create_incident(self, value: pulumi.Input[bool]):
        pulumi.set(self, "create_incident", value)

    @property
    @pulumi.getter(name="groupingConfiguration")
    def grouping_configuration(self) -> Optional[pulumi.Input['GroupingConfigurationArgs']]:
        """
        Set how the alerts that are triggered by this analytics rule, are grouped into incidents
        """
        return pulumi.get(self, "grouping_configuration")

    @grouping_configuration.setter
    def grouping_configuration(self, value: Optional[pulumi.Input['GroupingConfigurationArgs']]):
        pulumi.set(self, "grouping_configuration", value)


@pulumi.input_type
class WatchlistUserInfoArgs:
    def __init__(__self__, *,
                 object_id: Optional[pulumi.Input[str]] = None):
        """
        User information that made some action
        :param pulumi.Input[str] object_id: The object id of the user.
        """
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[str]]:
        """
        The object id of the user.
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_id", value)


