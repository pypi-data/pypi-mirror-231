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

__all__ = [
    'ErrorAdditionalInfoResponse',
    'ErrorDetailResponse',
    'ExtensionResponseAksAssignedIdentity',
    'ExtensionStatusResponse',
    'IdentityResponse',
    'KubernetesConfigurationPrivateLinkScopePropertiesResponse',
    'PlanResponse',
    'PrivateEndpointConnectionResponse',
    'PrivateEndpointResponse',
    'PrivateLinkServiceConnectionStateResponse',
    'ScopeClusterResponse',
    'ScopeNamespaceResponse',
    'ScopeResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    """
    The resource management error additional info.
    """
    def __init__(__self__, *,
                 info: Any,
                 type: str):
        """
        The resource management error additional info.
        :param Any info: The additional info.
        :param str type: The additional info type.
        """
        pulumi.set(__self__, "info", info)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def info(self) -> Any:
        """
        The additional info.
        """
        return pulumi.get(self, "info")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The additional info type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ErrorDetailResponse(dict):
    """
    The error detail.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "additionalInfo":
            suggest = "additional_info"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ErrorDetailResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ErrorDetailResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ErrorDetailResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 additional_info: Sequence['outputs.ErrorAdditionalInfoResponse'],
                 code: str,
                 details: Sequence['outputs.ErrorDetailResponse'],
                 message: str,
                 target: str):
        """
        The error detail.
        :param Sequence['ErrorAdditionalInfoResponse'] additional_info: The error additional info.
        :param str code: The error code.
        :param Sequence['ErrorDetailResponse'] details: The error details.
        :param str message: The error message.
        :param str target: The error target.
        """
        pulumi.set(__self__, "additional_info", additional_info)
        pulumi.set(__self__, "code", code)
        pulumi.set(__self__, "details", details)
        pulumi.set(__self__, "message", message)
        pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence['outputs.ErrorAdditionalInfoResponse']:
        """
        The error additional info.
        """
        return pulumi.get(self, "additional_info")

    @property
    @pulumi.getter
    def code(self) -> str:
        """
        The error code.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def details(self) -> Sequence['outputs.ErrorDetailResponse']:
        """
        The error details.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        The error message.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def target(self) -> str:
        """
        The error target.
        """
        return pulumi.get(self, "target")


