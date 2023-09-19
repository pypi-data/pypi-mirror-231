# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'ApiKeyAuthenticationArgs',
    'HealthCheckStepPropertiesArgs',
    'IdentityArgs',
    'PrePostStepArgs',
    'RestHealthCheckStepAttributesArgs',
    'RestHealthCheckArgs',
    'RestRequestArgs',
    'RestResponseRegexArgs',
    'RestResponseArgs',
    'RolloutIdentityAuthenticationArgs',
    'SasAuthenticationArgs',
    'ServiceUnitArtifactsArgs',
    'StepGroupArgs',
    'WaitStepAttributesArgs',
    'WaitStepPropertiesArgs',
]

@pulumi.input_type
class ApiKeyAuthenticationArgs:
    def __init__(__self__, *,
                 in_: pulumi.Input['RestAuthLocation'],
                 name: pulumi.Input[str],
                 type: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        ApiKey authentication gives a name and a value that can be included in either the request header or query parameters.
        :param pulumi.Input['RestAuthLocation'] in_: The location of the authentication key/value pair in the request.
        :param pulumi.Input[str] name: The key name of the authentication key/value pair.
        :param pulumi.Input[str] type: The authentication type.
               Expected value is 'ApiKey'.
        :param pulumi.Input[str] value: The value of the authentication key/value pair.
        """
        pulumi.set(__self__, "in_", in_)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", 'ApiKey')
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="in")
    def in_(self) -> pulumi.Input['RestAuthLocation']:
        """
        The location of the authentication key/value pair in the request.
        """
        return pulumi.get(self, "in_")

    @in_.setter
    def in_(self, value: pulumi.Input['RestAuthLocation']):
        pulumi.set(self, "in_", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The key name of the authentication key/value pair.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The authentication type.
        Expected value is 'ApiKey'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the authentication key/value pair.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class HealthCheckStepPropertiesArgs:
    def __init__(__self__, *,
                 attributes: pulumi.Input['RestHealthCheckStepAttributesArgs'],
                 step_type: pulumi.Input[str]):
        """
        Defines the properties of a health check step.
        :param pulumi.Input['RestHealthCheckStepAttributesArgs'] attributes: The health check step attributes
        :param pulumi.Input[str] step_type: The type of step.
               Expected value is 'HealthCheck'.
        """
        pulumi.set(__self__, "attributes", attributes)
        pulumi.set(__self__, "step_type", 'HealthCheck')

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Input['RestHealthCheckStepAttributesArgs']:
        """
        The health check step attributes
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: pulumi.Input['RestHealthCheckStepAttributesArgs']):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="stepType")
    def step_type(self) -> pulumi.Input[str]:
        """
        The type of step.
        Expected value is 'HealthCheck'.
        """
        return pulumi.get(self, "step_type")

    @step_type.setter
    def step_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "step_type", value)


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *,
                 identity_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 type: pulumi.Input[str]):
        """
        Identity for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identity_ids: The list of identities.
        :param pulumi.Input[str] type: The identity type.
        """
        pulumi.set(__self__, "identity_ids", identity_ids)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="identityIds")
    def identity_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of identities.
        """
        return pulumi.get(self, "identity_ids")

    @identity_ids.setter
    def identity_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "identity_ids", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class PrePostStepArgs:
    def __init__(__self__, *,
                 step_id: pulumi.Input[str]):
        """
        The properties that define a step.
        :param pulumi.Input[str] step_id: The resource Id of the step to be run.
        """
        pulumi.set(__self__, "step_id", step_id)

    @property
    @pulumi.getter(name="stepId")
    def step_id(self) -> pulumi.Input[str]:
        """
        The resource Id of the step to be run.
        """
        return pulumi.get(self, "step_id")

    @step_id.setter
    def step_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "step_id", value)


@pulumi.input_type
class RestHealthCheckStepAttributesArgs:
    def __init__(__self__, *,
                 health_checks: pulumi.Input[Sequence[pulumi.Input['RestHealthCheckArgs']]],
                 healthy_state_duration: pulumi.Input[str],
                 type: pulumi.Input[str],
                 max_elastic_duration: Optional[pulumi.Input[str]] = None,
                 wait_duration: Optional[pulumi.Input[str]] = None):
        """
        Defines the REST health check step properties.
        :param pulumi.Input[Sequence[pulumi.Input['RestHealthCheckArgs']]] health_checks: The list of checks that form the health check step.
        :param pulumi.Input[str] healthy_state_duration: The duration in ISO 8601 format for which the resource is expected to be continuously healthy. If maxElasticDuration is specified, healthy state duration is enforced after the detection of first healthy signal.
        :param pulumi.Input[str] type: The type of health check.
               Expected value is 'REST'.
        :param pulumi.Input[str] max_elastic_duration: The duration in ISO 8601 format for which the health check waits for the resource to become healthy. Health check fails if it doesn't. Health check starts to enforce healthyStateDuration once resource becomes healthy.
        :param pulumi.Input[str] wait_duration: The duration in ISO 8601 format for which health check waits idly without any checks.
        """
        pulumi.set(__self__, "health_checks", health_checks)
        pulumi.set(__self__, "healthy_state_duration", healthy_state_duration)
        pulumi.set(__self__, "type", 'REST')
        if max_elastic_duration is not None:
            pulumi.set(__self__, "max_elastic_duration", max_elastic_duration)
        if wait_duration is not None:
            pulumi.set(__self__, "wait_duration", wait_duration)

    @property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> pulumi.Input[Sequence[pulumi.Input['RestHealthCheckArgs']]]:
        """
        The list of checks that form the health check step.
        """
        return pulumi.get(self, "health_checks")

    @health_checks.setter
    def health_checks(self, value: pulumi.Input[Sequence[pulumi.Input['RestHealthCheckArgs']]]):
        pulumi.set(self, "health_checks", value)

    @property
    @pulumi.getter(name="healthyStateDuration")
    def healthy_state_duration(self) -> pulumi.Input[str]:
        """
        The duration in ISO 8601 format for which the resource is expected to be continuously healthy. If maxElasticDuration is specified, healthy state duration is enforced after the detection of first healthy signal.
        """
        return pulumi.get(self, "healthy_state_duration")

    @healthy_state_duration.setter
    def healthy_state_duration(self, value: pulumi.Input[str]):
        pulumi.set(self, "healthy_state_duration", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of health check.
        Expected value is 'REST'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="maxElasticDuration")
    def max_elastic_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The duration in ISO 8601 format for which the health check waits for the resource to become healthy. Health check fails if it doesn't. Health check starts to enforce healthyStateDuration once resource becomes healthy.
        """
        return pulumi.get(self, "max_elastic_duration")

    @max_elastic_duration.setter
    def max_elastic_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "max_elastic_duration", value)

    @property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The duration in ISO 8601 format for which health check waits idly without any checks.
        """
        return pulumi.get(self, "wait_duration")

    @wait_duration.setter
    def wait_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "wait_duration", value)


@pulumi.input_type
class RestHealthCheckArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 request: pulumi.Input['RestRequestArgs'],
                 response: Optional[pulumi.Input['RestResponseArgs']] = None):
        """
        A REST based health check
        :param pulumi.Input[str] name: A unique name for this check.
        :param pulumi.Input['RestRequestArgs'] request: The request to the health provider.
        :param pulumi.Input['RestResponseArgs'] response: The expected response from the health provider. If no expected response is provided, the default is to expect the received response to have an HTTP status code of 200 OK.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "request", request)
        if response is not None:
            pulumi.set(__self__, "response", response)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        A unique name for this check.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def request(self) -> pulumi.Input['RestRequestArgs']:
        """
        The request to the health provider.
        """
        return pulumi.get(self, "request")

    @request.setter
    def request(self, value: pulumi.Input['RestRequestArgs']):
        pulumi.set(self, "request", value)

    @property
    @pulumi.getter
    def response(self) -> Optional[pulumi.Input['RestResponseArgs']]:
        """
        The expected response from the health provider. If no expected response is provided, the default is to expect the received response to have an HTTP status code of 200 OK.
        """
        return pulumi.get(self, "response")

    @response.setter
    def response(self, value: Optional[pulumi.Input['RestResponseArgs']]):
        pulumi.set(self, "response", value)


