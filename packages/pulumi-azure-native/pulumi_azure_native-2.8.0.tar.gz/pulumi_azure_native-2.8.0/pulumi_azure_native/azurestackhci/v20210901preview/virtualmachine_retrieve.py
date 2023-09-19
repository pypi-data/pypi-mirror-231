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

__all__ = ['VirtualmachineRetrieveArgs', 'VirtualmachineRetrieve']

@pulumi.input_type
class VirtualmachineRetrieveArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 hardware_profile: Optional[pulumi.Input['VirtualmachinesPropertiesHardwareProfileArgs']] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input['VirtualmachinesPropertiesNetworkProfileArgs']] = None,
                 os_profile: Optional[pulumi.Input['VirtualmachinesPropertiesOsProfileArgs']] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input['VirtualmachinesPropertiesSecurityProfileArgs']] = None,
                 storage_profile: Optional[pulumi.Input['VirtualmachinesPropertiesStorageProfileArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtualmachines_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualmachineRetrieve resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extendedLocation of the resource.
        :param pulumi.Input['VirtualmachinesPropertiesHardwareProfileArgs'] hardware_profile: HardwareProfile - Specifies the hardware settings for the virtual machine.
        :param pulumi.Input['IdentityArgs'] identity: Identity for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['VirtualmachinesPropertiesNetworkProfileArgs'] network_profile: NetworkProfile - describes the network configuration the virtual machine
        :param pulumi.Input['VirtualmachinesPropertiesOsProfileArgs'] os_profile: OsProfile - describes the configuration of the operating system and sets login data
        :param pulumi.Input[str] resource_name: name of the object to be used in moc
        :param pulumi.Input['VirtualmachinesPropertiesSecurityProfileArgs'] security_profile: SecurityProfile - Specifies the security settings for the virtual machine.
        :param pulumi.Input['VirtualmachinesPropertiesStorageProfileArgs'] storage_profile: StorageProfile - contains information about the disks and storage information for the virtual machine
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if hardware_profile is not None:
            pulumi.set(__self__, "hardware_profile", hardware_profile)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if os_profile is not None:
            pulumi.set(__self__, "os_profile", os_profile)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if security_profile is not None:
            pulumi.set(__self__, "security_profile", security_profile)
        if storage_profile is not None:
            pulumi.set(__self__, "storage_profile", storage_profile)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtualmachines_name is not None:
            pulumi.set(__self__, "virtualmachines_name", virtualmachines_name)

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
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input['VirtualmachinesPropertiesHardwareProfileArgs']]:
        """
        HardwareProfile - Specifies the hardware settings for the virtual machine.
        """
        return pulumi.get(self, "hardware_profile")

    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input['VirtualmachinesPropertiesHardwareProfileArgs']]):
        pulumi.set(self, "hardware_profile", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

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
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['VirtualmachinesPropertiesNetworkProfileArgs']]:
        """
        NetworkProfile - describes the network configuration the virtual machine
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['VirtualmachinesPropertiesNetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input['VirtualmachinesPropertiesOsProfileArgs']]:
        """
        OsProfile - describes the configuration of the operating system and sets login data
        """
        return pulumi.get(self, "os_profile")

    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input['VirtualmachinesPropertiesOsProfileArgs']]):
        pulumi.set(self, "os_profile", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the object to be used in moc
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input['VirtualmachinesPropertiesSecurityProfileArgs']]:
        """
        SecurityProfile - Specifies the security settings for the virtual machine.
        """
        return pulumi.get(self, "security_profile")

    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input['VirtualmachinesPropertiesSecurityProfileArgs']]):
        pulumi.set(self, "security_profile", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['VirtualmachinesPropertiesStorageProfileArgs']]:
        """
        StorageProfile - contains information about the disks and storage information for the virtual machine
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['VirtualmachinesPropertiesStorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)

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

    @property
    @pulumi.getter(name="virtualmachinesName")
    def virtualmachines_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "virtualmachines_name")

    @virtualmachines_name.setter
    def virtualmachines_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtualmachines_name", value)