@pulumi.output_type
class ExtensionResponseAksAssignedIdentity(dict):
    """
    Identity of the Extension resource in an AKS cluster
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExtensionResponseAksAssignedIdentity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExtensionResponseAksAssignedIdentity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExtensionResponseAksAssignedIdentity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        Identity of the Extension resource in an AKS cluster
        :param str principal_id: The principal ID of resource identity.
        :param str tenant_id: The tenant ID of resource.
        :param str type: The identity type.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of resource identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of resource.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ExtensionStatusResponse(dict):
    """
    Status from the extension.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "displayStatus":
            suggest = "display_status"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExtensionStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExtensionStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExtensionStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 code: Optional[str] = None,
                 display_status: Optional[str] = None,
                 level: Optional[str] = None,
                 message: Optional[str] = None,
                 time: Optional[str] = None):
        """
        Status from the extension.
        :param str code: Status code provided by the Extension
        :param str display_status: Short description of status of the extension.
        :param str level: Level of the status.
        :param str message: Detailed message of the status from the Extension.
        :param str time: DateLiteral (per ISO8601) noting the time of installation status.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if display_status is not None:
            pulumi.set(__self__, "display_status", display_status)
        if level is None:
            level = 'Information'
        if level is not None:
            pulumi.set(__self__, "level", level)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if time is not None:
            pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter
    def code(self) -> Optional[str]:
        """
        Status code provided by the Extension
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter(name="displayStatus")
    def display_status(self) -> Optional[str]:
        """
        Short description of status of the extension.
        """
        return pulumi.get(self, "display_status")

    @property
    @pulumi.getter
    def level(self) -> Optional[str]:
        """
        Level of the status.
        """
        return pulumi.get(self, "level")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        Detailed message of the status from the Extension.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def time(self) -> Optional[str]:
        """
        DateLiteral (per ISO8601) noting the time of installation status.
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class IdentityResponse(dict):
    """
    Identity for the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        Identity for the resource.
        :param str principal_id: The principal ID of resource identity.
        :param str tenant_id: The tenant ID of resource.
        :param str type: The identity type.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of resource identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of resource.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class KubernetesConfigurationPrivateLinkScopePropertiesResponse(dict):
    """
    Properties that define a Azure Arc PrivateLinkScope resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clusterResourceId":
            suggest = "cluster_resource_id"
        elif key == "privateEndpointConnections":
            suggest = "private_endpoint_connections"
        elif key == "privateLinkScopeId":
            suggest = "private_link_scope_id"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "publicNetworkAccess":
            suggest = "public_network_access"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in KubernetesConfigurationPrivateLinkScopePropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        KubernetesConfigurationPrivateLinkScopePropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        KubernetesConfigurationPrivateLinkScopePropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cluster_resource_id: str,
                 private_endpoint_connections: Sequence['outputs.PrivateEndpointConnectionResponse'],
                 private_link_scope_id: str,
                 provisioning_state: str,
                 public_network_access: Optional[str] = None):
        """
        Properties that define a Azure Arc PrivateLinkScope resource.
        :param str cluster_resource_id: Managed Cluster ARM ID for the private link scope  (Required)
        :param Sequence['PrivateEndpointConnectionResponse'] private_endpoint_connections: The collection of associated Private Endpoint Connections.
        :param str private_link_scope_id: The Guid id of the private link scope.
        :param str provisioning_state: Current state of this PrivateLinkScope: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Provisioning ,Succeeded, Canceled and Failed.
        :param str public_network_access: Indicates whether machines associated with the private link scope can also use public Azure Arc service endpoints.
        """
        pulumi.set(__self__, "cluster_resource_id", cluster_resource_id)
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        pulumi.set(__self__, "private_link_scope_id", private_link_scope_id)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)

    @property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> str:
        """
        Managed Cluster ARM ID for the private link scope  (Required)
        """
        return pulumi.get(self, "cluster_resource_id")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        The collection of associated Private Endpoint Connections.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="privateLinkScopeId")
    def private_link_scope_id(self) -> str:
        """
        The Guid id of the private link scope.
        """
        return pulumi.get(self, "private_link_scope_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Current state of this PrivateLinkScope: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Provisioning ,Succeeded, Canceled and Failed.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Indicates whether machines associated with the private link scope can also use public Azure Arc service endpoints.
        """
        return pulumi.get(self, "public_network_access")


