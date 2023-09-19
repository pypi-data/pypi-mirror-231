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
    'GetRouteMapResult',
    'AwaitableGetRouteMapResult',
    'get_route_map',
    'get_route_map_output',
]

@pulumi.output_type
class GetRouteMapResult:
    """
    The RouteMap child resource of a Virtual hub.
    """
    def __init__(__self__, associated_inbound_connections=None, associated_outbound_connections=None, etag=None, id=None, name=None, provisioning_state=None, rules=None, type=None):
        if associated_inbound_connections and not isinstance(associated_inbound_connections, list):
            raise TypeError("Expected argument 'associated_inbound_connections' to be a list")
        pulumi.set(__self__, "associated_inbound_connections", associated_inbound_connections)
        if associated_outbound_connections and not isinstance(associated_outbound_connections, list):
            raise TypeError("Expected argument 'associated_outbound_connections' to be a list")
        pulumi.set(__self__, "associated_outbound_connections", associated_outbound_connections)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="associatedInboundConnections")
    def associated_inbound_connections(self) -> Optional[Sequence[str]]:
        """
        List of connections which have this RoutMap associated for inbound traffic.
        """
        return pulumi.get(self, "associated_inbound_connections")

    @property
    @pulumi.getter(name="associatedOutboundConnections")
    def associated_outbound_connections(self) -> Optional[Sequence[str]]:
        """
        List of connections which have this RoutMap associated for outbound traffic.
        """
        return pulumi.get(self, "associated_outbound_connections")

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
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the RouteMap resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.RouteMapRuleResponse']]:
        """
        List of RouteMap rules to be applied.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetRouteMapResult(GetRouteMapResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteMapResult(
            associated_inbound_connections=self.associated_inbound_connections,
            associated_outbound_connections=self.associated_outbound_connections,
            etag=self.etag,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            rules=self.rules,
            type=self.type)


def get_route_map(resource_group_name: Optional[str] = None,
                  route_map_name: Optional[str] = None,
                  virtual_hub_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouteMapResult:
    """
    Retrieves the details of a RouteMap.


    :param str resource_group_name: The resource group name of the RouteMap's resource group.
    :param str route_map_name: The name of the RouteMap.
    :param str virtual_hub_name: The name of the VirtualHub containing the RouteMap.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['routeMapName'] = route_map_name
    __args__['virtualHubName'] = virtual_hub_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230201:getRouteMap', __args__, opts=opts, typ=GetRouteMapResult).value

    return AwaitableGetRouteMapResult(
        associated_inbound_connections=pulumi.get(__ret__, 'associated_inbound_connections'),
        associated_outbound_connections=pulumi.get(__ret__, 'associated_outbound_connections'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        rules=pulumi.get(__ret__, 'rules'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_route_map)
def get_route_map_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                         route_map_name: Optional[pulumi.Input[str]] = None,
                         virtual_hub_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouteMapResult]:
    """
    Retrieves the details of a RouteMap.


    :param str resource_group_name: The resource group name of the RouteMap's resource group.
    :param str route_map_name: The name of the RouteMap.
    :param str virtual_hub_name: The name of the VirtualHub containing the RouteMap.
    """
    ...
