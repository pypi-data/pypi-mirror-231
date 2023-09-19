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
    'GetDraResult',
    'AwaitableGetDraResult',
    'get_dra',
    'get_dra_output',
]

@pulumi.output_type
class GetDraResult:
    """
    Dra model.
    """
    def __init__(__self__, id=None, name=None, properties=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Gets or sets the Id of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets or sets the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.DraModelPropertiesResponse':
        """
        Dra model properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.DraModelResponseSystemData':
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets or sets the type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetDraResult(GetDraResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDraResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_dra(fabric_agent_name: Optional[str] = None,
            fabric_name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDraResult:
    """
    Gets the details of the fabric agent.


    :param str fabric_agent_name: The fabric agent (Dra) name.
    :param str fabric_name: The fabric name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['fabricAgentName'] = fabric_agent_name
    __args__['fabricName'] = fabric_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datareplication/v20210216preview:getDra', __args__, opts=opts, typ=GetDraResult).value

    return AwaitableGetDraResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_dra)
def get_dra_output(fabric_agent_name: Optional[pulumi.Input[str]] = None,
                   fabric_name: Optional[pulumi.Input[str]] = None,
                   resource_group_name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDraResult]:
    """
    Gets the details of the fabric agent.


    :param str fabric_agent_name: The fabric agent (Dra) name.
    :param str fabric_name: The fabric name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
