# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'ApiEntityReferenceArgs',
    'CloudHsmClusterSecurityDomainPropertiesArgs',
    'CloudHsmClusterSkuArgs',
    'CloudHsmPropertiesArgs',
    'NetworkInterfaceArgs',
    'NetworkProfileArgs',
    'PrivateEndpointConnectionArgs',
    'PrivateLinkServiceConnectionStateArgs',
    'SkuArgs',
]

@pulumi.input_type
class ApiEntityReferenceArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        The API entity reference.
        :param pulumi.Input[str] id: The ARM resource id in the form of /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ARM resource id in the form of /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class CloudHsmClusterSecurityDomainPropertiesArgs:
    def __init__(__self__, *,
                 activation_status: Optional[pulumi.Input[str]] = None,
                 fips_state: Optional[pulumi.Input[int]] = None):
        """
        Security domain properties information for Cloud HSM cluster
        :param pulumi.Input[str] activation_status: status of security domain activation
        :param pulumi.Input[int] fips_state: FIPS state information for security domain
        """
        if activation_status is not None:
            pulumi.set(__self__, "activation_status", activation_status)
        if fips_state is not None:
            pulumi.set(__self__, "fips_state", fips_state)

    @property
    @pulumi.getter(name="activationStatus")
    def activation_status(self) -> Optional[pulumi.Input[str]]:
        """
        status of security domain activation
        """
        return pulumi.get(self, "activation_status")

    @activation_status.setter
    def activation_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "activation_status", value)

    @property
    @pulumi.getter(name="fipsState")
    def fips_state(self) -> Optional[pulumi.Input[int]]:
        """
        FIPS state information for security domain
        """
        return pulumi.get(self, "fips_state")

    @fips_state.setter
    def fips_state(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "fips_state", value)


@pulumi.input_type
class CloudHsmClusterSkuArgs:
    def __init__(__self__, *,
                 family: pulumi.Input[Union[str, 'CloudHsmClusterSkuFamily']],
                 name: pulumi.Input['CloudHsmClusterSkuName'],
                 capacity: Optional[pulumi.Input[int]] = None):
        """
        Cloud Hsm Cluster SKU information
        :param pulumi.Input[Union[str, 'CloudHsmClusterSkuFamily']] family: Sku family of the Cloud HSM Cluster
        :param pulumi.Input['CloudHsmClusterSkuName'] name: Sku name of the Cloud HSM Cluster
        :param pulumi.Input[int] capacity: Sku capacity
        """
        pulumi.set(__self__, "family", family)
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)

    @property
    @pulumi.getter
    def family(self) -> pulumi.Input[Union[str, 'CloudHsmClusterSkuFamily']]:
        """
        Sku family of the Cloud HSM Cluster
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: pulumi.Input[Union[str, 'CloudHsmClusterSkuFamily']]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input['CloudHsmClusterSkuName']:
        """
        Sku name of the Cloud HSM Cluster
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input['CloudHsmClusterSkuName']):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        Sku capacity
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)


@pulumi.input_type
class CloudHsmPropertiesArgs:
    def __init__(__self__, *,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 state_message: Optional[pulumi.Input[str]] = None):
        """
        The Cloud HSM Properties
        :param pulumi.Input[str] fqdn: FQDN of the Cloud HSM
        :param pulumi.Input[str] state: The Cloud HSM State
        :param pulumi.Input[str] state_message: The Cloud HSM State message
        """
        if fqdn is not None:
            pulumi.set(__self__, "fqdn", fqdn)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if state_message is not None:
            pulumi.set(__self__, "state_message", state_message)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        FQDN of the Cloud HSM
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The Cloud HSM State
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="stateMessage")
    def state_message(self) -> Optional[pulumi.Input[str]]:
        """
        The Cloud HSM State message
        """
        return pulumi.get(self, "state_message")

    @state_message.setter
    def state_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state_message", value)


@pulumi.input_type
class NetworkInterfaceArgs:
    def __init__(__self__, *,
                 private_ip_address: Optional[pulumi.Input[str]] = None):
        """
        The network interface definition.
        :param pulumi.Input[str] private_ip_address: Private Ip address of the interface
        """
        if private_ip_address is not None:
            pulumi.set(__self__, "private_ip_address", private_ip_address)

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        Private Ip address of the interface
        """
        return pulumi.get(self, "private_ip_address")

    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address", value)


@pulumi.input_type
class NetworkProfileArgs:
    def __init__(__self__, *,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceArgs']]]] = None,
                 subnet: Optional[pulumi.Input['ApiEntityReferenceArgs']] = None):
        """
        The network profile definition.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceArgs']]] network_interfaces: Specifies the list of resource Ids for the network interfaces associated with the dedicated HSM.
        :param pulumi.Input['ApiEntityReferenceArgs'] subnet: Specifies the identifier of the subnet.
        """
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceArgs']]]]:
        """
        Specifies the list of resource Ids for the network interfaces associated with the dedicated HSM.
        """
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceArgs']]]]):
        pulumi.set(self, "network_interfaces", value)

    @property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input['ApiEntityReferenceArgs']]:
        """
        Specifies the identifier of the subnet.
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input['ApiEntityReferenceArgs']]):
        pulumi.set(self, "subnet", value)


@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(__self__, *,
                 private_link_service_connection_state: pulumi.Input['PrivateLinkServiceConnectionStateArgs'],
                 etag: Optional[pulumi.Input[str]] = None):
        """
        The private endpoint connection resource.
        :param pulumi.Input['PrivateLinkServiceConnectionStateArgs'] private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] etag: Modified whenever there is a change in the state of private endpoint connection.
        """
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Input['PrivateLinkServiceConnectionStateArgs']:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: pulumi.Input['PrivateLinkServiceConnectionStateArgs']):
        pulumi.set(self, "private_link_service_connection_state", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        Modified whenever there is a change in the state of private endpoint connection.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param pulumi.Input[str] description: The reason for approval/rejection of the connection.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[str]]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[Union[str, 'SkuName']]] = None):
        """
        SKU of the dedicated HSM
        :param pulumi.Input[Union[str, 'SkuName']] name: SKU of the dedicated HSM
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[str, 'SkuName']]]:
        """
        SKU of the dedicated HSM
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[str, 'SkuName']]]):
        pulumi.set(self, "name", value)