@pulumi.input_type
class RestRequestArgs:
    def __init__(__self__, *,
                 authentication: pulumi.Input[Union['ApiKeyAuthenticationArgs', 'RolloutIdentityAuthenticationArgs']],
                 method: pulumi.Input['RestRequestMethod'],
                 uri: pulumi.Input[str]):
        """
        The properties that make up a REST request
        :param pulumi.Input[Union['ApiKeyAuthenticationArgs', 'RolloutIdentityAuthenticationArgs']] authentication: The authentication information required in the request to the health provider.
        :param pulumi.Input['RestRequestMethod'] method: The HTTP method to use for the request.
        :param pulumi.Input[str] uri: The HTTP URI to use for the request.
        """
        pulumi.set(__self__, "authentication", authentication)
        pulumi.set(__self__, "method", method)
        pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Input[Union['ApiKeyAuthenticationArgs', 'RolloutIdentityAuthenticationArgs']]:
        """
        The authentication information required in the request to the health provider.
        """
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: pulumi.Input[Union['ApiKeyAuthenticationArgs', 'RolloutIdentityAuthenticationArgs']]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter
    def method(self) -> pulumi.Input['RestRequestMethod']:
        """
        The HTTP method to use for the request.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: pulumi.Input['RestRequestMethod']):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Input[str]:
        """
        The HTTP URI to use for the request.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "uri", value)


