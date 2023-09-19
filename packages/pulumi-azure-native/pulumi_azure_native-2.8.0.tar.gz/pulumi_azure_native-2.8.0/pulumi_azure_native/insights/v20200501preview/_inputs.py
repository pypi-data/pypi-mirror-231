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
    'ActionArgs',
    'ConditionFailingPeriodsArgs',
    'ConditionArgs',
    'DimensionArgs',
    'ScheduledQueryRuleCriteriaArgs',
]

@pulumi.input_type
class ActionArgs:
    def __init__(__self__, *,
                 action_group_id: Optional[pulumi.Input[str]] = None,
                 web_hook_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Actions to invoke when the alert fires.
        :param pulumi.Input[str] action_group_id: Action Group resource Id to invoke when the alert fires.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] web_hook_properties: The properties of a webhook object.
        """
        if action_group_id is not None:
            pulumi.set(__self__, "action_group_id", action_group_id)
        if web_hook_properties is not None:
            pulumi.set(__self__, "web_hook_properties", web_hook_properties)

    @property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Action Group resource Id to invoke when the alert fires.
        """
        return pulumi.get(self, "action_group_id")

    @action_group_id.setter
    def action_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_group_id", value)

    @property
    @pulumi.getter(name="webHookProperties")
    def web_hook_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The properties of a webhook object.
        """
        return pulumi.get(self, "web_hook_properties")

    @web_hook_properties.setter
    def web_hook_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "web_hook_properties", value)


@pulumi.input_type
class ConditionFailingPeriodsArgs:
    def __init__(__self__, *,
                 min_failing_periods_to_alert: Optional[pulumi.Input[float]] = None,
                 number_of_evaluation_periods: Optional[pulumi.Input[float]] = None):
        """
        The minimum number of violations required within the selected lookback time window required to raise an alert.
        :param pulumi.Input[float] min_failing_periods_to_alert: The number of violations to trigger an alert. Should be smaller or equal to numberOfEvaluationPeriods. Default value is 1
        :param pulumi.Input[float] number_of_evaluation_periods: The number of aggregated lookback points. The lookback time window is calculated based on the aggregation granularity (windowSize) and the selected number of aggregated points. Default value is 1
        """
        if min_failing_periods_to_alert is None:
            min_failing_periods_to_alert = 1
        if min_failing_periods_to_alert is not None:
            pulumi.set(__self__, "min_failing_periods_to_alert", min_failing_periods_to_alert)
        if number_of_evaluation_periods is None:
            number_of_evaluation_periods = 1
        if number_of_evaluation_periods is not None:
            pulumi.set(__self__, "number_of_evaluation_periods", number_of_evaluation_periods)

    @property
    @pulumi.getter(name="minFailingPeriodsToAlert")
    def min_failing_periods_to_alert(self) -> Optional[pulumi.Input[float]]:
        """
        The number of violations to trigger an alert. Should be smaller or equal to numberOfEvaluationPeriods. Default value is 1
        """
        return pulumi.get(self, "min_failing_periods_to_alert")

    @min_failing_periods_to_alert.setter
    def min_failing_periods_to_alert(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "min_failing_periods_to_alert", value)

    @property
    @pulumi.getter(name="numberOfEvaluationPeriods")
    def number_of_evaluation_periods(self) -> Optional[pulumi.Input[float]]:
        """
        The number of aggregated lookback points. The lookback time window is calculated based on the aggregation granularity (windowSize) and the selected number of aggregated points. Default value is 1
        """
        return pulumi.get(self, "number_of_evaluation_periods")

    @number_of_evaluation_periods.setter
    def number_of_evaluation_periods(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "number_of_evaluation_periods", value)


@pulumi.input_type
class ConditionArgs:
    def __init__(__self__, *,
                 operator: pulumi.Input[Union[str, 'ConditionOperator']],
                 threshold: pulumi.Input[float],
                 time_aggregation: pulumi.Input[Union[str, 'TimeAggregation']],
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['DimensionArgs']]]] = None,
                 failing_periods: Optional[pulumi.Input['ConditionFailingPeriodsArgs']] = None,
                 metric_measure_column: Optional[pulumi.Input[str]] = None,
                 query: Optional[pulumi.Input[str]] = None,
                 resource_id_column: Optional[pulumi.Input[str]] = None):
        """
        A condition of the scheduled query rule.
        :param pulumi.Input[Union[str, 'ConditionOperator']] operator: The criteria operator.
        :param pulumi.Input[float] threshold: the criteria threshold value that activates the alert.
        :param pulumi.Input[Union[str, 'TimeAggregation']] time_aggregation: Aggregation type
        :param pulumi.Input[Sequence[pulumi.Input['DimensionArgs']]] dimensions: List of Dimensions conditions
        :param pulumi.Input['ConditionFailingPeriodsArgs'] failing_periods: The minimum number of violations required within the selected lookback time window required to raise an alert.
        :param pulumi.Input[str] metric_measure_column: The column containing the metric measure number.
        :param pulumi.Input[str] query: Log query alert
        :param pulumi.Input[str] resource_id_column: The column containing the resource id. The content of the column must be a uri formatted as resource id
        """
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "threshold", threshold)
        pulumi.set(__self__, "time_aggregation", time_aggregation)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if failing_periods is not None:
            pulumi.set(__self__, "failing_periods", failing_periods)
        if metric_measure_column is not None:
            pulumi.set(__self__, "metric_measure_column", metric_measure_column)
        if query is not None:
            pulumi.set(__self__, "query", query)
        if resource_id_column is not None:
            pulumi.set(__self__, "resource_id_column", resource_id_column)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[str, 'ConditionOperator']]:
        """
        The criteria operator.
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input[Union[str, 'ConditionOperator']]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[float]:
        """
        the criteria threshold value that activates the alert.
        """
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: pulumi.Input[float]):
        pulumi.set(self, "threshold", value)

    @property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(self) -> pulumi.Input[Union[str, 'TimeAggregation']]:
        """
        Aggregation type
        """
        return pulumi.get(self, "time_aggregation")

    @time_aggregation.setter
    def time_aggregation(self, value: pulumi.Input[Union[str, 'TimeAggregation']]):
        pulumi.set(self, "time_aggregation", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DimensionArgs']]]]:
        """
        List of Dimensions conditions
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter(name="failingPeriods")
    def failing_periods(self) -> Optional[pulumi.Input['ConditionFailingPeriodsArgs']]:
        """
        The minimum number of violations required within the selected lookback time window required to raise an alert.
        """
        return pulumi.get(self, "failing_periods")

    @failing_periods.setter
    def failing_periods(self, value: Optional[pulumi.Input['ConditionFailingPeriodsArgs']]):
        pulumi.set(self, "failing_periods", value)

    @property
    @pulumi.getter(name="metricMeasureColumn")
    def metric_measure_column(self) -> Optional[pulumi.Input[str]]:
        """
        The column containing the metric measure number.
        """
        return pulumi.get(self, "metric_measure_column")

    @metric_measure_column.setter
    def metric_measure_column(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_measure_column", value)

    @property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[str]]:
        """
        Log query alert
        """
        return pulumi.get(self, "query")

    @query.setter
    def query(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query", value)

    @property
    @pulumi.getter(name="resourceIdColumn")
    def resource_id_column(self) -> Optional[pulumi.Input[str]]:
        """
        The column containing the resource id. The content of the column must be a uri formatted as resource id
        """
        return pulumi.get(self, "resource_id_column")

    @resource_id_column.setter
    def resource_id_column(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id_column", value)


@pulumi.input_type
class DimensionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 operator: pulumi.Input[Union[str, 'DimensionOperator']],
                 values: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        Dimension splitting and filtering definition
        :param pulumi.Input[str] name: Name of the dimension
        :param pulumi.Input[Union[str, 'DimensionOperator']] operator: Operator for dimension values
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: List of dimension values
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the dimension
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[str, 'DimensionOperator']]:
        """
        Operator for dimension values
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input[Union[str, 'DimensionOperator']]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of dimension values
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class ScheduledQueryRuleCriteriaArgs:
    def __init__(__self__, *,
                 all_of: Optional[pulumi.Input[Sequence[pulumi.Input['ConditionArgs']]]] = None):
        """
        The rule criteria that defines the conditions of the scheduled query rule.
        :param pulumi.Input[Sequence[pulumi.Input['ConditionArgs']]] all_of: A list of conditions to evaluate against the specified scopes
        """
        if all_of is not None:
            pulumi.set(__self__, "all_of", all_of)

    @property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConditionArgs']]]]:
        """
        A list of conditions to evaluate against the specified scopes
        """
        return pulumi.get(self, "all_of")

    @all_of.setter
    def all_of(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConditionArgs']]]]):
        pulumi.set(self, "all_of", value)


