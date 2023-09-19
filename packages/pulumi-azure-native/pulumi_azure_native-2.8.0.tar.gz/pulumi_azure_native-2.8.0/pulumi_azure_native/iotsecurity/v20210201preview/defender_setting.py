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

__all__ = ['DefenderSettingArgs', 'DefenderSetting']

@pulumi.input_type
class DefenderSettingArgs:
    def __init__(__self__, *,
                 device_quota: pulumi.Input[int],
                 mde_integration: pulumi.Input['DefenderSettingsPropertiesMdeIntegrationArgs'],
                 onboarding_kind: pulumi.Input[Union[str, 'OnboardingKind']],
                 sentinel_workspace_resource_ids: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The set of arguments for constructing a DefenderSetting resource.
        :param pulumi.Input[int] device_quota: Size of the device quota. Value is required to be in multiples of 100.
        :param pulumi.Input['DefenderSettingsPropertiesMdeIntegrationArgs'] mde_integration: MDE integration configuration
        :param pulumi.Input[Union[str, 'OnboardingKind']] onboarding_kind: The kind of onboarding for the subscription
        :param pulumi.Input[Sequence[pulumi.Input[str]]] sentinel_workspace_resource_ids: Sentinel Workspace Resource Ids
        """
        pulumi.set(__self__, "device_quota", device_quota)
        pulumi.set(__self__, "mde_integration", mde_integration)
        pulumi.set(__self__, "onboarding_kind", onboarding_kind)
        pulumi.set(__self__, "sentinel_workspace_resource_ids", sentinel_workspace_resource_ids)

    @property
    @pulumi.getter(name="deviceQuota")
    def device_quota(self) -> pulumi.Input[int]:
        """
        Size of the device quota. Value is required to be in multiples of 100.
        """
        return pulumi.get(self, "device_quota")

    @device_quota.setter
    def device_quota(self, value: pulumi.Input[int]):
        pulumi.set(self, "device_quota", value)

    @property
    @pulumi.getter(name="mdeIntegration")
    def mde_integration(self) -> pulumi.Input['DefenderSettingsPropertiesMdeIntegrationArgs']:
        """
        MDE integration configuration
        """
        return pulumi.get(self, "mde_integration")

    @mde_integration.setter
    def mde_integration(self, value: pulumi.Input['DefenderSettingsPropertiesMdeIntegrationArgs']):
        pulumi.set(self, "mde_integration", value)

    @property
    @pulumi.getter(name="onboardingKind")
    def onboarding_kind(self) -> pulumi.Input[Union[str, 'OnboardingKind']]:
        """
        The kind of onboarding for the subscription
        """
        return pulumi.get(self, "onboarding_kind")

    @onboarding_kind.setter
    def onboarding_kind(self, value: pulumi.Input[Union[str, 'OnboardingKind']]):
        pulumi.set(self, "onboarding_kind", value)

    @property
    @pulumi.getter(name="sentinelWorkspaceResourceIds")
    def sentinel_workspace_resource_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Sentinel Workspace Resource Ids
        """
        return pulumi.get(self, "sentinel_workspace_resource_ids")

    @sentinel_workspace_resource_ids.setter
    def sentinel_workspace_resource_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "sentinel_workspace_resource_ids", value)


class DefenderSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device_quota: Optional[pulumi.Input[int]] = None,
                 mde_integration: Optional[pulumi.Input[pulumi.InputType['DefenderSettingsPropertiesMdeIntegrationArgs']]] = None,
                 onboarding_kind: Optional[pulumi.Input[Union[str, 'OnboardingKind']]] = None,
                 sentinel_workspace_resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        IoT Defender settings

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] device_quota: Size of the device quota. Value is required to be in multiples of 100.
        :param pulumi.Input[pulumi.InputType['DefenderSettingsPropertiesMdeIntegrationArgs']] mde_integration: MDE integration configuration
        :param pulumi.Input[Union[str, 'OnboardingKind']] onboarding_kind: The kind of onboarding for the subscription
        :param pulumi.Input[Sequence[pulumi.Input[str]]] sentinel_workspace_resource_ids: Sentinel Workspace Resource Ids
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DefenderSettingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        IoT Defender settings

        :param str resource_name: The name of the resource.
        :param DefenderSettingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DefenderSettingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device_quota: Optional[pulumi.Input[int]] = None,
                 mde_integration: Optional[pulumi.Input[pulumi.InputType['DefenderSettingsPropertiesMdeIntegrationArgs']]] = None,
                 onboarding_kind: Optional[pulumi.Input[Union[str, 'OnboardingKind']]] = None,
                 sentinel_workspace_resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DefenderSettingArgs.__new__(DefenderSettingArgs)

            if device_quota is None and not opts.urn:
                raise TypeError("Missing required property 'device_quota'")
            __props__.__dict__["device_quota"] = device_quota
            if mde_integration is None and not opts.urn:
                raise TypeError("Missing required property 'mde_integration'")
            __props__.__dict__["mde_integration"] = mde_integration
            if onboarding_kind is None and not opts.urn:
                raise TypeError("Missing required property 'onboarding_kind'")
            __props__.__dict__["onboarding_kind"] = onboarding_kind
            if sentinel_workspace_resource_ids is None and not opts.urn:
                raise TypeError("Missing required property 'sentinel_workspace_resource_ids'")
            __props__.__dict__["sentinel_workspace_resource_ids"] = sentinel_workspace_resource_ids
            __props__.__dict__["evaluation_end_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:iotsecurity:DefenderSetting")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DefenderSetting, __self__).__init__(
            'azure-native:iotsecurity/v20210201preview:DefenderSetting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DefenderSetting':
        """
        Get an existing DefenderSetting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DefenderSettingArgs.__new__(DefenderSettingArgs)

        __props__.__dict__["device_quota"] = None
        __props__.__dict__["evaluation_end_time"] = None
        __props__.__dict__["mde_integration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["onboarding_kind"] = None
        __props__.__dict__["sentinel_workspace_resource_ids"] = None
        __props__.__dict__["type"] = None
        return DefenderSetting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deviceQuota")
    def device_quota(self) -> pulumi.Output[int]:
        """
        Size of the device quota. Value is required to be in multiples of 100.
        """
        return pulumi.get(self, "device_quota")

    @property
    @pulumi.getter(name="evaluationEndTime")
    def evaluation_end_time(self) -> pulumi.Output[str]:
        """
        End time of the evaluation period, if such exist
        """
        return pulumi.get(self, "evaluation_end_time")

    @property
    @pulumi.getter(name="mdeIntegration")
    def mde_integration(self) -> pulumi.Output['outputs.DefenderSettingsPropertiesResponseMdeIntegration']:
        """
        MDE integration configuration
        """
        return pulumi.get(self, "mde_integration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="onboardingKind")
    def onboarding_kind(self) -> pulumi.Output[str]:
        """
        The kind of onboarding for the subscription
        """
        return pulumi.get(self, "onboarding_kind")

    @property
    @pulumi.getter(name="sentinelWorkspaceResourceIds")
    def sentinel_workspace_resource_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Sentinel Workspace Resource Ids
        """
        return pulumi.get(self, "sentinel_workspace_resource_ids")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