@pulumi.input_type
class RestResponseRegexArgs:
    def __init__(__self__, *,
                 match_quantifier: Optional[pulumi.Input['RestMatchQuantifier']] = None,
                 matches: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The regular expressions to match the response content with.
        :param pulumi.Input['RestMatchQuantifier'] match_quantifier: Indicates whether any or all of the expressions should match with the response content.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] matches: The list of regular expressions.
        """
        if match_quantifier is not None:
            pulumi.set(__self__, "match_quantifier", match_quantifier)
        if matches is not None:
            pulumi.set(__self__, "matches", matches)

    @property
    @pulumi.getter(name="matchQuantifier")
    def match_quantifier(self) -> Optional[pulumi.Input['RestMatchQuantifier']]:
        """
        Indicates whether any or all of the expressions should match with the response content.
        """
        return pulumi.get(self, "match_quantifier")

    @match_quantifier.setter
    def match_quantifier(self, value: Optional[pulumi.Input['RestMatchQuantifier']]):
        pulumi.set(self, "match_quantifier", value)

    @property
    @pulumi.getter
    def matches(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of regular expressions.
        """
        return pulumi.get(self, "matches")

    @matches.setter
    def matches(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "matches", value)


@pulumi.input_type
class RestResponseArgs:
    def __init__(__self__, *,
                 regex: Optional[pulumi.Input['RestResponseRegexArgs']] = None,
                 success_status_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The properties that make up the expected REST response
        :param pulumi.Input['RestResponseRegexArgs'] regex: The regular expressions to match the response content with.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] success_status_codes: The HTTP status codes expected in a successful health check response. The response is expected to match one of the given status codes. If no expected status codes are provided, default expected status code is 200 OK.
        """
        if regex is not None:
            pulumi.set(__self__, "regex", regex)
        if success_status_codes is not None:
            pulumi.set(__self__, "success_status_codes", success_status_codes)

    @property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input['RestResponseRegexArgs']]:
        """
        The regular expressions to match the response content with.
        """
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[pulumi.Input['RestResponseRegexArgs']]):
        pulumi.set(self, "regex", value)

    @property
    @pulumi.getter(name="successStatusCodes")
    def success_status_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The HTTP status codes expected in a successful health check response. The response is expected to match one of the given status codes. If no expected status codes are provided, default expected status code is 200 OK.
        """
        return pulumi.get(self, "success_status_codes")

    @success_status_codes.setter
    def success_status_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "success_status_codes", value)


