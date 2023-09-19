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
    'ACRArgs',
    'DeploymentPropertiesArgs',
    'GitHubWorkflowProfileOidcCredentialsArgs',
    'WorkflowRunArgs',
]

@pulumi.input_type
class ACRArgs:
    def __init__(__self__, *,
                 acr_registry_name: Optional[pulumi.Input[str]] = None,
                 acr_repository_name: Optional[pulumi.Input[str]] = None,
                 acr_resource_group: Optional[pulumi.Input[str]] = None,
                 acr_subscription_id: Optional[pulumi.Input[str]] = None):
        """
        Information on the azure container registry
        :param pulumi.Input[str] acr_registry_name: ACR registry
        :param pulumi.Input[str] acr_repository_name: ACR repository
        :param pulumi.Input[str] acr_resource_group: ACR resource group
        :param pulumi.Input[str] acr_subscription_id: ACR subscription id
        """
        if acr_registry_name is not None:
            pulumi.set(__self__, "acr_registry_name", acr_registry_name)
        if acr_repository_name is not None:
            pulumi.set(__self__, "acr_repository_name", acr_repository_name)
        if acr_resource_group is not None:
            pulumi.set(__self__, "acr_resource_group", acr_resource_group)
        if acr_subscription_id is not None:
            pulumi.set(__self__, "acr_subscription_id", acr_subscription_id)

    @property
    @pulumi.getter(name="acrRegistryName")
    def acr_registry_name(self) -> Optional[pulumi.Input[str]]:
        """
        ACR registry
        """
        return pulumi.get(self, "acr_registry_name")

    @acr_registry_name.setter
    def acr_registry_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acr_registry_name", value)

    @property
    @pulumi.getter(name="acrRepositoryName")
    def acr_repository_name(self) -> Optional[pulumi.Input[str]]:
        """
        ACR repository
        """
        return pulumi.get(self, "acr_repository_name")

    @acr_repository_name.setter
    def acr_repository_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acr_repository_name", value)

    @property
    @pulumi.getter(name="acrResourceGroup")
    def acr_resource_group(self) -> Optional[pulumi.Input[str]]:
        """
        ACR resource group
        """
        return pulumi.get(self, "acr_resource_group")

    @acr_resource_group.setter
    def acr_resource_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acr_resource_group", value)

    @property
    @pulumi.getter(name="acrSubscriptionId")
    def acr_subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        ACR subscription id
        """
        return pulumi.get(self, "acr_subscription_id")

    @acr_subscription_id.setter
    def acr_subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acr_subscription_id", value)


@pulumi.input_type
class DeploymentPropertiesArgs:
    def __init__(__self__, *,
                 helm_chart_path: Optional[pulumi.Input[str]] = None,
                 helm_values: Optional[pulumi.Input[str]] = None,
                 kube_manifest_locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 manifest_type: Optional[pulumi.Input[Union[str, 'ManifestType']]] = None,
                 overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] helm_chart_path: Helm chart directory path in repository.
        :param pulumi.Input[str] helm_values: Helm Values.yaml file location in repository.
        :param pulumi.Input[Union[str, 'ManifestType']] manifest_type: Determines the type of manifests within the repository.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] overrides: Manifest override values.
        """
        if helm_chart_path is not None:
            pulumi.set(__self__, "helm_chart_path", helm_chart_path)
        if helm_values is not None:
            pulumi.set(__self__, "helm_values", helm_values)
        if kube_manifest_locations is not None:
            pulumi.set(__self__, "kube_manifest_locations", kube_manifest_locations)
        if manifest_type is not None:
            pulumi.set(__self__, "manifest_type", manifest_type)
        if overrides is not None:
            pulumi.set(__self__, "overrides", overrides)

    @property
    @pulumi.getter(name="helmChartPath")
    def helm_chart_path(self) -> Optional[pulumi.Input[str]]:
        """
        Helm chart directory path in repository.
        """
        return pulumi.get(self, "helm_chart_path")

    @helm_chart_path.setter
    def helm_chart_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "helm_chart_path", value)

    @property
    @pulumi.getter(name="helmValues")
    def helm_values(self) -> Optional[pulumi.Input[str]]:
        """
        Helm Values.yaml file location in repository.
        """
        return pulumi.get(self, "helm_values")

    @helm_values.setter
    def helm_values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "helm_values", value)

    @property
    @pulumi.getter(name="kubeManifestLocations")
    def kube_manifest_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "kube_manifest_locations")

    @kube_manifest_locations.setter
    def kube_manifest_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "kube_manifest_locations", value)

    @property
    @pulumi.getter(name="manifestType")
    def manifest_type(self) -> Optional[pulumi.Input[Union[str, 'ManifestType']]]:
        """
        Determines the type of manifests within the repository.
        """
        return pulumi.get(self, "manifest_type")

    @manifest_type.setter
    def manifest_type(self, value: Optional[pulumi.Input[Union[str, 'ManifestType']]]):
        pulumi.set(self, "manifest_type", value)

    @property
    @pulumi.getter
    def overrides(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Manifest override values.
        """
        return pulumi.get(self, "overrides")

    @overrides.setter
    def overrides(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "overrides", value)


@pulumi.input_type
class GitHubWorkflowProfileOidcCredentialsArgs:
    def __init__(__self__, *,
                 azure_client_id: Optional[pulumi.Input[str]] = None,
                 azure_tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The fields needed for OIDC with GitHub.
        :param pulumi.Input[str] azure_client_id: Azure Application Client ID
        :param pulumi.Input[str] azure_tenant_id: Azure Directory (tenant) ID
        """
        if azure_client_id is not None:
            pulumi.set(__self__, "azure_client_id", azure_client_id)
        if azure_tenant_id is not None:
            pulumi.set(__self__, "azure_tenant_id", azure_tenant_id)

    @property
    @pulumi.getter(name="azureClientId")
    def azure_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        Azure Application Client ID
        """
        return pulumi.get(self, "azure_client_id")

    @azure_client_id.setter
    def azure_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_client_id", value)

    @property
    @pulumi.getter(name="azureTenantId")
    def azure_tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Azure Directory (tenant) ID
        """
        return pulumi.get(self, "azure_tenant_id")

    @azure_tenant_id.setter
    def azure_tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_tenant_id", value)


@pulumi.input_type
class WorkflowRunArgs:
    def __init__(__self__, *,
                 workflow_run_status: Optional[pulumi.Input[Union[str, 'WorkflowRunStatus']]] = None):
        """
        :param pulumi.Input[Union[str, 'WorkflowRunStatus']] workflow_run_status: Describes the status of the workflow run
        """
        if workflow_run_status is not None:
            pulumi.set(__self__, "workflow_run_status", workflow_run_status)

    @property
    @pulumi.getter(name="workflowRunStatus")
    def workflow_run_status(self) -> Optional[pulumi.Input[Union[str, 'WorkflowRunStatus']]]:
        """
        Describes the status of the workflow run
        """
        return pulumi.get(self, "workflow_run_status")

    @workflow_run_status.setter
    def workflow_run_status(self, value: Optional[pulumi.Input[Union[str, 'WorkflowRunStatus']]]):
        pulumi.set(self, "workflow_run_status", value)


