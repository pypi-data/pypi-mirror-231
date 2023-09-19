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
    'EncryptionPropertyArgs',
    'IdentityArgs',
    'KeyVaultPropertiesArgs',
    'SharedPrivateLinkResourceArgs',
    'SkuArgs',
]

@pulumi.input_type
class EncryptionPropertyArgs:
    def __init__(__self__, *,
                 key_vault_properties: pulumi.Input['KeyVaultPropertiesArgs'],
                 status: pulumi.Input[Union[str, 'EncryptionStatus']]):
        """
        :param pulumi.Input['KeyVaultPropertiesArgs'] key_vault_properties: Customer Key vault properties.
        :param pulumi.Input[Union[str, 'EncryptionStatus']] status: Indicates whether or not the encryption is enabled for the workspace.
        """
        pulumi.set(__self__, "key_vault_properties", key_vault_properties)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> pulumi.Input['KeyVaultPropertiesArgs']:
        """
        Customer Key vault properties.
        """
        return pulumi.get(self, "key_vault_properties")

    @key_vault_properties.setter
    def key_vault_properties(self, value: pulumi.Input['KeyVaultPropertiesArgs']):
        pulumi.set(self, "key_vault_properties", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[str, 'EncryptionStatus']]:
        """
        Indicates whether or not the encryption is enabled for the workspace.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[Union[str, 'EncryptionStatus']]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input['ResourceIdentityType'],
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Identity for the resource.
        :param pulumi.Input['ResourceIdentityType'] type: The identity type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['ResourceIdentityType']:
        """
        The identity type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['ResourceIdentityType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(__self__, *,
                 key_identifier: pulumi.Input[str],
                 key_vault_arm_id: pulumi.Input[str],
                 identity_client_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] key_identifier: Key vault uri to access the encryption key.
        :param pulumi.Input[str] key_vault_arm_id: The ArmId of the keyVault where the customer owned encryption key is present.
        :param pulumi.Input[str] identity_client_id: For future use - The client id of the identity which will be used to access key vault.
        """
        pulumi.set(__self__, "key_identifier", key_identifier)
        pulumi.set(__self__, "key_vault_arm_id", key_vault_arm_id)
        if identity_client_id is not None:
            pulumi.set(__self__, "identity_client_id", identity_client_id)

    @property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> pulumi.Input[str]:
        """
        Key vault uri to access the encryption key.
        """
        return pulumi.get(self, "key_identifier")

    @key_identifier.setter
    def key_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_identifier", value)

    @property
    @pulumi.getter(name="keyVaultArmId")
    def key_vault_arm_id(self) -> pulumi.Input[str]:
        """
        The ArmId of the keyVault where the customer owned encryption key is present.
        """
        return pulumi.get(self, "key_vault_arm_id")

    @key_vault_arm_id.setter
    def key_vault_arm_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_arm_id", value)

    @property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        For future use - The client id of the identity which will be used to access key vault.
        """
        return pulumi.get(self, "identity_client_id")

    @identity_client_id.setter
    def identity_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_client_id", value)


@pulumi.input_type
class SharedPrivateLinkResourceArgs:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 request_message: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        :param pulumi.Input[str] group_id: The private link resource group id.
        :param pulumi.Input[str] name: Unique name of the private link.
        :param pulumi.Input[str] private_link_resource_id: The resource id that private link links to.
        :param pulumi.Input[str] request_message: Request message.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_link_resource_id is not None:
            pulumi.set(__self__, "private_link_resource_id", private_link_resource_id)
        if request_message is not None:
            pulumi.set(__self__, "request_message", request_message)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The private link resource group id.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique name of the private link.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id that private link links to.
        """
        return pulumi.get(self, "private_link_resource_id")

    @private_link_resource_id.setter
    def private_link_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_resource_id", value)

    @property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[str]]:
        """
        Request message.
        """
        return pulumi.get(self, "request_message")

    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_message", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[str]] = None):
        """
        Sku of the resource
        :param pulumi.Input[str] name: Name of the sku
        :param pulumi.Input[str] tier: Tier of the sku like Basic or Enterprise
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the sku
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        Tier of the sku like Basic or Enterprise
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)


