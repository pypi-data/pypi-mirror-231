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
    'GetWCFRelayResult',
    'AwaitableGetWCFRelayResult',
    'get_wcf_relay',
    'get_wcf_relay_output',
]

@pulumi.output_type
class GetWCFRelayResult:
    """
    Description of the WCF relay resource.
    """
    def __init__(__self__, created_at=None, id=None, is_dynamic=None, listener_count=None, location=None, name=None, relay_type=None, requires_client_authorization=None, requires_transport_security=None, system_data=None, type=None, updated_at=None, user_metadata=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_dynamic and not isinstance(is_dynamic, bool):
            raise TypeError("Expected argument 'is_dynamic' to be a bool")
        pulumi.set(__self__, "is_dynamic", is_dynamic)
        if listener_count and not isinstance(listener_count, int):
            raise TypeError("Expected argument 'listener_count' to be a int")
        pulumi.set(__self__, "listener_count", listener_count)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if relay_type and not isinstance(relay_type, str):
            raise TypeError("Expected argument 'relay_type' to be a str")
        pulumi.set(__self__, "relay_type", relay_type)
        if requires_client_authorization and not isinstance(requires_client_authorization, bool):
            raise TypeError("Expected argument 'requires_client_authorization' to be a bool")
        pulumi.set(__self__, "requires_client_authorization", requires_client_authorization)
        if requires_transport_security and not isinstance(requires_transport_security, bool):
            raise TypeError("Expected argument 'requires_transport_security' to be a bool")
        pulumi.set(__self__, "requires_transport_security", requires_transport_security)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if user_metadata and not isinstance(user_metadata, str):
            raise TypeError("Expected argument 'user_metadata' to be a str")
        pulumi.set(__self__, "user_metadata", user_metadata)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time the WCF relay was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDynamic")
    def is_dynamic(self) -> bool:
        """
        Returns true if the relay is dynamic; otherwise, false.
        """
        return pulumi.get(self, "is_dynamic")

    @property
    @pulumi.getter(name="listenerCount")
    def listener_count(self) -> int:
        """
        The number of listeners for this relay. Note that min :1 and max:25 are supported.
        """
        return pulumi.get(self, "listener_count")

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
    @pulumi.getter(name="relayType")
    def relay_type(self) -> Optional[str]:
        """
        WCF relay type.
        """
        return pulumi.get(self, "relay_type")

    @property
    @pulumi.getter(name="requiresClientAuthorization")
    def requires_client_authorization(self) -> Optional[bool]:
        """
        Returns true if client authorization is needed for this relay; otherwise, false.
        """
        return pulumi.get(self, "requires_client_authorization")

    @property
    @pulumi.getter(name="requiresTransportSecurity")
    def requires_transport_security(self) -> Optional[bool]:
        """
        Returns true if transport security is needed for this relay; otherwise, false.
        """
        return pulumi.get(self, "requires_transport_security")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The time the namespace was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="userMetadata")
    def user_metadata(self) -> Optional[str]:
        """
        The usermetadata is a placeholder to store user-defined string data for the WCF Relay endpoint. For example, it can be used to store descriptive data, such as list of teams and their contact information. Also, user-defined configuration settings can be stored.
        """
        return pulumi.get(self, "user_metadata")


class AwaitableGetWCFRelayResult(GetWCFRelayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWCFRelayResult(
            created_at=self.created_at,
            id=self.id,
            is_dynamic=self.is_dynamic,
            listener_count=self.listener_count,
            location=self.location,
            name=self.name,
            relay_type=self.relay_type,
            requires_client_authorization=self.requires_client_authorization,
            requires_transport_security=self.requires_transport_security,
            system_data=self.system_data,
            type=self.type,
            updated_at=self.updated_at,
            user_metadata=self.user_metadata)


def get_wcf_relay(namespace_name: Optional[str] = None,
                  relay_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWCFRelayResult:
    """
    Returns the description for the specified WCF relay.
    Azure REST API version: 2021-11-01.


    :param str namespace_name: The namespace name
    :param str relay_name: The relay name.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    __args__['relayName'] = relay_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:relay:getWCFRelay', __args__, opts=opts, typ=GetWCFRelayResult).value

    return AwaitableGetWCFRelayResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        id=pulumi.get(__ret__, 'id'),
        is_dynamic=pulumi.get(__ret__, 'is_dynamic'),
        listener_count=pulumi.get(__ret__, 'listener_count'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        relay_type=pulumi.get(__ret__, 'relay_type'),
        requires_client_authorization=pulumi.get(__ret__, 'requires_client_authorization'),
        requires_transport_security=pulumi.get(__ret__, 'requires_transport_security'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        user_metadata=pulumi.get(__ret__, 'user_metadata'))


@_utilities.lift_output_func(get_wcf_relay)
def get_wcf_relay_output(namespace_name: Optional[pulumi.Input[str]] = None,
                         relay_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWCFRelayResult]:
    """
    Returns the description for the specified WCF relay.
    Azure REST API version: 2021-11-01.


    :param str namespace_name: The namespace name
    :param str relay_name: The relay name.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...
