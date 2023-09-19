# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'EventHandlerSettingsArgs',
    'EventHandlerTemplateArgs',
    'LiveTraceCategoryArgs',
    'LiveTraceConfigurationArgs',
    'ManagedIdentitySettingsArgs',
    'ManagedIdentityArgs',
    'NetworkACLArgs',
    'PrivateEndpointACLArgs',
    'ResourceSkuArgs',
    'UpstreamAuthSettingsArgs',
    'WebPubSubNetworkACLsArgs',
    'WebPubSubTlsSettingsArgs',
]

@pulumi.input_type
class EventHandlerSettingsArgs:
    def __init__(__self__, *,
                 items: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['EventHandlerTemplateArgs']]]]]] = None):
        """
        The settings for event handler in webpubsub service
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['EventHandlerTemplateArgs']]]]] items: Get or set the EventHandler items. The key is the hub name and the value is the corresponding EventHandlerTemplate.
        """
        if items is not None:
            pulumi.set(__self__, "items", items)

    @property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['EventHandlerTemplateArgs']]]]]]:
        """
        Get or set the EventHandler items. The key is the hub name and the value is the corresponding EventHandlerTemplate.
        """
        return pulumi.get(self, "items")

    @items.setter
    def items(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input['EventHandlerTemplateArgs']]]]]]):
        pulumi.set(self, "items", value)


