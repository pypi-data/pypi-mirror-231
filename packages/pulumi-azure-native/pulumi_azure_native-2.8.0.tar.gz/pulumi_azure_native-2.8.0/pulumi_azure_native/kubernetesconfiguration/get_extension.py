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
    'GetExtensionResult',
    'AwaitableGetExtensionResult',
    'get_extension',
    'get_extension_output',
]

@pulumi.output_type
class GetExtensionResult:
    """
    The Extension object.
    """
    def __init__(__self__, aks_assigned_identity=None, auto_upgrade_minor_version=None, configuration_protected_settings=None, configuration_settings=None, current_version=None, custom_location_settings=None, error_info=None, extension_type=None, id=None, identity=None, is_system_extension=None, name=None, package_uri=None, plan=None, provisioning_state=None, release_train=None, scope=None, statuses=None, system_data=None, type=None, version=None):
        if aks_assigned_identity and not isinstance(aks_assigned_identity, dict):
            raise TypeError("Expected argument 'aks_assigned_identity' to be a dict")
        pulumi.set(__self__, "aks_assigned_identity", aks_assigned_identity)
        if auto_upgrade_minor_version and not isinstance(auto_upgrade_minor_version, bool):
            raise TypeError("Expected argument 'auto_upgrade_minor_version' to be a bool")
        pulumi.set(__self__, "auto_upgrade_minor_version", auto_upgrade_minor_version)
        if configuration_protected_settings and not isinstance(configuration_protected_settings, dict):
            raise TypeError("Expected argument 'configuration_protected_settings' to be a dict")
        pulumi.set(__self__, "configuration_protected_settings", configuration_protected_settings)
        if configuration_settings and not isinstance(configuration_settings, dict):
            raise TypeError("Expected argument 'configuration_settings' to be a dict")
        pulumi.set(__self__, "configuration_settings", configuration_settings)
        if current_version and not isinstance(current_version, str):
            raise TypeError("Expected argument 'current_version' to be a str")
        pulumi.set(__self__, "current_version", current_version)
        if custom_location_settings and not isinstance(custom_location_settings, dict):
            raise TypeError("Expected argument 'custom_location_settings' to be a dict")
        pulumi.set(__self__, "custom_location_settings", custom_location_settings)
        if error_info and not isinstance(error_info, dict):
            raise TypeError("Expected argument 'error_info' to be a dict")
        pulumi.set(__self__, "error_info", error_info)
        if extension_type and not isinstance(extension_type, str):
            raise TypeError("Expected argument 'extension_type' to be a str")
        pulumi.set(__self__, "extension_type", extension_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if is_system_extension and not isinstance(is_system_extension, bool):
            raise TypeError("Expected argument 'is_system_extension' to be a bool")
        pulumi.set(__self__, "is_system_extension", is_system_extension)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if package_uri and not isinstance(package_uri, str):
            raise TypeError("Expected argument 'package_uri' to be a str")
        pulumi.set(__self__, "package_uri", package_uri)
        if plan and not isinstance(plan, dict):
            raise TypeError("Expected argument 'plan' to be a dict")
        pulumi.set(__self__, "plan", plan)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if release_train and not isinstance(release_train, str):
            raise TypeError("Expected argument 'release_train' to be a str")
        pulumi.set(__self__, "release_train", release_train)
        if scope and not isinstance(scope, dict):
            raise TypeError("Expected argument 'scope' to be a dict")
        pulumi.set(__self__, "scope", scope)
        if statuses and not isinstance(statuses, list):
            raise TypeError("Expected argument 'statuses' to be a list")
        pulumi.set(__self__, "statuses", statuses)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="aksAssignedIdentity")
    def aks_assigned_identity(self) -> Optional['outputs.ExtensionResponseAksAssignedIdentity']:
        """
        Identity of the Extension resource in an AKS cluster
        """
        return pulumi.get(self, "aks_assigned_identity")

    @property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[bool]:
        """
        Flag to note if this extension participates in auto upgrade of minor version, or not.
        """
        return pulumi.get(self, "auto_upgrade_minor_version")

    @property
    @pulumi.getter(name="configurationProtectedSettings")
    def configuration_protected_settings(self) -> Optional[Mapping[str, str]]:
        """
        Configuration settings that are sensitive, as name-value pairs for configuring this extension.
        """
        return pulumi.get(self, "configuration_protected_settings")

    @property
    @pulumi.getter(name="configurationSettings")
    def configuration_settings(self) -> Optional[Mapping[str, str]]:
        """
        Configuration settings, as name-value pairs for configuring this extension.
        """
        return pulumi.get(self, "configuration_settings")

    @property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> str:
        """
        Currently installed version of the extension.
        """
        return pulumi.get(self, "current_version")

    @property
    @pulumi.getter(name="customLocationSettings")
    def custom_location_settings(self) -> Mapping[str, str]:
        """
        Custom Location settings properties.
        """
        return pulumi.get(self, "custom_location_settings")

    @property
    @pulumi.getter(name="errorInfo")
    def error_info(self) -> 'outputs.ErrorDetailResponse':
        """
        Error information from the Agent - e.g. errors during installation.
        """
        return pulumi.get(self, "error_info")

    @property
    @pulumi.getter(name="extensionType")
    def extension_type(self) -> Optional[str]:
        """
        Type of the Extension, of which this resource is an instance of.  It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the Extension publisher.
        """
        return pulumi.get(self, "extension_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        Identity of the Extension resource
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="isSystemExtension")
    def is_system_extension(self) -> bool:
        """
        Flag to note if this extension is a system extension
        """
        return pulumi.get(self, "is_system_extension")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageUri")
    def package_uri(self) -> str:
        """
        Uri of the Helm package
        """
        return pulumi.get(self, "package_uri")

    @property
    @pulumi.getter
    def plan(self) -> Optional['outputs.PlanResponse']:
        """
        The plan information.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Status of installation of this extension.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="releaseTrain")
    def release_train(self) -> Optional[str]:
        """
        ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
        """
        return pulumi.get(self, "release_train")

    @property
    @pulumi.getter
    def scope(self) -> Optional['outputs.ScopeResponse']:
        """
        Scope at which the extension is installed.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence['outputs.ExtensionStatusResponse']]:
        """
        Status from this extension.
        """
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        User-specified version of the extension for this extension to 'pin'. To use 'version', autoUpgradeMinorVersion must be 'false'.
        """
        return pulumi.get(self, "version")


class AwaitableGetExtensionResult(GetExtensionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExtensionResult(
            aks_assigned_identity=self.aks_assigned_identity,
            auto_upgrade_minor_version=self.auto_upgrade_minor_version,
            configuration_protected_settings=self.configuration_protected_settings,
            configuration_settings=self.configuration_settings,
            current_version=self.current_version,
            custom_location_settings=self.custom_location_settings,
            error_info=self.error_info,
            extension_type=self.extension_type,
            id=self.id,
            identity=self.identity,
            is_system_extension=self.is_system_extension,
            name=self.name,
            package_uri=self.package_uri,
            plan=self.plan,
            provisioning_state=self.provisioning_state,
            release_train=self.release_train,
            scope=self.scope,
            statuses=self.statuses,
            system_data=self.system_data,
            type=self.type,
            version=self.version)


def get_extension(cluster_name: Optional[str] = None,
                  cluster_resource_name: Optional[str] = None,
                  cluster_rp: Optional[str] = None,
                  extension_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExtensionResult:
    """
    Gets Kubernetes Cluster Extension.
    Azure REST API version: 2023-05-01.


    :param str cluster_name: The name of the kubernetes cluster.
    :param str cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters, connectedClusters, provisionedClusters.
    :param str cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService, Microsoft.Kubernetes, Microsoft.HybridContainerService.
    :param str extension_name: Name of the Extension.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['clusterResourceName'] = cluster_resource_name
    __args__['clusterRp'] = cluster_rp
    __args__['extensionName'] = extension_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kubernetesconfiguration:getExtension', __args__, opts=opts, typ=GetExtensionResult).value

    return AwaitableGetExtensionResult(
        aks_assigned_identity=pulumi.get(__ret__, 'aks_assigned_identity'),
        auto_upgrade_minor_version=pulumi.get(__ret__, 'auto_upgrade_minor_version'),
        configuration_protected_settings=pulumi.get(__ret__, 'configuration_protected_settings'),
        configuration_settings=pulumi.get(__ret__, 'configuration_settings'),
        current_version=pulumi.get(__ret__, 'current_version'),
        custom_location_settings=pulumi.get(__ret__, 'custom_location_settings'),
        error_info=pulumi.get(__ret__, 'error_info'),
        extension_type=pulumi.get(__ret__, 'extension_type'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        is_system_extension=pulumi.get(__ret__, 'is_system_extension'),
        name=pulumi.get(__ret__, 'name'),
        package_uri=pulumi.get(__ret__, 'package_uri'),
        plan=pulumi.get(__ret__, 'plan'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        release_train=pulumi.get(__ret__, 'release_train'),
        scope=pulumi.get(__ret__, 'scope'),
        statuses=pulumi.get(__ret__, 'statuses'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_extension)
def get_extension_output(cluster_name: Optional[pulumi.Input[str]] = None,
                         cluster_resource_name: Optional[pulumi.Input[str]] = None,
                         cluster_rp: Optional[pulumi.Input[str]] = None,
                         extension_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExtensionResult]:
    """
    Gets Kubernetes Cluster Extension.
    Azure REST API version: 2023-05-01.


    :param str cluster_name: The name of the kubernetes cluster.
    :param str cluster_resource_name: The Kubernetes cluster resource name - i.e. managedClusters, connectedClusters, provisionedClusters.
    :param str cluster_rp: The Kubernetes cluster RP - i.e. Microsoft.ContainerService, Microsoft.Kubernetes, Microsoft.HybridContainerService.
    :param str extension_name: Name of the Extension.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
