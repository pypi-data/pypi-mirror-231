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
    'NetworkProfileResponse',
    'OpenShiftAPIPropertiesResponse',
    'OpenShiftManagedClusterAADIdentityProviderResponse',
    'OpenShiftManagedClusterAgentPoolProfileResponse',
    'OpenShiftManagedClusterAuthProfileResponse',
    'OpenShiftManagedClusterIdentityProviderResponse',
    'OpenShiftManagedClusterMasterPoolProfileResponse',
    'OpenShiftManagedClusterMonitorProfileResponse',
    'OpenShiftRouterProfileResponse',
    'PurchasePlanResponse',
]

@pulumi.output_type
class NetworkProfileResponse(dict):
    """
    Represents the OpenShift networking configuration
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "managementSubnetCidr":
            suggest = "management_subnet_cidr"
        elif key == "vnetCidr":
            suggest = "vnet_cidr"
        elif key == "vnetId":
            suggest = "vnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NetworkProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NetworkProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NetworkProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 management_subnet_cidr: Optional[str] = None,
                 vnet_cidr: Optional[str] = None,
                 vnet_id: Optional[str] = None):
        """
        Represents the OpenShift networking configuration
        :param str management_subnet_cidr: CIDR of subnet used to create PLS needed for management of the cluster
        :param str vnet_cidr: CIDR for the OpenShift Vnet.
        :param str vnet_id: ID of the Vnet created for OSA cluster.
        """
        if management_subnet_cidr is not None:
            pulumi.set(__self__, "management_subnet_cidr", management_subnet_cidr)
        if vnet_cidr is None:
            vnet_cidr = '10.0.0.0/8'
        if vnet_cidr is not None:
            pulumi.set(__self__, "vnet_cidr", vnet_cidr)
        if vnet_id is not None:
            pulumi.set(__self__, "vnet_id", vnet_id)

    @property
    @pulumi.getter(name="managementSubnetCidr")
    def management_subnet_cidr(self) -> Optional[str]:
        """
        CIDR of subnet used to create PLS needed for management of the cluster
        """
        return pulumi.get(self, "management_subnet_cidr")

    @property
    @pulumi.getter(name="vnetCidr")
    def vnet_cidr(self) -> Optional[str]:
        """
        CIDR for the OpenShift Vnet.
        """
        return pulumi.get(self, "vnet_cidr")

    @property
    @pulumi.getter(name="vnetId")
    def vnet_id(self) -> Optional[str]:
        """
        ID of the Vnet created for OSA cluster.
        """
        return pulumi.get(self, "vnet_id")


@pulumi.output_type
class OpenShiftAPIPropertiesResponse(dict):
    """
    Defines further properties on the API.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateApiServer":
            suggest = "private_api_server"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OpenShiftAPIPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OpenShiftAPIPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OpenShiftAPIPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 private_api_server: Optional[bool] = None):
        """
        Defines further properties on the API.
        :param bool private_api_server: Specifies if API server is public or private.
        """
        if private_api_server is not None:
            pulumi.set(__self__, "private_api_server", private_api_server)

    @property
    @pulumi.getter(name="privateApiServer")
    def private_api_server(self) -> Optional[bool]:
        """
        Specifies if API server is public or private.
        """
        return pulumi.get(self, "private_api_server")


