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
    'ACRResponse',
    'DeploymentPropertiesResponse',
    'GitHubWorkflowProfileResponseOidcCredentials',
    'SystemDataResponse',
    'WorkflowRunResponse',
]

@pulumi.output_type
class ACRResponse(dict):
    """
    Information on the azure container registry
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "acrRegistryName":
            suggest = "acr_registry_name"
        elif key == "acrRepositoryName":
            suggest = "acr_repository_name"
        elif key == "acrResourceGroup":
            suggest = "acr_resource_group"
        elif key == "acrSubscriptionId":
            suggest = "acr_subscription_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ACRResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ACRResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ACRResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 acr_registry_name: Optional[str] = None,
                 acr_repository_name: Optional[str] = None,
                 acr_resource_group: Optional[str] = None,
                 acr_subscription_id: Optional[str] = None):
        """
        Information on the azure container registry
        :param str acr_registry_name: ACR registry
        :param str acr_repository_name: ACR repository
        :param str acr_resource_group: ACR resource group
        :param str acr_subscription_id: ACR subscription id
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
    def acr_registry_name(self) -> Optional[str]:
        """
        ACR registry
        """
        return pulumi.get(self, "acr_registry_name")

    @property
    @pulumi.getter(name="acrRepositoryName")
    def acr_repository_name(self) -> Optional[str]:
        """
        ACR repository
        """
        return pulumi.get(self, "acr_repository_name")

    @property
    @pulumi.getter(name="acrResourceGroup")
    def acr_resource_group(self) -> Optional[str]:
        """
        ACR resource group
        """
        return pulumi.get(self, "acr_resource_group")

    @property
    @pulumi.getter(name="acrSubscriptionId")
    def acr_subscription_id(self) -> Optional[str]:
        """
        ACR subscription id
        """
        return pulumi.get(self, "acr_subscription_id")


@pulumi.output_type
class DeploymentPropertiesResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "helmChartPath":
            suggest = "helm_chart_path"
        elif key == "helmValues":
            suggest = "helm_values"
        elif key == "kubeManifestLocations":
            suggest = "kube_manifest_locations"
        elif key == "manifestType":
            suggest = "manifest_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DeploymentPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DeploymentPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DeploymentPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 helm_chart_path: Optional[str] = None,
                 helm_values: Optional[str] = None,
                 kube_manifest_locations: Optional[Sequence[str]] = None,
                 manifest_type: Optional[str] = None,
                 overrides: Optional[Mapping[str, str]] = None):
        """
        :param str helm_chart_path: Helm chart directory path in repository.
        :param str helm_values: Helm Values.yaml file location in repository.
        :param str manifest_type: Determines the type of manifests within the repository.
        :param Mapping[str, str] overrides: Manifest override values.
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
    def helm_chart_path(self) -> Optional[str]:
        """
        Helm chart directory path in repository.
        """
        return pulumi.get(self, "helm_chart_path")

    @property
    @pulumi.getter(name="helmValues")
    def helm_values(self) -> Optional[str]:
        """
        Helm Values.yaml file location in repository.
        """
        return pulumi.get(self, "helm_values")

    @property
    @pulumi.getter(name="kubeManifestLocations")
    def kube_manifest_locations(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "kube_manifest_locations")

    @property
    @pulumi.getter(name="manifestType")
    def manifest_type(self) -> Optional[str]:
        """
        Determines the type of manifests within the repository.
        """
        return pulumi.get(self, "manifest_type")

    @property
    @pulumi.getter
    def overrides(self) -> Optional[Mapping[str, str]]:
        """
        Manifest override values.
        """
        return pulumi.get(self, "overrides")


@pulumi.output_type
class GitHubWorkflowProfileResponseOidcCredentials(dict):
    """
    The fields needed for OIDC with GitHub.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "azureClientId":
            suggest = "azure_client_id"
        elif key == "azureTenantId":
            suggest = "azure_tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GitHubWorkflowProfileResponseOidcCredentials. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GitHubWorkflowProfileResponseOidcCredentials.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GitHubWorkflowProfileResponseOidcCredentials.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 azure_client_id: Optional[str] = None,
                 azure_tenant_id: Optional[str] = None):
        """
        The fields needed for OIDC with GitHub.
        :param str azure_client_id: Azure Application Client ID
        :param str azure_tenant_id: Azure Directory (tenant) ID
        """
        if azure_client_id is not None:
            pulumi.set(__self__, "azure_client_id", azure_client_id)
        if azure_tenant_id is not None:
            pulumi.set(__self__, "azure_tenant_id", azure_tenant_id)

    @property
    @pulumi.getter(name="azureClientId")
    def azure_client_id(self) -> Optional[str]:
        """
        Azure Application Client ID
        """
        return pulumi.get(self, "azure_client_id")

    @property
    @pulumi.getter(name="azureTenantId")
    def azure_tenant_id(self) -> Optional[str]:
        """
        Azure Directory (tenant) ID
        """
        return pulumi.get(self, "azure_tenant_id")


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
class WorkflowRunResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lastRunAt":
            suggest = "last_run_at"
        elif key == "workflowRunURL":
            suggest = "workflow_run_url"
        elif key == "workflowRunStatus":
            suggest = "workflow_run_status"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkflowRunResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkflowRunResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkflowRunResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 last_run_at: str,
                 succeeded: bool,
                 workflow_run_url: str,
                 workflow_run_status: Optional[str] = None):
        """
        :param str last_run_at: The timestamp of the last workflow run.
        :param bool succeeded: Describes if the workflow run succeeded.
        :param str workflow_run_url: URL to the run of the workflow.
        :param str workflow_run_status: Describes the status of the workflow run
        """
        pulumi.set(__self__, "last_run_at", last_run_at)
        pulumi.set(__self__, "succeeded", succeeded)
        pulumi.set(__self__, "workflow_run_url", workflow_run_url)
        if workflow_run_status is not None:
            pulumi.set(__self__, "workflow_run_status", workflow_run_status)

    @property
    @pulumi.getter(name="lastRunAt")
    def last_run_at(self) -> str:
        """
        The timestamp of the last workflow run.
        """
        return pulumi.get(self, "last_run_at")

    @property
    @pulumi.getter
    def succeeded(self) -> bool:
        """
        Describes if the workflow run succeeded.
        """
        return pulumi.get(self, "succeeded")

    @property
    @pulumi.getter(name="workflowRunURL")
    def workflow_run_url(self) -> str:
        """
        URL to the run of the workflow.
        """
        return pulumi.get(self, "workflow_run_url")

    @property
    @pulumi.getter(name="workflowRunStatus")
    def workflow_run_status(self) -> Optional[str]:
        """
        Describes the status of the workflow run
        """
        return pulumi.get(self, "workflow_run_status")


