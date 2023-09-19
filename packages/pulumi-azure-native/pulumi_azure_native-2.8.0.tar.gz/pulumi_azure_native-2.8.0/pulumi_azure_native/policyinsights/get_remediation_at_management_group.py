# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetRemediationAtManagementGroupResult',
    'AwaitableGetRemediationAtManagementGroupResult',
    'get_remediation_at_management_group',
    'get_remediation_at_management_group_output',
]

@pulumi.output_type
class GetRemediationAtManagementGroupResult:
    """
    The remediation definition.
    """
    def __init__(__self__, correlation_id=None, created_on=None, deployment_status=None, failure_threshold=None, filters=None, id=None, last_updated_on=None, name=None, parallel_deployments=None, policy_assignment_id=None, policy_definition_reference_id=None, provisioning_state=None, resource_count=None, resource_discovery_mode=None, status_message=None, system_data=None, type=None):
        if correlation_id and not isinstance(correlation_id, str):
            raise TypeError("Expected argument 'correlation_id' to be a str")
        pulumi.set(__self__, "correlation_id", correlation_id)
        if created_on and not isinstance(created_on, str):
            raise TypeError("Expected argument 'created_on' to be a str")
        pulumi.set(__self__, "created_on", created_on)
        if deployment_status and not isinstance(deployment_status, dict):
            raise TypeError("Expected argument 'deployment_status' to be a dict")
        pulumi.set(__self__, "deployment_status", deployment_status)
        if failure_threshold and not isinstance(failure_threshold, dict):
            raise TypeError("Expected argument 'failure_threshold' to be a dict")
        pulumi.set(__self__, "failure_threshold", failure_threshold)
        if filters and not isinstance(filters, dict):
            raise TypeError("Expected argument 'filters' to be a dict")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_updated_on and not isinstance(last_updated_on, str):
            raise TypeError("Expected argument 'last_updated_on' to be a str")
        pulumi.set(__self__, "last_updated_on", last_updated_on)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parallel_deployments and not isinstance(parallel_deployments, int):
            raise TypeError("Expected argument 'parallel_deployments' to be a int")
        pulumi.set(__self__, "parallel_deployments", parallel_deployments)
        if policy_assignment_id and not isinstance(policy_assignment_id, str):
            raise TypeError("Expected argument 'policy_assignment_id' to be a str")
        pulumi.set(__self__, "policy_assignment_id", policy_assignment_id)
        if policy_definition_reference_id and not isinstance(policy_definition_reference_id, str):
            raise TypeError("Expected argument 'policy_definition_reference_id' to be a str")
        pulumi.set(__self__, "policy_definition_reference_id", policy_definition_reference_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_count and not isinstance(resource_count, int):
            raise TypeError("Expected argument 'resource_count' to be a int")
        pulumi.set(__self__, "resource_count", resource_count)
        if resource_discovery_mode and not isinstance(resource_discovery_mode, str):
            raise TypeError("Expected argument 'resource_discovery_mode' to be a str")
        pulumi.set(__self__, "resource_discovery_mode", resource_discovery_mode)
        if status_message and not isinstance(status_message, str):
            raise TypeError("Expected argument 'status_message' to be a str")
        pulumi.set(__self__, "status_message", status_message)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> str:
        """
        The remediation correlation Id. Can be used to find events related to the remediation in the activity log.
        """
        return pulumi.get(self, "correlation_id")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> str:
        """
        The time at which the remediation was created.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> 'outputs.RemediationDeploymentSummaryResponse':
        """
        The deployment status summary for all deployments created by the remediation.
        """
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional['outputs.RemediationPropertiesResponseFailureThreshold']:
        """
        The remediation failure threshold settings
        """
        return pulumi.get(self, "failure_threshold")

    @property
    @pulumi.getter
    def filters(self) -> Optional['outputs.RemediationFiltersResponse']:
        """
        The filters that will be applied to determine which resources to remediate.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the remediation.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastUpdatedOn")
    def last_updated_on(self) -> str:
        """
        The time at which the remediation was last updated.
        """
        return pulumi.get(self, "last_updated_on")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the remediation.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parallelDeployments")
    def parallel_deployments(self) -> Optional[int]:
        """
        Determines how many resources to remediate at any given time. Can be used to increase or reduce the pace of the remediation. If not provided, the default parallel deployments value is used.
        """
        return pulumi.get(self, "parallel_deployments")

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> Optional[str]:
        """
        The resource ID of the policy assignment that should be remediated.
        """
        return pulumi.get(self, "policy_assignment_id")

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[str]:
        """
        The policy definition reference ID of the individual definition that should be remediated. Required when the policy assignment being remediated assigns a policy set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the remediation. This refers to the entire remediation task, not individual deployments. Allowed values are Evaluating, Canceled, Cancelling, Failed, Complete, or Succeeded.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceCount")
    def resource_count(self) -> Optional[int]:
        """
        Determines the max number of resources that can be remediated by the remediation job. If not provided, the default resource count is used.
        """
        return pulumi.get(self, "resource_count")

    @property
    @pulumi.getter(name="resourceDiscoveryMode")
    def resource_discovery_mode(self) -> Optional[str]:
        """
        The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified.
        """
        return pulumi.get(self, "resource_discovery_mode")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> str:
        """
        The remediation status message. Provides additional details regarding the state of the remediation.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the remediation.
        """
        return pulumi.get(self, "type")


class AwaitableGetRemediationAtManagementGroupResult(GetRemediationAtManagementGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRemediationAtManagementGroupResult(
            correlation_id=self.correlation_id,
            created_on=self.created_on,
            deployment_status=self.deployment_status,
            failure_threshold=self.failure_threshold,
            filters=self.filters,
            id=self.id,
            last_updated_on=self.last_updated_on,
            name=self.name,
            parallel_deployments=self.parallel_deployments,
            policy_assignment_id=self.policy_assignment_id,
            policy_definition_reference_id=self.policy_definition_reference_id,
            provisioning_state=self.provisioning_state,
            resource_count=self.resource_count,
            resource_discovery_mode=self.resource_discovery_mode,
            status_message=self.status_message,
            system_data=self.system_data,
            type=self.type)


def get_remediation_at_management_group(management_group_id: Optional[str] = None,
                                        management_groups_namespace: Optional[str] = None,
                                        remediation_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRemediationAtManagementGroupResult:
    """
    Gets an existing remediation at management group scope.
    Azure REST API version: 2021-10-01.


    :param str management_group_id: Management group ID.
    :param str management_groups_namespace: The namespace for Microsoft Management RP; only "Microsoft.Management" is allowed.
    :param str remediation_name: The name of the remediation.
    """
    __args__ = dict()
    __args__['managementGroupId'] = management_group_id
    __args__['managementGroupsNamespace'] = management_groups_namespace
    __args__['remediationName'] = remediation_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:policyinsights:getRemediationAtManagementGroup', __args__, opts=opts, typ=GetRemediationAtManagementGroupResult).value

    return AwaitableGetRemediationAtManagementGroupResult(
        correlation_id=pulumi.get(__ret__, 'correlation_id'),
        created_on=pulumi.get(__ret__, 'created_on'),
        deployment_status=pulumi.get(__ret__, 'deployment_status'),
        failure_threshold=pulumi.get(__ret__, 'failure_threshold'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        last_updated_on=pulumi.get(__ret__, 'last_updated_on'),
        name=pulumi.get(__ret__, 'name'),
        parallel_deployments=pulumi.get(__ret__, 'parallel_deployments'),
        policy_assignment_id=pulumi.get(__ret__, 'policy_assignment_id'),
        policy_definition_reference_id=pulumi.get(__ret__, 'policy_definition_reference_id'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_count=pulumi.get(__ret__, 'resource_count'),
        resource_discovery_mode=pulumi.get(__ret__, 'resource_discovery_mode'),
        status_message=pulumi.get(__ret__, 'status_message'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_remediation_at_management_group)
def get_remediation_at_management_group_output(management_group_id: Optional[pulumi.Input[str]] = None,
                                               management_groups_namespace: Optional[pulumi.Input[str]] = None,
                                               remediation_name: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRemediationAtManagementGroupResult]:
    """
    Gets an existing remediation at management group scope.
    Azure REST API version: 2021-10-01.


    :param str management_group_id: Management group ID.
    :param str management_groups_namespace: The namespace for Microsoft Management RP; only "Microsoft.Management" is allowed.
    :param str remediation_name: The name of the remediation.
    """
    ...
