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

__all__ = ['ProviderInstanceArgs', 'ProviderInstance']

@pulumi.input_type
class ProviderInstanceArgs:
    def __init__(__self__, *,
                 monitor_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['UserAssignedServiceIdentityArgs']] = None,
                 provider_instance_name: Optional[pulumi.Input[str]] = None,
                 provider_settings: Optional[pulumi.Input[Union['DB2ProviderInstancePropertiesArgs', 'HanaDbProviderInstancePropertiesArgs', 'MsSqlServerProviderInstancePropertiesArgs', 'PrometheusHaClusterProviderInstancePropertiesArgs', 'PrometheusOSProviderInstancePropertiesArgs', 'SapNetWeaverProviderInstancePropertiesArgs']]] = None):
        """
        The set of arguments for constructing a ProviderInstance resource.
        :param pulumi.Input[str] monitor_name: Name of the SAP monitor resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['UserAssignedServiceIdentityArgs'] identity: [currently not in use] Managed service identity(user assigned identities)
        :param pulumi.Input[str] provider_instance_name: Name of the provider instance.
        :param pulumi.Input[Union['DB2ProviderInstancePropertiesArgs', 'HanaDbProviderInstancePropertiesArgs', 'MsSqlServerProviderInstancePropertiesArgs', 'PrometheusHaClusterProviderInstancePropertiesArgs', 'PrometheusOSProviderInstancePropertiesArgs', 'SapNetWeaverProviderInstancePropertiesArgs']] provider_settings: Defines the provider specific properties.
        """
        pulumi.set(__self__, "monitor_name", monitor_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if provider_instance_name is not None:
            pulumi.set(__self__, "provider_instance_name", provider_instance_name)
        if provider_settings is not None:
            pulumi.set(__self__, "provider_settings", provider_settings)

    @property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Input[str]:
        """
        Name of the SAP monitor resource.
        """
        return pulumi.get(self, "monitor_name")

    @monitor_name.setter
    def monitor_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "monitor_name", value)

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
    def identity(self) -> Optional[pulumi.Input['UserAssignedServiceIdentityArgs']]:
        """
        [currently not in use] Managed service identity(user assigned identities)
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['UserAssignedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="providerInstanceName")
    def provider_instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the provider instance.
        """
        return pulumi.get(self, "provider_instance_name")

    @provider_instance_name.setter
    def provider_instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_instance_name", value)

    @property
    @pulumi.getter(name="providerSettings")
    def provider_settings(self) -> Optional[pulumi.Input[Union['DB2ProviderInstancePropertiesArgs', 'HanaDbProviderInstancePropertiesArgs', 'MsSqlServerProviderInstancePropertiesArgs', 'PrometheusHaClusterProviderInstancePropertiesArgs', 'PrometheusOSProviderInstancePropertiesArgs', 'SapNetWeaverProviderInstancePropertiesArgs']]]:
        """
        Defines the provider specific properties.
        """
        return pulumi.get(self, "provider_settings")

    @provider_settings.setter
    def provider_settings(self, value: Optional[pulumi.Input[Union['DB2ProviderInstancePropertiesArgs', 'HanaDbProviderInstancePropertiesArgs', 'MsSqlServerProviderInstancePropertiesArgs', 'PrometheusHaClusterProviderInstancePropertiesArgs', 'PrometheusOSProviderInstancePropertiesArgs', 'SapNetWeaverProviderInstancePropertiesArgs']]]):
        pulumi.set(self, "provider_settings", value)


class ProviderInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['UserAssignedServiceIdentityArgs']]] = None,
                 monitor_name: Optional[pulumi.Input[str]] = None,
                 provider_instance_name: Optional[pulumi.Input[str]] = None,
                 provider_settings: Optional[pulumi.Input[Union[pulumi.InputType['DB2ProviderInstancePropertiesArgs'], pulumi.InputType['HanaDbProviderInstancePropertiesArgs'], pulumi.InputType['MsSqlServerProviderInstancePropertiesArgs'], pulumi.InputType['PrometheusHaClusterProviderInstancePropertiesArgs'], pulumi.InputType['PrometheusOSProviderInstancePropertiesArgs'], pulumi.InputType['SapNetWeaverProviderInstancePropertiesArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A provider instance associated with SAP monitor.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['UserAssignedServiceIdentityArgs']] identity: [currently not in use] Managed service identity(user assigned identities)
        :param pulumi.Input[str] monitor_name: Name of the SAP monitor resource.
        :param pulumi.Input[str] provider_instance_name: Name of the provider instance.
        :param pulumi.Input[Union[pulumi.InputType['DB2ProviderInstancePropertiesArgs'], pulumi.InputType['HanaDbProviderInstancePropertiesArgs'], pulumi.InputType['MsSqlServerProviderInstancePropertiesArgs'], pulumi.InputType['PrometheusHaClusterProviderInstancePropertiesArgs'], pulumi.InputType['PrometheusOSProviderInstancePropertiesArgs'], pulumi.InputType['SapNetWeaverProviderInstancePropertiesArgs']]] provider_settings: Defines the provider specific properties.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A provider instance associated with SAP monitor.

        :param str resource_name: The name of the resource.
        :param ProviderInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['UserAssignedServiceIdentityArgs']]] = None,
                 monitor_name: Optional[pulumi.Input[str]] = None,
                 provider_instance_name: Optional[pulumi.Input[str]] = None,
                 provider_settings: Optional[pulumi.Input[Union[pulumi.InputType['DB2ProviderInstancePropertiesArgs'], pulumi.InputType['HanaDbProviderInstancePropertiesArgs'], pulumi.InputType['MsSqlServerProviderInstancePropertiesArgs'], pulumi.InputType['PrometheusHaClusterProviderInstancePropertiesArgs'], pulumi.InputType['PrometheusOSProviderInstancePropertiesArgs'], pulumi.InputType['SapNetWeaverProviderInstancePropertiesArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderInstanceArgs.__new__(ProviderInstanceArgs)

            __props__.__dict__["identity"] = identity
            if monitor_name is None and not opts.urn:
                raise TypeError("Missing required property 'monitor_name'")
            __props__.__dict__["monitor_name"] = monitor_name
            __props__.__dict__["provider_instance_name"] = provider_instance_name
            __props__.__dict__["provider_settings"] = provider_settings
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["errors"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:workloads:ProviderInstance"), pulumi.Alias(type_="azure-native:workloads/v20211201preview:ProviderInstance"), pulumi.Alias(type_="azure-native:workloads/v20221101preview:ProviderInstance")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ProviderInstance, __self__).__init__(
            'azure-native:workloads/v20230401:ProviderInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProviderInstance':
        """
        Get an existing ProviderInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProviderInstanceArgs.__new__(ProviderInstanceArgs)

        __props__.__dict__["errors"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provider_settings"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ProviderInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def errors(self) -> pulumi.Output['outputs.ProviderInstancePropertiesResponseErrors']:
        """
        Defines the provider instance errors.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.UserAssignedServiceIdentityResponse']]:
        """
        [currently not in use] Managed service identity(user assigned identities)
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="providerSettings")
    def provider_settings(self) -> pulumi.Output[Optional[Any]]:
        """
        Defines the provider specific properties.
        """
        return pulumi.get(self, "provider_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of provisioning of the provider instance
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
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