class VirtualmachineRetrieve(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 hardware_profile: Optional[pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesHardwareProfileArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesNetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesOsProfileArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesSecurityProfileArgs']]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesStorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtualmachines_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The virtual machine resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extendedLocation of the resource.
        :param pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesHardwareProfileArgs']] hardware_profile: HardwareProfile - Specifies the hardware settings for the virtual machine.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: Identity for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesNetworkProfileArgs']] network_profile: NetworkProfile - describes the network configuration the virtual machine
        :param pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesOsProfileArgs']] os_profile: OsProfile - describes the configuration of the operating system and sets login data
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: name of the object to be used in moc
        :param pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesSecurityProfileArgs']] security_profile: SecurityProfile - Specifies the security settings for the virtual machine.
        :param pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesStorageProfileArgs']] storage_profile: StorageProfile - contains information about the disks and storage information for the virtual machine
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualmachineRetrieveArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The virtual machine resource definition.

        :param str resource_name: The name of the resource.
        :param VirtualmachineRetrieveArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualmachineRetrieveArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 hardware_profile: Optional[pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesHardwareProfileArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesNetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesOsProfileArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 security_profile: Optional[pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesSecurityProfileArgs']]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['VirtualmachinesPropertiesStorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtualmachines_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualmachineRetrieveArgs.__new__(VirtualmachineRetrieveArgs)

            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["hardware_profile"] = hardware_profile
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["network_profile"] = network_profile
            __props__.__dict__["os_profile"] = os_profile
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["security_profile"] = security_profile
            __props__.__dict__["storage_profile"] = storage_profile
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtualmachines_name"] = virtualmachines_name
            __props__.__dict__["guest_agent_profile"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["vm_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci/v20210901preview:virtualmachineRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci:VirtualmachineRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci:virtualmachineRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20210701preview:VirtualmachineRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20210701preview:virtualmachineRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:VirtualmachineRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:virtualmachineRetrieve")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualmachineRetrieve, __self__).__init__(
            'azure-native:azurestackhci/v20210901preview:VirtualmachineRetrieve',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualmachineRetrieve':
        """
        Get an existing VirtualmachineRetrieve resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualmachineRetrieveArgs.__new__(VirtualmachineRetrieveArgs)

        __props__.__dict__["extended_location"] = None
        __props__.__dict__["guest_agent_profile"] = None
        __props__.__dict__["hardware_profile"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["os_profile"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_name"] = None
        __props__.__dict__["security_profile"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["storage_profile"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vm_id"] = None
        return VirtualmachineRetrieve(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="guestAgentProfile")
    def guest_agent_profile(self) -> pulumi.Output[Optional['outputs.GuestAgentProfileResponse']]:
        """
        Guest agent status properties.
        """
        return pulumi.get(self, "guest_agent_profile")

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> pulumi.Output[Optional['outputs.VirtualmachinesPropertiesResponseHardwareProfile']]:
        """
        HardwareProfile - Specifies the hardware settings for the virtual machine.
        """
        return pulumi.get(self, "hardware_profile")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

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
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional['outputs.VirtualmachinesPropertiesResponseNetworkProfile']]:
        """
        NetworkProfile - describes the network configuration the virtual machine
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output[Optional['outputs.VirtualmachinesPropertiesResponseOsProfile']]:
        """
        OsProfile - describes the configuration of the operating system and sets login data
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Output[Optional[str]]:
        """
        name of the object to be used in moc
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Output[Optional['outputs.VirtualmachinesPropertiesResponseSecurityProfile']]:
        """
        SecurityProfile - Specifies the security settings for the virtual machine.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.VirtualMachineStatusResponse']:
        """
        VirtualMachineStatus defines the observed state of virtualmachines
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional['outputs.VirtualmachinesPropertiesResponseStorageProfile']]:
        """
        StorageProfile - contains information about the disks and storage information for the virtual machine
        """
        return pulumi.get(self, "storage_profile")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
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

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[str]:
        """
        Unique identifier for the vm resource.
        """
        return pulumi.get(self, "vm_id")

