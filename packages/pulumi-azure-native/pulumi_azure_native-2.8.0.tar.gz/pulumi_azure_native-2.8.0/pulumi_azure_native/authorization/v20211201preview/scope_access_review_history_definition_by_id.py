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

__all__ = ['ScopeAccessReviewHistoryDefinitionByIdArgs', 'ScopeAccessReviewHistoryDefinitionById']

@pulumi.input_type
class ScopeAccessReviewHistoryDefinitionByIdArgs:
    def __init__(__self__, *,
                 scope: pulumi.Input[str],
                 decisions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AccessReviewResult']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 history_definition_id: Optional[pulumi.Input[str]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewHistoryInstanceArgs']]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 number_of_occurrences: Optional[pulumi.Input[int]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewScopeArgs']]]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'AccessReviewRecurrenceRangeType']]] = None):
        """
        The set of arguments for constructing a ScopeAccessReviewHistoryDefinitionById resource.
        :param pulumi.Input[str] scope: The scope of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AccessReviewResult']]]] decisions: Collection of review decisions which the history data should be filtered on. For example if Approve and Deny are supplied the data will only contain review results in which the decision maker approved or denied a review request.
        :param pulumi.Input[str] display_name: The display name for the history definition.
        :param pulumi.Input[str] end_date: The DateTime when the review is scheduled to end. Required if type is endDate
        :param pulumi.Input[str] history_definition_id: The id of the access review history definition.
        :param pulumi.Input[Sequence[pulumi.Input['AccessReviewHistoryInstanceArgs']]] instances: Set of access review history instances for this history definition.
        :param pulumi.Input[int] interval: The interval for recurrence. For a quarterly review, the interval is 3 for type : absoluteMonthly.
        :param pulumi.Input[int] number_of_occurrences: The number of times to repeat the access review. Required and must be positive if type is numbered.
        :param pulumi.Input[Sequence[pulumi.Input['AccessReviewScopeArgs']]] scopes: A collection of scopes used when selecting review history data
        :param pulumi.Input[str] start_date: The DateTime when the review is scheduled to be start. This could be a date in the future. Required on create.
        :param pulumi.Input[Union[str, 'AccessReviewRecurrenceRangeType']] type: The recurrence range type. The possible values are: endDate, noEnd, numbered.
        """
        pulumi.set(__self__, "scope", scope)
        if decisions is not None:
            pulumi.set(__self__, "decisions", decisions)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if end_date is not None:
            pulumi.set(__self__, "end_date", end_date)
        if history_definition_id is not None:
            pulumi.set(__self__, "history_definition_id", history_definition_id)
        if instances is not None:
            pulumi.set(__self__, "instances", instances)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if number_of_occurrences is not None:
            pulumi.set(__self__, "number_of_occurrences", number_of_occurrences)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if start_date is not None:
            pulumi.set(__self__, "start_date", start_date)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope of the resource.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def decisions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AccessReviewResult']]]]]:
        """
        Collection of review decisions which the history data should be filtered on. For example if Approve and Deny are supplied the data will only contain review results in which the decision maker approved or denied a review request.
        """
        return pulumi.get(self, "decisions")

    @decisions.setter
    def decisions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AccessReviewResult']]]]]):
        pulumi.set(self, "decisions", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name for the history definition.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[str]]:
        """
        The DateTime when the review is scheduled to end. Required if type is endDate
        """
        return pulumi.get(self, "end_date")

    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_date", value)

    @property
    @pulumi.getter(name="historyDefinitionId")
    def history_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the access review history definition.
        """
        return pulumi.get(self, "history_definition_id")

    @history_definition_id.setter
    def history_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "history_definition_id", value)

    @property
    @pulumi.getter
    def instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewHistoryInstanceArgs']]]]:
        """
        Set of access review history instances for this history definition.
        """
        return pulumi.get(self, "instances")

    @instances.setter
    def instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewHistoryInstanceArgs']]]]):
        pulumi.set(self, "instances", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        The interval for recurrence. For a quarterly review, the interval is 3 for type : absoluteMonthly.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter(name="numberOfOccurrences")
    def number_of_occurrences(self) -> Optional[pulumi.Input[int]]:
        """
        The number of times to repeat the access review. Required and must be positive if type is numbered.
        """
        return pulumi.get(self, "number_of_occurrences")

    @number_of_occurrences.setter
    def number_of_occurrences(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "number_of_occurrences", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewScopeArgs']]]]:
        """
        A collection of scopes used when selecting review history data
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewScopeArgs']]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[str]]:
        """
        The DateTime when the review is scheduled to be start. This could be a date in the future. Required on create.
        """
        return pulumi.get(self, "start_date")

    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_date", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'AccessReviewRecurrenceRangeType']]]:
        """
        The recurrence range type. The possible values are: endDate, noEnd, numbered.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'AccessReviewRecurrenceRangeType']]]):
        pulumi.set(self, "type", value)


class ScopeAccessReviewHistoryDefinitionById(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 decisions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AccessReviewResult']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 history_definition_id: Optional[pulumi.Input[str]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessReviewHistoryInstanceArgs']]]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 number_of_occurrences: Optional[pulumi.Input[int]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessReviewScopeArgs']]]]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'AccessReviewRecurrenceRangeType']]] = None,
                 __props__=None):
        """
        Access Review History Definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AccessReviewResult']]]] decisions: Collection of review decisions which the history data should be filtered on. For example if Approve and Deny are supplied the data will only contain review results in which the decision maker approved or denied a review request.
        :param pulumi.Input[str] display_name: The display name for the history definition.
        :param pulumi.Input[str] end_date: The DateTime when the review is scheduled to end. Required if type is endDate
        :param pulumi.Input[str] history_definition_id: The id of the access review history definition.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessReviewHistoryInstanceArgs']]]] instances: Set of access review history instances for this history definition.
        :param pulumi.Input[int] interval: The interval for recurrence. For a quarterly review, the interval is 3 for type : absoluteMonthly.
        :param pulumi.Input[int] number_of_occurrences: The number of times to repeat the access review. Required and must be positive if type is numbered.
        :param pulumi.Input[str] scope: The scope of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessReviewScopeArgs']]]] scopes: A collection of scopes used when selecting review history data
        :param pulumi.Input[str] start_date: The DateTime when the review is scheduled to be start. This could be a date in the future. Required on create.
        :param pulumi.Input[Union[str, 'AccessReviewRecurrenceRangeType']] type: The recurrence range type. The possible values are: endDate, noEnd, numbered.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScopeAccessReviewHistoryDefinitionByIdArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Access Review History Definition.

        :param str resource_name: The name of the resource.
        :param ScopeAccessReviewHistoryDefinitionByIdArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScopeAccessReviewHistoryDefinitionByIdArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 decisions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AccessReviewResult']]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 history_definition_id: Optional[pulumi.Input[str]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessReviewHistoryInstanceArgs']]]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 number_of_occurrences: Optional[pulumi.Input[int]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessReviewScopeArgs']]]]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'AccessReviewRecurrenceRangeType']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScopeAccessReviewHistoryDefinitionByIdArgs.__new__(ScopeAccessReviewHistoryDefinitionByIdArgs)

            __props__.__dict__["decisions"] = decisions
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["end_date"] = end_date
            __props__.__dict__["history_definition_id"] = history_definition_id
            __props__.__dict__["instances"] = instances
            __props__.__dict__["interval"] = interval
            __props__.__dict__["number_of_occurrences"] = number_of_occurrences
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["start_date"] = start_date
            __props__.__dict__["type"] = type
            __props__.__dict__["created_date_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["principal_id"] = None
            __props__.__dict__["principal_name"] = None
            __props__.__dict__["principal_type"] = None
            __props__.__dict__["review_history_period_end_date_time"] = None
            __props__.__dict__["review_history_period_start_date_time"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["user_principal_name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:authorization:ScopeAccessReviewHistoryDefinitionById")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ScopeAccessReviewHistoryDefinitionById, __self__).__init__(
            'azure-native:authorization/v20211201preview:ScopeAccessReviewHistoryDefinitionById',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScopeAccessReviewHistoryDefinitionById':
        """
        Get an existing ScopeAccessReviewHistoryDefinitionById resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScopeAccessReviewHistoryDefinitionByIdArgs.__new__(ScopeAccessReviewHistoryDefinitionByIdArgs)

        __props__.__dict__["created_date_time"] = None
        __props__.__dict__["decisions"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["end_date"] = None
        __props__.__dict__["instances"] = None
        __props__.__dict__["interval"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["number_of_occurrences"] = None
        __props__.__dict__["principal_id"] = None
        __props__.__dict__["principal_name"] = None
        __props__.__dict__["principal_type"] = None
        __props__.__dict__["review_history_period_end_date_time"] = None
        __props__.__dict__["review_history_period_start_date_time"] = None
        __props__.__dict__["scopes"] = None
        __props__.__dict__["start_date"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_principal_name"] = None
        return ScopeAccessReviewHistoryDefinitionById(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> pulumi.Output[str]:
        """
        Date time when history definition was created
        """
        return pulumi.get(self, "created_date_time")

    @property
    @pulumi.getter
    def decisions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Collection of review decisions which the history data should be filtered on. For example if Approve and Deny are supplied the data will only contain review results in which the decision maker approved or denied a review request.
        """
        return pulumi.get(self, "decisions")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name for the history definition.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[Optional[str]]:
        """
        The DateTime when the review is scheduled to end. Required if type is endDate
        """
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Optional[Sequence['outputs.AccessReviewHistoryInstanceResponse']]]:
        """
        Set of access review history instances for this history definition.
        """
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter
    def interval(self) -> pulumi.Output[Optional[int]]:
        """
        The interval for recurrence. For a quarterly review, the interval is 3 for type : absoluteMonthly.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The access review history definition unique id.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numberOfOccurrences")
    def number_of_occurrences(self) -> pulumi.Output[Optional[int]]:
        """
        The number of times to repeat the access review. Required and must be positive if type is numbered.
        """
        return pulumi.get(self, "number_of_occurrences")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[str]:
        """
        The identity id
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> pulumi.Output[str]:
        """
        The identity display name
        """
        return pulumi.get(self, "principal_name")

    @property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[str]:
        """
        The identity type : user/servicePrincipal
        """
        return pulumi.get(self, "principal_type")

    @property
    @pulumi.getter(name="reviewHistoryPeriodEndDateTime")
    def review_history_period_end_date_time(self) -> pulumi.Output[str]:
        """
        Date time used when selecting review data, all reviews included in data end on or before this date. For use only with one-time/non-recurring reports.
        """
        return pulumi.get(self, "review_history_period_end_date_time")

    @property
    @pulumi.getter(name="reviewHistoryPeriodStartDateTime")
    def review_history_period_start_date_time(self) -> pulumi.Output[str]:
        """
        Date time used when selecting review data, all reviews included in data start on or after this date. For use only with one-time/non-recurring reports.
        """
        return pulumi.get(self, "review_history_period_start_date_time")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence['outputs.AccessReviewScopeResponse']]]:
        """
        A collection of scopes used when selecting review history data
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[Optional[str]]:
        """
        The DateTime when the review is scheduled to be start. This could be a date in the future. Required on create.
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        This read-only field specifies the of the requested review history data. This is either requested, in-progress, done or error.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> pulumi.Output[str]:
        """
        The user principal name(if valid)
        """
        return pulumi.get(self, "user_principal_name")

