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
    'GetPartnerTopicResult',
    'AwaitableGetPartnerTopicResult',
    'get_partner_topic',
    'get_partner_topic_output',
]

@pulumi.output_type
class GetPartnerTopicResult:
    """
    Event Grid Partner Topic.
    """
    def __init__(__self__, activation_state=None, event_type_info=None, expiration_time_if_not_activated_utc=None, id=None, identity=None, location=None, message_for_activation=None, name=None, partner_registration_immutable_id=None, partner_topic_friendly_description=None, provisioning_state=None, source=None, system_data=None, tags=None, type=None):
        if activation_state and not isinstance(activation_state, str):
            raise TypeError("Expected argument 'activation_state' to be a str")
        pulumi.set(__self__, "activation_state", activation_state)
        if event_type_info and not isinstance(event_type_info, dict):
            raise TypeError("Expected argument 'event_type_info' to be a dict")
        pulumi.set(__self__, "event_type_info", event_type_info)
        if expiration_time_if_not_activated_utc and not isinstance(expiration_time_if_not_activated_utc, str):
            raise TypeError("Expected argument 'expiration_time_if_not_activated_utc' to be a str")
        pulumi.set(__self__, "expiration_time_if_not_activated_utc", expiration_time_if_not_activated_utc)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if message_for_activation and not isinstance(message_for_activation, str):
            raise TypeError("Expected argument 'message_for_activation' to be a str")
        pulumi.set(__self__, "message_for_activation", message_for_activation)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partner_registration_immutable_id and not isinstance(partner_registration_immutable_id, str):
            raise TypeError("Expected argument 'partner_registration_immutable_id' to be a str")
        pulumi.set(__self__, "partner_registration_immutable_id", partner_registration_immutable_id)
        if partner_topic_friendly_description and not isinstance(partner_topic_friendly_description, str):
            raise TypeError("Expected argument 'partner_topic_friendly_description' to be a str")
        pulumi.set(__self__, "partner_topic_friendly_description", partner_topic_friendly_description)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="activationState")
    def activation_state(self) -> Optional[str]:
        """
        Activation state of the partner topic.
        """
        return pulumi.get(self, "activation_state")

    @property
    @pulumi.getter(name="eventTypeInfo")
    def event_type_info(self) -> Optional['outputs.EventTypeInfoResponse']:
        """
        Event Type information from the corresponding event channel.
        """
        return pulumi.get(self, "event_type_info")

    @property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> Optional[str]:
        """
        Expiration time of the partner topic. If this timer expires while the partner topic is still never activated,
        the partner topic and corresponding event channel are deleted.
        """
        return pulumi.get(self, "expiration_time_if_not_activated_utc")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityInfoResponse']:
        """
        Identity information for the Partner Topic resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> Optional[str]:
        """
        Context or helpful message that can be used during the approval process by the subscriber.
        """
        return pulumi.get(self, "message_for_activation")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerRegistrationImmutableId")
    def partner_registration_immutable_id(self) -> Optional[str]:
        """
        The immutableId of the corresponding partner registration.
        """
        return pulumi.get(self, "partner_registration_immutable_id")

    @property
    @pulumi.getter(name="partnerTopicFriendlyDescription")
    def partner_topic_friendly_description(self) -> Optional[str]:
        """
        Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic.
        This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer.
        """
        return pulumi.get(self, "partner_topic_friendly_description")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the partner topic.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> Optional[str]:
        """
        Source associated with this partner topic. This represents a unique partner resource.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to Partner Topic resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetPartnerTopicResult(GetPartnerTopicResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPartnerTopicResult(
            activation_state=self.activation_state,
            event_type_info=self.event_type_info,
            expiration_time_if_not_activated_utc=self.expiration_time_if_not_activated_utc,
            id=self.id,
            identity=self.identity,
            location=self.location,
            message_for_activation=self.message_for_activation,
            name=self.name,
            partner_registration_immutable_id=self.partner_registration_immutable_id,
            partner_topic_friendly_description=self.partner_topic_friendly_description,
            provisioning_state=self.provisioning_state,
            source=self.source,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_partner_topic(partner_topic_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPartnerTopicResult:
    """
    Get properties of a partner topic.


    :param str partner_topic_name: Name of the partner topic.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    __args__ = dict()
    __args__['partnerTopicName'] = partner_topic_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid/v20220615:getPartnerTopic', __args__, opts=opts, typ=GetPartnerTopicResult).value

    return AwaitableGetPartnerTopicResult(
        activation_state=pulumi.get(__ret__, 'activation_state'),
        event_type_info=pulumi.get(__ret__, 'event_type_info'),
        expiration_time_if_not_activated_utc=pulumi.get(__ret__, 'expiration_time_if_not_activated_utc'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        message_for_activation=pulumi.get(__ret__, 'message_for_activation'),
        name=pulumi.get(__ret__, 'name'),
        partner_registration_immutable_id=pulumi.get(__ret__, 'partner_registration_immutable_id'),
        partner_topic_friendly_description=pulumi.get(__ret__, 'partner_topic_friendly_description'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        source=pulumi.get(__ret__, 'source'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_partner_topic)
def get_partner_topic_output(partner_topic_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPartnerTopicResult]:
    """
    Get properties of a partner topic.


    :param str partner_topic_name: Name of the partner topic.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    ...
