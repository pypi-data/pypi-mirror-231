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
    'GetAutoScaleVCoreResult',
    'AwaitableGetAutoScaleVCoreResult',
    'get_auto_scale_v_core',
    'get_auto_scale_v_core_output',
]

@pulumi.output_type
class GetAutoScaleVCoreResult:
    """
    Represents an instance of an auto scale v-core resource.
    """
    def __init__(__self__, capacity_limit=None, capacity_object_id=None, id=None, location=None, name=None, provisioning_state=None, sku=None, system_data=None, tags=None, type=None):
        if capacity_limit and not isinstance(capacity_limit, int):
            raise TypeError("Expected argument 'capacity_limit' to be a int")
        pulumi.set(__self__, "capacity_limit", capacity_limit)
        if capacity_object_id and not isinstance(capacity_object_id, str):
            raise TypeError("Expected argument 'capacity_object_id' to be a str")
        pulumi.set(__self__, "capacity_object_id", capacity_object_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="capacityLimit")
    def capacity_limit(self) -> Optional[int]:
        """
        The maximum capacity of an auto scale v-core resource.
        """
        return pulumi.get(self, "capacity_limit")

    @property
    @pulumi.getter(name="capacityObjectId")
    def capacity_object_id(self) -> Optional[str]:
        """
        The object ID of the capacity resource associated with the auto scale v-core resource.
        """
        return pulumi.get(self, "capacity_object_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        An identifier that represents the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment state of an auto scale v-core resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.AutoScaleVCoreSkuResponse':
        """
        The SKU of the auto scale v-core resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> Optional['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Key-value pairs of additional resource provisioning properties.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetAutoScaleVCoreResult(GetAutoScaleVCoreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutoScaleVCoreResult(
            capacity_limit=self.capacity_limit,
            capacity_object_id=self.capacity_object_id,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_auto_scale_v_core(resource_group_name: Optional[str] = None,
                          vcore_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutoScaleVCoreResult:
    """
    Gets details about the specified auto scale v-core.
    Azure REST API version: 2021-01-01.


    :param str resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    :param str vcore_name: The name of the auto scale v-core. It must be a minimum of 3 characters, and a maximum of 63.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['vcoreName'] = vcore_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:powerbidedicated:getAutoScaleVCore', __args__, opts=opts, typ=GetAutoScaleVCoreResult).value

    return AwaitableGetAutoScaleVCoreResult(
        capacity_limit=pulumi.get(__ret__, 'capacity_limit'),
        capacity_object_id=pulumi.get(__ret__, 'capacity_object_id'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_auto_scale_v_core)
def get_auto_scale_v_core_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                 vcore_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAutoScaleVCoreResult]:
    """
    Gets details about the specified auto scale v-core.
    Azure REST API version: 2021-01-01.


    :param str resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    :param str vcore_name: The name of the auto scale v-core. It must be a minimum of 3 characters, and a maximum of 63.
    """
    ...
