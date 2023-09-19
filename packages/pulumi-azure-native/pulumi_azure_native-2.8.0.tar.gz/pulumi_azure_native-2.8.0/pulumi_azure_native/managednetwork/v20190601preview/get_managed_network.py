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
    'GetManagedNetworkResult',
    'AwaitableGetManagedNetworkResult',
    'get_managed_network',
    'get_managed_network_output',
]

@pulumi.output_type
class GetManagedNetworkResult:
    """
    The Managed Network resource
    """
    def __init__(__self__, connectivity=None, etag=None, id=None, location=None, name=None, provisioning_state=None, scope=None, tags=None, type=None):
        if connectivity and not isinstance(connectivity, dict):
            raise TypeError("Expected argument 'connectivity' to be a dict")
        pulumi.set(__self__, "connectivity", connectivity)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
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
        if scope and not isinstance(scope, dict):
            raise TypeError("Expected argument 'scope' to be a dict")
        pulumi.set(__self__, "scope", scope)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def connectivity(self) -> 'outputs.ConnectivityCollectionResponse':
        """
        The collection of groups and policies concerned with connectivity
        """
        return pulumi.get(self, "connectivity")

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
        Provisioning state of the ManagedNetwork resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def scope(self) -> Optional['outputs.ScopeResponse']:
        """
        The collection of management groups, subscriptions, virtual networks, and subnets by the Managed Network. This is a read-only property that is reflective of all ScopeAssignments for this Managed Network
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedNetworkResult(GetManagedNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedNetworkResult(
            connectivity=self.connectivity,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            scope=self.scope,
            tags=self.tags,
            type=self.type)


def get_managed_network(managed_network_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedNetworkResult:
    """
    The Get ManagedNetworks operation gets a Managed Network Resource, specified by the resource group and Managed Network name


    :param str managed_network_name: The name of the Managed Network.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['managedNetworkName'] = managed_network_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetwork/v20190601preview:getManagedNetwork', __args__, opts=opts, typ=GetManagedNetworkResult).value

    return AwaitableGetManagedNetworkResult(
        connectivity=pulumi.get(__ret__, 'connectivity'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        scope=pulumi.get(__ret__, 'scope'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_managed_network)
def get_managed_network_output(managed_network_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedNetworkResult]:
    """
    The Get ManagedNetworks operation gets a Managed Network Resource, specified by the resource group and Managed Network name


    :param str managed_network_name: The name of the Managed Network.
    :param str resource_group_name: The name of the resource group.
    """
    ...