@pulumi.output_type
class OpenShiftManagedClusterAADIdentityProviderResponse(dict):
    """
    Defines the Identity provider for MS AAD.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "customerAdminGroupId":
            suggest = "customer_admin_group_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OpenShiftManagedClusterAADIdentityProviderResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OpenShiftManagedClusterAADIdentityProviderResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OpenShiftManagedClusterAADIdentityProviderResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kind: str,
                 client_id: Optional[str] = None,
                 customer_admin_group_id: Optional[str] = None,
                 secret: Optional[str] = None,
                 tenant_id: Optional[str] = None):
        """
        Defines the Identity provider for MS AAD.
        :param str kind: The kind of the provider.
               Expected value is 'AADIdentityProvider'.
        :param str client_id: The clientId password associated with the provider.
        :param str customer_admin_group_id: The groupId to be granted cluster admin role.
        :param str secret: The secret password associated with the provider.
        :param str tenant_id: The tenantId associated with the provider.
        """
        pulumi.set(__self__, "kind", 'AADIdentityProvider')
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if customer_admin_group_id is not None:
            pulumi.set(__self__, "customer_admin_group_id", customer_admin_group_id)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of the provider.
        Expected value is 'AADIdentityProvider'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[str]:
        """
        The clientId password associated with the provider.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="customerAdminGroupId")
    def customer_admin_group_id(self) -> Optional[str]:
        """
        The groupId to be granted cluster admin role.
        """
        return pulumi.get(self, "customer_admin_group_id")

    @property
    @pulumi.getter
    def secret(self) -> Optional[str]:
        """
        The secret password associated with the provider.
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The tenantId associated with the provider.
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class OpenShiftManagedClusterAgentPoolProfileResponse(dict):
    """
    Defines the configuration of the OpenShift cluster VMs.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "vmSize":
            suggest = "vm_size"
        elif key == "osType":
            suggest = "os_type"
        elif key == "subnetCidr":
            suggest = "subnet_cidr"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OpenShiftManagedClusterAgentPoolProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OpenShiftManagedClusterAgentPoolProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OpenShiftManagedClusterAgentPoolProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 count: int,
                 name: str,
                 vm_size: str,
                 os_type: Optional[str] = None,
                 role: Optional[str] = None,
                 subnet_cidr: Optional[str] = None):
        """
        Defines the configuration of the OpenShift cluster VMs.
        :param int count: Number of agents (VMs) to host docker containers.
        :param str name: Unique name of the pool profile in the context of the subscription and resource group.
        :param str vm_size: Size of agent VMs.
        :param str os_type: OsType to be used to specify os type. Choose from Linux and Windows. Default to Linux.
        :param str role: Define the role of the AgentPoolProfile.
        :param str subnet_cidr: Subnet CIDR for the peering.
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "vm_size", vm_size)
        if os_type is not None:
            pulumi.set(__self__, "os_type", os_type)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if subnet_cidr is None:
            subnet_cidr = '10.0.0.0/24'
        if subnet_cidr is not None:
            pulumi.set(__self__, "subnet_cidr", subnet_cidr)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        Number of agents (VMs) to host docker containers.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Unique name of the pool profile in the context of the subscription and resource group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> str:
        """
        Size of agent VMs.
        """
        return pulumi.get(self, "vm_size")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        OsType to be used to specify os type. Choose from Linux and Windows. Default to Linux.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter
    def role(self) -> Optional[str]:
        """
        Define the role of the AgentPoolProfile.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="subnetCidr")
    def subnet_cidr(self) -> Optional[str]:
        """
        Subnet CIDR for the peering.
        """
        return pulumi.get(self, "subnet_cidr")


@pulumi.output_type
class OpenShiftManagedClusterAuthProfileResponse(dict):
    """
    Defines all possible authentication profiles for the OpenShift cluster.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "identityProviders":
            suggest = "identity_providers"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OpenShiftManagedClusterAuthProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OpenShiftManagedClusterAuthProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OpenShiftManagedClusterAuthProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 identity_providers: Optional[Sequence['outputs.OpenShiftManagedClusterIdentityProviderResponse']] = None):
        """
        Defines all possible authentication profiles for the OpenShift cluster.
        :param Sequence['OpenShiftManagedClusterIdentityProviderResponse'] identity_providers: Type of authentication profile to use.
        """
        if identity_providers is not None:
            pulumi.set(__self__, "identity_providers", identity_providers)

    @property
    @pulumi.getter(name="identityProviders")
    def identity_providers(self) -> Optional[Sequence['outputs.OpenShiftManagedClusterIdentityProviderResponse']]:
        """
        Type of authentication profile to use.
        """
        return pulumi.get(self, "identity_providers")


@pulumi.output_type
class OpenShiftManagedClusterIdentityProviderResponse(dict):
    """
    Defines the configuration of the identity providers to be used in the OpenShift cluster.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 provider: Optional['outputs.OpenShiftManagedClusterAADIdentityProviderResponse'] = None):
        """
        Defines the configuration of the identity providers to be used in the OpenShift cluster.
        :param str name: Name of the provider.
        :param 'OpenShiftManagedClusterAADIdentityProviderResponse' provider: Configuration of the provider.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provider is not None:
            pulumi.set(__self__, "provider", provider)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the provider.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def provider(self) -> Optional['outputs.OpenShiftManagedClusterAADIdentityProviderResponse']:
        """
        Configuration of the provider.
        """
        return pulumi.get(self, "provider")


@pulumi.output_type
class OpenShiftManagedClusterMasterPoolProfileResponse(dict):
    """
    OpenShiftManagedClusterMaterPoolProfile contains configuration for OpenShift master VMs.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "vmSize":
            suggest = "vm_size"
        elif key == "apiProperties":
            suggest = "api_properties"
        elif key == "subnetCidr":
            suggest = "subnet_cidr"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OpenShiftManagedClusterMasterPoolProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OpenShiftManagedClusterMasterPoolProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OpenShiftManagedClusterMasterPoolProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 count: int,
                 vm_size: str,
                 api_properties: Optional['outputs.OpenShiftAPIPropertiesResponse'] = None,
                 subnet_cidr: Optional[str] = None):
        """
        OpenShiftManagedClusterMaterPoolProfile contains configuration for OpenShift master VMs.
        :param int count: Number of masters (VMs) to host docker containers. The default value is 3.
        :param str vm_size: Size of agent VMs.
        :param 'OpenShiftAPIPropertiesResponse' api_properties: Defines further properties on the API.
        :param str subnet_cidr: Subnet CIDR for the peering.
        """
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "vm_size", vm_size)
        if api_properties is not None:
            pulumi.set(__self__, "api_properties", api_properties)
        if subnet_cidr is not None:
            pulumi.set(__self__, "subnet_cidr", subnet_cidr)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        Number of masters (VMs) to host docker containers. The default value is 3.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> str:
        """
        Size of agent VMs.
        """
        return pulumi.get(self, "vm_size")

    @property
    @pulumi.getter(name="apiProperties")
    def api_properties(self) -> Optional['outputs.OpenShiftAPIPropertiesResponse']:
        """
        Defines further properties on the API.
        """
        return pulumi.get(self, "api_properties")

    @property
    @pulumi.getter(name="subnetCidr")
    def subnet_cidr(self) -> Optional[str]:
        """
        Subnet CIDR for the peering.
        """
        return pulumi.get(self, "subnet_cidr")


