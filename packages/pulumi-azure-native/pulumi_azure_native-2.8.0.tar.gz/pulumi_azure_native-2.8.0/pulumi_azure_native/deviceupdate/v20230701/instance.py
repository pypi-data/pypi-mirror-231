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

__all__ = ['InstanceArgs', 'Instance']

@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 diagnostic_storage_properties: Optional[pulumi.Input['DiagnosticStoragePropertiesArgs']] = None,
                 enable_diagnostics: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 iot_hubs: Optional[pulumi.Input[Sequence[pulumi.Input['IotHubSettingsArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Instance resource.
        :param pulumi.Input[str] account_name: Account name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input['DiagnosticStoragePropertiesArgs'] diagnostic_storage_properties: Customer-initiated diagnostic log collection storage properties
        :param pulumi.Input[bool] enable_diagnostics: Enables or Disables the diagnostic logs collection
        :param pulumi.Input[str] instance_name: Instance name.
        :param pulumi.Input[Sequence[pulumi.Input['IotHubSettingsArgs']]] iot_hubs: List of IoT Hubs associated with the account.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if diagnostic_storage_properties is not None:
            pulumi.set(__self__, "diagnostic_storage_properties", diagnostic_storage_properties)
        if enable_diagnostics is not None:
            pulumi.set(__self__, "enable_diagnostics", enable_diagnostics)
        if instance_name is not None:
            pulumi.set(__self__, "instance_name", instance_name)
        if iot_hubs is not None:
            pulumi.set(__self__, "iot_hubs", iot_hubs)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="diagnosticStorageProperties")
    def diagnostic_storage_properties(self) -> Optional[pulumi.Input['DiagnosticStoragePropertiesArgs']]:
        """
        Customer-initiated diagnostic log collection storage properties
        """
        return pulumi.get(self, "diagnostic_storage_properties")

    @diagnostic_storage_properties.setter
    def diagnostic_storage_properties(self, value: Optional[pulumi.Input['DiagnosticStoragePropertiesArgs']]):
        pulumi.set(self, "diagnostic_storage_properties", value)

    @property
    @pulumi.getter(name="enableDiagnostics")
    def enable_diagnostics(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables or Disables the diagnostic logs collection
        """
        return pulumi.get(self, "enable_diagnostics")

    @enable_diagnostics.setter
    def enable_diagnostics(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_diagnostics", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        Instance name.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IotHubSettingsArgs']]]]:
        """
        List of IoT Hubs associated with the account.
        """
        return pulumi.get(self, "iot_hubs")

    @iot_hubs.setter
    def iot_hubs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IotHubSettingsArgs']]]]):
        pulumi.set(self, "iot_hubs", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 diagnostic_storage_properties: Optional[pulumi.Input[pulumi.InputType['DiagnosticStoragePropertiesArgs']]] = None,
                 enable_diagnostics: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 iot_hubs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IotHubSettingsArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Device Update instance details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Account name.
        :param pulumi.Input[pulumi.InputType['DiagnosticStoragePropertiesArgs']] diagnostic_storage_properties: Customer-initiated diagnostic log collection storage properties
        :param pulumi.Input[bool] enable_diagnostics: Enables or Disables the diagnostic logs collection
        :param pulumi.Input[str] instance_name: Instance name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IotHubSettingsArgs']]]] iot_hubs: List of IoT Hubs associated with the account.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Device Update instance details.

        :param str resource_name: The name of the resource.
        :param InstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 diagnostic_storage_properties: Optional[pulumi.Input[pulumi.InputType['DiagnosticStoragePropertiesArgs']]] = None,
                 enable_diagnostics: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 iot_hubs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IotHubSettingsArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceArgs.__new__(InstanceArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["diagnostic_storage_properties"] = diagnostic_storage_properties
            __props__.__dict__["enable_diagnostics"] = enable_diagnostics
            __props__.__dict__["instance_name"] = instance_name
            __props__.__dict__["iot_hubs"] = iot_hubs
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:deviceupdate:Instance"), pulumi.Alias(type_="azure-native:deviceupdate/v20200301preview:Instance"), pulumi.Alias(type_="azure-native:deviceupdate/v20220401preview:Instance"), pulumi.Alias(type_="azure-native:deviceupdate/v20221001:Instance"), pulumi.Alias(type_="azure-native:deviceupdate/v20221201preview:Instance")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Instance, __self__).__init__(
            'azure-native:deviceupdate/v20230701:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceArgs.__new__(InstanceArgs)

        __props__.__dict__["account_name"] = None
        __props__.__dict__["diagnostic_storage_properties"] = None
        __props__.__dict__["enable_diagnostics"] = None
        __props__.__dict__["iot_hubs"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        Parent Device Update Account name which Instance belongs to.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="diagnosticStorageProperties")
    def diagnostic_storage_properties(self) -> pulumi.Output[Optional['outputs.DiagnosticStoragePropertiesResponse']]:
        """
        Customer-initiated diagnostic log collection storage properties
        """
        return pulumi.get(self, "diagnostic_storage_properties")

    @property
    @pulumi.getter(name="enableDiagnostics")
    def enable_diagnostics(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables or Disables the diagnostic logs collection
        """
        return pulumi.get(self, "enable_diagnostics")

    @property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(self) -> pulumi.Output[Optional[Sequence['outputs.IotHubSettingsResponse']]]:
        """
        List of IoT Hubs associated with the account.
        """
        return pulumi.get(self, "iot_hubs")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

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

