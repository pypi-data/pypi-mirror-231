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
    'GetPredictionResult',
    'AwaitableGetPredictionResult',
    'get_prediction',
    'get_prediction_output',
]

@pulumi.output_type
class GetPredictionResult:
    """
    The prediction resource format.
    """
    def __init__(__self__, auto_analyze=None, description=None, display_name=None, grades=None, id=None, involved_interaction_types=None, involved_kpi_types=None, involved_relationships=None, mappings=None, name=None, negative_outcome_expression=None, positive_outcome_expression=None, prediction_name=None, primary_profile_type=None, provisioning_state=None, scope_expression=None, score_label=None, system_generated_entities=None, tenant_id=None, type=None):
        if auto_analyze and not isinstance(auto_analyze, bool):
            raise TypeError("Expected argument 'auto_analyze' to be a bool")
        pulumi.set(__self__, "auto_analyze", auto_analyze)
        if description and not isinstance(description, dict):
            raise TypeError("Expected argument 'description' to be a dict")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, dict):
            raise TypeError("Expected argument 'display_name' to be a dict")
        pulumi.set(__self__, "display_name", display_name)
        if grades and not isinstance(grades, list):
            raise TypeError("Expected argument 'grades' to be a list")
        pulumi.set(__self__, "grades", grades)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if involved_interaction_types and not isinstance(involved_interaction_types, list):
            raise TypeError("Expected argument 'involved_interaction_types' to be a list")
        pulumi.set(__self__, "involved_interaction_types", involved_interaction_types)
        if involved_kpi_types and not isinstance(involved_kpi_types, list):
            raise TypeError("Expected argument 'involved_kpi_types' to be a list")
        pulumi.set(__self__, "involved_kpi_types", involved_kpi_types)
        if involved_relationships and not isinstance(involved_relationships, list):
            raise TypeError("Expected argument 'involved_relationships' to be a list")
        pulumi.set(__self__, "involved_relationships", involved_relationships)
        if mappings and not isinstance(mappings, dict):
            raise TypeError("Expected argument 'mappings' to be a dict")
        pulumi.set(__self__, "mappings", mappings)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if negative_outcome_expression and not isinstance(negative_outcome_expression, str):
            raise TypeError("Expected argument 'negative_outcome_expression' to be a str")
        pulumi.set(__self__, "negative_outcome_expression", negative_outcome_expression)
        if positive_outcome_expression and not isinstance(positive_outcome_expression, str):
            raise TypeError("Expected argument 'positive_outcome_expression' to be a str")
        pulumi.set(__self__, "positive_outcome_expression", positive_outcome_expression)
        if prediction_name and not isinstance(prediction_name, str):
            raise TypeError("Expected argument 'prediction_name' to be a str")
        pulumi.set(__self__, "prediction_name", prediction_name)
        if primary_profile_type and not isinstance(primary_profile_type, str):
            raise TypeError("Expected argument 'primary_profile_type' to be a str")
        pulumi.set(__self__, "primary_profile_type", primary_profile_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if scope_expression and not isinstance(scope_expression, str):
            raise TypeError("Expected argument 'scope_expression' to be a str")
        pulumi.set(__self__, "scope_expression", scope_expression)
        if score_label and not isinstance(score_label, str):
            raise TypeError("Expected argument 'score_label' to be a str")
        pulumi.set(__self__, "score_label", score_label)
        if system_generated_entities and not isinstance(system_generated_entities, dict):
            raise TypeError("Expected argument 'system_generated_entities' to be a dict")
        pulumi.set(__self__, "system_generated_entities", system_generated_entities)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoAnalyze")
    def auto_analyze(self) -> bool:
        """
        Whether do auto analyze.
        """
        return pulumi.get(self, "auto_analyze")

    @property
    @pulumi.getter
    def description(self) -> Optional[Mapping[str, str]]:
        """
        Description of the prediction.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, str]]:
        """
        Display name of the prediction.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def grades(self) -> Optional[Sequence['outputs.PredictionResponseGrades']]:
        """
        The prediction grades.
        """
        return pulumi.get(self, "grades")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="involvedInteractionTypes")
    def involved_interaction_types(self) -> Optional[Sequence[str]]:
        """
        Interaction types involved in the prediction.
        """
        return pulumi.get(self, "involved_interaction_types")

    @property
    @pulumi.getter(name="involvedKpiTypes")
    def involved_kpi_types(self) -> Optional[Sequence[str]]:
        """
        KPI types involved in the prediction.
        """
        return pulumi.get(self, "involved_kpi_types")

    @property
    @pulumi.getter(name="involvedRelationships")
    def involved_relationships(self) -> Optional[Sequence[str]]:
        """
        Relationships involved in the prediction.
        """
        return pulumi.get(self, "involved_relationships")

    @property
    @pulumi.getter
    def mappings(self) -> 'outputs.PredictionResponseMappings':
        """
        Definition of the link mapping of prediction.
        """
        return pulumi.get(self, "mappings")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="negativeOutcomeExpression")
    def negative_outcome_expression(self) -> str:
        """
        Negative outcome expression.
        """
        return pulumi.get(self, "negative_outcome_expression")

    @property
    @pulumi.getter(name="positiveOutcomeExpression")
    def positive_outcome_expression(self) -> str:
        """
        Positive outcome expression.
        """
        return pulumi.get(self, "positive_outcome_expression")

    @property
    @pulumi.getter(name="predictionName")
    def prediction_name(self) -> Optional[str]:
        """
        Name of the prediction.
        """
        return pulumi.get(self, "prediction_name")

    @property
    @pulumi.getter(name="primaryProfileType")
    def primary_profile_type(self) -> str:
        """
        Primary profile type.
        """
        return pulumi.get(self, "primary_profile_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="scopeExpression")
    def scope_expression(self) -> str:
        """
        Scope expression.
        """
        return pulumi.get(self, "scope_expression")

    @property
    @pulumi.getter(name="scoreLabel")
    def score_label(self) -> str:
        """
        Score label.
        """
        return pulumi.get(self, "score_label")

    @property
    @pulumi.getter(name="systemGeneratedEntities")
    def system_generated_entities(self) -> 'outputs.PredictionResponseSystemGeneratedEntities':
        """
        System generated entities.
        """
        return pulumi.get(self, "system_generated_entities")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetPredictionResult(GetPredictionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPredictionResult(
            auto_analyze=self.auto_analyze,
            description=self.description,
            display_name=self.display_name,
            grades=self.grades,
            id=self.id,
            involved_interaction_types=self.involved_interaction_types,
            involved_kpi_types=self.involved_kpi_types,
            involved_relationships=self.involved_relationships,
            mappings=self.mappings,
            name=self.name,
            negative_outcome_expression=self.negative_outcome_expression,
            positive_outcome_expression=self.positive_outcome_expression,
            prediction_name=self.prediction_name,
            primary_profile_type=self.primary_profile_type,
            provisioning_state=self.provisioning_state,
            scope_expression=self.scope_expression,
            score_label=self.score_label,
            system_generated_entities=self.system_generated_entities,
            tenant_id=self.tenant_id,
            type=self.type)


def get_prediction(hub_name: Optional[str] = None,
                   prediction_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPredictionResult:
    """
    Gets a Prediction in the hub.


    :param str hub_name: The name of the hub.
    :param str prediction_name: The name of the Prediction.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['hubName'] = hub_name
    __args__['predictionName'] = prediction_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:customerinsights/v20170426:getPrediction', __args__, opts=opts, typ=GetPredictionResult).value

    return AwaitableGetPredictionResult(
        auto_analyze=pulumi.get(__ret__, 'auto_analyze'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        grades=pulumi.get(__ret__, 'grades'),
        id=pulumi.get(__ret__, 'id'),
        involved_interaction_types=pulumi.get(__ret__, 'involved_interaction_types'),
        involved_kpi_types=pulumi.get(__ret__, 'involved_kpi_types'),
        involved_relationships=pulumi.get(__ret__, 'involved_relationships'),
        mappings=pulumi.get(__ret__, 'mappings'),
        name=pulumi.get(__ret__, 'name'),
        negative_outcome_expression=pulumi.get(__ret__, 'negative_outcome_expression'),
        positive_outcome_expression=pulumi.get(__ret__, 'positive_outcome_expression'),
        prediction_name=pulumi.get(__ret__, 'prediction_name'),
        primary_profile_type=pulumi.get(__ret__, 'primary_profile_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        scope_expression=pulumi.get(__ret__, 'scope_expression'),
        score_label=pulumi.get(__ret__, 'score_label'),
        system_generated_entities=pulumi.get(__ret__, 'system_generated_entities'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_prediction)
def get_prediction_output(hub_name: Optional[pulumi.Input[str]] = None,
                          prediction_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPredictionResult]:
    """
    Gets a Prediction in the hub.


    :param str hub_name: The name of the hub.
    :param str prediction_name: The name of the Prediction.
    :param str resource_group_name: The name of the resource group.
    """
    ...
