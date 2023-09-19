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
    'GetLabResult',
    'AwaitableGetLabResult',
    'get_lab',
    'get_lab_output',
]

@pulumi.output_type
class GetLabResult:
    """
    The lab resource.
    """
    def __init__(__self__, auto_shutdown_profile=None, connection_profile=None, description=None, id=None, lab_plan_id=None, location=None, name=None, network_profile=None, provisioning_state=None, roster_profile=None, security_profile=None, state=None, system_data=None, tags=None, title=None, type=None, virtual_machine_profile=None):
        if auto_shutdown_profile and not isinstance(auto_shutdown_profile, dict):
            raise TypeError("Expected argument 'auto_shutdown_profile' to be a dict")
        pulumi.set(__self__, "auto_shutdown_profile", auto_shutdown_profile)
        if connection_profile and not isinstance(connection_profile, dict):
            raise TypeError("Expected argument 'connection_profile' to be a dict")
        pulumi.set(__self__, "connection_profile", connection_profile)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lab_plan_id and not isinstance(lab_plan_id, str):
            raise TypeError("Expected argument 'lab_plan_id' to be a str")
        pulumi.set(__self__, "lab_plan_id", lab_plan_id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if roster_profile and not isinstance(roster_profile, dict):
            raise TypeError("Expected argument 'roster_profile' to be a dict")
        pulumi.set(__self__, "roster_profile", roster_profile)
        if security_profile and not isinstance(security_profile, dict):
            raise TypeError("Expected argument 'security_profile' to be a dict")
        pulumi.set(__self__, "security_profile", security_profile)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_machine_profile and not isinstance(virtual_machine_profile, dict):
            raise TypeError("Expected argument 'virtual_machine_profile' to be a dict")
        pulumi.set(__self__, "virtual_machine_profile", virtual_machine_profile)

    @property
    @pulumi.getter(name="autoShutdownProfile")
    def auto_shutdown_profile(self) -> 'outputs.AutoShutdownProfileResponse':
        """
        The resource auto shutdown configuration for the lab. This controls whether actions are taken on resources that are sitting idle.
        """
        return pulumi.get(self, "auto_shutdown_profile")

    @property
    @pulumi.getter(name="connectionProfile")
    def connection_profile(self) -> 'outputs.ConnectionProfileResponse':
        """
        The connection profile for the lab. This controls settings such as web access to lab resources or whether RDP or SSH ports are open.
        """
        return pulumi.get(self, "connection_profile")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the lab.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="labPlanId")
    def lab_plan_id(self) -> Optional[str]:
        """
        The ID of the lab plan. Used during resource creation to provide defaults and acts as a permission container when creating a lab via labs.azure.com. Setting a labPlanId on an existing lab provides organization..
        """
        return pulumi.get(self, "lab_plan_id")

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
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional['outputs.LabNetworkProfileResponse']:
        """
        The network profile for the lab, typically applied via a lab plan. This profile cannot be modified once a lab has been created.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Current provisioning state of the lab.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rosterProfile")
    def roster_profile(self) -> Optional['outputs.RosterProfileResponse']:
        """
        The lab user list management profile.
        """
        return pulumi.get(self, "roster_profile")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> 'outputs.SecurityProfileResponse':
        """
        The lab security profile.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The lab state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the lab.
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
    def title(self) -> Optional[str]:
        """
        The title of the lab.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(self) -> 'outputs.VirtualMachineProfileResponse':
        """
        The profile used for creating lab virtual machines.
        """
        return pulumi.get(self, "virtual_machine_profile")


class AwaitableGetLabResult(GetLabResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLabResult(
            auto_shutdown_profile=self.auto_shutdown_profile,
            connection_profile=self.connection_profile,
            description=self.description,
            id=self.id,
            lab_plan_id=self.lab_plan_id,
            location=self.location,
            name=self.name,
            network_profile=self.network_profile,
            provisioning_state=self.provisioning_state,
            roster_profile=self.roster_profile,
            security_profile=self.security_profile,
            state=self.state,
            system_data=self.system_data,
            tags=self.tags,
            title=self.title,
            type=self.type,
            virtual_machine_profile=self.virtual_machine_profile)


def get_lab(lab_name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLabResult:
    """
    Returns the properties of a lab resource.


    :param str lab_name: The name of the lab that uniquely identifies it within containing lab plan. Used in resource URIs.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['labName'] = lab_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:labservices/v20220801:getLab', __args__, opts=opts, typ=GetLabResult).value

    return AwaitableGetLabResult(
        auto_shutdown_profile=pulumi.get(__ret__, 'auto_shutdown_profile'),
        connection_profile=pulumi.get(__ret__, 'connection_profile'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        lab_plan_id=pulumi.get(__ret__, 'lab_plan_id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_profile=pulumi.get(__ret__, 'network_profile'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        roster_profile=pulumi.get(__ret__, 'roster_profile'),
        security_profile=pulumi.get(__ret__, 'security_profile'),
        state=pulumi.get(__ret__, 'state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        title=pulumi.get(__ret__, 'title'),
        type=pulumi.get(__ret__, 'type'),
        virtual_machine_profile=pulumi.get(__ret__, 'virtual_machine_profile'))


@_utilities.lift_output_func(get_lab)
def get_lab_output(lab_name: Optional[pulumi.Input[str]] = None,
                   resource_group_name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLabResult]:
    """
    Returns the properties of a lab resource.


    :param str lab_name: The name of the lab that uniquely identifies it within containing lab plan. Used in resource URIs.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
