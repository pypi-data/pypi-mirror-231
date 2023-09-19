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

__all__ = ['DisasterRecoveryConfigArgs', 'DisasterRecoveryConfig']

@pulumi.input_type
class DisasterRecoveryConfigArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 alias: Optional[pulumi.Input[str]] = None,
                 alternate_name: Optional[pulumi.Input[str]] = None,
                 partner_namespace: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DisasterRecoveryConfig resource.
        :param pulumi.Input[str] namespace_name: The Namespace name
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the azure subscription.
        :param pulumi.Input[str] alias: The Disaster Recovery configuration name
        :param pulumi.Input[str] alternate_name: Alternate name specified when alias and namespace names are same.
        :param pulumi.Input[str] partner_namespace: ARM Id of the Primary/Secondary eventhub namespace name, which is part of GEO DR pairing
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if alias is not None:
            pulumi.set(__self__, "alias", alias)
        if alternate_name is not None:
            pulumi.set(__self__, "alternate_name", alternate_name)
        if partner_namespace is not None:
            pulumi.set(__self__, "partner_namespace", partner_namespace)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The Namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group within the azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[str]]:
        """
        The Disaster Recovery configuration name
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> Optional[pulumi.Input[str]]:
        """
        Alternate name specified when alias and namespace names are same.
        """
        return pulumi.get(self, "alternate_name")

    @alternate_name.setter
    def alternate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alternate_name", value)

    @property
    @pulumi.getter(name="partnerNamespace")
    def partner_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        ARM Id of the Primary/Secondary eventhub namespace name, which is part of GEO DR pairing
        """
        return pulumi.get(self, "partner_namespace")

    @partner_namespace.setter
    def partner_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_namespace", value)


class DisasterRecoveryConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 alternate_name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 partner_namespace: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Single item in List or Get Alias(Disaster Recovery configuration) operation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The Disaster Recovery configuration name
        :param pulumi.Input[str] alternate_name: Alternate name specified when alias and namespace names are same.
        :param pulumi.Input[str] namespace_name: The Namespace name
        :param pulumi.Input[str] partner_namespace: ARM Id of the Primary/Secondary eventhub namespace name, which is part of GEO DR pairing
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the azure subscription.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DisasterRecoveryConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Single item in List or Get Alias(Disaster Recovery configuration) operation

        :param str resource_name: The name of the resource.
        :param DisasterRecoveryConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DisasterRecoveryConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 alternate_name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 partner_namespace: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DisasterRecoveryConfigArgs.__new__(DisasterRecoveryConfigArgs)

            __props__.__dict__["alias"] = alias
            __props__.__dict__["alternate_name"] = alternate_name
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["partner_namespace"] = partner_namespace
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["pending_replication_operations_count"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["role"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventhub:DisasterRecoveryConfig"), pulumi.Alias(type_="azure-native:eventhub/v20170401:DisasterRecoveryConfig"), pulumi.Alias(type_="azure-native:eventhub/v20180101preview:DisasterRecoveryConfig"), pulumi.Alias(type_="azure-native:eventhub/v20210101preview:DisasterRecoveryConfig"), pulumi.Alias(type_="azure-native:eventhub/v20210601preview:DisasterRecoveryConfig"), pulumi.Alias(type_="azure-native:eventhub/v20211101:DisasterRecoveryConfig"), pulumi.Alias(type_="azure-native:eventhub/v20220101preview:DisasterRecoveryConfig"), pulumi.Alias(type_="azure-native:eventhub/v20221001preview:DisasterRecoveryConfig")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DisasterRecoveryConfig, __self__).__init__(
            'azure-native:eventhub/v20230101preview:DisasterRecoveryConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DisasterRecoveryConfig':
        """
        Get an existing DisasterRecoveryConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DisasterRecoveryConfigArgs.__new__(DisasterRecoveryConfigArgs)

        __props__.__dict__["alternate_name"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partner_namespace"] = None
        __props__.__dict__["pending_replication_operations_count"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["role"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return DisasterRecoveryConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> pulumi.Output[Optional[str]]:
        """
        Alternate name specified when alias and namespace names are same.
        """
        return pulumi.get(self, "alternate_name")

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
    @pulumi.getter(name="partnerNamespace")
    def partner_namespace(self) -> pulumi.Output[Optional[str]]:
        """
        ARM Id of the Primary/Secondary eventhub namespace name, which is part of GEO DR pairing
        """
        return pulumi.get(self, "partner_namespace")

    @property
    @pulumi.getter(name="pendingReplicationOperationsCount")
    def pending_replication_operations_count(self) -> pulumi.Output[float]:
        """
        Number of entities pending to be replicated.
        """
        return pulumi.get(self, "pending_replication_operations_count")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the Alias(Disaster Recovery configuration) - possible values 'Accepted' or 'Succeeded' or 'Failed'
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        role of namespace in GEO DR - possible values 'Primary' or 'PrimaryNotReplicating' or 'Secondary'
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs"
        """
        return pulumi.get(self, "type")

