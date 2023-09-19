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
    'GetPoolResult',
    'AwaitableGetPoolResult',
    'get_pool',
    'get_pool_output',
]

@pulumi.output_type
class GetPoolResult:
    """
    A pool of Virtual Machines.
    """
    def __init__(__self__, dev_box_definition_name=None, health_status=None, health_status_details=None, id=None, license_type=None, local_administrator=None, location=None, name=None, network_connection_name=None, provisioning_state=None, stop_on_disconnect=None, system_data=None, tags=None, type=None):
        if dev_box_definition_name and not isinstance(dev_box_definition_name, str):
            raise TypeError("Expected argument 'dev_box_definition_name' to be a str")
        pulumi.set(__self__, "dev_box_definition_name", dev_box_definition_name)
        if health_status and not isinstance(health_status, str):
            raise TypeError("Expected argument 'health_status' to be a str")
        pulumi.set(__self__, "health_status", health_status)
        if health_status_details and not isinstance(health_status_details, list):
            raise TypeError("Expected argument 'health_status_details' to be a list")
        pulumi.set(__self__, "health_status_details", health_status_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if license_type and not isinstance(license_type, str):
            raise TypeError("Expected argument 'license_type' to be a str")
        pulumi.set(__self__, "license_type", license_type)
        if local_administrator and not isinstance(local_administrator, str):
            raise TypeError("Expected argument 'local_administrator' to be a str")
        pulumi.set(__self__, "local_administrator", local_administrator)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_connection_name and not isinstance(network_connection_name, str):
            raise TypeError("Expected argument 'network_connection_name' to be a str")
        pulumi.set(__self__, "network_connection_name", network_connection_name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if stop_on_disconnect and not isinstance(stop_on_disconnect, dict):
            raise TypeError("Expected argument 'stop_on_disconnect' to be a dict")
        pulumi.set(__self__, "stop_on_disconnect", stop_on_disconnect)
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
    @pulumi.getter(name="devBoxDefinitionName")
    def dev_box_definition_name(self) -> str:
        """
        Name of a Dev Box definition in parent Project of this Pool
        """
        return pulumi.get(self, "dev_box_definition_name")

    @property
    @pulumi.getter(name="healthStatus")
    def health_status(self) -> str:
        """
        Overall health status of the Pool. Indicates whether or not the Pool is available to create Dev Boxes.
        """
        return pulumi.get(self, "health_status")

    @property
    @pulumi.getter(name="healthStatusDetails")
    def health_status_details(self) -> Sequence['outputs.HealthStatusDetailResponse']:
        """
        Details on the Pool health status to help diagnose issues. This is only populated when the pool status indicates the pool is in a non-healthy state
        """
        return pulumi.get(self, "health_status_details")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> str:
        """
        Specifies the license type indicating the caller has already acquired licenses for the Dev Boxes that will be created.
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter(name="localAdministrator")
    def local_administrator(self) -> str:
        """
        Indicates whether owners of Dev Boxes in this pool are added as local administrators on the Dev Box.
        """
        return pulumi.get(self, "local_administrator")

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
    @pulumi.getter(name="networkConnectionName")
    def network_connection_name(self) -> str:
        """
        Name of a Network Connection in parent Project of this Pool
        """
        return pulumi.get(self, "network_connection_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="stopOnDisconnect")
    def stop_on_disconnect(self) -> Optional['outputs.StopOnDisconnectConfigurationResponse']:
        """
        Stop on disconnect configuration settings for Dev Boxes created in this pool.
        """
        return pulumi.get(self, "stop_on_disconnect")

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


class AwaitableGetPoolResult(GetPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPoolResult(
            dev_box_definition_name=self.dev_box_definition_name,
            health_status=self.health_status,
            health_status_details=self.health_status_details,
            id=self.id,
            license_type=self.license_type,
            local_administrator=self.local_administrator,
            location=self.location,
            name=self.name,
            network_connection_name=self.network_connection_name,
            provisioning_state=self.provisioning_state,
            stop_on_disconnect=self.stop_on_disconnect,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_pool(pool_name: Optional[str] = None,
             project_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPoolResult:
    """
    Gets a machine pool


    :param str pool_name: Name of the pool.
    :param str project_name: The name of the project.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['poolName'] = pool_name
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20230401:getPool', __args__, opts=opts, typ=GetPoolResult).value

    return AwaitableGetPoolResult(
        dev_box_definition_name=pulumi.get(__ret__, 'dev_box_definition_name'),
        health_status=pulumi.get(__ret__, 'health_status'),
        health_status_details=pulumi.get(__ret__, 'health_status_details'),
        id=pulumi.get(__ret__, 'id'),
        license_type=pulumi.get(__ret__, 'license_type'),
        local_administrator=pulumi.get(__ret__, 'local_administrator'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_connection_name=pulumi.get(__ret__, 'network_connection_name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        stop_on_disconnect=pulumi.get(__ret__, 'stop_on_disconnect'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_pool)
def get_pool_output(pool_name: Optional[pulumi.Input[str]] = None,
                    project_name: Optional[pulumi.Input[str]] = None,
                    resource_group_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPoolResult]:
    """
    Gets a machine pool


    :param str pool_name: Name of the pool.
    :param str project_name: The name of the project.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
