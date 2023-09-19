# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetServerCommunicationLinkResult',
    'AwaitableGetServerCommunicationLinkResult',
    'get_server_communication_link',
    'get_server_communication_link_output',
]

@pulumi.output_type
class GetServerCommunicationLinkResult:
    """
    Server communication link.
    """
    def __init__(__self__, id=None, kind=None, location=None, name=None, partner_server=None, state=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partner_server and not isinstance(partner_server, str):
            raise TypeError("Expected argument 'partner_server' to be a str")
        pulumi.set(__self__, "partner_server", partner_server)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Communication link kind.  This property is used for Azure Portal metadata.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Communication link location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerServer")
    def partner_server(self) -> str:
        """
        The name of the partner server.
        """
        return pulumi.get(self, "partner_server")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetServerCommunicationLinkResult(GetServerCommunicationLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerCommunicationLinkResult(
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            partner_server=self.partner_server,
            state=self.state,
            type=self.type)


def get_server_communication_link(communication_link_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  server_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerCommunicationLinkResult:
    """
    Returns a server communication link.


    :param str communication_link_name: The name of the server communication link.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['communicationLinkName'] = communication_link_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20140401:getServerCommunicationLink', __args__, opts=opts, typ=GetServerCommunicationLinkResult).value

    return AwaitableGetServerCommunicationLinkResult(
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        partner_server=pulumi.get(__ret__, 'partner_server'),
        state=pulumi.get(__ret__, 'state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_server_communication_link)
def get_server_communication_link_output(communication_link_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         server_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerCommunicationLinkResult]:
    """
    Returns a server communication link.


    :param str communication_link_name: The name of the server communication link.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
