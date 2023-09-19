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
from ._inputs import *

__all__ = ['WorkspaceArgs', 'Workspace']

@pulumi.input_type
class WorkspaceArgs:
    def __init__(__self__, *,
                 managed_resource_group_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 authorizations: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceProviderAuthorizationArgs']]]] = None,
                 encryption: Optional[pulumi.Input['WorkspacePropertiesEncryptionArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input['WorkspaceCustomParametersArgs']] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 required_nsg_rules: Optional[pulumi.Input[Union[str, 'RequiredNsgRules']]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ui_definition_uri: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Workspace resource.
        :param pulumi.Input[str] managed_resource_group_id: The managed resource group Id.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['WorkspaceProviderAuthorizationArgs']]] authorizations: The workspace provider authorizations.
        :param pulumi.Input['WorkspacePropertiesEncryptionArgs'] encryption: Encryption properties for databricks workspace
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['WorkspaceCustomParametersArgs'] parameters: The workspace's custom parameters.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: The network access type for accessing workspace. Set value to disabled to access workspace only via private link.
        :param pulumi.Input[Union[str, 'RequiredNsgRules']] required_nsg_rules: Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint. Supported values are 'AllRules' and 'NoAzureDatabricksRules'. 'NoAzureServiceRules' value is for internal use only.
        :param pulumi.Input['SkuArgs'] sku: The SKU of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] ui_definition_uri: The blob URI where the UI definition file is located.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        pulumi.set(__self__, "managed_resource_group_id", managed_resource_group_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authorizations is not None:
            pulumi.set(__self__, "authorizations", authorizations)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if required_nsg_rules is not None:
            pulumi.set(__self__, "required_nsg_rules", required_nsg_rules)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if ui_definition_uri is not None:
            pulumi.set(__self__, "ui_definition_uri", ui_definition_uri)
        if workspace_name is not None:
            pulumi.set(__self__, "workspace_name", workspace_name)

    @property
    @pulumi.getter(name="managedResourceGroupId")
    def managed_resource_group_id(self) -> pulumi.Input[str]:
        """
        The managed resource group Id.
        """
        return pulumi.get(self, "managed_resource_group_id")

    @managed_resource_group_id.setter
    def managed_resource_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_resource_group_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def authorizations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceProviderAuthorizationArgs']]]]:
        """
        The workspace provider authorizations.
        """
        return pulumi.get(self, "authorizations")

    @authorizations.setter
    def authorizations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkspaceProviderAuthorizationArgs']]]]):
        pulumi.set(self, "authorizations", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['WorkspacePropertiesEncryptionArgs']]:
        """
        Encryption properties for databricks workspace
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['WorkspacePropertiesEncryptionArgs']]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input['WorkspaceCustomParametersArgs']]:
        """
        The workspace's custom parameters.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input['WorkspaceCustomParametersArgs']]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        The network access type for accessing workspace. Set value to disabled to access workspace only via private link.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter(name="requiredNsgRules")
    def required_nsg_rules(self) -> Optional[pulumi.Input[Union[str, 'RequiredNsgRules']]]:
        """
        Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint. Supported values are 'AllRules' and 'NoAzureDatabricksRules'. 'NoAzureServiceRules' value is for internal use only.
        """
        return pulumi.get(self, "required_nsg_rules")

    @required_nsg_rules.setter
    def required_nsg_rules(self, value: Optional[pulumi.Input[Union[str, 'RequiredNsgRules']]]):
        pulumi.set(self, "required_nsg_rules", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The SKU of the resource.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="uiDefinitionUri")
    def ui_definition_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The blob URI where the UI definition file is located.
        """
        return pulumi.get(self, "ui_definition_uri")

    @ui_definition_uri.setter
    def ui_definition_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ui_definition_uri", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_name", value)


class Workspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorizations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkspaceProviderAuthorizationArgs']]]]] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['WorkspacePropertiesEncryptionArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['WorkspaceCustomParametersArgs']]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 required_nsg_rules: Optional[pulumi.Input[Union[str, 'RequiredNsgRules']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ui_definition_uri: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Information about workspace.
        Azure REST API version: 2023-02-01. Prior API version in Azure Native 1.x: 2018-04-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkspaceProviderAuthorizationArgs']]]] authorizations: The workspace provider authorizations.
        :param pulumi.Input[pulumi.InputType['WorkspacePropertiesEncryptionArgs']] encryption: Encryption properties for databricks workspace
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] managed_resource_group_id: The managed resource group Id.
        :param pulumi.Input[pulumi.InputType['WorkspaceCustomParametersArgs']] parameters: The workspace's custom parameters.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: The network access type for accessing workspace. Set value to disabled to access workspace only via private link.
        :param pulumi.Input[Union[str, 'RequiredNsgRules']] required_nsg_rules: Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint. Supported values are 'AllRules' and 'NoAzureDatabricksRules'. 'NoAzureServiceRules' value is for internal use only.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The SKU of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] ui_definition_uri: The blob URI where the UI definition file is located.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Information about workspace.
        Azure REST API version: 2023-02-01. Prior API version in Azure Native 1.x: 2018-04-01

        :param str resource_name: The name of the resource.
        :param WorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorizations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkspaceProviderAuthorizationArgs']]]]] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['WorkspacePropertiesEncryptionArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['WorkspaceCustomParametersArgs']]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 required_nsg_rules: Optional[pulumi.Input[Union[str, 'RequiredNsgRules']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ui_definition_uri: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

            __props__.__dict__["authorizations"] = authorizations
            __props__.__dict__["encryption"] = encryption
            __props__.__dict__["location"] = location
            if managed_resource_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'managed_resource_group_id'")
            __props__.__dict__["managed_resource_group_id"] = managed_resource_group_id
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["public_network_access"] = public_network_access
            __props__.__dict__["required_nsg_rules"] = required_nsg_rules
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["ui_definition_uri"] = ui_definition_uri
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["created_by"] = None
            __props__.__dict__["created_date_time"] = None
            __props__.__dict__["disk_encryption_set_id"] = None
            __props__.__dict__["managed_disk_identity"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["storage_account_identity"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_by"] = None
            __props__.__dict__["workspace_id"] = None
            __props__.__dict__["workspace_url"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:databricks/v20180401:Workspace"), pulumi.Alias(type_="azure-native:databricks/v20210401preview:Workspace"), pulumi.Alias(type_="azure-native:databricks/v20220401preview:Workspace"), pulumi.Alias(type_="azure-native:databricks/v20230201:Workspace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Workspace, __self__).__init__(
            'azure-native:databricks:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workspace':
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

        __props__.__dict__["authorizations"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["created_date_time"] = None
        __props__.__dict__["disk_encryption_set_id"] = None
        __props__.__dict__["encryption"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_disk_identity"] = None
        __props__.__dict__["managed_resource_group_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["required_nsg_rules"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["storage_account_identity"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["ui_definition_uri"] = None
        __props__.__dict__["updated_by"] = None
        __props__.__dict__["workspace_id"] = None
        __props__.__dict__["workspace_url"] = None
        return Workspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authorizations(self) -> pulumi.Output[Optional[Sequence['outputs.WorkspaceProviderAuthorizationResponse']]]:
        """
        The workspace provider authorizations.
        """
        return pulumi.get(self, "authorizations")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional['outputs.CreatedByResponse']]:
        """
        Indicates the Object ID, PUID and Application ID of entity that created the workspace.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> pulumi.Output[str]:
        """
        Specifies the date and time when the workspace is created.
        """
        return pulumi.get(self, "created_date_time")

    @property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> pulumi.Output[str]:
        """
        The resource Id of the managed disk encryption set.
        """
        return pulumi.get(self, "disk_encryption_set_id")

    @property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional['outputs.WorkspacePropertiesResponseEncryption']]:
        """
        Encryption properties for databricks workspace
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedDiskIdentity")
    def managed_disk_identity(self) -> pulumi.Output[Optional['outputs.ManagedIdentityConfigurationResponse']]:
        """
        The details of Managed Identity of Disk Encryption Set used for Managed Disk Encryption
        """
        return pulumi.get(self, "managed_disk_identity")

    @property
    @pulumi.getter(name="managedResourceGroupId")
    def managed_resource_group_id(self) -> pulumi.Output[str]:
        """
        The managed resource group Id.
        """
        return pulumi.get(self, "managed_resource_group_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional['outputs.WorkspaceCustomParametersResponse']]:
        """
        The workspace's custom parameters.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        Private endpoint connections created on the workspace
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The workspace provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        The network access type for accessing workspace. Set value to disabled to access workspace only via private link.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="requiredNsgRules")
    def required_nsg_rules(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets a value indicating whether data plane (clusters) to control plane communication happen over private endpoint. Supported values are 'AllRules' and 'NoAzureDatabricksRules'. 'NoAzureServiceRules' value is for internal use only.
        """
        return pulumi.get(self, "required_nsg_rules")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The SKU of the resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="storageAccountIdentity")
    def storage_account_identity(self) -> pulumi.Output[Optional['outputs.ManagedIdentityConfigurationResponse']]:
        """
        The details of Managed Identity of Storage Account
        """
        return pulumi.get(self, "storage_account_identity")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to this resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uiDefinitionUri")
    def ui_definition_uri(self) -> pulumi.Output[Optional[str]]:
        """
        The blob URI where the UI definition file is located.
        """
        return pulumi.get(self, "ui_definition_uri")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[Optional['outputs.CreatedByResponse']]:
        """
        Indicates the Object ID, PUID and Application ID of entity that last updated the workspace.
        """
        return pulumi.get(self, "updated_by")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[str]:
        """
        The unique identifier of the databricks workspace in databricks control plane.
        """
        return pulumi.get(self, "workspace_id")

    @property
    @pulumi.getter(name="workspaceUrl")
    def workspace_url(self) -> pulumi.Output[str]:
        """
        The workspace URL which is of the format 'adb-{workspaceId}.{random}.azuredatabricks.net'
        """
        return pulumi.get(self, "workspace_url")

