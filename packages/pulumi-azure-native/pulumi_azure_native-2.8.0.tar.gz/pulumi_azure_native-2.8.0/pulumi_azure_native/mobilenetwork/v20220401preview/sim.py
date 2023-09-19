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

__all__ = ['SimArgs', 'Sim']

@pulumi.input_type
class SimArgs:
    def __init__(__self__, *,
                 international_mobile_subscriber_identity: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 sim_group_name: pulumi.Input[str],
                 authentication_key: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 device_type: Optional[pulumi.Input[str]] = None,
                 integrated_circuit_card_identifier: Optional[pulumi.Input[str]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 operator_key_code: Optional[pulumi.Input[str]] = None,
                 sim_name: Optional[pulumi.Input[str]] = None,
                 sim_policy: Optional[pulumi.Input['SimPolicyResourceIdArgs']] = None,
                 static_ip_configuration: Optional[pulumi.Input[Sequence[pulumi.Input['SimStaticIpPropertiesArgs']]]] = None):
        """
        The set of arguments for constructing a Sim resource.
        :param pulumi.Input[str] international_mobile_subscriber_identity: The international mobile subscriber identity (IMSI) for the SIM.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sim_group_name: The name of the SIM Group.
        :param pulumi.Input[str] authentication_key: The Ki value for the SIM.
        :param pulumi.Input[str] created_at: The timestamp of resource creation (UTC).
        :param pulumi.Input[str] created_by: The identity that created the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] created_by_type: The type of identity that created the resource.
        :param pulumi.Input[str] device_type: An optional free-form text field that can be used to record the device type this SIM is associated with, for example 'Video camera'. The Azure portal allows SIMs to be grouped and filtered based on this value.
        :param pulumi.Input[str] integrated_circuit_card_identifier: The integrated circuit card ID (ICCID) for the SIM.
        :param pulumi.Input[str] last_modified_at: The timestamp of resource last modification (UTC)
        :param pulumi.Input[str] last_modified_by: The identity that last modified the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] last_modified_by_type: The type of identity that last modified the resource.
        :param pulumi.Input[str] operator_key_code: The Opc value for the SIM.
        :param pulumi.Input[str] sim_name: The name of the SIM.
        :param pulumi.Input['SimPolicyResourceIdArgs'] sim_policy: The SIM policy used by this SIM.
        :param pulumi.Input[Sequence[pulumi.Input['SimStaticIpPropertiesArgs']]] static_ip_configuration: A list of static IP addresses assigned to this SIM. Each address is assigned at a defined network scope, made up of {attached data network, slice}.
        """
        pulumi.set(__self__, "international_mobile_subscriber_identity", international_mobile_subscriber_identity)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sim_group_name", sim_group_name)
        if authentication_key is not None:
            pulumi.set(__self__, "authentication_key", authentication_key)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if device_type is not None:
            pulumi.set(__self__, "device_type", device_type)
        if integrated_circuit_card_identifier is not None:
            pulumi.set(__self__, "integrated_circuit_card_identifier", integrated_circuit_card_identifier)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)
        if operator_key_code is not None:
            pulumi.set(__self__, "operator_key_code", operator_key_code)
        if sim_name is not None:
            pulumi.set(__self__, "sim_name", sim_name)
        if sim_policy is not None:
            pulumi.set(__self__, "sim_policy", sim_policy)
        if static_ip_configuration is not None:
            pulumi.set(__self__, "static_ip_configuration", static_ip_configuration)

    @property
    @pulumi.getter(name="internationalMobileSubscriberIdentity")
    def international_mobile_subscriber_identity(self) -> pulumi.Input[str]:
        """
        The international mobile subscriber identity (IMSI) for the SIM.
        """
        return pulumi.get(self, "international_mobile_subscriber_identity")

    @international_mobile_subscriber_identity.setter
    def international_mobile_subscriber_identity(self, value: pulumi.Input[str]):
        pulumi.set(self, "international_mobile_subscriber_identity", value)

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
    @pulumi.getter(name="simGroupName")
    def sim_group_name(self) -> pulumi.Input[str]:
        """
        The name of the SIM Group.
        """
        return pulumi.get(self, "sim_group_name")

    @sim_group_name.setter
    def sim_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sim_group_name", value)

    @property
    @pulumi.getter(name="authenticationKey")
    def authentication_key(self) -> Optional[pulumi.Input[str]]:
        """
        The Ki value for the SIM.
        """
        return pulumi.get(self, "authentication_key")

    @authentication_key.setter
    def authentication_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_key", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[pulumi.Input[Union[str, 'CreatedByType']]]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @created_by_type.setter
    def created_by_type(self, value: Optional[pulumi.Input[Union[str, 'CreatedByType']]]):
        pulumi.set(self, "created_by_type", value)

    @property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> Optional[pulumi.Input[str]]:
        """
        An optional free-form text field that can be used to record the device type this SIM is associated with, for example 'Video camera'. The Azure portal allows SIMs to be grouped and filtered based on this value.
        """
        return pulumi.get(self, "device_type")

    @device_type.setter
    def device_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_type", value)

    @property
    @pulumi.getter(name="integratedCircuitCardIdentifier")
    def integrated_circuit_card_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The integrated circuit card ID (ICCID) for the SIM.
        """
        return pulumi.get(self, "integrated_circuit_card_identifier")

    @integrated_circuit_card_identifier.setter
    def integrated_circuit_card_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integrated_circuit_card_identifier", value)

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @last_modified_at.setter
    def last_modified_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_at", value)

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[pulumi.Input[str]]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @last_modified_by.setter
    def last_modified_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_by", value)

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[pulumi.Input[Union[str, 'CreatedByType']]]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @last_modified_by_type.setter
    def last_modified_by_type(self, value: Optional[pulumi.Input[Union[str, 'CreatedByType']]]):
        pulumi.set(self, "last_modified_by_type", value)

    @property
    @pulumi.getter(name="operatorKeyCode")
    def operator_key_code(self) -> Optional[pulumi.Input[str]]:
        """
        The Opc value for the SIM.
        """
        return pulumi.get(self, "operator_key_code")

    @operator_key_code.setter
    def operator_key_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operator_key_code", value)

    @property
    @pulumi.getter(name="simName")
    def sim_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SIM.
        """
        return pulumi.get(self, "sim_name")

    @sim_name.setter
    def sim_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sim_name", value)

    @property
    @pulumi.getter(name="simPolicy")
    def sim_policy(self) -> Optional[pulumi.Input['SimPolicyResourceIdArgs']]:
        """
        The SIM policy used by this SIM.
        """
        return pulumi.get(self, "sim_policy")

    @sim_policy.setter
    def sim_policy(self, value: Optional[pulumi.Input['SimPolicyResourceIdArgs']]):
        pulumi.set(self, "sim_policy", value)

    @property
    @pulumi.getter(name="staticIpConfiguration")
    def static_ip_configuration(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SimStaticIpPropertiesArgs']]]]:
        """
        A list of static IP addresses assigned to this SIM. Each address is assigned at a defined network scope, made up of {attached data network, slice}.
        """
        return pulumi.get(self, "static_ip_configuration")

    @static_ip_configuration.setter
    def static_ip_configuration(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SimStaticIpPropertiesArgs']]]]):
        pulumi.set(self, "static_ip_configuration", value)


class Sim(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_key: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 device_type: Optional[pulumi.Input[str]] = None,
                 integrated_circuit_card_identifier: Optional[pulumi.Input[str]] = None,
                 international_mobile_subscriber_identity: Optional[pulumi.Input[str]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 operator_key_code: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sim_group_name: Optional[pulumi.Input[str]] = None,
                 sim_name: Optional[pulumi.Input[str]] = None,
                 sim_policy: Optional[pulumi.Input[pulumi.InputType['SimPolicyResourceIdArgs']]] = None,
                 static_ip_configuration: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SimStaticIpPropertiesArgs']]]]] = None,
                 __props__=None):
        """
        SIM resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_key: The Ki value for the SIM.
        :param pulumi.Input[str] created_at: The timestamp of resource creation (UTC).
        :param pulumi.Input[str] created_by: The identity that created the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] created_by_type: The type of identity that created the resource.
        :param pulumi.Input[str] device_type: An optional free-form text field that can be used to record the device type this SIM is associated with, for example 'Video camera'. The Azure portal allows SIMs to be grouped and filtered based on this value.
        :param pulumi.Input[str] integrated_circuit_card_identifier: The integrated circuit card ID (ICCID) for the SIM.
        :param pulumi.Input[str] international_mobile_subscriber_identity: The international mobile subscriber identity (IMSI) for the SIM.
        :param pulumi.Input[str] last_modified_at: The timestamp of resource last modification (UTC)
        :param pulumi.Input[str] last_modified_by: The identity that last modified the resource.
        :param pulumi.Input[Union[str, 'CreatedByType']] last_modified_by_type: The type of identity that last modified the resource.
        :param pulumi.Input[str] operator_key_code: The Opc value for the SIM.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sim_group_name: The name of the SIM Group.
        :param pulumi.Input[str] sim_name: The name of the SIM.
        :param pulumi.Input[pulumi.InputType['SimPolicyResourceIdArgs']] sim_policy: The SIM policy used by this SIM.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SimStaticIpPropertiesArgs']]]] static_ip_configuration: A list of static IP addresses assigned to this SIM. Each address is assigned at a defined network scope, made up of {attached data network, slice}.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SimArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        SIM resource.

        :param str resource_name: The name of the resource.
        :param SimArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SimArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_key: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 created_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 device_type: Optional[pulumi.Input[str]] = None,
                 integrated_circuit_card_identifier: Optional[pulumi.Input[str]] = None,
                 international_mobile_subscriber_identity: Optional[pulumi.Input[str]] = None,
                 last_modified_at: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 last_modified_by_type: Optional[pulumi.Input[Union[str, 'CreatedByType']]] = None,
                 operator_key_code: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sim_group_name: Optional[pulumi.Input[str]] = None,
                 sim_name: Optional[pulumi.Input[str]] = None,
                 sim_policy: Optional[pulumi.Input[pulumi.InputType['SimPolicyResourceIdArgs']]] = None,
                 static_ip_configuration: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SimStaticIpPropertiesArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SimArgs.__new__(SimArgs)

            __props__.__dict__["authentication_key"] = authentication_key
            __props__.__dict__["created_at"] = created_at
            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["created_by_type"] = created_by_type
            __props__.__dict__["device_type"] = device_type
            __props__.__dict__["integrated_circuit_card_identifier"] = integrated_circuit_card_identifier
            if international_mobile_subscriber_identity is None and not opts.urn:
                raise TypeError("Missing required property 'international_mobile_subscriber_identity'")
            __props__.__dict__["international_mobile_subscriber_identity"] = international_mobile_subscriber_identity
            __props__.__dict__["last_modified_at"] = last_modified_at
            __props__.__dict__["last_modified_by"] = last_modified_by
            __props__.__dict__["last_modified_by_type"] = last_modified_by_type
            __props__.__dict__["operator_key_code"] = operator_key_code
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sim_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'sim_group_name'")
            __props__.__dict__["sim_group_name"] = sim_group_name
            __props__.__dict__["sim_name"] = sim_name
            __props__.__dict__["sim_policy"] = sim_policy
            __props__.__dict__["static_ip_configuration"] = static_ip_configuration
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["sim_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:mobilenetwork:Sim"), pulumi.Alias(type_="azure-native:mobilenetwork/v20221101:Sim"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230601:Sim")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Sim, __self__).__init__(
            'azure-native:mobilenetwork/v20220401preview:Sim',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Sim':
        """
        Get an existing Sim resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SimArgs.__new__(SimArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["created_by_type"] = None
        __props__.__dict__["device_type"] = None
        __props__.__dict__["integrated_circuit_card_identifier"] = None
        __props__.__dict__["international_mobile_subscriber_identity"] = None
        __props__.__dict__["last_modified_at"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_by_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sim_policy"] = None
        __props__.__dict__["sim_state"] = None
        __props__.__dict__["static_ip_configuration"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Sim(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional[str]]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> pulumi.Output[Optional[str]]:
        """
        An optional free-form text field that can be used to record the device type this SIM is associated with, for example 'Video camera'. The Azure portal allows SIMs to be grouped and filtered based on this value.
        """
        return pulumi.get(self, "device_type")

    @property
    @pulumi.getter(name="integratedCircuitCardIdentifier")
    def integrated_circuit_card_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The integrated circuit card ID (ICCID) for the SIM.
        """
        return pulumi.get(self, "integrated_circuit_card_identifier")

    @property
    @pulumi.getter(name="internationalMobileSubscriberIdentity")
    def international_mobile_subscriber_identity(self) -> pulumi.Output[str]:
        """
        The international mobile subscriber identity (IMSI) for the SIM.
        """
        return pulumi.get(self, "international_mobile_subscriber_identity")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> pulumi.Output[Optional[str]]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional[str]]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

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
        The provisioning state of the SIM resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="simPolicy")
    def sim_policy(self) -> pulumi.Output[Optional['outputs.SimPolicyResourceIdResponse']]:
        """
        The SIM policy used by this SIM.
        """
        return pulumi.get(self, "sim_policy")

    @property
    @pulumi.getter(name="simState")
    def sim_state(self) -> pulumi.Output[str]:
        """
        The state of the SIM resource.
        """
        return pulumi.get(self, "sim_state")

    @property
    @pulumi.getter(name="staticIpConfiguration")
    def static_ip_configuration(self) -> pulumi.Output[Optional[Sequence['outputs.SimStaticIpPropertiesResponse']]]:
        """
        A list of static IP addresses assigned to this SIM. Each address is assigned at a defined network scope, made up of {attached data network, slice}.
        """
        return pulumi.get(self, "static_ip_configuration")

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

