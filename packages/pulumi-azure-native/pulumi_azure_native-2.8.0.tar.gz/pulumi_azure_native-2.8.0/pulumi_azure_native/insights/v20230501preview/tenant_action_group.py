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
from ._inputs import *

__all__ = ['TenantActionGroupArgs', 'TenantActionGroup']

@pulumi.input_type
class TenantActionGroupArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 group_short_name: pulumi.Input[str],
                 management_group_id: pulumi.Input[str],
                 azure_app_push_receivers: Optional[pulumi.Input[Sequence[pulumi.Input['AzureAppPushReceiverArgs']]]] = None,
                 email_receivers: Optional[pulumi.Input[Sequence[pulumi.Input['EmailReceiverArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 sms_receivers: Optional[pulumi.Input[Sequence[pulumi.Input['SmsReceiverArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenant_action_group_name: Optional[pulumi.Input[str]] = None,
                 voice_receivers: Optional[pulumi.Input[Sequence[pulumi.Input['VoiceReceiverArgs']]]] = None,
                 webhook_receivers: Optional[pulumi.Input[Sequence[pulumi.Input['WebhookReceiverArgs']]]] = None):
        """
        The set of arguments for constructing a TenantActionGroup resource.
        :param pulumi.Input[bool] enabled: Indicates whether this tenant action group is enabled. If a tenant action group is not enabled, then none of its receivers will receive communications.
        :param pulumi.Input[str] group_short_name: The short name of the action group. This will be used in SMS messages.
        :param pulumi.Input[str] management_group_id: The management group id.
        :param pulumi.Input[Sequence[pulumi.Input['AzureAppPushReceiverArgs']]] azure_app_push_receivers: The list of AzureAppPush receivers that are part of this tenant action group.
        :param pulumi.Input[Sequence[pulumi.Input['EmailReceiverArgs']]] email_receivers: The list of email receivers that are part of this tenant action group.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Sequence[pulumi.Input['SmsReceiverArgs']]] sms_receivers: The list of SMS receivers that are part of this tenant action group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] tenant_action_group_name: The name of the action group.
        :param pulumi.Input[Sequence[pulumi.Input['VoiceReceiverArgs']]] voice_receivers: The list of voice receivers that are part of this tenant action group.
        :param pulumi.Input[Sequence[pulumi.Input['WebhookReceiverArgs']]] webhook_receivers: The list of webhook receivers that are part of this tenant action group.
        """
        if enabled is None:
            enabled = True
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "group_short_name", group_short_name)
        pulumi.set(__self__, "management_group_id", management_group_id)
        if azure_app_push_receivers is not None:
            pulumi.set(__self__, "azure_app_push_receivers", azure_app_push_receivers)
        if email_receivers is not None:
            pulumi.set(__self__, "email_receivers", email_receivers)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if sms_receivers is not None:
            pulumi.set(__self__, "sms_receivers", sms_receivers)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tenant_action_group_name is not None:
            pulumi.set(__self__, "tenant_action_group_name", tenant_action_group_name)
        if voice_receivers is not None:
            pulumi.set(__self__, "voice_receivers", voice_receivers)
        if webhook_receivers is not None:
            pulumi.set(__self__, "webhook_receivers", webhook_receivers)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Indicates whether this tenant action group is enabled. If a tenant action group is not enabled, then none of its receivers will receive communications.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="groupShortName")
    def group_short_name(self) -> pulumi.Input[str]:
        """
        The short name of the action group. This will be used in SMS messages.
        """
        return pulumi.get(self, "group_short_name")

    @group_short_name.setter
    def group_short_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_short_name", value)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[str]:
        """
        The management group id.
        """
        return pulumi.get(self, "management_group_id")

    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "management_group_id", value)

    @property
    @pulumi.getter(name="azureAppPushReceivers")
    def azure_app_push_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AzureAppPushReceiverArgs']]]]:
        """
        The list of AzureAppPush receivers that are part of this tenant action group.
        """
        return pulumi.get(self, "azure_app_push_receivers")

    @azure_app_push_receivers.setter
    def azure_app_push_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AzureAppPushReceiverArgs']]]]):
        pulumi.set(self, "azure_app_push_receivers", value)

    @property
    @pulumi.getter(name="emailReceivers")
    def email_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EmailReceiverArgs']]]]:
        """
        The list of email receivers that are part of this tenant action group.
        """
        return pulumi.get(self, "email_receivers")

    @email_receivers.setter
    def email_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EmailReceiverArgs']]]]):
        pulumi.set(self, "email_receivers", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="smsReceivers")
    def sms_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SmsReceiverArgs']]]]:
        """
        The list of SMS receivers that are part of this tenant action group.
        """
        return pulumi.get(self, "sms_receivers")

    @sms_receivers.setter
    def sms_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SmsReceiverArgs']]]]):
        pulumi.set(self, "sms_receivers", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tenantActionGroupName")
    def tenant_action_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the action group.
        """
        return pulumi.get(self, "tenant_action_group_name")

    @tenant_action_group_name.setter
    def tenant_action_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_action_group_name", value)

    @property
    @pulumi.getter(name="voiceReceivers")
    def voice_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VoiceReceiverArgs']]]]:
        """
        The list of voice receivers that are part of this tenant action group.
        """
        return pulumi.get(self, "voice_receivers")

    @voice_receivers.setter
    def voice_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VoiceReceiverArgs']]]]):
        pulumi.set(self, "voice_receivers", value)

    @property
    @pulumi.getter(name="webhookReceivers")
    def webhook_receivers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WebhookReceiverArgs']]]]:
        """
        The list of webhook receivers that are part of this tenant action group.
        """
        return pulumi.get(self, "webhook_receivers")

    @webhook_receivers.setter
    def webhook_receivers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WebhookReceiverArgs']]]]):
        pulumi.set(self, "webhook_receivers", value)


class TenantActionGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_app_push_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureAppPushReceiverArgs']]]]] = None,
                 email_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailReceiverArgs']]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 group_short_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 sms_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SmsReceiverArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenant_action_group_name: Optional[pulumi.Input[str]] = None,
                 voice_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VoiceReceiverArgs']]]]] = None,
                 webhook_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebhookReceiverArgs']]]]] = None,
                 __props__=None):
        """
        A tenant action group resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureAppPushReceiverArgs']]]] azure_app_push_receivers: The list of AzureAppPush receivers that are part of this tenant action group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailReceiverArgs']]]] email_receivers: The list of email receivers that are part of this tenant action group.
        :param pulumi.Input[bool] enabled: Indicates whether this tenant action group is enabled. If a tenant action group is not enabled, then none of its receivers will receive communications.
        :param pulumi.Input[str] group_short_name: The short name of the action group. This will be used in SMS messages.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] management_group_id: The management group id.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SmsReceiverArgs']]]] sms_receivers: The list of SMS receivers that are part of this tenant action group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] tenant_action_group_name: The name of the action group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VoiceReceiverArgs']]]] voice_receivers: The list of voice receivers that are part of this tenant action group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebhookReceiverArgs']]]] webhook_receivers: The list of webhook receivers that are part of this tenant action group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TenantActionGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A tenant action group resource.

        :param str resource_name: The name of the resource.
        :param TenantActionGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TenantActionGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_app_push_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AzureAppPushReceiverArgs']]]]] = None,
                 email_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailReceiverArgs']]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 group_short_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 sms_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SmsReceiverArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenant_action_group_name: Optional[pulumi.Input[str]] = None,
                 voice_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VoiceReceiverArgs']]]]] = None,
                 webhook_receivers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebhookReceiverArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TenantActionGroupArgs.__new__(TenantActionGroupArgs)

            __props__.__dict__["azure_app_push_receivers"] = azure_app_push_receivers
            __props__.__dict__["email_receivers"] = email_receivers
            if enabled is None:
                enabled = True
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            if group_short_name is None and not opts.urn:
                raise TypeError("Missing required property 'group_short_name'")
            __props__.__dict__["group_short_name"] = group_short_name
            __props__.__dict__["location"] = location
            if management_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'management_group_id'")
            __props__.__dict__["management_group_id"] = management_group_id
            __props__.__dict__["sms_receivers"] = sms_receivers
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tenant_action_group_name"] = tenant_action_group_name
            __props__.__dict__["voice_receivers"] = voice_receivers
            __props__.__dict__["webhook_receivers"] = webhook_receivers
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights:TenantActionGroup"), pulumi.Alias(type_="azure-native:insights/v20230301preview:TenantActionGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(TenantActionGroup, __self__).__init__(
            'azure-native:insights/v20230501preview:TenantActionGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TenantActionGroup':
        """
        Get an existing TenantActionGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TenantActionGroupArgs.__new__(TenantActionGroupArgs)

        __props__.__dict__["azure_app_push_receivers"] = None
        __props__.__dict__["email_receivers"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["group_short_name"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sms_receivers"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["voice_receivers"] = None
        __props__.__dict__["webhook_receivers"] = None
        return TenantActionGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureAppPushReceivers")
    def azure_app_push_receivers(self) -> pulumi.Output[Optional[Sequence['outputs.AzureAppPushReceiverResponse']]]:
        """
        The list of AzureAppPush receivers that are part of this tenant action group.
        """
        return pulumi.get(self, "azure_app_push_receivers")

    @property
    @pulumi.getter(name="emailReceivers")
    def email_receivers(self) -> pulumi.Output[Optional[Sequence['outputs.EmailReceiverResponse']]]:
        """
        The list of email receivers that are part of this tenant action group.
        """
        return pulumi.get(self, "email_receivers")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Indicates whether this tenant action group is enabled. If a tenant action group is not enabled, then none of its receivers will receive communications.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="groupShortName")
    def group_short_name(self) -> pulumi.Output[str]:
        """
        The short name of the action group. This will be used in SMS messages.
        """
        return pulumi.get(self, "group_short_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="smsReceivers")
    def sms_receivers(self) -> pulumi.Output[Optional[Sequence['outputs.SmsReceiverResponse']]]:
        """
        The list of SMS receivers that are part of this tenant action group.
        """
        return pulumi.get(self, "sms_receivers")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="voiceReceivers")
    def voice_receivers(self) -> pulumi.Output[Optional[Sequence['outputs.VoiceReceiverResponse']]]:
        """
        The list of voice receivers that are part of this tenant action group.
        """
        return pulumi.get(self, "voice_receivers")

    @property
    @pulumi.getter(name="webhookReceivers")
    def webhook_receivers(self) -> pulumi.Output[Optional[Sequence['outputs.WebhookReceiverResponse']]]:
        """
        The list of webhook receivers that are part of this tenant action group.
        """
        return pulumi.get(self, "webhook_receivers")

