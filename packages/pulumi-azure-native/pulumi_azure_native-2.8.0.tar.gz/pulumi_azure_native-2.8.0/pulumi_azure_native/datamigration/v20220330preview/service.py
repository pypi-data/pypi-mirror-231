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

__all__ = ['ServiceArgs', 'Service']

@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *,
                 group_name: pulumi.Input[str],
                 auto_stop_delay: Optional[pulumi.Input[str]] = None,
                 delete_resources_on_stop: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['ServiceSkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_nic_id: Optional[pulumi.Input[str]] = None,
                 virtual_subnet_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Service resource.
        :param pulumi.Input[str] group_name: Name of the resource group
        :param pulumi.Input[str] auto_stop_delay: The time delay before the service is auto-stopped when idle.
        :param pulumi.Input[bool] delete_resources_on_stop: Whether service resources should be deleted when stopped. (Turned on by default)
        :param pulumi.Input[str] kind: The resource kind. Only 'vm' (the default) is supported.
        :param pulumi.Input[str] public_key: The public key of the service, used to encrypt secrets sent to the service
        :param pulumi.Input[str] service_name: Name of the service
        :param pulumi.Input['ServiceSkuArgs'] sku: Service SKU
        :param pulumi.Input[str] virtual_nic_id: The ID of the Microsoft.Network/networkInterfaces resource which the service have
        :param pulumi.Input[str] virtual_subnet_id: The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined
        """
        pulumi.set(__self__, "group_name", group_name)
        if auto_stop_delay is not None:
            pulumi.set(__self__, "auto_stop_delay", auto_stop_delay)
        if delete_resources_on_stop is not None:
            pulumi.set(__self__, "delete_resources_on_stop", delete_resources_on_stop)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if public_key is not None:
            pulumi.set(__self__, "public_key", public_key)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_nic_id is not None:
            pulumi.set(__self__, "virtual_nic_id", virtual_nic_id)
        if virtual_subnet_id is not None:
            pulumi.set(__self__, "virtual_subnet_id", virtual_subnet_id)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="autoStopDelay")
    def auto_stop_delay(self) -> Optional[pulumi.Input[str]]:
        """
        The time delay before the service is auto-stopped when idle.
        """
        return pulumi.get(self, "auto_stop_delay")

    @auto_stop_delay.setter
    def auto_stop_delay(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_stop_delay", value)

    @property
    @pulumi.getter(name="deleteResourcesOnStop")
    def delete_resources_on_stop(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether service resources should be deleted when stopped. (Turned on by default)
        """
        return pulumi.get(self, "delete_resources_on_stop")

    @delete_resources_on_stop.setter
    def delete_resources_on_stop(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_resources_on_stop", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The resource kind. Only 'vm' (the default) is supported.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        The public key of the service, used to encrypt secrets sent to the service
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the service
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['ServiceSkuArgs']]:
        """
        Service SKU
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['ServiceSkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="virtualNicId")
    def virtual_nic_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Microsoft.Network/networkInterfaces resource which the service have
        """
        return pulumi.get(self, "virtual_nic_id")

    @virtual_nic_id.setter
    def virtual_nic_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_nic_id", value)

    @property
    @pulumi.getter(name="virtualSubnetId")
    def virtual_subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined
        """
        return pulumi.get(self, "virtual_subnet_id")

    @virtual_subnet_id.setter
    def virtual_subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_subnet_id", value)


class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_stop_delay: Optional[pulumi.Input[str]] = None,
                 delete_resources_on_stop: Optional[pulumi.Input[bool]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ServiceSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_nic_id: Optional[pulumi.Input[str]] = None,
                 virtual_subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure Database Migration Service (classic) resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_stop_delay: The time delay before the service is auto-stopped when idle.
        :param pulumi.Input[bool] delete_resources_on_stop: Whether service resources should be deleted when stopped. (Turned on by default)
        :param pulumi.Input[str] group_name: Name of the resource group
        :param pulumi.Input[str] kind: The resource kind. Only 'vm' (the default) is supported.
        :param pulumi.Input[str] public_key: The public key of the service, used to encrypt secrets sent to the service
        :param pulumi.Input[str] service_name: Name of the service
        :param pulumi.Input[pulumi.InputType['ServiceSkuArgs']] sku: Service SKU
        :param pulumi.Input[str] virtual_nic_id: The ID of the Microsoft.Network/networkInterfaces resource which the service have
        :param pulumi.Input[str] virtual_subnet_id: The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure Database Migration Service (classic) resource

        :param str resource_name: The name of the resource.
        :param ServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_stop_delay: Optional[pulumi.Input[str]] = None,
                 delete_resources_on_stop: Optional[pulumi.Input[bool]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ServiceSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_nic_id: Optional[pulumi.Input[str]] = None,
                 virtual_subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceArgs.__new__(ServiceArgs)

            __props__.__dict__["auto_stop_delay"] = auto_stop_delay
            __props__.__dict__["delete_resources_on_stop"] = delete_resources_on_stop
            if group_name is None and not opts.urn:
                raise TypeError("Missing required property 'group_name'")
            __props__.__dict__["group_name"] = group_name
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["public_key"] = public_key
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_nic_id"] = virtual_nic_id
            __props__.__dict__["virtual_subnet_id"] = virtual_subnet_id
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datamigration:Service"), pulumi.Alias(type_="azure-native:datamigration/v20171115preview:Service"), pulumi.Alias(type_="azure-native:datamigration/v20180315preview:Service"), pulumi.Alias(type_="azure-native:datamigration/v20180331preview:Service"), pulumi.Alias(type_="azure-native:datamigration/v20180419:Service"), pulumi.Alias(type_="azure-native:datamigration/v20180715preview:Service"), pulumi.Alias(type_="azure-native:datamigration/v20210630:Service"), pulumi.Alias(type_="azure-native:datamigration/v20211030preview:Service"), pulumi.Alias(type_="azure-native:datamigration/v20220130preview:Service")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Service, __self__).__init__(
            'azure-native:datamigration/v20220330preview:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceArgs.__new__(ServiceArgs)

        __props__.__dict__["auto_stop_delay"] = None
        __props__.__dict__["delete_resources_on_stop"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_key"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_nic_id"] = None
        __props__.__dict__["virtual_subnet_id"] = None
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoStopDelay")
    def auto_stop_delay(self) -> pulumi.Output[Optional[str]]:
        """
        The time delay before the service is auto-stopped when idle.
        """
        return pulumi.get(self, "auto_stop_delay")

    @property
    @pulumi.getter(name="deleteResourcesOnStop")
    def delete_resources_on_stop(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether service resources should be deleted when stopped. (Turned on by default)
        """
        return pulumi.get(self, "delete_resources_on_stop")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        HTTP strong entity tag value. Ignored if submitted
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The resource kind. Only 'vm' (the default) is supported.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The resource's provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[Optional[str]]:
        """
        The public key of the service, used to encrypt secrets sent to the service
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.ServiceSkuResponse']]:
        """
        Service SKU
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNicId")
    def virtual_nic_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the Microsoft.Network/networkInterfaces resource which the service have
        """
        return pulumi.get(self, "virtual_nic_id")

    @property
    @pulumi.getter(name="virtualSubnetId")
    def virtual_subnet_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined
        """
        return pulumi.get(self, "virtual_subnet_id")

