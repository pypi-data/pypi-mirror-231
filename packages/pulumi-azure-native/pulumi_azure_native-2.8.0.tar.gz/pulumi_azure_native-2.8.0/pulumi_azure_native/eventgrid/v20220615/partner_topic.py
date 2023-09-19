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
from ._inputs import *

__all__ = ['PartnerTopicArgs', 'PartnerTopic']

@pulumi.input_type
class PartnerTopicArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 activation_state: Optional[pulumi.Input[Union[str, 'PartnerTopicActivationState']]] = None,
                 event_type_info: Optional[pulumi.Input['EventTypeInfoArgs']] = None,
                 expiration_time_if_not_activated_utc: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['IdentityInfoArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 message_for_activation: Optional[pulumi.Input[str]] = None,
                 partner_registration_immutable_id: Optional[pulumi.Input[str]] = None,
                 partner_topic_friendly_description: Optional[pulumi.Input[str]] = None,
                 partner_topic_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PartnerTopic resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[Union[str, 'PartnerTopicActivationState']] activation_state: Activation state of the partner topic.
        :param pulumi.Input['EventTypeInfoArgs'] event_type_info: Event Type information from the corresponding event channel.
        :param pulumi.Input[str] expiration_time_if_not_activated_utc: Expiration time of the partner topic. If this timer expires while the partner topic is still never activated,
               the partner topic and corresponding event channel are deleted.
        :param pulumi.Input['IdentityInfoArgs'] identity: Identity information for the Partner Topic resource.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[str] message_for_activation: Context or helpful message that can be used during the approval process by the subscriber.
        :param pulumi.Input[str] partner_registration_immutable_id: The immutableId of the corresponding partner registration.
        :param pulumi.Input[str] partner_topic_friendly_description: Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic.
               This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer.
        :param pulumi.Input[str] partner_topic_name: Name of the partner topic.
        :param pulumi.Input[str] source: Source associated with this partner topic. This represents a unique partner resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if activation_state is not None:
            pulumi.set(__self__, "activation_state", activation_state)
        if event_type_info is not None:
            pulumi.set(__self__, "event_type_info", event_type_info)
        if expiration_time_if_not_activated_utc is not None:
            pulumi.set(__self__, "expiration_time_if_not_activated_utc", expiration_time_if_not_activated_utc)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if message_for_activation is not None:
            pulumi.set(__self__, "message_for_activation", message_for_activation)
        if partner_registration_immutable_id is not None:
            pulumi.set(__self__, "partner_registration_immutable_id", partner_registration_immutable_id)
        if partner_topic_friendly_description is not None:
            pulumi.set(__self__, "partner_topic_friendly_description", partner_topic_friendly_description)
        if partner_topic_name is not None:
            pulumi.set(__self__, "partner_topic_name", partner_topic_name)
        if source is not None:
            pulumi.set(__self__, "source", source)
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
    def activation_state(self) -> Optional[pulumi.Input[Union[str, 'PartnerTopicActivationState']]]:
        """
        Activation state of the partner topic.
        """
        return pulumi.get(self, "activation_state")

    @activation_state.setter
    def activation_state(self, value: Optional[pulumi.Input[Union[str, 'PartnerTopicActivationState']]]):
        pulumi.set(self, "activation_state", value)

    @property
    @pulumi.getter(name="eventTypeInfo")
    def event_type_info(self) -> Optional[pulumi.Input['EventTypeInfoArgs']]:
        """
        Event Type information from the corresponding event channel.
        """
        return pulumi.get(self, "event_type_info")

    @event_type_info.setter
    def event_type_info(self, value: Optional[pulumi.Input['EventTypeInfoArgs']]):
        pulumi.set(self, "event_type_info", value)

    @property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Expiration time of the partner topic. If this timer expires while the partner topic is still never activated,
        the partner topic and corresponding event channel are deleted.
        """
        return pulumi.get(self, "expiration_time_if_not_activated_utc")

    @expiration_time_if_not_activated_utc.setter
    def expiration_time_if_not_activated_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_time_if_not_activated_utc", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityInfoArgs']]:
        """
        Identity information for the Partner Topic resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityInfoArgs']]):
        pulumi.set(self, "identity", value)

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
        Context or helpful message that can be used during the approval process by the subscriber.
        """
        return pulumi.get(self, "message_for_activation")

    @message_for_activation.setter
    def message_for_activation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message_for_activation", value)

    @property
    @pulumi.getter(name="partnerRegistrationImmutableId")
    def partner_registration_immutable_id(self) -> Optional[pulumi.Input[str]]:
        """
        The immutableId of the corresponding partner registration.
        """
        return pulumi.get(self, "partner_registration_immutable_id")

    @partner_registration_immutable_id.setter
    def partner_registration_immutable_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_registration_immutable_id", value)

    @property
    @pulumi.getter(name="partnerTopicFriendlyDescription")
    def partner_topic_friendly_description(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic.
        This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer.
        """
        return pulumi.get(self, "partner_topic_friendly_description")

    @partner_topic_friendly_description.setter
    def partner_topic_friendly_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_topic_friendly_description", value)

    @property
    @pulumi.getter(name="partnerTopicName")
    def partner_topic_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the partner topic.
        """
        return pulumi.get(self, "partner_topic_name")

    @partner_topic_name.setter
    def partner_topic_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_topic_name", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Source associated with this partner topic. This represents a unique partner resource.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

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


class PartnerTopic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activation_state: Optional[pulumi.Input[Union[str, 'PartnerTopicActivationState']]] = None,
                 event_type_info: Optional[pulumi.Input[pulumi.InputType['EventTypeInfoArgs']]] = None,
                 expiration_time_if_not_activated_utc: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityInfoArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 message_for_activation: Optional[pulumi.Input[str]] = None,
                 partner_registration_immutable_id: Optional[pulumi.Input[str]] = None,
                 partner_topic_friendly_description: Optional[pulumi.Input[str]] = None,
                 partner_topic_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Event Grid Partner Topic.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'PartnerTopicActivationState']] activation_state: Activation state of the partner topic.
        :param pulumi.Input[pulumi.InputType['EventTypeInfoArgs']] event_type_info: Event Type information from the corresponding event channel.
        :param pulumi.Input[str] expiration_time_if_not_activated_utc: Expiration time of the partner topic. If this timer expires while the partner topic is still never activated,
               the partner topic and corresponding event channel are deleted.
        :param pulumi.Input[pulumi.InputType['IdentityInfoArgs']] identity: Identity information for the Partner Topic resource.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[str] message_for_activation: Context or helpful message that can be used during the approval process by the subscriber.
        :param pulumi.Input[str] partner_registration_immutable_id: The immutableId of the corresponding partner registration.
        :param pulumi.Input[str] partner_topic_friendly_description: Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic.
               This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer.
        :param pulumi.Input[str] partner_topic_name: Name of the partner topic.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[str] source: Source associated with this partner topic. This represents a unique partner resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PartnerTopicArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Event Grid Partner Topic.

        :param str resource_name: The name of the resource.
        :param PartnerTopicArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PartnerTopicArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activation_state: Optional[pulumi.Input[Union[str, 'PartnerTopicActivationState']]] = None,
                 event_type_info: Optional[pulumi.Input[pulumi.InputType['EventTypeInfoArgs']]] = None,
                 expiration_time_if_not_activated_utc: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityInfoArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 message_for_activation: Optional[pulumi.Input[str]] = None,
                 partner_registration_immutable_id: Optional[pulumi.Input[str]] = None,
                 partner_topic_friendly_description: Optional[pulumi.Input[str]] = None,
                 partner_topic_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PartnerTopicArgs.__new__(PartnerTopicArgs)

            __props__.__dict__["activation_state"] = activation_state
            __props__.__dict__["event_type_info"] = event_type_info
            __props__.__dict__["expiration_time_if_not_activated_utc"] = expiration_time_if_not_activated_utc
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["message_for_activation"] = message_for_activation
            __props__.__dict__["partner_registration_immutable_id"] = partner_registration_immutable_id
            __props__.__dict__["partner_topic_friendly_description"] = partner_topic_friendly_description
            __props__.__dict__["partner_topic_name"] = partner_topic_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid:PartnerTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20211015preview:PartnerTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20230601preview:PartnerTopic")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PartnerTopic, __self__).__init__(
            'azure-native:eventgrid/v20220615:PartnerTopic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PartnerTopic':
        """
        Get an existing PartnerTopic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PartnerTopicArgs.__new__(PartnerTopicArgs)

        __props__.__dict__["activation_state"] = None
        __props__.__dict__["event_type_info"] = None
        __props__.__dict__["expiration_time_if_not_activated_utc"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["message_for_activation"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partner_registration_immutable_id"] = None
        __props__.__dict__["partner_topic_friendly_description"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return PartnerTopic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> pulumi.Output[Optional[str]]:
        """
        Activation state of the partner topic.
        """
        return pulumi.get(self, "activation_state")

    @property
    @pulumi.getter(name="eventTypeInfo")
    def event_type_info(self) -> pulumi.Output[Optional['outputs.EventTypeInfoResponse']]:
        """
        Event Type information from the corresponding event channel.
        """
        return pulumi.get(self, "event_type_info")

    @property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> pulumi.Output[Optional[str]]:
        """
        Expiration time of the partner topic. If this timer expires while the partner topic is still never activated,
        the partner topic and corresponding event channel are deleted.
        """
        return pulumi.get(self, "expiration_time_if_not_activated_utc")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityInfoResponse']]:
        """
        Identity information for the Partner Topic resource.
        """
        return pulumi.get(self, "identity")

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
        Context or helpful message that can be used during the approval process by the subscriber.
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
        The immutableId of the corresponding partner registration.
        """
        return pulumi.get(self, "partner_registration_immutable_id")

    @property
    @pulumi.getter(name="partnerTopicFriendlyDescription")
    def partner_topic_friendly_description(self) -> pulumi.Output[Optional[str]]:
        """
        Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic.
        This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer.
        """
        return pulumi.get(self, "partner_topic_friendly_description")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the partner topic.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        """
        Source associated with this partner topic. This represents a unique partner resource.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to Partner Topic resource.
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

