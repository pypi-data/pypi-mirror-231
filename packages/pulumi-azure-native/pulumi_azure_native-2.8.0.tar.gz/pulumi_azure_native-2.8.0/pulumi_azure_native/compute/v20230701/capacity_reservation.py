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

__all__ = ['CapacityReservationArgs', 'CapacityReservation']

@pulumi.input_type
class CapacityReservationArgs:
    def __init__(__self__, *,
                 capacity_reservation_group_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['SkuArgs'],
                 capacity_reservation_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CapacityReservation resource.
        :param pulumi.Input[str] capacity_reservation_group_name: The name of the capacity reservation group.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['SkuArgs'] sku: SKU of the resource for which capacity needs be reserved. The SKU name and capacity is required to be set. Currently VM Skus with the capability called 'CapacityReservationSupported' set to true are supported. Refer to List Microsoft.Compute SKUs in a region (https://docs.microsoft.com/rest/api/compute/resourceskus/list) for supported values.
        :param pulumi.Input[str] capacity_reservation_name: The name of the capacity reservation.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: Availability Zone to use for this capacity reservation. The zone has to be single value and also should be part for the list of zones specified during the capacity reservation group creation. The zone can be assigned only during creation. If not provided, the reservation supports only non-zonal deployments. If provided, enforces VM/VMSS using this capacity reservation to be in same zone.
        """
        pulumi.set(__self__, "capacity_reservation_group_name", capacity_reservation_group_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if capacity_reservation_name is not None:
            pulumi.set(__self__, "capacity_reservation_name", capacity_reservation_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="capacityReservationGroupName")
    def capacity_reservation_group_name(self) -> pulumi.Input[str]:
        """
        The name of the capacity reservation group.
        """
        return pulumi.get(self, "capacity_reservation_group_name")

    @capacity_reservation_group_name.setter
    def capacity_reservation_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "capacity_reservation_group_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        SKU of the resource for which capacity needs be reserved. The SKU name and capacity is required to be set. Currently VM Skus with the capability called 'CapacityReservationSupported' set to true are supported. Refer to List Microsoft.Compute SKUs in a region (https://docs.microsoft.com/rest/api/compute/resourceskus/list) for supported values.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="capacityReservationName")
    def capacity_reservation_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the capacity reservation.
        """
        return pulumi.get(self, "capacity_reservation_name")

    @capacity_reservation_name.setter
    def capacity_reservation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity_reservation_name", value)

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
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Availability Zone to use for this capacity reservation. The zone has to be single value and also should be part for the list of zones specified during the capacity reservation group creation. The zone can be assigned only during creation. If not provided, the reservation supports only non-zonal deployments. If provided, enforces VM/VMSS using this capacity reservation to be in same zone.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


class CapacityReservation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_reservation_group_name: Optional[pulumi.Input[str]] = None,
                 capacity_reservation_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Specifies information about the capacity reservation.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] capacity_reservation_group_name: The name of the capacity reservation group.
        :param pulumi.Input[str] capacity_reservation_name: The name of the capacity reservation.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: SKU of the resource for which capacity needs be reserved. The SKU name and capacity is required to be set. Currently VM Skus with the capability called 'CapacityReservationSupported' set to true are supported. Refer to List Microsoft.Compute SKUs in a region (https://docs.microsoft.com/rest/api/compute/resourceskus/list) for supported values.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: Availability Zone to use for this capacity reservation. The zone has to be single value and also should be part for the list of zones specified during the capacity reservation group creation. The zone can be assigned only during creation. If not provided, the reservation supports only non-zonal deployments. If provided, enforces VM/VMSS using this capacity reservation to be in same zone.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CapacityReservationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Specifies information about the capacity reservation.

        :param str resource_name: The name of the resource.
        :param CapacityReservationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CapacityReservationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_reservation_group_name: Optional[pulumi.Input[str]] = None,
                 capacity_reservation_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CapacityReservationArgs.__new__(CapacityReservationArgs)

            if capacity_reservation_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'capacity_reservation_group_name'")
            __props__.__dict__["capacity_reservation_group_name"] = capacity_reservation_group_name
            __props__.__dict__["capacity_reservation_name"] = capacity_reservation_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zones"] = zones
            __props__.__dict__["instance_view"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["platform_fault_domain_count"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["provisioning_time"] = None
            __props__.__dict__["reservation_id"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["virtual_machines_associated"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:compute:CapacityReservation"), pulumi.Alias(type_="azure-native:compute/v20210401:CapacityReservation"), pulumi.Alias(type_="azure-native:compute/v20210701:CapacityReservation"), pulumi.Alias(type_="azure-native:compute/v20211101:CapacityReservation"), pulumi.Alias(type_="azure-native:compute/v20220301:CapacityReservation"), pulumi.Alias(type_="azure-native:compute/v20220801:CapacityReservation"), pulumi.Alias(type_="azure-native:compute/v20221101:CapacityReservation"), pulumi.Alias(type_="azure-native:compute/v20230301:CapacityReservation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CapacityReservation, __self__).__init__(
            'azure-native:compute/v20230701:CapacityReservation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CapacityReservation':
        """
        Get an existing CapacityReservation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CapacityReservationArgs.__new__(CapacityReservationArgs)

        __props__.__dict__["instance_view"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["platform_fault_domain_count"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["provisioning_time"] = None
        __props__.__dict__["reservation_id"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["time_created"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_machines_associated"] = None
        __props__.__dict__["zones"] = None
        return CapacityReservation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> pulumi.Output['outputs.CapacityReservationInstanceViewResponse']:
        """
        The Capacity reservation instance view.
        """
        return pulumi.get(self, "instance_view")

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
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> pulumi.Output[int]:
        """
        Specifies the value of fault domain count that Capacity Reservation supports for requested VM size. **Note:** The fault domain count specified for a resource (like virtual machines scale set) must be less than or equal to this value if it deploys using capacity reservation. Minimum api-version: 2022-08-01.
        """
        return pulumi.get(self, "platform_fault_domain_count")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="provisioningTime")
    def provisioning_time(self) -> pulumi.Output[str]:
        """
        The date time when the capacity reservation was last updated.
        """
        return pulumi.get(self, "provisioning_time")

    @property
    @pulumi.getter(name="reservationId")
    def reservation_id(self) -> pulumi.Output[str]:
        """
        A unique id generated and assigned to the capacity reservation by the platform which does not change throughout the lifetime of the resource.
        """
        return pulumi.get(self, "reservation_id")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        SKU of the resource for which capacity needs be reserved. The SKU name and capacity is required to be set. Currently VM Skus with the capability called 'CapacityReservationSupported' set to true are supported. Refer to List Microsoft.Compute SKUs in a region (https://docs.microsoft.com/rest/api/compute/resourceskus/list) for supported values.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        Specifies the time at which the Capacity Reservation resource was created. Minimum api-version: 2021-11-01.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachinesAssociated")
    def virtual_machines_associated(self) -> pulumi.Output[Sequence['outputs.SubResourceReadOnlyResponse']]:
        """
        A list of all virtual machine resource ids that are associated with the capacity reservation.
        """
        return pulumi.get(self, "virtual_machines_associated")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Availability Zone to use for this capacity reservation. The zone has to be single value and also should be part for the list of zones specified during the capacity reservation group creation. The zone can be assigned only during creation. If not provided, the reservation supports only non-zonal deployments. If provided, enforces VM/VMSS using this capacity reservation to be in same zone.
        """
        return pulumi.get(self, "zones")

