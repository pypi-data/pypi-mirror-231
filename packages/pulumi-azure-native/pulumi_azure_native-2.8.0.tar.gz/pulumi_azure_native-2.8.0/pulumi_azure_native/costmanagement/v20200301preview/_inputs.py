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
    'CostAllocationProportionArgs',
    'CostAllocationRuleDetailsArgs',
    'CostAllocationRulePropertiesArgs',
    'SourceCostAllocationResourceArgs',
    'TargetCostAllocationResourceArgs',
]

@pulumi.input_type
class CostAllocationProportionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 percentage: pulumi.Input[float]):
        """
        Target resources and allocation
        :param pulumi.Input[str] name: Target resource for cost allocation
        :param pulumi.Input[float] percentage: Percentage of source cost to allocate to this resource. This value can be specified to two decimal places and the total percentage of all resources in this rule must sum to 100.00.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "percentage", percentage)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Target resource for cost allocation
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def percentage(self) -> pulumi.Input[float]:
        """
        Percentage of source cost to allocate to this resource. This value can be specified to two decimal places and the total percentage of all resources in this rule must sum to 100.00.
        """
        return pulumi.get(self, "percentage")

    @percentage.setter
    def percentage(self, value: pulumi.Input[float]):
        pulumi.set(self, "percentage", value)


@pulumi.input_type
class CostAllocationRuleDetailsArgs:
    def __init__(__self__, *,
                 source_resources: Optional[pulumi.Input[Sequence[pulumi.Input['SourceCostAllocationResourceArgs']]]] = None,
                 target_resources: Optional[pulumi.Input[Sequence[pulumi.Input['TargetCostAllocationResourceArgs']]]] = None):
        """
        Resource details of the cost allocation rule
        :param pulumi.Input[Sequence[pulumi.Input['SourceCostAllocationResourceArgs']]] source_resources: Source resources for cost allocation. At this time, this list can contain no more than one element.
        :param pulumi.Input[Sequence[pulumi.Input['TargetCostAllocationResourceArgs']]] target_resources: Target resources for cost allocation. At this time, this list can contain no more than one element.
        """
        if source_resources is not None:
            pulumi.set(__self__, "source_resources", source_resources)
        if target_resources is not None:
            pulumi.set(__self__, "target_resources", target_resources)

    @property
    @pulumi.getter(name="sourceResources")
    def source_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SourceCostAllocationResourceArgs']]]]:
        """
        Source resources for cost allocation. At this time, this list can contain no more than one element.
        """
        return pulumi.get(self, "source_resources")

    @source_resources.setter
    def source_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SourceCostAllocationResourceArgs']]]]):
        pulumi.set(self, "source_resources", value)

    @property
    @pulumi.getter(name="targetResources")
    def target_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TargetCostAllocationResourceArgs']]]]:
        """
        Target resources for cost allocation. At this time, this list can contain no more than one element.
        """
        return pulumi.get(self, "target_resources")

    @target_resources.setter
    def target_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TargetCostAllocationResourceArgs']]]]):
        pulumi.set(self, "target_resources", value)


@pulumi.input_type
class CostAllocationRulePropertiesArgs:
    def __init__(__self__, *,
                 details: pulumi.Input['CostAllocationRuleDetailsArgs'],
                 status: pulumi.Input[Union[str, 'RuleStatus']],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The properties of a cost allocation rule
        :param pulumi.Input['CostAllocationRuleDetailsArgs'] details: Resource information for the cost allocation rule
        :param pulumi.Input[Union[str, 'RuleStatus']] status: Status of the rule
        :param pulumi.Input[str] description: Description of a cost allocation rule.
        """
        pulumi.set(__self__, "details", details)
        pulumi.set(__self__, "status", status)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def details(self) -> pulumi.Input['CostAllocationRuleDetailsArgs']:
        """
        Resource information for the cost allocation rule
        """
        return pulumi.get(self, "details")

    @details.setter
    def details(self, value: pulumi.Input['CostAllocationRuleDetailsArgs']):
        pulumi.set(self, "details", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[str, 'RuleStatus']]:
        """
        Status of the rule
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[Union[str, 'RuleStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of a cost allocation rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class SourceCostAllocationResourceArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_type: pulumi.Input[Union[str, 'CostAllocationResourceType']],
                 values: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        Source resources for cost allocation
        :param pulumi.Input[str] name: If resource type is dimension, this must be either ResourceGroupName or SubscriptionId. If resource type is tag, this must be a valid Azure tag
        :param pulumi.Input[Union[str, 'CostAllocationResourceType']] resource_type: Type of resources contained in this cost allocation rule
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: Source Resources for cost allocation. This list cannot contain more than 25 values.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_type", resource_type)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        If resource type is dimension, this must be either ResourceGroupName or SubscriptionId. If resource type is tag, this must be a valid Azure tag
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[Union[str, 'CostAllocationResourceType']]:
        """
        Type of resources contained in this cost allocation rule
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[Union[str, 'CostAllocationResourceType']]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Source Resources for cost allocation. This list cannot contain more than 25 values.
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class TargetCostAllocationResourceArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 policy_type: pulumi.Input[Union[str, 'CostAllocationPolicyType']],
                 resource_type: pulumi.Input[Union[str, 'CostAllocationResourceType']],
                 values: pulumi.Input[Sequence[pulumi.Input['CostAllocationProportionArgs']]]):
        """
        Target resources for cost allocation.
        :param pulumi.Input[str] name: If resource type is dimension, this must be either ResourceGroupName or SubscriptionId. If resource type is tag, this must be a valid Azure tag
        :param pulumi.Input[Union[str, 'CostAllocationPolicyType']] policy_type: Method of cost allocation for the rule
        :param pulumi.Input[Union[str, 'CostAllocationResourceType']] resource_type: Type of resources contained in this cost allocation rule
        :param pulumi.Input[Sequence[pulumi.Input['CostAllocationProportionArgs']]] values: Target resources for cost allocation. This list cannot contain more than 25 values.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "policy_type", policy_type)
        pulumi.set(__self__, "resource_type", resource_type)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        If resource type is dimension, this must be either ResourceGroupName or SubscriptionId. If resource type is tag, this must be a valid Azure tag
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Input[Union[str, 'CostAllocationPolicyType']]:
        """
        Method of cost allocation for the rule
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: pulumi.Input[Union[str, 'CostAllocationPolicyType']]):
        pulumi.set(self, "policy_type", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[Union[str, 'CostAllocationResourceType']]:
        """
        Type of resources contained in this cost allocation rule
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[Union[str, 'CostAllocationResourceType']]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input['CostAllocationProportionArgs']]]:
        """
        Target resources for cost allocation. This list cannot contain more than 25 values.
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input['CostAllocationProportionArgs']]]):
        pulumi.set(self, "values", value)


