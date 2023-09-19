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
from ._enums import *
from ._inputs import *

__all__ = ['NetworkTapArgs', 'NetworkTap']

@pulumi.input_type
class NetworkTapArgs:
    def __init__(__self__, *,
                 destinations: pulumi.Input[Sequence[pulumi.Input['NetworkTapPropertiesDestinationsArgs']]],
                 network_packet_broker_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 annotation: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_tap_name: Optional[pulumi.Input[str]] = None,
                 polling_type: Optional[pulumi.Input[Union[str, 'PollingType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkTap resource.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkTapPropertiesDestinationsArgs']]] destinations: List of destinations to send the filter traffic.
        :param pulumi.Input[str] network_packet_broker_id: ARM resource ID of the Network Packet Broker.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] network_tap_name: Name of the Network Tap.
        :param pulumi.Input[Union[str, 'PollingType']] polling_type: Polling type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "destinations", destinations)
        pulumi.set(__self__, "network_packet_broker_id", network_packet_broker_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if annotation is not None:
            pulumi.set(__self__, "annotation", annotation)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_tap_name is not None:
            pulumi.set(__self__, "network_tap_name", network_tap_name)
        if polling_type is None:
            polling_type = 'Pull'
        if polling_type is not None:
            pulumi.set(__self__, "polling_type", polling_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def destinations(self) -> pulumi.Input[Sequence[pulumi.Input['NetworkTapPropertiesDestinationsArgs']]]:
        """
        List of destinations to send the filter traffic.
        """
        return pulumi.get(self, "destinations")

    @destinations.setter
    def destinations(self, value: pulumi.Input[Sequence[pulumi.Input['NetworkTapPropertiesDestinationsArgs']]]):
        pulumi.set(self, "destinations", value)

    @property
    @pulumi.getter(name="networkPacketBrokerId")
    def network_packet_broker_id(self) -> pulumi.Input[str]:
        """
        ARM resource ID of the Network Packet Broker.
        """
        return pulumi.get(self, "network_packet_broker_id")

    @network_packet_broker_id.setter
    def network_packet_broker_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_packet_broker_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "annotation", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="networkTapName")
    def network_tap_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Network Tap.
        """
        return pulumi.get(self, "network_tap_name")

    @network_tap_name.setter
    def network_tap_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_tap_name", value)

    @property
    @pulumi.getter(name="pollingType")
    def polling_type(self) -> Optional[pulumi.Input[Union[str, 'PollingType']]]:
        """
        Polling type.
        """
        return pulumi.get(self, "polling_type")

    @polling_type.setter
    def polling_type(self, value: Optional[pulumi.Input[Union[str, 'PollingType']]]):
        pulumi.set(self, "polling_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class NetworkTap(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkTapPropertiesDestinationsArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_packet_broker_id: Optional[pulumi.Input[str]] = None,
                 network_tap_name: Optional[pulumi.Input[str]] = None,
                 polling_type: Optional[pulumi.Input[Union[str, 'PollingType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The Network Tap resource definition.
        Azure REST API version: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkTapPropertiesDestinationsArgs']]]] destinations: List of destinations to send the filter traffic.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] network_packet_broker_id: ARM resource ID of the Network Packet Broker.
        :param pulumi.Input[str] network_tap_name: Name of the Network Tap.
        :param pulumi.Input[Union[str, 'PollingType']] polling_type: Polling type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkTapArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Network Tap resource definition.
        Azure REST API version: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param NetworkTapArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkTapArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkTapPropertiesDestinationsArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_packet_broker_id: Optional[pulumi.Input[str]] = None,
                 network_tap_name: Optional[pulumi.Input[str]] = None,
                 polling_type: Optional[pulumi.Input[Union[str, 'PollingType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkTapArgs.__new__(NetworkTapArgs)

            __props__.__dict__["annotation"] = annotation
            if destinations is None and not opts.urn:
                raise TypeError("Missing required property 'destinations'")
            __props__.__dict__["destinations"] = destinations
            __props__.__dict__["location"] = location
            if network_packet_broker_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_packet_broker_id'")
            __props__.__dict__["network_packet_broker_id"] = network_packet_broker_id
            __props__.__dict__["network_tap_name"] = network_tap_name
            if polling_type is None:
                polling_type = 'Pull'
            __props__.__dict__["polling_type"] = polling_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["administrative_state"] = None
            __props__.__dict__["configuration_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["source_tap_rule_id"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetworkfabric/v20230615:NetworkTap")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkTap, __self__).__init__(
            'azure-native:managednetworkfabric:NetworkTap',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkTap':
        """
        Get an existing NetworkTap resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkTapArgs.__new__(NetworkTapArgs)

        __props__.__dict__["administrative_state"] = None
        __props__.__dict__["annotation"] = None
        __props__.__dict__["configuration_state"] = None
        __props__.__dict__["destinations"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_packet_broker_id"] = None
        __props__.__dict__["polling_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source_tap_rule_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return NetworkTap(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[str]:
        """
        Administrative state of the resource. Example -Enabled/Disabled
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> pulumi.Output[str]:
        """
        Gets the configurations state of the resource.
        """
        return pulumi.get(self, "configuration_state")

    @property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Sequence['outputs.NetworkTapPropertiesResponseDestinations']]:
        """
        List of destinations to send the filter traffic.
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkPacketBrokerId")
    def network_packet_broker_id(self) -> pulumi.Output[str]:
        """
        ARM resource ID of the Network Packet Broker.
        """
        return pulumi.get(self, "network_packet_broker_id")

    @property
    @pulumi.getter(name="pollingType")
    def polling_type(self) -> pulumi.Output[Optional[str]]:
        """
        Polling type.
        """
        return pulumi.get(self, "polling_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provides you the latest status of the NFC service, whether it is Accepted, updating, Succeeded or Failed. During this process, the states keep changing based on the status of Network Tap provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceTapRuleId")
    def source_tap_rule_id(self) -> pulumi.Output[str]:
        """
        Source Tap Rule Id. ARM Resource ID of the Network Tap Rule.
        """
        return pulumi.get(self, "source_tap_rule_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

