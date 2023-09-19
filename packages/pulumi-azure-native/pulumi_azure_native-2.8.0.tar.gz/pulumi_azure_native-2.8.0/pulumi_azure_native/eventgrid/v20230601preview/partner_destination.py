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
from ._enums import *

__all__ = ['PartnerDestinationArgs', 'PartnerDestination']

@pulumi.input_type
class PartnerDestinationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 activation_state: Optional[pulumi.Input[Union[str, 'PartnerDestinationActivationState']]] = None,
                 endpoint_base_url: Optional[pulumi.Input[str]] = None,
                 endpoint_service_context: Optional[pulumi.Input[str]] = None,
                 expiration_time_if_not_activated_utc: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 message_for_activation: Optional[pulumi.Input[str]] = None,
                 partner_destination_name: Optional[pulumi.Input[str]] = None,
                 partner_registration_immutable_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PartnerDestination resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[Union[str, 'PartnerDestinationActivationState']] activation_state: Activation state of the partner destination.
        :param pulumi.Input[str] endpoint_base_url: Endpoint Base URL of the partner destination
        :param pulumi.Input[str] endpoint_service_context: Endpoint context associated with this partner destination.
        :param pulumi.Input[str] expiration_time_if_not_activated_utc: Expiration time of the partner destination. If this timer expires and the partner destination was never activated,
               the partner destination and corresponding channel are deleted.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[str] message_for_activation: Context or helpful message that can be used during the approval process.
        :param pulumi.Input[str] partner_destination_name: Name of the partner destination.
        :param pulumi.Input[str] partner_registration_immutable_id: The immutable Id of the corresponding partner registration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if activation_state is not None:
            pulumi.set(__self__, "activation_state", activation_state)
        if endpoint_base_url is not None:
            pulumi.set(__self__, "endpoint_base_url", endpoint_base_url)
        if endpoint_service_context is not None:
            pulumi.set(__self__, "endpoint_service_context", endpoint_service_context)
        if expiration_time_if_not_activated_utc is not None:
            pulumi.set(__self__, "expiration_time_if_not_activated_utc", expiration_time_if_not_activated_utc)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if message_for_activation is not None:
            pulumi.set(__self__, "message_for_activation", message_for_activation)
        if partner_destination_name is not None:
            pulumi.set(__self__, "partner_destination_name", partner_destination_name)
        if partner_registration_immutable_id is not None:
            pulumi.set(__self__, "partner_registration_immutable_id", partner_registration_immutable_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> Optional[pulumi.Input[Union[str, 'PartnerDestinationActivationState']]]:
        """
        Activation state of the partner destination.
        """
        return pulumi.get(self, "activation_state")

    @activation_state.setter
    def activation_state(self, value: Optional[pulumi.Input[Union[str, 'PartnerDestinationActivationState']]]):
        pulumi.set(self, "activation_state", value)

    @property
    @pulumi.getter(name="endpointBaseUrl")
    def endpoint_base_url(self) -> Optional[pulumi.Input[str]]:
        """
        Endpoint Base URL of the partner destination
        """
        return pulumi.get(self, "endpoint_base_url")

    @endpoint_base_url.setter
    def endpoint_base_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_base_url", value)

    @property
    @pulumi.getter(name="endpointServiceContext")
    def endpoint_service_context(self) -> Optional[pulumi.Input[str]]:
        """
        Endpoint context associated with this partner destination.
        """
        return pulumi.get(self, "endpoint_service_context")

    @endpoint_service_context.setter
    def endpoint_service_context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_service_context", value)

    @property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Expiration time of the partner destination. If this timer expires and the partner destination was never activated,
        the partner destination and corresponding channel are deleted.
        """
        return pulumi.get(self, "expiration_time_if_not_activated_utc")

    @expiration_time_if_not_activated_utc.setter
    def expiration_time_if_not_activated_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_time_if_not_activated_utc", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> Optional[pulumi.Input[str]]:
        """
        Context or helpful message that can be used during the approval process.
        """
        return pulumi.get(self, "message_for_activation")

    @message_for_activation.setter
    def message_for_activation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message_for_activation", value)

    @property
    @pulumi.getter(name="partnerDestinationName")
    def partner_destination_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the partner destination.
        """
        return pulumi.get(self, "partner_destination_name")

    @partner_destination_name.setter
    def partner_destination_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_destination_name", value)

    @property
    @pulumi.getter(name="partnerRegistrationImmutableId")
    def partner_registration_immutable_id(self) -> Optional[pulumi.Input[str]]:
        """
        The immutable Id of the corresponding partner registration.
        """
        return pulumi.get(self, "partner_registration_immutable_id")

    @partner_registration_immutable_id.setter
    def partner_registration_immutable_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_registration_immutable_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class PartnerDestination(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activation_state: Optional[pulumi.Input[Union[str, 'PartnerDestinationActivationState']]] = None,
                 endpoint_base_url: Optional[pulumi.Input[str]] = None,
                 endpoint_service_context: Optional[pulumi.Input[str]] = None,
                 expiration_time_if_not_activated_utc: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 message_for_activation: Optional[pulumi.Input[str]] = None,
                 partner_destination_name: Optional[pulumi.Input[str]] = None,
                 partner_registration_immutable_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Event Grid Partner Destination.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'PartnerDestinationActivationState']] activation_state: Activation state of the partner destination.
        :param pulumi.Input[str] endpoint_base_url: Endpoint Base URL of the partner destination
        :param pulumi.Input[str] endpoint_service_context: Endpoint context associated with this partner destination.
        :param pulumi.Input[str] expiration_time_if_not_activated_utc: Expiration time of the partner destination. If this timer expires and the partner destination was never activated,
               the partner destination and corresponding channel are deleted.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[str] message_for_activation: Context or helpful message that can be used during the approval process.
        :param pulumi.Input[str] partner_destination_name: Name of the partner destination.
        :param pulumi.Input[str] partner_registration_immutable_id: The immutable Id of the corresponding partner registration.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PartnerDestinationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Event Grid Partner Destination.

        :param str resource_name: The name of the resource.
        :param PartnerDestinationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PartnerDestinationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activation_state: Optional[pulumi.Input[Union[str, 'PartnerDestinationActivationState']]] = None,
                 endpoint_base_url: Optional[pulumi.Input[str]] = None,
                 endpoint_service_context: Optional[pulumi.Input[str]] = None,
                 expiration_time_if_not_activated_utc: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 message_for_activation: Optional[pulumi.Input[str]] = None,
                 partner_destination_name: Optional[pulumi.Input[str]] = None,
                 partner_registration_immutable_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PartnerDestinationArgs.__new__(PartnerDestinationArgs)

            __props__.__dict__["activation_state"] = activation_state
            __props__.__dict__["endpoint_base_url"] = endpoint_base_url
            __props__.__dict__["endpoint_service_context"] = endpoint_service_context
            __props__.__dict__["expiration_time_if_not_activated_utc"] = expiration_time_if_not_activated_utc
            __props__.__dict__["location"] = location
            __props__.__dict__["message_for_activation"] = message_for_activation
            __props__.__dict__["partner_destination_name"] = partner_destination_name
            __props__.__dict__["partner_registration_immutable_id"] = partner_registration_immutable_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid:PartnerDestination"), pulumi.Alias(type_="azure-native:eventgrid/v20211015preview:PartnerDestination")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PartnerDestination, __self__).__init__(
            'azure-native:eventgrid/v20230601preview:PartnerDestination',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PartnerDestination':
        """
        Get an existing PartnerDestination resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PartnerDestinationArgs.__new__(PartnerDestinationArgs)

        __props__.__dict__["activation_state"] = None
        __props__.__dict__["endpoint_base_url"] = None
        __props__.__dict__["endpoint_service_context"] = None
        __props__.__dict__["expiration_time_if_not_activated_utc"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["message_for_activation"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partner_registration_immutable_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return PartnerDestination(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> pulumi.Output[Optional[str]]:
        """
        Activation state of the partner destination.
        """
        return pulumi.get(self, "activation_state")

    @property
    @pulumi.getter(name="endpointBaseUrl")
    def endpoint_base_url(self) -> pulumi.Output[Optional[str]]:
        """
        Endpoint Base URL of the partner destination
        """
        return pulumi.get(self, "endpoint_base_url")

    @property
    @pulumi.getter(name="endpointServiceContext")
    def endpoint_service_context(self) -> pulumi.Output[Optional[str]]:
        """
        Endpoint context associated with this partner destination.
        """
        return pulumi.get(self, "endpoint_service_context")

    @property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> pulumi.Output[Optional[str]]:
        """
        Expiration time of the partner destination. If this timer expires and the partner destination was never activated,
        the partner destination and corresponding channel are deleted.
        """
        return pulumi.get(self, "expiration_time_if_not_activated_utc")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> pulumi.Output[Optional[str]]:
        """
        Context or helpful message that can be used during the approval process.
        """
        return pulumi.get(self, "message_for_activation")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerRegistrationImmutableId")
    def partner_registration_immutable_id(self) -> pulumi.Output[Optional[str]]:
        """
        The immutable Id of the corresponding partner registration.
        """
        return pulumi.get(self, "partner_registration_immutable_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the partner destination.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to Partner Destination resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

