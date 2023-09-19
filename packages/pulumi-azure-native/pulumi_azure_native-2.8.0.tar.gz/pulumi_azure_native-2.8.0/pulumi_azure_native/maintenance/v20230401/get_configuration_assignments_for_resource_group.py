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
    'GetConfigurationAssignmentsForResourceGroupResult',
    'AwaitableGetConfigurationAssignmentsForResourceGroupResult',
    'get_configuration_assignments_for_resource_group',
    'get_configuration_assignments_for_resource_group_output',
]

@pulumi.output_type
class GetConfigurationAssignmentsForResourceGroupResult:
    """
    Configuration Assignment
    """
    def __init__(__self__, filter=None, id=None, location=None, maintenance_configuration_id=None, name=None, resource_id=None, system_data=None, type=None):
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_configuration_id and not isinstance(maintenance_configuration_id, str):
            raise TypeError("Expected argument 'maintenance_configuration_id' to be a str")
        pulumi.set(__self__, "maintenance_configuration_id", maintenance_configuration_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.ConfigurationAssignmentFilterPropertiesResponse']:
        """
        Properties of the configuration assignment
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Location of the resource
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(self) -> Optional[str]:
        """
        The maintenance configuration Id
        """
        return pulumi.get(self, "maintenance_configuration_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        The unique resourceId
        """
        return pulumi.get(self, "resource_id")

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
        Type of the resource
        """
        return pulumi.get(self, "type")


class AwaitableGetConfigurationAssignmentsForResourceGroupResult(GetConfigurationAssignmentsForResourceGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationAssignmentsForResourceGroupResult(
            filter=self.filter,
            id=self.id,
            location=self.location,
            maintenance_configuration_id=self.maintenance_configuration_id,
            name=self.name,
            resource_id=self.resource_id,
            system_data=self.system_data,
            type=self.type)


def get_configuration_assignments_for_resource_group(configuration_assignment_name: Optional[str] = None,
                                                     resource_group_name: Optional[str] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationAssignmentsForResourceGroupResult:
    """
    Get configuration assignment for resource..


    :param str configuration_assignment_name: Configuration assignment name
    :param str resource_group_name: Resource group name
    """
    __args__ = dict()
    __args__['configurationAssignmentName'] = configuration_assignment_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:maintenance/v20230401:getConfigurationAssignmentsForResourceGroup', __args__, opts=opts, typ=GetConfigurationAssignmentsForResourceGroupResult).value

    return AwaitableGetConfigurationAssignmentsForResourceGroupResult(
        filter=pulumi.get(__ret__, 'filter'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_configuration_id=pulumi.get(__ret__, 'maintenance_configuration_id'),
        name=pulumi.get(__ret__, 'name'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_configuration_assignments_for_resource_group)
def get_configuration_assignments_for_resource_group_output(configuration_assignment_name: Optional[pulumi.Input[str]] = None,
                                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationAssignmentsForResourceGroupResult]:
    """
    Get configuration assignment for resource..


    :param str configuration_assignment_name: Configuration assignment name
    :param str resource_group_name: Resource group name
    """
    ...