@pulumi.input_type
class RolloutIdentityAuthenticationArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str]):
        """
        RolloutIdentity uses the user-assigned managed identity authentication context specified in the Identity property during rollout creation.
        :param pulumi.Input[str] type: The authentication type.
               Expected value is 'RolloutIdentity'.
        """
        pulumi.set(__self__, "type", 'RolloutIdentity')

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The authentication type.
        Expected value is 'RolloutIdentity'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class SasAuthenticationArgs:
    def __init__(__self__, *,
                 sas_uri: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        Defines the properties to access the artifacts using an Azure Storage SAS URI.
        :param pulumi.Input[str] sas_uri: The SAS URI to the Azure Storage blob container. Any offset from the root of the container to where the artifacts are located can be defined in the artifactRoot.
        :param pulumi.Input[str] type: The authentication type
               Expected value is 'Sas'.
        """
        pulumi.set(__self__, "sas_uri", sas_uri)
        pulumi.set(__self__, "type", 'Sas')

    @property
    @pulumi.getter(name="sasUri")
    def sas_uri(self) -> pulumi.Input[str]:
        """
        The SAS URI to the Azure Storage blob container. Any offset from the root of the container to where the artifacts are located can be defined in the artifactRoot.
        """
        return pulumi.get(self, "sas_uri")

    @sas_uri.setter
    def sas_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "sas_uri", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The authentication type
        Expected value is 'Sas'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class ServiceUnitArtifactsArgs:
    def __init__(__self__, *,
                 parameters_artifact_source_relative_path: Optional[pulumi.Input[str]] = None,
                 parameters_uri: Optional[pulumi.Input[str]] = None,
                 template_artifact_source_relative_path: Optional[pulumi.Input[str]] = None,
                 template_uri: Optional[pulumi.Input[str]] = None):
        """
        Defines the artifacts of a service unit.
        :param pulumi.Input[str] parameters_artifact_source_relative_path: The path to the ARM parameters file relative to the artifact source.
        :param pulumi.Input[str] parameters_uri: The full URI of the ARM parameters file with the SAS token.
        :param pulumi.Input[str] template_artifact_source_relative_path: The path to the ARM template file relative to the artifact source.
        :param pulumi.Input[str] template_uri: The full URI of the ARM template file with the SAS token.
        """
        if parameters_artifact_source_relative_path is not None:
            pulumi.set(__self__, "parameters_artifact_source_relative_path", parameters_artifact_source_relative_path)
        if parameters_uri is not None:
            pulumi.set(__self__, "parameters_uri", parameters_uri)
        if template_artifact_source_relative_path is not None:
            pulumi.set(__self__, "template_artifact_source_relative_path", template_artifact_source_relative_path)
        if template_uri is not None:
            pulumi.set(__self__, "template_uri", template_uri)

    @property
    @pulumi.getter(name="parametersArtifactSourceRelativePath")
    def parameters_artifact_source_relative_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the ARM parameters file relative to the artifact source.
        """
        return pulumi.get(self, "parameters_artifact_source_relative_path")

    @parameters_artifact_source_relative_path.setter
    def parameters_artifact_source_relative_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameters_artifact_source_relative_path", value)

    @property
    @pulumi.getter(name="parametersUri")
    def parameters_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The full URI of the ARM parameters file with the SAS token.
        """
        return pulumi.get(self, "parameters_uri")

    @parameters_uri.setter
    def parameters_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameters_uri", value)

    @property
    @pulumi.getter(name="templateArtifactSourceRelativePath")
    def template_artifact_source_relative_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the ARM template file relative to the artifact source.
        """
        return pulumi.get(self, "template_artifact_source_relative_path")

    @template_artifact_source_relative_path.setter
    def template_artifact_source_relative_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_artifact_source_relative_path", value)

    @property
    @pulumi.getter(name="templateUri")
    def template_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The full URI of the ARM template file with the SAS token.
        """
        return pulumi.get(self, "template_uri")

    @template_uri.setter
    def template_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_uri", value)


@pulumi.input_type
class StepGroupArgs:
    def __init__(__self__, *,
                 deployment_target_id: pulumi.Input[str],
                 name: pulumi.Input[str],
                 depends_on_step_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 post_deployment_steps: Optional[pulumi.Input[Sequence[pulumi.Input['PrePostStepArgs']]]] = None,
                 pre_deployment_steps: Optional[pulumi.Input[Sequence[pulumi.Input['PrePostStepArgs']]]] = None):
        """
        The properties that define a Step group in a rollout.
        :param pulumi.Input[str] deployment_target_id: The resource Id of service unit to be deployed. The service unit should be from the service topology referenced in targetServiceTopologyId
        :param pulumi.Input[str] name: The name of the step group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] depends_on_step_groups: The list of step group names on which this step group depends on.
        :param pulumi.Input[Sequence[pulumi.Input['PrePostStepArgs']]] post_deployment_steps: The list of steps to be run after deploying the target.
        :param pulumi.Input[Sequence[pulumi.Input['PrePostStepArgs']]] pre_deployment_steps: The list of steps to be run before deploying the target.
        """
        pulumi.set(__self__, "deployment_target_id", deployment_target_id)
        pulumi.set(__self__, "name", name)
        if depends_on_step_groups is not None:
            pulumi.set(__self__, "depends_on_step_groups", depends_on_step_groups)
        if post_deployment_steps is not None:
            pulumi.set(__self__, "post_deployment_steps", post_deployment_steps)
        if pre_deployment_steps is not None:
            pulumi.set(__self__, "pre_deployment_steps", pre_deployment_steps)

    @property
    @pulumi.getter(name="deploymentTargetId")
    def deployment_target_id(self) -> pulumi.Input[str]:
        """
        The resource Id of service unit to be deployed. The service unit should be from the service topology referenced in targetServiceTopologyId
        """
        return pulumi.get(self, "deployment_target_id")

    @deployment_target_id.setter
    def deployment_target_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "deployment_target_id", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the step group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="dependsOnStepGroups")
    def depends_on_step_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of step group names on which this step group depends on.
        """
        return pulumi.get(self, "depends_on_step_groups")

    @depends_on_step_groups.setter
    def depends_on_step_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "depends_on_step_groups", value)

    @property
    @pulumi.getter(name="postDeploymentSteps")
    def post_deployment_steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrePostStepArgs']]]]:
        """
        The list of steps to be run after deploying the target.
        """
        return pulumi.get(self, "post_deployment_steps")

    @post_deployment_steps.setter
    def post_deployment_steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrePostStepArgs']]]]):
        pulumi.set(self, "post_deployment_steps", value)

    @property
    @pulumi.getter(name="preDeploymentSteps")
    def pre_deployment_steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrePostStepArgs']]]]:
        """
        The list of steps to be run before deploying the target.
        """
        return pulumi.get(self, "pre_deployment_steps")

    @pre_deployment_steps.setter
    def pre_deployment_steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrePostStepArgs']]]]):
        pulumi.set(self, "pre_deployment_steps", value)