@pulumi.output_type
class PlanResponse(dict):
    """
    Plan for the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "promotionCode":
            suggest = "promotion_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PlanResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PlanResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PlanResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 product: str,
                 publisher: str,
                 promotion_code: Optional[str] = None,
                 version: Optional[str] = None):
        """
        Plan for the resource.
        :param str name: A user defined name of the 3rd Party Artifact that is being procured.
        :param str product: The 3rd Party artifact that is being procured. E.g. NewRelic. Product maps to the OfferID specified for the artifact at the time of Data Market onboarding. 
        :param str publisher: The publisher of the 3rd Party Artifact that is being bought. E.g. NewRelic
        :param str promotion_code: A publisher provided promotion code as provisioned in Data Market for the said product/artifact.
        :param str version: The version of the desired product/artifact.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "product", product)
        pulumi.set(__self__, "publisher", publisher)
        if promotion_code is not None:
            pulumi.set(__self__, "promotion_code", promotion_code)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A user defined name of the 3rd Party Artifact that is being procured.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def product(self) -> str:
        """
        The 3rd Party artifact that is being procured. E.g. NewRelic. Product maps to the OfferID specified for the artifact at the time of Data Market onboarding. 
        """
        return pulumi.get(self, "product")

    @property
    @pulumi.getter
    def publisher(self) -> str:
        """
        The publisher of the 3rd Party Artifact that is being bought. E.g. NewRelic
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[str]:
        """
        A publisher provided promotion code as provisioned in Data Market for the said product/artifact.
        """
        return pulumi.get(self, "promotion_code")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version of the desired product/artifact.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    """
    The Private Endpoint Connection resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateLinkServiceConnectionState":
            suggest = "private_link_service_connection_state"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "systemData":
            suggest = "system_data"
        elif key == "privateEndpoint":
            suggest = "private_endpoint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 name: str,
                 private_link_service_connection_state: 'outputs.PrivateLinkServiceConnectionStateResponse',
                 provisioning_state: str,
                 system_data: 'outputs.SystemDataResponse',
                 type: str,
                 private_endpoint: Optional['outputs.PrivateEndpointResponse'] = None):
        """
        The Private Endpoint Connection resource.
        :param str id: Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        :param str name: The name of the resource
        :param 'PrivateLinkServiceConnectionStateResponse' private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param str provisioning_state: The provisioning state of the private endpoint connection resource.
        :param 'SystemDataResponse' system_data: Azure Resource Manager metadata containing createdBy and modifiedBy information.
        :param str type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        :param 'PrivateEndpointResponse' private_endpoint: The resource of private end point.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "system_data", system_data)
        pulumi.set(__self__, "type", type)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> 'outputs.PrivateLinkServiceConnectionStateResponse':
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.PrivateEndpointResponse']:
        """
        The resource of private end point.
        """
        return pulumi.get(self, "private_endpoint")


@pulumi.output_type
class PrivateEndpointResponse(dict):
    """
    The Private Endpoint resource.
    """
    def __init__(__self__, *,
                 id: str):
        """
        The Private Endpoint resource.
        :param str id: The ARM identifier for Private Endpoint
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM identifier for Private Endpoint
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    """
    A collection of information about the state of the connection between service consumer and provider.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionsRequired":
            suggest = "actions_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateLinkServiceConnectionStateResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions_required: Optional[str] = None,
                 description: Optional[str] = None,
                 status: Optional[str] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param str actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param str description: The reason for approval/rejection of the connection.
        :param str status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[str]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class ScopeClusterResponse(dict):
    """
    Specifies that the scope of the extension is Cluster
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "releaseNamespace":
            suggest = "release_namespace"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScopeClusterResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScopeClusterResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScopeClusterResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 release_namespace: Optional[str] = None):
        """
        Specifies that the scope of the extension is Cluster
        :param str release_namespace: Namespace where the extension Release must be placed, for a Cluster scoped extension.  If this namespace does not exist, it will be created
        """
        if release_namespace is not None:
            pulumi.set(__self__, "release_namespace", release_namespace)

    @property
    @pulumi.getter(name="releaseNamespace")
    def release_namespace(self) -> Optional[str]:
        """
        Namespace where the extension Release must be placed, for a Cluster scoped extension.  If this namespace does not exist, it will be created
        """
        return pulumi.get(self, "release_namespace")


@pulumi.output_type
class ScopeNamespaceResponse(dict):
    """
    Specifies that the scope of the extension is Namespace
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetNamespace":
            suggest = "target_namespace"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScopeNamespaceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScopeNamespaceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScopeNamespaceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_namespace: Optional[str] = None):
        """
        Specifies that the scope of the extension is Namespace
        :param str target_namespace: Namespace where the extension will be created for an Namespace scoped extension.  If this namespace does not exist, it will be created
        """
        if target_namespace is not None:
            pulumi.set(__self__, "target_namespace", target_namespace)

    @property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> Optional[str]:
        """
        Namespace where the extension will be created for an Namespace scoped extension.  If this namespace does not exist, it will be created
        """
        return pulumi.get(self, "target_namespace")


@pulumi.output_type
class ScopeResponse(dict):
    """
    Scope of the extension. It can be either Cluster or Namespace; but not both.
    """
    def __init__(__self__, *,
                 cluster: Optional['outputs.ScopeClusterResponse'] = None,
                 namespace: Optional['outputs.ScopeNamespaceResponse'] = None):
        """
        Scope of the extension. It can be either Cluster or Namespace; but not both.
        :param 'ScopeClusterResponse' cluster: Specifies that the scope of the extension is Cluster
        :param 'ScopeNamespaceResponse' namespace: Specifies that the scope of the extension is Namespace
        """
        if cluster is not None:
            pulumi.set(__self__, "cluster", cluster)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def cluster(self) -> Optional['outputs.ScopeClusterResponse']:
        """
        Specifies that the scope of the extension is Cluster
        """
        return pulumi.get(self, "cluster")

    @property
    @pulumi.getter
    def namespace(self) -> Optional['outputs.ScopeNamespaceResponse']:
        """
        Specifies that the scope of the extension is Namespace
        """
        return pulumi.get(self, "namespace")


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


