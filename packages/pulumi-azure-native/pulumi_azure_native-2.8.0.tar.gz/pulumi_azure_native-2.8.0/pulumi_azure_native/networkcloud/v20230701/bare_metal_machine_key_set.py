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

__all__ = ['BareMetalMachineKeySetArgs', 'BareMetalMachineKeySet']

@pulumi.input_type
class BareMetalMachineKeySetArgs:
    def __init__(__self__, *,
                 azure_group_id: pulumi.Input[str],
                 cluster_name: pulumi.Input[str],
                 expiration: pulumi.Input[str],
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 jump_hosts_allowed: pulumi.Input[Sequence[pulumi.Input[str]]],
                 privilege_level: pulumi.Input[Union[str, 'BareMetalMachineKeySetPrivilegeLevel']],
                 resource_group_name: pulumi.Input[str],
                 user_list: pulumi.Input[Sequence[pulumi.Input['KeySetUserArgs']]],
                 bare_metal_machine_key_set_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a BareMetalMachineKeySet resource.
        :param pulumi.Input[str] azure_group_id: The object ID of Azure Active Directory group that all users in the list must be in for access to be granted. Users that are not in the group will not have access.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[str] expiration: The date and time after which the users in this key set will be removed from the bare metal machines.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jump_hosts_allowed: The list of IP addresses of jump hosts with management network access from which a login will be allowed for the users.
        :param pulumi.Input[Union[str, 'BareMetalMachineKeySetPrivilegeLevel']] privilege_level: The access level allowed for the users in this key set.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['KeySetUserArgs']]] user_list: The unique list of permitted users.
        :param pulumi.Input[str] bare_metal_machine_key_set_name: The name of the bare metal machine key set.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] os_group_name: The name of the group that users will be assigned to on the operating system of the machines.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "azure_group_id", azure_group_id)
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "expiration", expiration)
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "jump_hosts_allowed", jump_hosts_allowed)
        pulumi.set(__self__, "privilege_level", privilege_level)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "user_list", user_list)
        if bare_metal_machine_key_set_name is not None:
            pulumi.set(__self__, "bare_metal_machine_key_set_name", bare_metal_machine_key_set_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if os_group_name is not None:
            pulumi.set(__self__, "os_group_name", os_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="azureGroupId")
    def azure_group_id(self) -> pulumi.Input[str]:
        """
        The object ID of Azure Active Directory group that all users in the list must be in for access to be granted. Users that are not in the group will not have access.
        """
        return pulumi.get(self, "azure_group_id")

    @azure_group_id.setter
    def azure_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "azure_group_id", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter
    def expiration(self) -> pulumi.Input[str]:
        """
        The date and time after which the users in this key set will be removed from the bare metal machines.
        """
        return pulumi.get(self, "expiration")

    @expiration.setter
    def expiration(self, value: pulumi.Input[str]):
        pulumi.set(self, "expiration", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="jumpHostsAllowed")
    def jump_hosts_allowed(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of IP addresses of jump hosts with management network access from which a login will be allowed for the users.
        """
        return pulumi.get(self, "jump_hosts_allowed")

    @jump_hosts_allowed.setter
    def jump_hosts_allowed(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "jump_hosts_allowed", value)

    @property
    @pulumi.getter(name="privilegeLevel")
    def privilege_level(self) -> pulumi.Input[Union[str, 'BareMetalMachineKeySetPrivilegeLevel']]:
        """
        The access level allowed for the users in this key set.
        """
        return pulumi.get(self, "privilege_level")

    @privilege_level.setter
    def privilege_level(self, value: pulumi.Input[Union[str, 'BareMetalMachineKeySetPrivilegeLevel']]):
        pulumi.set(self, "privilege_level", value)

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
    @pulumi.getter(name="userList")
    def user_list(self) -> pulumi.Input[Sequence[pulumi.Input['KeySetUserArgs']]]:
        """
        The unique list of permitted users.
        """
        return pulumi.get(self, "user_list")

    @user_list.setter
    def user_list(self, value: pulumi.Input[Sequence[pulumi.Input['KeySetUserArgs']]]):
        pulumi.set(self, "user_list", value)

    @property
    @pulumi.getter(name="bareMetalMachineKeySetName")
    def bare_metal_machine_key_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the bare metal machine key set.
        """
        return pulumi.get(self, "bare_metal_machine_key_set_name")

    @bare_metal_machine_key_set_name.setter
    def bare_metal_machine_key_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bare_metal_machine_key_set_name", value)

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
    @pulumi.getter(name="osGroupName")
    def os_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the group that users will be assigned to on the operating system of the machines.
        """
        return pulumi.get(self, "os_group_name")

    @os_group_name.setter
    def os_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_group_name", value)

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


class BareMetalMachineKeySet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_group_id: Optional[pulumi.Input[str]] = None,
                 bare_metal_machine_key_set_name: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 expiration: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 jump_hosts_allowed: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_group_name: Optional[pulumi.Input[str]] = None,
                 privilege_level: Optional[pulumi.Input[Union[str, 'BareMetalMachineKeySetPrivilegeLevel']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_list: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeySetUserArgs']]]]] = None,
                 __props__=None):
        """
        Create a BareMetalMachineKeySet resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] azure_group_id: The object ID of Azure Active Directory group that all users in the list must be in for access to be granted. Users that are not in the group will not have access.
        :param pulumi.Input[str] bare_metal_machine_key_set_name: The name of the bare metal machine key set.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[str] expiration: The date and time after which the users in this key set will be removed from the bare metal machines.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] jump_hosts_allowed: The list of IP addresses of jump hosts with management network access from which a login will be allowed for the users.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] os_group_name: The name of the group that users will be assigned to on the operating system of the machines.
        :param pulumi.Input[Union[str, 'BareMetalMachineKeySetPrivilegeLevel']] privilege_level: The access level allowed for the users in this key set.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeySetUserArgs']]]] user_list: The unique list of permitted users.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BareMetalMachineKeySetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a BareMetalMachineKeySet resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param BareMetalMachineKeySetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BareMetalMachineKeySetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_group_id: Optional[pulumi.Input[str]] = None,
                 bare_metal_machine_key_set_name: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 expiration: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 jump_hosts_allowed: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_group_name: Optional[pulumi.Input[str]] = None,
                 privilege_level: Optional[pulumi.Input[Union[str, 'BareMetalMachineKeySetPrivilegeLevel']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_list: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeySetUserArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BareMetalMachineKeySetArgs.__new__(BareMetalMachineKeySetArgs)

            if azure_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'azure_group_id'")
            __props__.__dict__["azure_group_id"] = azure_group_id
            __props__.__dict__["bare_metal_machine_key_set_name"] = bare_metal_machine_key_set_name
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if expiration is None and not opts.urn:
                raise TypeError("Missing required property 'expiration'")
            __props__.__dict__["expiration"] = expiration
            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            if jump_hosts_allowed is None and not opts.urn:
                raise TypeError("Missing required property 'jump_hosts_allowed'")
            __props__.__dict__["jump_hosts_allowed"] = jump_hosts_allowed
            __props__.__dict__["location"] = location
            __props__.__dict__["os_group_name"] = os_group_name
            if privilege_level is None and not opts.urn:
                raise TypeError("Missing required property 'privilege_level'")
            __props__.__dict__["privilege_level"] = privilege_level
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if user_list is None and not opts.urn:
                raise TypeError("Missing required property 'user_list'")
            __props__.__dict__["user_list"] = user_list
            __props__.__dict__["detailed_status"] = None
            __props__.__dict__["detailed_status_message"] = None
            __props__.__dict__["last_validation"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["user_list_status"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkcloud:BareMetalMachineKeySet"), pulumi.Alias(type_="azure-native:networkcloud/v20221212preview:BareMetalMachineKeySet"), pulumi.Alias(type_="azure-native:networkcloud/v20230501preview:BareMetalMachineKeySet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BareMetalMachineKeySet, __self__).__init__(
            'azure-native:networkcloud/v20230701:BareMetalMachineKeySet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BareMetalMachineKeySet':
        """
        Get an existing BareMetalMachineKeySet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BareMetalMachineKeySetArgs.__new__(BareMetalMachineKeySetArgs)

        __props__.__dict__["azure_group_id"] = None
        __props__.__dict__["detailed_status"] = None
        __props__.__dict__["detailed_status_message"] = None
        __props__.__dict__["expiration"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["jump_hosts_allowed"] = None
        __props__.__dict__["last_validation"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["os_group_name"] = None
        __props__.__dict__["privilege_level"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_list"] = None
        __props__.__dict__["user_list_status"] = None
        return BareMetalMachineKeySet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureGroupId")
    def azure_group_id(self) -> pulumi.Output[str]:
        """
        The object ID of Azure Active Directory group that all users in the list must be in for access to be granted. Users that are not in the group will not have access.
        """
        return pulumi.get(self, "azure_group_id")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[str]:
        """
        The more detailed status of the key set.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[str]:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter
    def expiration(self) -> pulumi.Output[str]:
        """
        The date and time after which the users in this key set will be removed from the bare metal machines.
        """
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="jumpHostsAllowed")
    def jump_hosts_allowed(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of IP addresses of jump hosts with management network access from which a login will be allowed for the users.
        """
        return pulumi.get(self, "jump_hosts_allowed")

    @property
    @pulumi.getter(name="lastValidation")
    def last_validation(self) -> pulumi.Output[str]:
        """
        The last time this key set was validated.
        """
        return pulumi.get(self, "last_validation")

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
    @pulumi.getter(name="osGroupName")
    def os_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the group that users will be assigned to on the operating system of the machines.
        """
        return pulumi.get(self, "os_group_name")

    @property
    @pulumi.getter(name="privilegeLevel")
    def privilege_level(self) -> pulumi.Output[str]:
        """
        The access level allowed for the users in this key set.
        """
        return pulumi.get(self, "privilege_level")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the bare metal machine key set.
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

    @property
    @pulumi.getter(name="userList")
    def user_list(self) -> pulumi.Output[Sequence['outputs.KeySetUserResponse']]:
        """
        The unique list of permitted users.
        """
        return pulumi.get(self, "user_list")

    @property
    @pulumi.getter(name="userListStatus")
    def user_list_status(self) -> pulumi.Output[Sequence['outputs.KeySetUserStatusResponse']]:
        """
        The status evaluation of each user.
        """
        return pulumi.get(self, "user_list_status")

