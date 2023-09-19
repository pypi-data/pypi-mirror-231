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
from ._inputs import *

__all__ = ['ApplicationDefinitionArgs', 'ApplicationDefinition']

@pulumi.input_type
class ApplicationDefinitionArgs:
    def __init__(__self__, *,
                 lock_level: pulumi.Input['ApplicationLockLevel'],
                 resource_group_name: pulumi.Input[str],
                 application_definition_name: Optional[pulumi.Input[str]] = None,
                 artifacts: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationDefinitionArtifactArgs']]]] = None,
                 authorizations: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationAuthorizationArgs']]]] = None,
                 create_ui_definition: Optional[Any] = None,
                 deployment_policy: Optional[pulumi.Input['ApplicationDeploymentPolicyArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 locking_policy: Optional[pulumi.Input['ApplicationPackageLockingPolicyDefinitionArgs']] = None,
                 main_template: Optional[Any] = None,
                 managed_by: Optional[pulumi.Input[str]] = None,
                 management_policy: Optional[pulumi.Input['ApplicationManagementPolicyArgs']] = None,
                 notification_policy: Optional[pulumi.Input['ApplicationNotificationPolicyArgs']] = None,
                 package_file_uri: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationPolicyArgs']]]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ApplicationDefinition resource.
        :param pulumi.Input['ApplicationLockLevel'] lock_level: The managed application lock level.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] application_definition_name: The name of the managed application definition.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationDefinitionArtifactArgs']]] artifacts: The collection of managed application artifacts. The portal will use the files specified as artifacts to construct the user experience of creating a managed application from a managed application definition.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationAuthorizationArgs']]] authorizations: The managed application provider authorizations.
        :param Any create_ui_definition: The createUiDefinition json for the backing template with Microsoft.Solutions/applications resource. It can be a JObject or well-formed JSON string.
        :param pulumi.Input['ApplicationDeploymentPolicyArgs'] deployment_policy: The managed application deployment policy.
        :param pulumi.Input[str] description: The managed application definition description.
        :param pulumi.Input[str] display_name: The managed application definition display name.
        :param pulumi.Input[bool] is_enabled: A value indicating whether the package is enabled or not.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['ApplicationPackageLockingPolicyDefinitionArgs'] locking_policy: The managed application locking policy.
        :param Any main_template: The inline main template json which has resources to be provisioned. It can be a JObject or well-formed JSON string.
        :param pulumi.Input[str] managed_by: ID of the resource that manages this resource.
        :param pulumi.Input['ApplicationManagementPolicyArgs'] management_policy: The managed application management policy that determines publisher's access to the managed resource group.
        :param pulumi.Input['ApplicationNotificationPolicyArgs'] notification_policy: The managed application notification policy.
        :param pulumi.Input[str] package_file_uri: The managed application definition package file Uri. Use this element
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationPolicyArgs']]] policies: The managed application provider policies.
        :param pulumi.Input['SkuArgs'] sku: The SKU of the resource.
        :param pulumi.Input[str] storage_account_id: The storage account id for bring your own storage scenario.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "lock_level", lock_level)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if application_definition_name is not None:
            pulumi.set(__self__, "application_definition_name", application_definition_name)
        if artifacts is not None:
            pulumi.set(__self__, "artifacts", artifacts)
        if authorizations is not None:
            pulumi.set(__self__, "authorizations", authorizations)
        if create_ui_definition is not None:
            pulumi.set(__self__, "create_ui_definition", create_ui_definition)
        if deployment_policy is not None:
            pulumi.set(__self__, "deployment_policy", deployment_policy)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if locking_policy is not None:
            pulumi.set(__self__, "locking_policy", locking_policy)
        if main_template is not None:
            pulumi.set(__self__, "main_template", main_template)
        if managed_by is not None:
            pulumi.set(__self__, "managed_by", managed_by)
        if management_policy is not None:
            pulumi.set(__self__, "management_policy", management_policy)
        if notification_policy is not None:
            pulumi.set(__self__, "notification_policy", notification_policy)
        if package_file_uri is not None:
            pulumi.set(__self__, "package_file_uri", package_file_uri)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if storage_account_id is not None:
            pulumi.set(__self__, "storage_account_id", storage_account_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="lockLevel")
    def lock_level(self) -> pulumi.Input['ApplicationLockLevel']:
        """
        The managed application lock level.
        """
        return pulumi.get(self, "lock_level")

    @lock_level.setter
    def lock_level(self, value: pulumi.Input['ApplicationLockLevel']):
        pulumi.set(self, "lock_level", value)

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
    @pulumi.getter(name="applicationDefinitionName")
    def application_definition_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the managed application definition.
        """
        return pulumi.get(self, "application_definition_name")

    @application_definition_name.setter
    def application_definition_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_definition_name", value)

    @property
    @pulumi.getter
    def artifacts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationDefinitionArtifactArgs']]]]:
        """
        The collection of managed application artifacts. The portal will use the files specified as artifacts to construct the user experience of creating a managed application from a managed application definition.
        """
        return pulumi.get(self, "artifacts")

    @artifacts.setter
    def artifacts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationDefinitionArtifactArgs']]]]):
        pulumi.set(self, "artifacts", value)

    @property
    @pulumi.getter
    def authorizations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationAuthorizationArgs']]]]:
        """
        The managed application provider authorizations.
        """
        return pulumi.get(self, "authorizations")

    @authorizations.setter
    def authorizations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationAuthorizationArgs']]]]):
        pulumi.set(self, "authorizations", value)

    @property
    @pulumi.getter(name="createUiDefinition")
    def create_ui_definition(self) -> Optional[Any]:
        """
        The createUiDefinition json for the backing template with Microsoft.Solutions/applications resource. It can be a JObject or well-formed JSON string.
        """
        return pulumi.get(self, "create_ui_definition")

    @create_ui_definition.setter
    def create_ui_definition(self, value: Optional[Any]):
        pulumi.set(self, "create_ui_definition", value)

    @property
    @pulumi.getter(name="deploymentPolicy")
    def deployment_policy(self) -> Optional[pulumi.Input['ApplicationDeploymentPolicyArgs']]:
        """
        The managed application deployment policy.
        """
        return pulumi.get(self, "deployment_policy")

    @deployment_policy.setter
    def deployment_policy(self, value: Optional[pulumi.Input['ApplicationDeploymentPolicyArgs']]):
        pulumi.set(self, "deployment_policy", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The managed application definition description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The managed application definition display name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        A value indicating whether the package is enabled or not.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="lockingPolicy")
    def locking_policy(self) -> Optional[pulumi.Input['ApplicationPackageLockingPolicyDefinitionArgs']]:
        """
        The managed application locking policy.
        """
        return pulumi.get(self, "locking_policy")

    @locking_policy.setter
    def locking_policy(self, value: Optional[pulumi.Input['ApplicationPackageLockingPolicyDefinitionArgs']]):
        pulumi.set(self, "locking_policy", value)

    @property
    @pulumi.getter(name="mainTemplate")
    def main_template(self) -> Optional[Any]:
        """
        The inline main template json which has resources to be provisioned. It can be a JObject or well-formed JSON string.
        """
        return pulumi.get(self, "main_template")

    @main_template.setter
    def main_template(self, value: Optional[Any]):
        pulumi.set(self, "main_template", value)

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the resource that manages this resource.
        """
        return pulumi.get(self, "managed_by")

    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_by", value)

    @property
    @pulumi.getter(name="managementPolicy")
    def management_policy(self) -> Optional[pulumi.Input['ApplicationManagementPolicyArgs']]:
        """
        The managed application management policy that determines publisher's access to the managed resource group.
        """
        return pulumi.get(self, "management_policy")

    @management_policy.setter
    def management_policy(self, value: Optional[pulumi.Input['ApplicationManagementPolicyArgs']]):
        pulumi.set(self, "management_policy", value)

    @property
    @pulumi.getter(name="notificationPolicy")
    def notification_policy(self) -> Optional[pulumi.Input['ApplicationNotificationPolicyArgs']]:
        """
        The managed application notification policy.
        """
        return pulumi.get(self, "notification_policy")

    @notification_policy.setter
    def notification_policy(self, value: Optional[pulumi.Input['ApplicationNotificationPolicyArgs']]):
        pulumi.set(self, "notification_policy", value)

    @property
    @pulumi.getter(name="packageFileUri")
    def package_file_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The managed application definition package file Uri. Use this element
        """
        return pulumi.get(self, "package_file_uri")

    @package_file_uri.setter
    def package_file_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "package_file_uri", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationPolicyArgs']]]]:
        """
        The managed application provider policies.
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationPolicyArgs']]]]):
        pulumi.set(self, "policies", value)

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
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The storage account id for bring your own storage scenario.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ApplicationDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_definition_name: Optional[pulumi.Input[str]] = None,
                 artifacts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationDefinitionArtifactArgs']]]]] = None,
                 authorizations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationAuthorizationArgs']]]]] = None,
                 create_ui_definition: Optional[Any] = None,
                 deployment_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationDeploymentPolicyArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lock_level: Optional[pulumi.Input['ApplicationLockLevel']] = None,
                 locking_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationPackageLockingPolicyDefinitionArgs']]] = None,
                 main_template: Optional[Any] = None,
                 managed_by: Optional[pulumi.Input[str]] = None,
                 management_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationManagementPolicyArgs']]] = None,
                 notification_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationNotificationPolicyArgs']]] = None,
                 package_file_uri: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationPolicyArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Information about managed application definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_definition_name: The name of the managed application definition.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationDefinitionArtifactArgs']]]] artifacts: The collection of managed application artifacts. The portal will use the files specified as artifacts to construct the user experience of creating a managed application from a managed application definition.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationAuthorizationArgs']]]] authorizations: The managed application provider authorizations.
        :param Any create_ui_definition: The createUiDefinition json for the backing template with Microsoft.Solutions/applications resource. It can be a JObject or well-formed JSON string.
        :param pulumi.Input[pulumi.InputType['ApplicationDeploymentPolicyArgs']] deployment_policy: The managed application deployment policy.
        :param pulumi.Input[str] description: The managed application definition description.
        :param pulumi.Input[str] display_name: The managed application definition display name.
        :param pulumi.Input[bool] is_enabled: A value indicating whether the package is enabled or not.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['ApplicationLockLevel'] lock_level: The managed application lock level.
        :param pulumi.Input[pulumi.InputType['ApplicationPackageLockingPolicyDefinitionArgs']] locking_policy: The managed application locking policy.
        :param Any main_template: The inline main template json which has resources to be provisioned. It can be a JObject or well-formed JSON string.
        :param pulumi.Input[str] managed_by: ID of the resource that manages this resource.
        :param pulumi.Input[pulumi.InputType['ApplicationManagementPolicyArgs']] management_policy: The managed application management policy that determines publisher's access to the managed resource group.
        :param pulumi.Input[pulumi.InputType['ApplicationNotificationPolicyArgs']] notification_policy: The managed application notification policy.
        :param pulumi.Input[str] package_file_uri: The managed application definition package file Uri. Use this element
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationPolicyArgs']]]] policies: The managed application provider policies.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The SKU of the resource.
        :param pulumi.Input[str] storage_account_id: The storage account id for bring your own storage scenario.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Information about managed application definition.

        :param str resource_name: The name of the resource.
        :param ApplicationDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_definition_name: Optional[pulumi.Input[str]] = None,
                 artifacts: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationDefinitionArtifactArgs']]]]] = None,
                 authorizations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationAuthorizationArgs']]]]] = None,
                 create_ui_definition: Optional[Any] = None,
                 deployment_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationDeploymentPolicyArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lock_level: Optional[pulumi.Input['ApplicationLockLevel']] = None,
                 locking_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationPackageLockingPolicyDefinitionArgs']]] = None,
                 main_template: Optional[Any] = None,
                 managed_by: Optional[pulumi.Input[str]] = None,
                 management_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationManagementPolicyArgs']]] = None,
                 notification_policy: Optional[pulumi.Input[pulumi.InputType['ApplicationNotificationPolicyArgs']]] = None,
                 package_file_uri: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationPolicyArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationDefinitionArgs.__new__(ApplicationDefinitionArgs)

            __props__.__dict__["application_definition_name"] = application_definition_name
            __props__.__dict__["artifacts"] = artifacts
            __props__.__dict__["authorizations"] = authorizations
            __props__.__dict__["create_ui_definition"] = create_ui_definition
            __props__.__dict__["deployment_policy"] = deployment_policy
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["is_enabled"] = is_enabled
            __props__.__dict__["location"] = location
            if lock_level is None and not opts.urn:
                raise TypeError("Missing required property 'lock_level'")
            __props__.__dict__["lock_level"] = lock_level
            __props__.__dict__["locking_policy"] = locking_policy
            __props__.__dict__["main_template"] = main_template
            __props__.__dict__["managed_by"] = managed_by
            __props__.__dict__["management_policy"] = management_policy
            __props__.__dict__["notification_policy"] = notification_policy
            __props__.__dict__["package_file_uri"] = package_file_uri
            __props__.__dict__["policies"] = policies
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["storage_account_id"] = storage_account_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:solutions:ApplicationDefinition"), pulumi.Alias(type_="azure-native:solutions/v20160901preview:ApplicationDefinition"), pulumi.Alias(type_="azure-native:solutions/v20170901:ApplicationDefinition"), pulumi.Alias(type_="azure-native:solutions/v20171201:ApplicationDefinition"), pulumi.Alias(type_="azure-native:solutions/v20180201:ApplicationDefinition"), pulumi.Alias(type_="azure-native:solutions/v20180301:ApplicationDefinition"), pulumi.Alias(type_="azure-native:solutions/v20180601:ApplicationDefinition"), pulumi.Alias(type_="azure-native:solutions/v20180901preview:ApplicationDefinition"), pulumi.Alias(type_="azure-native:solutions/v20190701:ApplicationDefinition"), pulumi.Alias(type_="azure-native:solutions/v20200821preview:ApplicationDefinition"), pulumi.Alias(type_="azure-native:solutions/v20210201preview:ApplicationDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApplicationDefinition, __self__).__init__(
            'azure-native:solutions/v20210701:ApplicationDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationDefinition':
        """
        Get an existing ApplicationDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationDefinitionArgs.__new__(ApplicationDefinitionArgs)

        __props__.__dict__["artifacts"] = None
        __props__.__dict__["authorizations"] = None
        __props__.__dict__["create_ui_definition"] = None
        __props__.__dict__["deployment_policy"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["is_enabled"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["lock_level"] = None
        __props__.__dict__["locking_policy"] = None
        __props__.__dict__["main_template"] = None
        __props__.__dict__["managed_by"] = None
        __props__.__dict__["management_policy"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification_policy"] = None
        __props__.__dict__["package_file_uri"] = None
        __props__.__dict__["policies"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["storage_account_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ApplicationDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def artifacts(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationDefinitionArtifactResponse']]]:
        """
        The collection of managed application artifacts. The portal will use the files specified as artifacts to construct the user experience of creating a managed application from a managed application definition.
        """
        return pulumi.get(self, "artifacts")

    @property
    @pulumi.getter
    def authorizations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationAuthorizationResponse']]]:
        """
        The managed application provider authorizations.
        """
        return pulumi.get(self, "authorizations")

    @property
    @pulumi.getter(name="createUiDefinition")
    def create_ui_definition(self) -> pulumi.Output[Optional[Any]]:
        """
        The createUiDefinition json for the backing template with Microsoft.Solutions/applications resource. It can be a JObject or well-formed JSON string.
        """
        return pulumi.get(self, "create_ui_definition")

    @property
    @pulumi.getter(name="deploymentPolicy")
    def deployment_policy(self) -> pulumi.Output[Optional['outputs.ApplicationDeploymentPolicyResponse']]:
        """
        The managed application deployment policy.
        """
        return pulumi.get(self, "deployment_policy")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The managed application definition description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The managed application definition display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        A value indicating whether the package is enabled or not.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="lockLevel")
    def lock_level(self) -> pulumi.Output[str]:
        """
        The managed application lock level.
        """
        return pulumi.get(self, "lock_level")

    @property
    @pulumi.getter(name="lockingPolicy")
    def locking_policy(self) -> pulumi.Output[Optional['outputs.ApplicationPackageLockingPolicyDefinitionResponse']]:
        """
        The managed application locking policy.
        """
        return pulumi.get(self, "locking_policy")

    @property
    @pulumi.getter(name="mainTemplate")
    def main_template(self) -> pulumi.Output[Optional[Any]]:
        """
        The inline main template json which has resources to be provisioned. It can be a JObject or well-formed JSON string.
        """
        return pulumi.get(self, "main_template")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the resource that manages this resource.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter(name="managementPolicy")
    def management_policy(self) -> pulumi.Output[Optional['outputs.ApplicationManagementPolicyResponse']]:
        """
        The managed application management policy that determines publisher's access to the managed resource group.
        """
        return pulumi.get(self, "management_policy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationPolicy")
    def notification_policy(self) -> pulumi.Output[Optional['outputs.ApplicationNotificationPolicyResponse']]:
        """
        The managed application notification policy.
        """
        return pulumi.get(self, "notification_policy")

    @property
    @pulumi.getter(name="packageFileUri")
    def package_file_uri(self) -> pulumi.Output[Optional[str]]:
        """
        The managed application definition package file Uri. Use this element
        """
        return pulumi.get(self, "package_file_uri")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationPolicyResponse']]]:
        """
        The managed application provider policies.
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The SKU of the resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[Optional[str]]:
        """
        The storage account id for bring your own storage scenario.
        """
        return pulumi.get(self, "storage_account_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