@pulumi.output_type
class OpenShiftManagedClusterMonitorProfileResponse(dict):
    """
    Defines the configuration for Log Analytics integration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "workspaceResourceID":
            suggest = "workspace_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OpenShiftManagedClusterMonitorProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OpenShiftManagedClusterMonitorProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OpenShiftManagedClusterMonitorProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 workspace_resource_id: Optional[str] = None):
        """
        Defines the configuration for Log Analytics integration.
        :param bool enabled: If the Log analytics integration should be turned on or off
        :param str workspace_resource_id: Azure Resource Manager Resource ID for the Log Analytics workspace to integrate with.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if workspace_resource_id is not None:
            pulumi.set(__self__, "workspace_resource_id", workspace_resource_id)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        If the Log analytics integration should be turned on or off
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="workspaceResourceID")
    def workspace_resource_id(self) -> Optional[str]:
        """
        Azure Resource Manager Resource ID for the Log Analytics workspace to integrate with.
        """
        return pulumi.get(self, "workspace_resource_id")


@pulumi.output_type
class OpenShiftRouterProfileResponse(dict):
    """
    Represents an OpenShift router
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "publicSubdomain":
            suggest = "public_subdomain"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OpenShiftRouterProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OpenShiftRouterProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OpenShiftRouterProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fqdn: str,
                 public_subdomain: str,
                 name: Optional[str] = None):
        """
        Represents an OpenShift router
        :param str fqdn: Auto-allocated FQDN for the OpenShift router.
        :param str public_subdomain: DNS subdomain for OpenShift router.
        :param str name: Name of the router profile.
        """
        pulumi.set(__self__, "fqdn", fqdn)
        pulumi.set(__self__, "public_subdomain", public_subdomain)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        Auto-allocated FQDN for the OpenShift router.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="publicSubdomain")
    def public_subdomain(self) -> str:
        """
        DNS subdomain for OpenShift router.
        """
        return pulumi.get(self, "public_subdomain")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the router profile.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class PurchasePlanResponse(dict):
    """
    Used for establishing the purchase context of any 3rd Party artifact through MarketPlace.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "promotionCode":
            suggest = "promotion_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PurchasePlanResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PurchasePlanResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PurchasePlanResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: Optional[str] = None,
                 product: Optional[str] = None,
                 promotion_code: Optional[str] = None,
                 publisher: Optional[str] = None):
        """
        Used for establishing the purchase context of any 3rd Party artifact through MarketPlace.
        :param str name: The plan ID.
        :param str product: Specifies the product of the image from the marketplace. This is the same value as Offer under the imageReference element.
        :param str promotion_code: The promotion code.
        :param str publisher: The plan ID.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if product is not None:
            pulumi.set(__self__, "product", product)
        if promotion_code is not None:
            pulumi.set(__self__, "promotion_code", promotion_code)
        if publisher is not None:
            pulumi.set(__self__, "publisher", publisher)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The plan ID.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def product(self) -> Optional[str]:
        """
        Specifies the product of the image from the marketplace. This is the same value as Offer under the imageReference element.
        """
        return pulumi.get(self, "product")

    @property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[str]:
        """
        The promotion code.
        """
        return pulumi.get(self, "promotion_code")

    @property
    @pulumi.getter
    def publisher(self) -> Optional[str]:
        """
        The plan ID.
        """
        return pulumi.get(self, "publisher")


