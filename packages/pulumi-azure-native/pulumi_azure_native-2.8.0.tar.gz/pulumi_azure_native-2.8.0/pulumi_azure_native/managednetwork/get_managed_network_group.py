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
    'GetManagedNetworkGroupResult',
    'AwaitableGetManagedNetworkGroupResult',
    'get_managed_network_group',
    'get_managed_network_group_output',
]

@pulumi.output_type
class GetManagedNetworkGroupResult:
    """
    The Managed Network Group resource
    """
    def __init__(__self__, etag=None, id=None, kind=None, location=None, management_groups=None, name=None, provisioning_state=None, subnets=None, subscriptions=None, type=None, virtual_networks=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if management_groups and not isinstance(management_groups, list):
            raise TypeError("Expected argument 'management_groups' to be a list")
        pulumi.set(__self__, "management_groups", management_groups)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if subnets and not isinstance(subnets, list):
            raise TypeError("Expected argument 'subnets' to be a list")
        pulumi.set(__self__, "subnets", subnets)
        if subscriptions and not isinstance(subscriptions, list):
            raise TypeError("Expected argument 'subscriptions' to be a list")
        pulumi.set(__self__, "subscriptions", subscriptions)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_networks and not isinstance(virtual_networks, list):
            raise TypeError("Expected argument 'virtual_networks' to be a list")
        pulumi.set(__self__, "virtual_networks", virtual_networks)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Responsibility role under which this Managed Network Group will be created
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of management groups covered by the Managed Network
        """
        return pulumi.get(self, "management_groups")

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
        Provisioning state of the ManagedNetwork resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def subnets(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of  subnets covered by the Managed Network
        """
        return pulumi.get(self, "subnets")

    @property
    @pulumi.getter
    def subscriptions(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of subscriptions covered by the Managed Network
        """
        return pulumi.get(self, "subscriptions")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> Optional[Sequence['outputs.ResourceIdResponse']]:
        """
        The collection of virtual nets covered by the Managed Network
        """
        return pulumi.get(self, "virtual_networks")


class AwaitableGetManagedNetworkGroupResult(GetManagedNetworkGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedNetworkGroupResult(
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            location=self.location,
            management_groups=self.management_groups,
            name=self.name,
            provisioning_state=self.provisioning_state,
            subnets=self.subnets,
            subscriptions=self.subscriptions,
            type=self.type,
            virtual_networks=self.virtual_networks)


def get_managed_network_group(managed_network_group_name: Optional[str] = None,
                              managed_network_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedNetworkGroupResult:
    """
    The Get ManagedNetworkGroups operation gets a Managed Network Group specified by the resource group, Managed Network name, and group name
    Azure REST API version: 2019-06-01-preview.


    :param str managed_network_group_name: The name of the Managed Network Group.
    :param str managed_network_name: The name of the Managed Network.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['managedNetworkGroupName'] = managed_network_group_name
    __args__['managedNetworkName'] = managed_network_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetwork:getManagedNetworkGroup', __args__, opts=opts, typ=GetManagedNetworkGroupResult).value

    return AwaitableGetManagedNetworkGroupResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        management_groups=pulumi.get(__ret__, 'management_groups'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        subnets=pulumi.get(__ret__, 'subnets'),
        subscriptions=pulumi.get(__ret__, 'subscriptions'),
        type=pulumi.get(__ret__, 'type'),
        virtual_networks=pulumi.get(__ret__, 'virtual_networks'))


@_utilities.lift_output_func(get_managed_network_group)
def get_managed_network_group_output(managed_network_group_name: Optional[pulumi.Input[str]] = None,
                                     managed_network_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedNetworkGroupResult]:
    """
    The Get ManagedNetworkGroups operation gets a Managed Network Group specified by the resource group, Managed Network name, and group name
    Azure REST API version: 2019-06-01-preview.


    :param str managed_network_group_name: The name of the Managed Network Group.
    :param str managed_network_name: The name of the Managed Network.
    :param str resource_group_name: The name of the resource group.
    """
    ...
