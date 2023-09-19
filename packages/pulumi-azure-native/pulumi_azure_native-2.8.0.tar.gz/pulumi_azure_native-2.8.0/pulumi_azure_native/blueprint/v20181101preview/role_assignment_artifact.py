# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['RoleAssignmentArtifactArgs', 'RoleAssignmentArtifact']

@pulumi.input_type
class RoleAssignmentArtifactArgs:
    def __init__(__self__, *,
                 blueprint_name: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 principal_ids: Any,
                 resource_scope: pulumi.Input[str],
                 role_definition_id: pulumi.Input[str],
                 artifact_name: Optional[pulumi.Input[str]] = None,
                 depends_on: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RoleAssignmentArtifact resource.
        :param pulumi.Input[str] blueprint_name: Name of the blueprint definition.
        :param pulumi.Input[str] kind: Specifies the kind of blueprint artifact.
               Expected value is 'roleAssignment'.
        :param Any principal_ids: Array of user or group identities in Azure Active Directory. The roleDefinition will apply to each identity.
        :param pulumi.Input[str] resource_scope: The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}').
        :param pulumi.Input[str] role_definition_id: Azure resource ID of the RoleDefinition.
        :param pulumi.Input[str] artifact_name: Name of the blueprint artifact.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] depends_on: Artifacts which need to be deployed before the specified artifact.
        :param pulumi.Input[str] description: Multi-line explain this resource.
        :param pulumi.Input[str] display_name: One-liner string explain this resource.
        :param pulumi.Input[str] resource_group: RoleAssignment will be scope to this resourceGroup. If empty, it scopes to the subscription.
        """
        pulumi.set(__self__, "blueprint_name", blueprint_name)
        pulumi.set(__self__, "kind", 'roleAssignment')
        pulumi.set(__self__, "principal_ids", principal_ids)
        pulumi.set(__self__, "resource_scope", resource_scope)
        pulumi.set(__self__, "role_definition_id", role_definition_id)
        if artifact_name is not None:
            pulumi.set(__self__, "artifact_name", artifact_name)
        if depends_on is not None:
            pulumi.set(__self__, "depends_on", depends_on)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if resource_group is not None:
            pulumi.set(__self__, "resource_group", resource_group)

    @property
    @pulumi.getter(name="blueprintName")
    def blueprint_name(self) -> pulumi.Input[str]:
        """
        Name of the blueprint definition.
        """
        return pulumi.get(self, "blueprint_name")

    @blueprint_name.setter
    def blueprint_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "blueprint_name", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Specifies the kind of blueprint artifact.
        Expected value is 'roleAssignment'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="principalIds")
    def principal_ids(self) -> Any:
        """
        Array of user or group identities in Azure Active Directory. The roleDefinition will apply to each identity.
        """
        return pulumi.get(self, "principal_ids")

    @principal_ids.setter
    def principal_ids(self, value: Any):
        pulumi.set(self, "principal_ids", value)

    @property
    @pulumi.getter(name="resourceScope")
    def resource_scope(self) -> pulumi.Input[str]:
        """
        The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}').
        """
        return pulumi.get(self, "resource_scope")

    @resource_scope.setter
    def resource_scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_scope", value)

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Input[str]:
        """
        Azure resource ID of the RoleDefinition.
        """
        return pulumi.get(self, "role_definition_id")

    @role_definition_id.setter
    def role_definition_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_definition_id", value)

    @property
    @pulumi.getter(name="artifactName")
    def artifact_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the blueprint artifact.
        """
        return pulumi.get(self, "artifact_name")

    @artifact_name.setter
    def artifact_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "artifact_name", value)

    @property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Artifacts which need to be deployed before the specified artifact.
        """
        return pulumi.get(self, "depends_on")

    @depends_on.setter
    def depends_on(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "depends_on", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Multi-line explain this resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        One-liner string explain this resource.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[str]]:
        """
        RoleAssignment will be scope to this resourceGroup. If empty, it scopes to the subscription.
        """
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group", value)


class RoleAssignmentArtifact(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_name: Optional[pulumi.Input[str]] = None,
                 blueprint_name: Optional[pulumi.Input[str]] = None,
                 depends_on: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 principal_ids: Optional[Any] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 resource_scope: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Blueprint artifact that applies a Role assignment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] artifact_name: Name of the blueprint artifact.
        :param pulumi.Input[str] blueprint_name: Name of the blueprint definition.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] depends_on: Artifacts which need to be deployed before the specified artifact.
        :param pulumi.Input[str] description: Multi-line explain this resource.
        :param pulumi.Input[str] display_name: One-liner string explain this resource.
        :param pulumi.Input[str] kind: Specifies the kind of blueprint artifact.
               Expected value is 'roleAssignment'.
        :param Any principal_ids: Array of user or group identities in Azure Active Directory. The roleDefinition will apply to each identity.
        :param pulumi.Input[str] resource_group: RoleAssignment will be scope to this resourceGroup. If empty, it scopes to the subscription.
        :param pulumi.Input[str] resource_scope: The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}').
        :param pulumi.Input[str] role_definition_id: Azure resource ID of the RoleDefinition.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoleAssignmentArtifactArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Blueprint artifact that applies a Role assignment.

        :param str resource_name: The name of the resource.
        :param RoleAssignmentArtifactArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoleAssignmentArtifactArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifact_name: Optional[pulumi.Input[str]] = None,
                 blueprint_name: Optional[pulumi.Input[str]] = None,
                 depends_on: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 principal_ids: Optional[Any] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 resource_scope: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoleAssignmentArtifactArgs.__new__(RoleAssignmentArtifactArgs)

            __props__.__dict__["artifact_name"] = artifact_name
            if blueprint_name is None and not opts.urn:
                raise TypeError("Missing required property 'blueprint_name'")
            __props__.__dict__["blueprint_name"] = blueprint_name
            __props__.__dict__["depends_on"] = depends_on
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'roleAssignment'
            if principal_ids is None and not opts.urn:
                raise TypeError("Missing required property 'principal_ids'")
            __props__.__dict__["principal_ids"] = principal_ids
            __props__.__dict__["resource_group"] = resource_group
            if resource_scope is None and not opts.urn:
                raise TypeError("Missing required property 'resource_scope'")
            __props__.__dict__["resource_scope"] = resource_scope
            if role_definition_id is None and not opts.urn:
                raise TypeError("Missing required property 'role_definition_id'")
            __props__.__dict__["role_definition_id"] = role_definition_id
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:blueprint:RoleAssignmentArtifact")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RoleAssignmentArtifact, __self__).__init__(
            'azure-native:blueprint/v20181101preview:RoleAssignmentArtifact',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RoleAssignmentArtifact':
        """
        Get an existing RoleAssignmentArtifact resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RoleAssignmentArtifactArgs.__new__(RoleAssignmentArtifactArgs)

        __props__.__dict__["depends_on"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["principal_ids"] = None
        __props__.__dict__["resource_group"] = None
        __props__.__dict__["role_definition_id"] = None
        __props__.__dict__["type"] = None
        return RoleAssignmentArtifact(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Artifacts which need to be deployed before the specified artifact.
        """
        return pulumi.get(self, "depends_on")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Multi-line explain this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        One-liner string explain this resource.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Specifies the kind of blueprint artifact.
        Expected value is 'roleAssignment'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalIds")
    def principal_ids(self) -> pulumi.Output[Any]:
        """
        Array of user or group identities in Azure Active Directory. The roleDefinition will apply to each identity.
        """
        return pulumi.get(self, "principal_ids")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Output[Optional[str]]:
        """
        RoleAssignment will be scope to this resourceGroup. If empty, it scopes to the subscription.
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Output[str]:
        """
        Azure resource ID of the RoleDefinition.
        """
        return pulumi.get(self, "role_definition_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")

