# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = ['VolumeQuotaRuleArgs', 'VolumeQuotaRule']

@pulumi.input_type
class VolumeQuotaRuleArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 pool_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 volume_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 quota_size_in_ki_bs: Optional[pulumi.Input[float]] = None,
                 quota_target: Optional[pulumi.Input[str]] = None,
                 quota_type: Optional[pulumi.Input[Union[str, 'Type']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 volume_quota_rule_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VolumeQuotaRule resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[str] pool_name: The name of the capacity pool
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] volume_name: The name of the volume
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[float] quota_size_in_ki_bs: Size of quota
        :param pulumi.Input[str] quota_target: UserID/GroupID/SID based on the quota target type. UserID and groupID can be found by running ‘id’ or ‘getent’ command for the user or group and SID can be found by running <wmic useraccount where name='user-name' get sid>
        :param pulumi.Input[Union[str, 'Type']] quota_type: Type of quota
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] volume_quota_rule_name: The name of volume quota rule
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "pool_name", pool_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "volume_name", volume_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if quota_size_in_ki_bs is not None:
            pulumi.set(__self__, "quota_size_in_ki_bs", quota_size_in_ki_bs)
        if quota_target is not None:
            pulumi.set(__self__, "quota_target", quota_target)
        if quota_type is not None:
            pulumi.set(__self__, "quota_type", quota_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if volume_quota_rule_name is not None:
            pulumi.set(__self__, "volume_quota_rule_name", volume_quota_rule_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the NetApp account
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Input[str]:
        """
        The name of the capacity pool
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool_name", value)

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
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Input[str]:
        """
        The name of the volume
        """
        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "volume_name", value)

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
    @pulumi.getter(name="quotaSizeInKiBs")
    def quota_size_in_ki_bs(self) -> Optional[pulumi.Input[float]]:
        """
        Size of quota
        """
        return pulumi.get(self, "quota_size_in_ki_bs")

    @quota_size_in_ki_bs.setter
    def quota_size_in_ki_bs(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "quota_size_in_ki_bs", value)

    @property
    @pulumi.getter(name="quotaTarget")
    def quota_target(self) -> Optional[pulumi.Input[str]]:
        """
        UserID/GroupID/SID based on the quota target type. UserID and groupID can be found by running ‘id’ or ‘getent’ command for the user or group and SID can be found by running <wmic useraccount where name='user-name' get sid>
        """
        return pulumi.get(self, "quota_target")

    @quota_target.setter
    def quota_target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "quota_target", value)

    @property
    @pulumi.getter(name="quotaType")
    def quota_type(self) -> Optional[pulumi.Input[Union[str, 'Type']]]:
        """
        Type of quota
        """
        return pulumi.get(self, "quota_type")

    @quota_type.setter
    def quota_type(self, value: Optional[pulumi.Input[Union[str, 'Type']]]):
        pulumi.set(self, "quota_type", value)

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
    @pulumi.getter(name="volumeQuotaRuleName")
    def volume_quota_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of volume quota rule
        """
        return pulumi.get(self, "volume_quota_rule_name")

    @volume_quota_rule_name.setter
    def volume_quota_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_quota_rule_name", value)


class VolumeQuotaRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 quota_size_in_ki_bs: Optional[pulumi.Input[float]] = None,
                 quota_target: Optional[pulumi.Input[str]] = None,
                 quota_type: Optional[pulumi.Input[Union[str, 'Type']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 volume_quota_rule_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Quota Rule of a Volume
        Azure REST API version: 2022-11-01. Prior API version in Azure Native 1.x: 2022-01-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] pool_name: The name of the capacity pool
        :param pulumi.Input[float] quota_size_in_ki_bs: Size of quota
        :param pulumi.Input[str] quota_target: UserID/GroupID/SID based on the quota target type. UserID and groupID can be found by running ‘id’ or ‘getent’ command for the user or group and SID can be found by running <wmic useraccount where name='user-name' get sid>
        :param pulumi.Input[Union[str, 'Type']] quota_type: Type of quota
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] volume_name: The name of the volume
        :param pulumi.Input[str] volume_quota_rule_name: The name of volume quota rule
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeQuotaRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Quota Rule of a Volume
        Azure REST API version: 2022-11-01. Prior API version in Azure Native 1.x: 2022-01-01

        :param str resource_name: The name of the resource.
        :param VolumeQuotaRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeQuotaRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 quota_size_in_ki_bs: Optional[pulumi.Input[float]] = None,
                 quota_target: Optional[pulumi.Input[str]] = None,
                 quota_type: Optional[pulumi.Input[Union[str, 'Type']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 volume_quota_rule_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeQuotaRuleArgs.__new__(VolumeQuotaRuleArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["location"] = location
            if pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'pool_name'")
            __props__.__dict__["pool_name"] = pool_name
            __props__.__dict__["quota_size_in_ki_bs"] = quota_size_in_ki_bs
            __props__.__dict__["quota_target"] = quota_target
            __props__.__dict__["quota_type"] = quota_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if volume_name is None and not opts.urn:
                raise TypeError("Missing required property 'volume_name'")
            __props__.__dict__["volume_name"] = volume_name
            __props__.__dict__["volume_quota_rule_name"] = volume_quota_rule_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:netapp/v20220101:VolumeQuotaRule"), pulumi.Alias(type_="azure-native:netapp/v20220301:VolumeQuotaRule"), pulumi.Alias(type_="azure-native:netapp/v20220501:VolumeQuotaRule"), pulumi.Alias(type_="azure-native:netapp/v20220901:VolumeQuotaRule"), pulumi.Alias(type_="azure-native:netapp/v20221101:VolumeQuotaRule"), pulumi.Alias(type_="azure-native:netapp/v20221101preview:VolumeQuotaRule"), pulumi.Alias(type_="azure-native:netapp/v20230501:VolumeQuotaRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VolumeQuotaRule, __self__).__init__(
            'azure-native:netapp:VolumeQuotaRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VolumeQuotaRule':
        """
        Get an existing VolumeQuotaRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VolumeQuotaRuleArgs.__new__(VolumeQuotaRuleArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["quota_size_in_ki_bs"] = None
        __props__.__dict__["quota_target"] = None
        __props__.__dict__["quota_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return VolumeQuotaRule(resource_name, opts=opts, __props__=__props__)

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
        Gets the status of the VolumeQuotaRule at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="quotaSizeInKiBs")
    def quota_size_in_ki_bs(self) -> pulumi.Output[Optional[float]]:
        """
        Size of quota
        """
        return pulumi.get(self, "quota_size_in_ki_bs")

    @property
    @pulumi.getter(name="quotaTarget")
    def quota_target(self) -> pulumi.Output[Optional[str]]:
        """
        UserID/GroupID/SID based on the quota target type. UserID and groupID can be found by running ‘id’ or ‘getent’ command for the user or group and SID can be found by running <wmic useraccount where name='user-name' get sid>
        """
        return pulumi.get(self, "quota_target")

    @property
    @pulumi.getter(name="quotaType")
    def quota_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of quota
        """
        return pulumi.get(self, "quota_type")

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

