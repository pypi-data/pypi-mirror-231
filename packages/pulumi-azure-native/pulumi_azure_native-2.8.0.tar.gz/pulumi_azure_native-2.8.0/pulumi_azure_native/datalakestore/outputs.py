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
from ._enums import *

__all__ = [
    'EncryptionConfigResponse',
    'EncryptionIdentityResponse',
    'FirewallRuleResponse',
    'KeyVaultMetaInfoResponse',
    'TrustedIdProviderResponse',
    'VirtualNetworkRuleResponse',
]

@pulumi.output_type
class EncryptionConfigResponse(dict):
    """
    The encryption configuration for the account.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyVaultMetaInfo":
            suggest = "key_vault_meta_info"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EncryptionConfigResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EncryptionConfigResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EncryptionConfigResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 key_vault_meta_info: Optional['outputs.KeyVaultMetaInfoResponse'] = None):
        """
        The encryption configuration for the account.
        :param str type: The type of encryption configuration being used. Currently the only supported types are 'UserManaged' and 'ServiceManaged'.
        :param 'KeyVaultMetaInfoResponse' key_vault_meta_info: The Key Vault information for connecting to user managed encryption keys.
        """
        pulumi.set(__self__, "type", type)
        if key_vault_meta_info is not None:
            pulumi.set(__self__, "key_vault_meta_info", key_vault_meta_info)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of encryption configuration being used. Currently the only supported types are 'UserManaged' and 'ServiceManaged'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="keyVaultMetaInfo")
    def key_vault_meta_info(self) -> Optional['outputs.KeyVaultMetaInfoResponse']:
        """
        The Key Vault information for connecting to user managed encryption keys.
        """
        return pulumi.get(self, "key_vault_meta_info")


@pulumi.output_type
class EncryptionIdentityResponse(dict):
    """
    The encryption identity properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EncryptionIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EncryptionIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EncryptionIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: str):
        """
        The encryption identity properties.
        :param str principal_id: The principal identifier associated with the encryption.
        :param str tenant_id: The tenant identifier associated with the encryption.
        :param str type: The type of encryption being used. Currently the only supported type is 'SystemAssigned'.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal identifier associated with the encryption.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant identifier associated with the encryption.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of encryption being used. Currently the only supported type is 'SystemAssigned'.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class FirewallRuleResponse(dict):
    """
    Data Lake Store firewall rule information.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endIpAddress":
            suggest = "end_ip_address"
        elif key == "startIpAddress":
            suggest = "start_ip_address"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FirewallRuleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FirewallRuleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FirewallRuleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 end_ip_address: str,
                 id: str,
                 name: str,
                 start_ip_address: str,
                 type: str):
        """
        Data Lake Store firewall rule information.
        :param str end_ip_address: The end IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
        :param str id: The resource identifier.
        :param str name: The resource name.
        :param str start_ip_address: The start IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
        :param str type: The resource type.
        """
        pulumi.set(__self__, "end_ip_address", end_ip_address)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "start_ip_address", start_ip_address)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> str:
        """
        The end IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
        """
        return pulumi.get(self, "end_ip_address")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> str:
        """
        The start IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
        """
        return pulumi.get(self, "start_ip_address")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class KeyVaultMetaInfoResponse(dict):
    """
    Metadata information used by account encryption.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "encryptionKeyName":
            suggest = "encryption_key_name"
        elif key == "encryptionKeyVersion":
            suggest = "encryption_key_version"
        elif key == "keyVaultResourceId":
            suggest = "key_vault_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in KeyVaultMetaInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        KeyVaultMetaInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        KeyVaultMetaInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 encryption_key_name: str,
                 encryption_key_version: str,
                 key_vault_resource_id: str):
        """
        Metadata information used by account encryption.
        :param str encryption_key_name: The name of the user managed encryption key.
        :param str encryption_key_version: The version of the user managed encryption key.
        :param str key_vault_resource_id: The resource identifier for the user managed Key Vault being used to encrypt.
        """
        pulumi.set(__self__, "encryption_key_name", encryption_key_name)
        pulumi.set(__self__, "encryption_key_version", encryption_key_version)
        pulumi.set(__self__, "key_vault_resource_id", key_vault_resource_id)

    @property
    @pulumi.getter(name="encryptionKeyName")
    def encryption_key_name(self) -> str:
        """
        The name of the user managed encryption key.
        """
        return pulumi.get(self, "encryption_key_name")

    @property
    @pulumi.getter(name="encryptionKeyVersion")
    def encryption_key_version(self) -> str:
        """
        The version of the user managed encryption key.
        """
        return pulumi.get(self, "encryption_key_version")

    @property
    @pulumi.getter(name="keyVaultResourceId")
    def key_vault_resource_id(self) -> str:
        """
        The resource identifier for the user managed Key Vault being used to encrypt.
        """
        return pulumi.get(self, "key_vault_resource_id")


@pulumi.output_type
class TrustedIdProviderResponse(dict):
    """
    Data Lake Store trusted identity provider information.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "idProvider":
            suggest = "id_provider"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TrustedIdProviderResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TrustedIdProviderResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TrustedIdProviderResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 id_provider: str,
                 name: str,
                 type: str):
        """
        Data Lake Store trusted identity provider information.
        :param str id: The resource identifier.
        :param str id_provider: The URL of this trusted identity provider.
        :param str name: The resource name.
        :param str type: The resource type.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "id_provider", id_provider)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idProvider")
    def id_provider(self) -> str:
        """
        The URL of this trusted identity provider.
        """
        return pulumi.get(self, "id_provider")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class VirtualNetworkRuleResponse(dict):
    """
    Data Lake Store virtual network rule information.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetId":
            suggest = "subnet_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VirtualNetworkRuleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VirtualNetworkRuleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VirtualNetworkRuleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 name: str,
                 subnet_id: str,
                 type: str):
        """
        Data Lake Store virtual network rule information.
        :param str id: The resource identifier.
        :param str name: The resource name.
        :param str subnet_id: The resource identifier for the subnet.
        :param str type: The resource type.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "subnet_id", subnet_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The resource identifier for the subnet.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