@pulumi.input_type
class EventHandlerTemplateArgs:
    def __init__(__self__, *,
                 url_template: pulumi.Input[str],
                 auth: Optional[pulumi.Input['UpstreamAuthSettingsArgs']] = None,
                 system_event_pattern: Optional[pulumi.Input[str]] = None,
                 user_event_pattern: Optional[pulumi.Input[str]] = None):
        """
        EventHandler template item settings.
        :param pulumi.Input[str] url_template: Gets or sets the EventHandler URL template. You can use a predefined parameter {hub} and {event} inside the template, the value of the EventHandler URL is dynamically calculated when the client request comes in.
               For example, UrlTemplate can be `http://example.com/api/{hub}/{event}`. The host part can't contains parameters.
        :param pulumi.Input['UpstreamAuthSettingsArgs'] auth: Gets or sets the auth settings for an event handler. If not set, no auth is used.
        :param pulumi.Input[str] system_event_pattern: Gets ot sets the system event pattern.
               There are 2 kind of patterns supported:
                   1. The single event name, for example, "connect", it matches "connect"
                   2. Combine multiple events with ",", for example "connect,disconnected", it matches event "connect" and "disconnected"
        :param pulumi.Input[str] user_event_pattern: Gets or sets the matching pattern for event names.
               There are 3 kind of patterns supported:
                   1. "*", it to matches any event name
                   2. Combine multiple events with ",", for example "event1,event2", it matches event "event1" and "event2"
                   3. The single event name, for example, "event1", it matches "event1"
        """
        pulumi.set(__self__, "url_template", url_template)
        if auth is not None:
            pulumi.set(__self__, "auth", auth)
        if system_event_pattern is not None:
            pulumi.set(__self__, "system_event_pattern", system_event_pattern)
        if user_event_pattern is not None:
            pulumi.set(__self__, "user_event_pattern", user_event_pattern)

    @property
    @pulumi.getter(name="urlTemplate")
    def url_template(self) -> pulumi.Input[str]:
        """
        Gets or sets the EventHandler URL template. You can use a predefined parameter {hub} and {event} inside the template, the value of the EventHandler URL is dynamically calculated when the client request comes in.
        For example, UrlTemplate can be `http://example.com/api/{hub}/{event}`. The host part can't contains parameters.
        """
        return pulumi.get(self, "url_template")

    @url_template.setter
    def url_template(self, value: pulumi.Input[str]):
        pulumi.set(self, "url_template", value)

    @property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input['UpstreamAuthSettingsArgs']]:
        """
        Gets or sets the auth settings for an event handler. If not set, no auth is used.
        """
        return pulumi.get(self, "auth")

    @auth.setter
    def auth(self, value: Optional[pulumi.Input['UpstreamAuthSettingsArgs']]):
        pulumi.set(self, "auth", value)

    @property
    @pulumi.getter(name="systemEventPattern")
    def system_event_pattern(self) -> Optional[pulumi.Input[str]]:
        """
        Gets ot sets the system event pattern.
        There are 2 kind of patterns supported:
            1. The single event name, for example, "connect", it matches "connect"
            2. Combine multiple events with ",", for example "connect,disconnected", it matches event "connect" and "disconnected"
        """
        return pulumi.get(self, "system_event_pattern")

    @system_event_pattern.setter
    def system_event_pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "system_event_pattern", value)

    @property
    @pulumi.getter(name="userEventPattern")
    def user_event_pattern(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the matching pattern for event names.
        There are 3 kind of patterns supported:
            1. "*", it to matches any event name
            2. Combine multiple events with ",", for example "event1,event2", it matches event "event1" and "event2"
            3. The single event name, for example, "event1", it matches "event1"
        """
        return pulumi.get(self, "user_event_pattern")

    @user_event_pattern.setter
    def user_event_pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_event_pattern", value)


@pulumi.input_type
class LiveTraceCategoryArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        live trace category configuration of a Microsoft.SignalRService resource.
        :param pulumi.Input[str] enabled: Indicates whether or the log category is enabled.
               Available values: true, false.
               Case insensitive.
        :param pulumi.Input[str] name: Gets or sets the log category's name.
               Available values: ConnectivityLogs, MessagingLogs.
               Case insensitive.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether or the log category is enabled.
        Available values: true, false.
        Case insensitive.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the log category's name.
        Available values: ConnectivityLogs, MessagingLogs.
        Case insensitive.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class LiveTraceConfigurationArgs:
    def __init__(__self__, *,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input['LiveTraceCategoryArgs']]]] = None,
                 enabled: Optional[pulumi.Input[str]] = None):
        """
        Live trace configuration of a Microsoft.SignalRService resource.
        :param pulumi.Input[Sequence[pulumi.Input['LiveTraceCategoryArgs']]] categories: Gets or sets the list of category configurations.
        :param pulumi.Input[str] enabled: Indicates whether or not enable live trace.
               When it's set to true, live trace client can connect to the service.
               Otherwise, live trace client can't connect to the service, so that you are unable to receive any log, no matter what you configure in "categories".
               Available values: true, false.
               Case insensitive.
        """
        if categories is not None:
            pulumi.set(__self__, "categories", categories)
        if enabled is None:
            enabled = 'false'
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LiveTraceCategoryArgs']]]]:
        """
        Gets or sets the list of category configurations.
        """
        return pulumi.get(self, "categories")

    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LiveTraceCategoryArgs']]]]):
        pulumi.set(self, "categories", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether or not enable live trace.
        When it's set to true, live trace client can connect to the service.
        Otherwise, live trace client can't connect to the service, so that you are unable to receive any log, no matter what you configure in "categories".
        Available values: true, false.
        Case insensitive.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class ManagedIdentitySettingsArgs:
    def __init__(__self__, *,
                 resource: Optional[pulumi.Input[str]] = None):
        """
        Managed identity settings for upstream.
        :param pulumi.Input[str] resource: The Resource indicating the App ID URI of the target resource.
               It also appears in the aud (audience) claim of the issued token.
        """
        if resource is not None:
            pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[str]]:
        """
        The Resource indicating the App ID URI of the target resource.
        It also appears in the aud (audience) claim of the issued token.
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource", value)


@pulumi.input_type
class ManagedIdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input[Union[str, 'ManagedIdentityType']]] = None,
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        A class represent managed identities used for request and response
        :param pulumi.Input[Union[str, 'ManagedIdentityType']] type: Represent the identity type: systemAssigned, userAssigned, None
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: Get or set the user assigned identities
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'ManagedIdentityType']]]:
        """
        Represent the identity type: systemAssigned, userAssigned, None
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'ManagedIdentityType']]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Get or set the user assigned identities
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class NetworkACLArgs:
    def __init__(__self__, *,
                 allow: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]] = None,
                 deny: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]] = None):
        """
        Network ACL
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]] allow: Allowed request types. The value can be one or more of: ClientConnection, ServerConnection, RESTAPI.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]] deny: Denied request types. The value can be one or more of: ClientConnection, ServerConnection, RESTAPI.
        """
        if allow is not None:
            pulumi.set(__self__, "allow", allow)
        if deny is not None:
            pulumi.set(__self__, "deny", deny)

    @property
    @pulumi.getter
    def allow(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]]:
        """
        Allowed request types. The value can be one or more of: ClientConnection, ServerConnection, RESTAPI.
        """
        return pulumi.get(self, "allow")

    @allow.setter
    def allow(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]]):
        pulumi.set(self, "allow", value)

    @property
    @pulumi.getter
    def deny(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]]:
        """
        Denied request types. The value can be one or more of: ClientConnection, ServerConnection, RESTAPI.
        """
        return pulumi.get(self, "deny")

    @deny.setter
    def deny(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]]):
        pulumi.set(self, "deny", value)


@pulumi.input_type
class PrivateEndpointACLArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 allow: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]] = None,
                 deny: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]] = None):
        """
        ACL for a private endpoint
        :param pulumi.Input[str] name: Name of the private endpoint connection
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]] allow: Allowed request types. The value can be one or more of: ClientConnection, ServerConnection, RESTAPI.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]] deny: Denied request types. The value can be one or more of: ClientConnection, ServerConnection, RESTAPI.
        """
        pulumi.set(__self__, "name", name)
        if allow is not None:
            pulumi.set(__self__, "allow", allow)
        if deny is not None:
            pulumi.set(__self__, "deny", deny)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the private endpoint connection
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def allow(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]]:
        """
        Allowed request types. The value can be one or more of: ClientConnection, ServerConnection, RESTAPI.
        """
        return pulumi.get(self, "allow")

    @allow.setter
    def allow(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]]):
        pulumi.set(self, "allow", value)

    @property
    @pulumi.getter
    def deny(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]]:
        """
        Denied request types. The value can be one or more of: ClientConnection, ServerConnection, RESTAPI.
        """
        return pulumi.get(self, "deny")

    @deny.setter
    def deny(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'WebPubSubRequestType']]]]]):
        pulumi.set(self, "deny", value)


@pulumi.input_type
class ResourceSkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 capacity: Optional[pulumi.Input[int]] = None,
                 tier: Optional[pulumi.Input[Union[str, 'WebPubSubSkuTier']]] = None):
        """
        The billing information of the resource.
        :param pulumi.Input[str] name: The name of the SKU. Required.
               
               Allowed values: Standard_S1, Free_F1
        :param pulumi.Input[int] capacity: Optional, integer. The unit count of the resource. 1 by default.
               
               If present, following values are allowed:
                   Free: 1
                   Standard: 1,2,5,10,20,50,100
        :param pulumi.Input[Union[str, 'WebPubSubSkuTier']] tier: Optional tier of this particular SKU. 'Standard' or 'Free'. 
               
               `Basic` is deprecated, use `Standard` instead.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the SKU. Required.
        
        Allowed values: Standard_S1, Free_F1
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        Optional, integer. The unit count of the resource. 1 by default.
        
        If present, following values are allowed:
            Free: 1
            Standard: 1,2,5,10,20,50,100
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[str, 'WebPubSubSkuTier']]]:
        """
        Optional tier of this particular SKU. 'Standard' or 'Free'. 
        
        `Basic` is deprecated, use `Standard` instead.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[str, 'WebPubSubSkuTier']]]):
        pulumi.set(self, "tier", value)


@pulumi.input_type
class UpstreamAuthSettingsArgs:
    def __init__(__self__, *,
                 managed_identity: Optional[pulumi.Input['ManagedIdentitySettingsArgs']] = None,
                 type: Optional[pulumi.Input[Union[str, 'UpstreamAuthType']]] = None):
        """
        Upstream auth settings.
        :param pulumi.Input['ManagedIdentitySettingsArgs'] managed_identity: Gets or sets the managed identity settings. It's required if the auth type is set to ManagedIdentity.
        :param pulumi.Input[Union[str, 'UpstreamAuthType']] type: Gets or sets the type of auth. None or ManagedIdentity is supported now.
        """
        if managed_identity is not None:
            pulumi.set(__self__, "managed_identity", managed_identity)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[pulumi.Input['ManagedIdentitySettingsArgs']]:
        """
        Gets or sets the managed identity settings. It's required if the auth type is set to ManagedIdentity.
        """
        return pulumi.get(self, "managed_identity")

    @managed_identity.setter
    def managed_identity(self, value: Optional[pulumi.Input['ManagedIdentitySettingsArgs']]):
        pulumi.set(self, "managed_identity", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'UpstreamAuthType']]]:
        """
        Gets or sets the type of auth. None or ManagedIdentity is supported now.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'UpstreamAuthType']]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class WebPubSubNetworkACLsArgs:
    def __init__(__self__, *,
                 default_action: Optional[pulumi.Input[Union[str, 'ACLAction']]] = None,
                 private_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointACLArgs']]]] = None,
                 public_network: Optional[pulumi.Input['NetworkACLArgs']] = None):
        """
        Network ACLs for the resource
        :param pulumi.Input[Union[str, 'ACLAction']] default_action: Default action when no other rule matches
        :param pulumi.Input[Sequence[pulumi.Input['PrivateEndpointACLArgs']]] private_endpoints: ACLs for requests from private endpoints
        :param pulumi.Input['NetworkACLArgs'] public_network: ACL for requests from public network
        """
        if default_action is None:
            default_action = 'Deny'
        if default_action is not None:
            pulumi.set(__self__, "default_action", default_action)
        if private_endpoints is not None:
            pulumi.set(__self__, "private_endpoints", private_endpoints)
        if public_network is not None:
            pulumi.set(__self__, "public_network", public_network)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[Union[str, 'ACLAction']]]:
        """
        Default action when no other rule matches
        """
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[Union[str, 'ACLAction']]]):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter(name="privateEndpoints")
    def private_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointACLArgs']]]]:
        """
        ACLs for requests from private endpoints
        """
        return pulumi.get(self, "private_endpoints")

    @private_endpoints.setter
    def private_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointACLArgs']]]]):
        pulumi.set(self, "private_endpoints", value)

    @property
    @pulumi.getter(name="publicNetwork")
    def public_network(self) -> Optional[pulumi.Input['NetworkACLArgs']]:
        """
        ACL for requests from public network
        """
        return pulumi.get(self, "public_network")

    @public_network.setter
    def public_network(self, value: Optional[pulumi.Input['NetworkACLArgs']]):
        pulumi.set(self, "public_network", value)


@pulumi.input_type
class WebPubSubTlsSettingsArgs:
    def __init__(__self__, *,
                 client_cert_enabled: Optional[pulumi.Input[bool]] = None):
        """
        TLS settings for the resource
        :param pulumi.Input[bool] client_cert_enabled: Request client certificate during TLS handshake if enabled
        """
        if client_cert_enabled is None:
            client_cert_enabled = True
        if client_cert_enabled is not None:
            pulumi.set(__self__, "client_cert_enabled", client_cert_enabled)

    @property
    @pulumi.getter(name="clientCertEnabled")
    def client_cert_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Request client certificate during TLS handshake if enabled
        """
        return pulumi.get(self, "client_cert_enabled")

    @client_cert_enabled.setter
    def client_cert_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "client_cert_enabled", value)