@pulumi.input_type
class WaitStepAttributesArgs:
    def __init__(__self__, *,
                 duration: pulumi.Input[str]):
        """
        The parameters for the wait step.
        :param pulumi.Input[str] duration: The duration in ISO 8601 format of how long the wait should be.
        """
        pulumi.set(__self__, "duration", duration)

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Input[str]:
        """
        The duration in ISO 8601 format of how long the wait should be.
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: pulumi.Input[str]):
        pulumi.set(self, "duration", value)


@pulumi.input_type
class WaitStepPropertiesArgs:
    def __init__(__self__, *,
                 attributes: pulumi.Input['WaitStepAttributesArgs'],
                 step_type: pulumi.Input[str]):
        """
        Defines the properties of a Wait step.
        :param pulumi.Input['WaitStepAttributesArgs'] attributes: The Wait attributes
        :param pulumi.Input[str] step_type: The type of step.
               Expected value is 'Wait'.
        """
        pulumi.set(__self__, "attributes", attributes)
        pulumi.set(__self__, "step_type", 'Wait')

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Input['WaitStepAttributesArgs']:
        """
        The Wait attributes
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: pulumi.Input['WaitStepAttributesArgs']):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="stepType")
    def step_type(self) -> pulumi.Input[str]:
        """
        The type of step.
        Expected value is 'Wait'.
        """
        return pulumi.get(self, "step_type")

    @step_type.setter
    def step_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "step_type", value)


