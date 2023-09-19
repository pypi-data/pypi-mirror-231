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

__all__ = [
    'GetBlueprintResult',
    'AwaitableGetBlueprintResult',
    'get_blueprint',
    'get_blueprint_output',
]

@pulumi.output_type
class GetBlueprintResult:
    """
    Represents a Blueprint definition.
    """
    def __init__(__self__, description=None, display_name=None, id=None, layout=None, name=None, parameters=None, resource_groups=None, status=None, target_scope=None, type=None, versions=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if layout and not isinstance(layout, dict):
            raise TypeError("Expected argument 'layout' to be a dict")
        pulumi.set(__self__, "layout", layout)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if resource_groups and not isinstance(resource_groups, dict):
            raise TypeError("Expected argument 'resource_groups' to be a dict")
        pulumi.set(__self__, "resource_groups", resource_groups)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if target_scope and not isinstance(target_scope, str):
            raise TypeError("Expected argument 'target_scope' to be a str")
        pulumi.set(__self__, "target_scope", target_scope)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if versions and not isinstance(versions, dict):
            raise TypeError("Expected argument 'versions' to be a dict")
        pulumi.set(__self__, "versions", versions)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Multi-line explain this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        One-liner string explain this resource.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        String Id used to locate any resource on Azure.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def layout(self) -> Any:
        """
        Layout view of the blueprint definition for UI reference.
        """
        return pulumi.get(self, "layout")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, 'outputs.ParameterDefinitionResponse']]:
        """
        Parameters required by this blueprint definition.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Optional[Mapping[str, 'outputs.ResourceGroupDefinitionResponse']]:
        """
        Resource group placeholders defined by this blueprint definition.
        """
        return pulumi.get(self, "resource_groups")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.BlueprintStatusResponse':
        """
        Status of the blueprint. This field is readonly.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="targetScope")
    def target_scope(self) -> str:
        """
        The scope where this blueprint definition can be assigned.
        """
        return pulumi.get(self, "target_scope")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def versions(self) -> Optional[Any]:
        """
        Published versions of this blueprint definition.
        """
        return pulumi.get(self, "versions")


class AwaitableGetBlueprintResult(GetBlueprintResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBlueprintResult(
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            layout=self.layout,
            name=self.name,
            parameters=self.parameters,
            resource_groups=self.resource_groups,
            status=self.status,
            target_scope=self.target_scope,
            type=self.type,
            versions=self.versions)


def get_blueprint(blueprint_name: Optional[str] = None,
                  resource_scope: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBlueprintResult:
    """
    Get a blueprint definition.


    :param str blueprint_name: Name of the blueprint definition.
    :param str resource_scope: The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}').
    """
    __args__ = dict()
    __args__['blueprintName'] = blueprint_name
    __args__['resourceScope'] = resource_scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:blueprint/v20181101preview:getBlueprint', __args__, opts=opts, typ=GetBlueprintResult).value

    return AwaitableGetBlueprintResult(
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        layout=pulumi.get(__ret__, 'layout'),
        name=pulumi.get(__ret__, 'name'),
        parameters=pulumi.get(__ret__, 'parameters'),
        resource_groups=pulumi.get(__ret__, 'resource_groups'),
        status=pulumi.get(__ret__, 'status'),
        target_scope=pulumi.get(__ret__, 'target_scope'),
        type=pulumi.get(__ret__, 'type'),
        versions=pulumi.get(__ret__, 'versions'))


@_utilities.lift_output_func(get_blueprint)
def get_blueprint_output(blueprint_name: Optional[pulumi.Input[str]] = None,
                         resource_scope: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBlueprintResult]:
    """
    Get a blueprint definition.


    :param str blueprint_name: Name of the blueprint definition.
    :param str resource_scope: The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}').
    """
    ...
