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
from ._inputs import *

__all__ = ['ScalingPlanPooledScheduleArgs', 'ScalingPlanPooledSchedule']

@pulumi.input_type
class ScalingPlanPooledScheduleArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 scaling_plan_name: pulumi.Input[str],
                 days_of_week: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'DayOfWeek']]]]] = None,
                 off_peak_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 off_peak_start_time: Optional[pulumi.Input['TimeArgs']] = None,
                 peak_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 peak_start_time: Optional[pulumi.Input['TimeArgs']] = None,
                 ramp_down_capacity_threshold_pct: Optional[pulumi.Input[int]] = None,
                 ramp_down_force_logoff_users: Optional[pulumi.Input[bool]] = None,
                 ramp_down_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 ramp_down_minimum_hosts_pct: Optional[pulumi.Input[int]] = None,
                 ramp_down_notification_message: Optional[pulumi.Input[str]] = None,
                 ramp_down_start_time: Optional[pulumi.Input['TimeArgs']] = None,
                 ramp_down_stop_hosts_when: Optional[pulumi.Input[Union[str, 'StopHostsWhen']]] = None,
                 ramp_down_wait_time_minutes: Optional[pulumi.Input[int]] = None,
                 ramp_up_capacity_threshold_pct: Optional[pulumi.Input[int]] = None,
                 ramp_up_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 ramp_up_minimum_hosts_pct: Optional[pulumi.Input[int]] = None,
                 ramp_up_start_time: Optional[pulumi.Input['TimeArgs']] = None,
                 scaling_plan_schedule_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ScalingPlanPooledSchedule resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] scaling_plan_name: The name of the scaling plan.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'DayOfWeek']]]] days_of_week: Set of days of the week on which this schedule is active.
        :param pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']] off_peak_load_balancing_algorithm: Load balancing algorithm for off-peak period.
        :param pulumi.Input['TimeArgs'] off_peak_start_time: Starting time for off-peak period.
        :param pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']] peak_load_balancing_algorithm: Load balancing algorithm for peak period.
        :param pulumi.Input['TimeArgs'] peak_start_time: Starting time for peak period.
        :param pulumi.Input[int] ramp_down_capacity_threshold_pct: Capacity threshold for ramp down period.
        :param pulumi.Input[bool] ramp_down_force_logoff_users: Should users be logged off forcefully from hosts.
        :param pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']] ramp_down_load_balancing_algorithm: Load balancing algorithm for ramp down period.
        :param pulumi.Input[int] ramp_down_minimum_hosts_pct: Minimum host percentage for ramp down period.
        :param pulumi.Input[str] ramp_down_notification_message: Notification message for users during ramp down period.
        :param pulumi.Input['TimeArgs'] ramp_down_start_time: Starting time for ramp down period.
        :param pulumi.Input[Union[str, 'StopHostsWhen']] ramp_down_stop_hosts_when: Specifies when to stop hosts during ramp down period.
        :param pulumi.Input[int] ramp_down_wait_time_minutes: Number of minutes to wait to stop hosts during ramp down period.
        :param pulumi.Input[int] ramp_up_capacity_threshold_pct: Capacity threshold for ramp up period.
        :param pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']] ramp_up_load_balancing_algorithm: Load balancing algorithm for ramp up period.
        :param pulumi.Input[int] ramp_up_minimum_hosts_pct: Minimum host percentage for ramp up period.
        :param pulumi.Input['TimeArgs'] ramp_up_start_time: Starting time for ramp up period.
        :param pulumi.Input[str] scaling_plan_schedule_name: The name of the ScalingPlanSchedule
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "scaling_plan_name", scaling_plan_name)
        if days_of_week is not None:
            pulumi.set(__self__, "days_of_week", days_of_week)
        if off_peak_load_balancing_algorithm is not None:
            pulumi.set(__self__, "off_peak_load_balancing_algorithm", off_peak_load_balancing_algorithm)
        if off_peak_start_time is not None:
            pulumi.set(__self__, "off_peak_start_time", off_peak_start_time)
        if peak_load_balancing_algorithm is not None:
            pulumi.set(__self__, "peak_load_balancing_algorithm", peak_load_balancing_algorithm)
        if peak_start_time is not None:
            pulumi.set(__self__, "peak_start_time", peak_start_time)
        if ramp_down_capacity_threshold_pct is not None:
            pulumi.set(__self__, "ramp_down_capacity_threshold_pct", ramp_down_capacity_threshold_pct)
        if ramp_down_force_logoff_users is not None:
            pulumi.set(__self__, "ramp_down_force_logoff_users", ramp_down_force_logoff_users)
        if ramp_down_load_balancing_algorithm is not None:
            pulumi.set(__self__, "ramp_down_load_balancing_algorithm", ramp_down_load_balancing_algorithm)
        if ramp_down_minimum_hosts_pct is not None:
            pulumi.set(__self__, "ramp_down_minimum_hosts_pct", ramp_down_minimum_hosts_pct)
        if ramp_down_notification_message is not None:
            pulumi.set(__self__, "ramp_down_notification_message", ramp_down_notification_message)
        if ramp_down_start_time is not None:
            pulumi.set(__self__, "ramp_down_start_time", ramp_down_start_time)
        if ramp_down_stop_hosts_when is not None:
            pulumi.set(__self__, "ramp_down_stop_hosts_when", ramp_down_stop_hosts_when)
        if ramp_down_wait_time_minutes is not None:
            pulumi.set(__self__, "ramp_down_wait_time_minutes", ramp_down_wait_time_minutes)
        if ramp_up_capacity_threshold_pct is not None:
            pulumi.set(__self__, "ramp_up_capacity_threshold_pct", ramp_up_capacity_threshold_pct)
        if ramp_up_load_balancing_algorithm is not None:
            pulumi.set(__self__, "ramp_up_load_balancing_algorithm", ramp_up_load_balancing_algorithm)
        if ramp_up_minimum_hosts_pct is not None:
            pulumi.set(__self__, "ramp_up_minimum_hosts_pct", ramp_up_minimum_hosts_pct)
        if ramp_up_start_time is not None:
            pulumi.set(__self__, "ramp_up_start_time", ramp_up_start_time)
        if scaling_plan_schedule_name is not None:
            pulumi.set(__self__, "scaling_plan_schedule_name", scaling_plan_schedule_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="scalingPlanName")
    def scaling_plan_name(self) -> pulumi.Input[str]:
        """
        The name of the scaling plan.
        """
        return pulumi.get(self, "scaling_plan_name")

    @scaling_plan_name.setter
    def scaling_plan_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "scaling_plan_name", value)

    @property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'DayOfWeek']]]]]:
        """
        Set of days of the week on which this schedule is active.
        """
        return pulumi.get(self, "days_of_week")

    @days_of_week.setter
    def days_of_week(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'DayOfWeek']]]]]):
        pulumi.set(self, "days_of_week", value)

    @property
    @pulumi.getter(name="offPeakLoadBalancingAlgorithm")
    def off_peak_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]]:
        """
        Load balancing algorithm for off-peak period.
        """
        return pulumi.get(self, "off_peak_load_balancing_algorithm")

    @off_peak_load_balancing_algorithm.setter
    def off_peak_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]]):
        pulumi.set(self, "off_peak_load_balancing_algorithm", value)

    @property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> Optional[pulumi.Input['TimeArgs']]:
        """
        Starting time for off-peak period.
        """
        return pulumi.get(self, "off_peak_start_time")

    @off_peak_start_time.setter
    def off_peak_start_time(self, value: Optional[pulumi.Input['TimeArgs']]):
        pulumi.set(self, "off_peak_start_time", value)

    @property
    @pulumi.getter(name="peakLoadBalancingAlgorithm")
    def peak_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]]:
        """
        Load balancing algorithm for peak period.
        """
        return pulumi.get(self, "peak_load_balancing_algorithm")

    @peak_load_balancing_algorithm.setter
    def peak_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]]):
        pulumi.set(self, "peak_load_balancing_algorithm", value)

    @property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> Optional[pulumi.Input['TimeArgs']]:
        """
        Starting time for peak period.
        """
        return pulumi.get(self, "peak_start_time")

    @peak_start_time.setter
    def peak_start_time(self, value: Optional[pulumi.Input['TimeArgs']]):
        pulumi.set(self, "peak_start_time", value)

    @property
    @pulumi.getter(name="rampDownCapacityThresholdPct")
    def ramp_down_capacity_threshold_pct(self) -> Optional[pulumi.Input[int]]:
        """
        Capacity threshold for ramp down period.
        """
        return pulumi.get(self, "ramp_down_capacity_threshold_pct")

    @ramp_down_capacity_threshold_pct.setter
    def ramp_down_capacity_threshold_pct(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ramp_down_capacity_threshold_pct", value)

    @property
    @pulumi.getter(name="rampDownForceLogoffUsers")
    def ramp_down_force_logoff_users(self) -> Optional[pulumi.Input[bool]]:
        """
        Should users be logged off forcefully from hosts.
        """
        return pulumi.get(self, "ramp_down_force_logoff_users")

    @ramp_down_force_logoff_users.setter
    def ramp_down_force_logoff_users(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ramp_down_force_logoff_users", value)

    @property
    @pulumi.getter(name="rampDownLoadBalancingAlgorithm")
    def ramp_down_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]]:
        """
        Load balancing algorithm for ramp down period.
        """
        return pulumi.get(self, "ramp_down_load_balancing_algorithm")

    @ramp_down_load_balancing_algorithm.setter
    def ramp_down_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]]):
        pulumi.set(self, "ramp_down_load_balancing_algorithm", value)

    @property
    @pulumi.getter(name="rampDownMinimumHostsPct")
    def ramp_down_minimum_hosts_pct(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum host percentage for ramp down period.
        """
        return pulumi.get(self, "ramp_down_minimum_hosts_pct")

    @ramp_down_minimum_hosts_pct.setter
    def ramp_down_minimum_hosts_pct(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ramp_down_minimum_hosts_pct", value)

    @property
    @pulumi.getter(name="rampDownNotificationMessage")
    def ramp_down_notification_message(self) -> Optional[pulumi.Input[str]]:
        """
        Notification message for users during ramp down period.
        """
        return pulumi.get(self, "ramp_down_notification_message")

    @ramp_down_notification_message.setter
    def ramp_down_notification_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ramp_down_notification_message", value)

    @property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> Optional[pulumi.Input['TimeArgs']]:
        """
        Starting time for ramp down period.
        """
        return pulumi.get(self, "ramp_down_start_time")

    @ramp_down_start_time.setter
    def ramp_down_start_time(self, value: Optional[pulumi.Input['TimeArgs']]):
        pulumi.set(self, "ramp_down_start_time", value)

    @property
    @pulumi.getter(name="rampDownStopHostsWhen")
    def ramp_down_stop_hosts_when(self) -> Optional[pulumi.Input[Union[str, 'StopHostsWhen']]]:
        """
        Specifies when to stop hosts during ramp down period.
        """
        return pulumi.get(self, "ramp_down_stop_hosts_when")

    @ramp_down_stop_hosts_when.setter
    def ramp_down_stop_hosts_when(self, value: Optional[pulumi.Input[Union[str, 'StopHostsWhen']]]):
        pulumi.set(self, "ramp_down_stop_hosts_when", value)

    @property
    @pulumi.getter(name="rampDownWaitTimeMinutes")
    def ramp_down_wait_time_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        Number of minutes to wait to stop hosts during ramp down period.
        """
        return pulumi.get(self, "ramp_down_wait_time_minutes")

    @ramp_down_wait_time_minutes.setter
    def ramp_down_wait_time_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ramp_down_wait_time_minutes", value)

    @property
    @pulumi.getter(name="rampUpCapacityThresholdPct")
    def ramp_up_capacity_threshold_pct(self) -> Optional[pulumi.Input[int]]:
        """
        Capacity threshold for ramp up period.
        """
        return pulumi.get(self, "ramp_up_capacity_threshold_pct")

    @ramp_up_capacity_threshold_pct.setter
    def ramp_up_capacity_threshold_pct(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ramp_up_capacity_threshold_pct", value)

    @property
    @pulumi.getter(name="rampUpLoadBalancingAlgorithm")
    def ramp_up_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]]:
        """
        Load balancing algorithm for ramp up period.
        """
        return pulumi.get(self, "ramp_up_load_balancing_algorithm")

    @ramp_up_load_balancing_algorithm.setter
    def ramp_up_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]]):
        pulumi.set(self, "ramp_up_load_balancing_algorithm", value)

    @property
    @pulumi.getter(name="rampUpMinimumHostsPct")
    def ramp_up_minimum_hosts_pct(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum host percentage for ramp up period.
        """
        return pulumi.get(self, "ramp_up_minimum_hosts_pct")

    @ramp_up_minimum_hosts_pct.setter
    def ramp_up_minimum_hosts_pct(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ramp_up_minimum_hosts_pct", value)

    @property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> Optional[pulumi.Input['TimeArgs']]:
        """
        Starting time for ramp up period.
        """
        return pulumi.get(self, "ramp_up_start_time")

    @ramp_up_start_time.setter
    def ramp_up_start_time(self, value: Optional[pulumi.Input['TimeArgs']]):
        pulumi.set(self, "ramp_up_start_time", value)

    @property
    @pulumi.getter(name="scalingPlanScheduleName")
    def scaling_plan_schedule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ScalingPlanSchedule
        """
        return pulumi.get(self, "scaling_plan_schedule_name")

    @scaling_plan_schedule_name.setter
    def scaling_plan_schedule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scaling_plan_schedule_name", value)


class ScalingPlanPooledSchedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 days_of_week: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'DayOfWeek']]]]] = None,
                 off_peak_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 off_peak_start_time: Optional[pulumi.Input[pulumi.InputType['TimeArgs']]] = None,
                 peak_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 peak_start_time: Optional[pulumi.Input[pulumi.InputType['TimeArgs']]] = None,
                 ramp_down_capacity_threshold_pct: Optional[pulumi.Input[int]] = None,
                 ramp_down_force_logoff_users: Optional[pulumi.Input[bool]] = None,
                 ramp_down_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 ramp_down_minimum_hosts_pct: Optional[pulumi.Input[int]] = None,
                 ramp_down_notification_message: Optional[pulumi.Input[str]] = None,
                 ramp_down_start_time: Optional[pulumi.Input[pulumi.InputType['TimeArgs']]] = None,
                 ramp_down_stop_hosts_when: Optional[pulumi.Input[Union[str, 'StopHostsWhen']]] = None,
                 ramp_down_wait_time_minutes: Optional[pulumi.Input[int]] = None,
                 ramp_up_capacity_threshold_pct: Optional[pulumi.Input[int]] = None,
                 ramp_up_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 ramp_up_minimum_hosts_pct: Optional[pulumi.Input[int]] = None,
                 ramp_up_start_time: Optional[pulumi.Input[pulumi.InputType['TimeArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scaling_plan_name: Optional[pulumi.Input[str]] = None,
                 scaling_plan_schedule_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a ScalingPlanPooledSchedule definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'DayOfWeek']]]] days_of_week: Set of days of the week on which this schedule is active.
        :param pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']] off_peak_load_balancing_algorithm: Load balancing algorithm for off-peak period.
        :param pulumi.Input[pulumi.InputType['TimeArgs']] off_peak_start_time: Starting time for off-peak period.
        :param pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']] peak_load_balancing_algorithm: Load balancing algorithm for peak period.
        :param pulumi.Input[pulumi.InputType['TimeArgs']] peak_start_time: Starting time for peak period.
        :param pulumi.Input[int] ramp_down_capacity_threshold_pct: Capacity threshold for ramp down period.
        :param pulumi.Input[bool] ramp_down_force_logoff_users: Should users be logged off forcefully from hosts.
        :param pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']] ramp_down_load_balancing_algorithm: Load balancing algorithm for ramp down period.
        :param pulumi.Input[int] ramp_down_minimum_hosts_pct: Minimum host percentage for ramp down period.
        :param pulumi.Input[str] ramp_down_notification_message: Notification message for users during ramp down period.
        :param pulumi.Input[pulumi.InputType['TimeArgs']] ramp_down_start_time: Starting time for ramp down period.
        :param pulumi.Input[Union[str, 'StopHostsWhen']] ramp_down_stop_hosts_when: Specifies when to stop hosts during ramp down period.
        :param pulumi.Input[int] ramp_down_wait_time_minutes: Number of minutes to wait to stop hosts during ramp down period.
        :param pulumi.Input[int] ramp_up_capacity_threshold_pct: Capacity threshold for ramp up period.
        :param pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']] ramp_up_load_balancing_algorithm: Load balancing algorithm for ramp up period.
        :param pulumi.Input[int] ramp_up_minimum_hosts_pct: Minimum host percentage for ramp up period.
        :param pulumi.Input[pulumi.InputType['TimeArgs']] ramp_up_start_time: Starting time for ramp up period.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] scaling_plan_name: The name of the scaling plan.
        :param pulumi.Input[str] scaling_plan_schedule_name: The name of the ScalingPlanSchedule
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScalingPlanPooledScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a ScalingPlanPooledSchedule definition.

        :param str resource_name: The name of the resource.
        :param ScalingPlanPooledScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScalingPlanPooledScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 days_of_week: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'DayOfWeek']]]]] = None,
                 off_peak_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 off_peak_start_time: Optional[pulumi.Input[pulumi.InputType['TimeArgs']]] = None,
                 peak_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 peak_start_time: Optional[pulumi.Input[pulumi.InputType['TimeArgs']]] = None,
                 ramp_down_capacity_threshold_pct: Optional[pulumi.Input[int]] = None,
                 ramp_down_force_logoff_users: Optional[pulumi.Input[bool]] = None,
                 ramp_down_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 ramp_down_minimum_hosts_pct: Optional[pulumi.Input[int]] = None,
                 ramp_down_notification_message: Optional[pulumi.Input[str]] = None,
                 ramp_down_start_time: Optional[pulumi.Input[pulumi.InputType['TimeArgs']]] = None,
                 ramp_down_stop_hosts_when: Optional[pulumi.Input[Union[str, 'StopHostsWhen']]] = None,
                 ramp_down_wait_time_minutes: Optional[pulumi.Input[int]] = None,
                 ramp_up_capacity_threshold_pct: Optional[pulumi.Input[int]] = None,
                 ramp_up_load_balancing_algorithm: Optional[pulumi.Input[Union[str, 'SessionHostLoadBalancingAlgorithm']]] = None,
                 ramp_up_minimum_hosts_pct: Optional[pulumi.Input[int]] = None,
                 ramp_up_start_time: Optional[pulumi.Input[pulumi.InputType['TimeArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scaling_plan_name: Optional[pulumi.Input[str]] = None,
                 scaling_plan_schedule_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScalingPlanPooledScheduleArgs.__new__(ScalingPlanPooledScheduleArgs)

            __props__.__dict__["days_of_week"] = days_of_week
            __props__.__dict__["off_peak_load_balancing_algorithm"] = off_peak_load_balancing_algorithm
            __props__.__dict__["off_peak_start_time"] = off_peak_start_time
            __props__.__dict__["peak_load_balancing_algorithm"] = peak_load_balancing_algorithm
            __props__.__dict__["peak_start_time"] = peak_start_time
            __props__.__dict__["ramp_down_capacity_threshold_pct"] = ramp_down_capacity_threshold_pct
            __props__.__dict__["ramp_down_force_logoff_users"] = ramp_down_force_logoff_users
            __props__.__dict__["ramp_down_load_balancing_algorithm"] = ramp_down_load_balancing_algorithm
            __props__.__dict__["ramp_down_minimum_hosts_pct"] = ramp_down_minimum_hosts_pct
            __props__.__dict__["ramp_down_notification_message"] = ramp_down_notification_message
            __props__.__dict__["ramp_down_start_time"] = ramp_down_start_time
            __props__.__dict__["ramp_down_stop_hosts_when"] = ramp_down_stop_hosts_when
            __props__.__dict__["ramp_down_wait_time_minutes"] = ramp_down_wait_time_minutes
            __props__.__dict__["ramp_up_capacity_threshold_pct"] = ramp_up_capacity_threshold_pct
            __props__.__dict__["ramp_up_load_balancing_algorithm"] = ramp_up_load_balancing_algorithm
            __props__.__dict__["ramp_up_minimum_hosts_pct"] = ramp_up_minimum_hosts_pct
            __props__.__dict__["ramp_up_start_time"] = ramp_up_start_time
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if scaling_plan_name is None and not opts.urn:
                raise TypeError("Missing required property 'scaling_plan_name'")
            __props__.__dict__["scaling_plan_name"] = scaling_plan_name
            __props__.__dict__["scaling_plan_schedule_name"] = scaling_plan_schedule_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:desktopvirtualization:ScalingPlanPooledSchedule"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20220401preview:ScalingPlanPooledSchedule"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20220909:ScalingPlanPooledSchedule"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20221014preview:ScalingPlanPooledSchedule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ScalingPlanPooledSchedule, __self__).__init__(
            'azure-native:desktopvirtualization/v20230707preview:ScalingPlanPooledSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScalingPlanPooledSchedule':
        """
        Get an existing ScalingPlanPooledSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScalingPlanPooledScheduleArgs.__new__(ScalingPlanPooledScheduleArgs)

        __props__.__dict__["days_of_week"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["off_peak_load_balancing_algorithm"] = None
        __props__.__dict__["off_peak_start_time"] = None
        __props__.__dict__["peak_load_balancing_algorithm"] = None
        __props__.__dict__["peak_start_time"] = None
        __props__.__dict__["ramp_down_capacity_threshold_pct"] = None
        __props__.__dict__["ramp_down_force_logoff_users"] = None
        __props__.__dict__["ramp_down_load_balancing_algorithm"] = None
        __props__.__dict__["ramp_down_minimum_hosts_pct"] = None
        __props__.__dict__["ramp_down_notification_message"] = None
        __props__.__dict__["ramp_down_start_time"] = None
        __props__.__dict__["ramp_down_stop_hosts_when"] = None
        __props__.__dict__["ramp_down_wait_time_minutes"] = None
        __props__.__dict__["ramp_up_capacity_threshold_pct"] = None
        __props__.__dict__["ramp_up_load_balancing_algorithm"] = None
        __props__.__dict__["ramp_up_minimum_hosts_pct"] = None
        __props__.__dict__["ramp_up_start_time"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ScalingPlanPooledSchedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Set of days of the week on which this schedule is active.
        """
        return pulumi.get(self, "days_of_week")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="offPeakLoadBalancingAlgorithm")
    def off_peak_load_balancing_algorithm(self) -> pulumi.Output[Optional[str]]:
        """
        Load balancing algorithm for off-peak period.
        """
        return pulumi.get(self, "off_peak_load_balancing_algorithm")

    @property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> pulumi.Output[Optional['outputs.TimeResponse']]:
        """
        Starting time for off-peak period.
        """
        return pulumi.get(self, "off_peak_start_time")

    @property
    @pulumi.getter(name="peakLoadBalancingAlgorithm")
    def peak_load_balancing_algorithm(self) -> pulumi.Output[Optional[str]]:
        """
        Load balancing algorithm for peak period.
        """
        return pulumi.get(self, "peak_load_balancing_algorithm")

    @property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> pulumi.Output[Optional['outputs.TimeResponse']]:
        """
        Starting time for peak period.
        """
        return pulumi.get(self, "peak_start_time")

    @property
    @pulumi.getter(name="rampDownCapacityThresholdPct")
    def ramp_down_capacity_threshold_pct(self) -> pulumi.Output[Optional[int]]:
        """
        Capacity threshold for ramp down period.
        """
        return pulumi.get(self, "ramp_down_capacity_threshold_pct")

    @property
    @pulumi.getter(name="rampDownForceLogoffUsers")
    def ramp_down_force_logoff_users(self) -> pulumi.Output[Optional[bool]]:
        """
        Should users be logged off forcefully from hosts.
        """
        return pulumi.get(self, "ramp_down_force_logoff_users")

    @property
    @pulumi.getter(name="rampDownLoadBalancingAlgorithm")
    def ramp_down_load_balancing_algorithm(self) -> pulumi.Output[Optional[str]]:
        """
        Load balancing algorithm for ramp down period.
        """
        return pulumi.get(self, "ramp_down_load_balancing_algorithm")

    @property
    @pulumi.getter(name="rampDownMinimumHostsPct")
    def ramp_down_minimum_hosts_pct(self) -> pulumi.Output[Optional[int]]:
        """
        Minimum host percentage for ramp down period.
        """
        return pulumi.get(self, "ramp_down_minimum_hosts_pct")

    @property
    @pulumi.getter(name="rampDownNotificationMessage")
    def ramp_down_notification_message(self) -> pulumi.Output[Optional[str]]:
        """
        Notification message for users during ramp down period.
        """
        return pulumi.get(self, "ramp_down_notification_message")

    @property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> pulumi.Output[Optional['outputs.TimeResponse']]:
        """
        Starting time for ramp down period.
        """
        return pulumi.get(self, "ramp_down_start_time")

    @property
    @pulumi.getter(name="rampDownStopHostsWhen")
    def ramp_down_stop_hosts_when(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies when to stop hosts during ramp down period.
        """
        return pulumi.get(self, "ramp_down_stop_hosts_when")

    @property
    @pulumi.getter(name="rampDownWaitTimeMinutes")
    def ramp_down_wait_time_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        Number of minutes to wait to stop hosts during ramp down period.
        """
        return pulumi.get(self, "ramp_down_wait_time_minutes")

    @property
    @pulumi.getter(name="rampUpCapacityThresholdPct")
    def ramp_up_capacity_threshold_pct(self) -> pulumi.Output[Optional[int]]:
        """
        Capacity threshold for ramp up period.
        """
        return pulumi.get(self, "ramp_up_capacity_threshold_pct")

    @property
    @pulumi.getter(name="rampUpLoadBalancingAlgorithm")
    def ramp_up_load_balancing_algorithm(self) -> pulumi.Output[Optional[str]]:
        """
        Load balancing algorithm for ramp up period.
        """
        return pulumi.get(self, "ramp_up_load_balancing_algorithm")

    @property
    @pulumi.getter(name="rampUpMinimumHostsPct")
    def ramp_up_minimum_hosts_pct(self) -> pulumi.Output[Optional[int]]:
        """
        Minimum host percentage for ramp up period.
        """
        return pulumi.get(self, "ramp_up_minimum_hosts_pct")

    @property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> pulumi.Output[Optional['outputs.TimeResponse']]:
        """
        Starting time for ramp up period.
        """
        return pulumi.get(self, "ramp_up_start_time")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

