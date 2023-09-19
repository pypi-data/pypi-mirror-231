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
    'GetPolicyDefinitionVersionAtManagementGroupResult',
    'AwaitableGetPolicyDefinitionVersionAtManagementGroupResult',
    'get_policy_definition_version_at_management_group',
    'get_policy_definition_version_at_management_group_output',
]

@pulumi.output_type
class GetPolicyDefinitionVersionAtManagementGroupResult:
    """
    The ID of the policy definition version.
    """
    def __init__(__self__, description=None, display_name=None, id=None, metadata=None, mode=None, name=None, parameters=None, policy_rule=None, policy_type=None, system_data=None, type=None, version=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if policy_rule and not isinstance(policy_rule, dict):
            raise TypeError("Expected argument 'policy_rule' to be a dict")
        pulumi.set(__self__, "policy_rule", policy_rule)
        if policy_type and not isinstance(policy_type, str):
            raise TypeError("Expected argument 'policy_type' to be a str")
        pulumi.set(__self__, "policy_type", policy_type)
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
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The policy definition description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the policy definition.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the policy definition version.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The policy definition metadata.  Metadata is an open ended object and is typically a collection of key value pairs.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def mode(self) -> Optional[str]:
        """
        The policy definition mode. Some examples are All, Indexed, Microsoft.KeyVault.Data.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy definition version.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, 'outputs.ParameterDefinitionsValueResponse']]:
        """
        The parameter definitions for parameters used in the policy rule. The keys are the parameter names.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="policyRule")
    def policy_rule(self) -> Optional[Any]:
        """
        The policy rule.
        """
        return pulumi.get(self, "policy_rule")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[str]:
        """
        The type of policy definition. Possible values are NotSpecified, BuiltIn, Custom, and Static.
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource (Microsoft.Authorization/policyDefinitions/versions).
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The policy definition version in #.#.# format.
        """
        return pulumi.get(self, "version")


class AwaitableGetPolicyDefinitionVersionAtManagementGroupResult(GetPolicyDefinitionVersionAtManagementGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyDefinitionVersionAtManagementGroupResult(
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            metadata=self.metadata,
            mode=self.mode,
            name=self.name,
            parameters=self.parameters,
            policy_rule=self.policy_rule,
            policy_type=self.policy_type,
            system_data=self.system_data,
            type=self.type,
            version=self.version)


def get_policy_definition_version_at_management_group(management_group_name: Optional[str] = None,
                                                      policy_definition_name: Optional[str] = None,
                                                      policy_definition_version: Optional[str] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyDefinitionVersionAtManagementGroupResult:
    """
    This operation retrieves the policy definition version in the given management group with the given name.
    Azure REST API version: 2023-04-01.


    :param str management_group_name: The name of the management group. The name is case insensitive.
    :param str policy_definition_name: The name of the policy definition.
    :param str policy_definition_version: The policy definition version.  The format is x.y.z where x is the major version number, y is the minor version number, and z is the patch number
    """
    __args__ = dict()
    __args__['managementGroupName'] = management_group_name
    __args__['policyDefinitionName'] = policy_definition_name
    __args__['policyDefinitionVersion'] = policy_definition_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:authorization:getPolicyDefinitionVersionAtManagementGroup', __args__, opts=opts, typ=GetPolicyDefinitionVersionAtManagementGroupResult).value

    return AwaitableGetPolicyDefinitionVersionAtManagementGroupResult(
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        metadata=pulumi.get(__ret__, 'metadata'),
        mode=pulumi.get(__ret__, 'mode'),
        name=pulumi.get(__ret__, 'name'),
        parameters=pulumi.get(__ret__, 'parameters'),
        policy_rule=pulumi.get(__ret__, 'policy_rule'),
        policy_type=pulumi.get(__ret__, 'policy_type'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_policy_definition_version_at_management_group)
def get_policy_definition_version_at_management_group_output(management_group_name: Optional[pulumi.Input[str]] = None,
                                                             policy_definition_name: Optional[pulumi.Input[str]] = None,
                                                             policy_definition_version: Optional[pulumi.Input[str]] = None,
                                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPolicyDefinitionVersionAtManagementGroupResult]:
    """
    This operation retrieves the policy definition version in the given management group with the given name.
    Azure REST API version: 2023-04-01.


    :param str management_group_name: The name of the management group. The name is case insensitive.
    :param str policy_definition_name: The name of the policy definition.
    :param str policy_definition_version: The policy definition version.  The format is x.y.z where x is the major version number, y is the minor version number, and z is the patch number
    """
    ...
