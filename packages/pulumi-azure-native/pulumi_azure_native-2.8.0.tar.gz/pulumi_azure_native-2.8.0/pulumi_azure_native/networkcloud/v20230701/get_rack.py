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
    'GetRackResult',
    'AwaitableGetRackResult',
    'get_rack',
    'get_rack_output',
]

@pulumi.output_type
class GetRackResult:
    def __init__(__self__, availability_zone=None, cluster_id=None, detailed_status=None, detailed_status_message=None, extended_location=None, id=None, location=None, name=None, provisioning_state=None, rack_location=None, rack_serial_number=None, rack_sku_id=None, system_data=None, tags=None, type=None):
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if detailed_status and not isinstance(detailed_status, str):
            raise TypeError("Expected argument 'detailed_status' to be a str")
        pulumi.set(__self__, "detailed_status", detailed_status)
        if detailed_status_message and not isinstance(detailed_status_message, str):
            raise TypeError("Expected argument 'detailed_status_message' to be a str")
        pulumi.set(__self__, "detailed_status_message", detailed_status_message)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
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
        if rack_location and not isinstance(rack_location, str):
            raise TypeError("Expected argument 'rack_location' to be a str")
        pulumi.set(__self__, "rack_location", rack_location)
        if rack_serial_number and not isinstance(rack_serial_number, str):
            raise TypeError("Expected argument 'rack_serial_number' to be a str")
        pulumi.set(__self__, "rack_serial_number", rack_serial_number)
        if rack_sku_id and not isinstance(rack_sku_id, str):
            raise TypeError("Expected argument 'rack_sku_id' to be a str")
        pulumi.set(__self__, "rack_sku_id", rack_sku_id)
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
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        """
        The value that will be used for machines in this rack to represent the availability zones that can be referenced by Hybrid AKS Clusters for node arrangement.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The resource ID of the cluster the rack is created for. This value is set when the rack is created by the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> str:
        """
        The more detailed status of the rack.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> str:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the rack resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rackLocation")
    def rack_location(self) -> str:
        """
        The free-form description of the rack location. (e.g. “DTN Datacenter, Floor 3, Isle 9, Rack 2B”)
        """
        return pulumi.get(self, "rack_location")

    @property
    @pulumi.getter(name="rackSerialNumber")
    def rack_serial_number(self) -> str:
        """
        The unique identifier for the rack within Network Cloud cluster. An alternate unique alphanumeric value other than a serial number may be provided if desired.
        """
        return pulumi.get(self, "rack_serial_number")

    @property
    @pulumi.getter(name="rackSkuId")
    def rack_sku_id(self) -> str:
        """
        The SKU for the rack.
        """
        return pulumi.get(self, "rack_sku_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetRackResult(GetRackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRackResult(
            availability_zone=self.availability_zone,
            cluster_id=self.cluster_id,
            detailed_status=self.detailed_status,
            detailed_status_message=self.detailed_status_message,
            extended_location=self.extended_location,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            rack_location=self.rack_location,
            rack_serial_number=self.rack_serial_number,
            rack_sku_id=self.rack_sku_id,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_rack(rack_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRackResult:
    """
    Get properties of the provided rack.


    :param str rack_name: The name of the rack.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['rackName'] = rack_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkcloud/v20230701:getRack', __args__, opts=opts, typ=GetRackResult).value

    return AwaitableGetRackResult(
        availability_zone=pulumi.get(__ret__, 'availability_zone'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        detailed_status=pulumi.get(__ret__, 'detailed_status'),
        detailed_status_message=pulumi.get(__ret__, 'detailed_status_message'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        rack_location=pulumi.get(__ret__, 'rack_location'),
        rack_serial_number=pulumi.get(__ret__, 'rack_serial_number'),
        rack_sku_id=pulumi.get(__ret__, 'rack_sku_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_rack)
def get_rack_output(rack_name: Optional[pulumi.Input[str]] = None,
                    resource_group_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRackResult]:
    """
    Get properties of the provided rack.


    :param str rack_name: The name of the rack.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
