# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'StorageBillingPropertiesArgs',
    'StoragePropertiesArgs',
]

@pulumi.input_type
class StorageBillingPropertiesArgs:
    def __init__(__self__, *,
                 azure_bare_metal_storage_instance_size: Optional[pulumi.Input[str]] = None,
                 billing_mode: Optional[pulumi.Input[str]] = None):
        """
        Describes the billing related details of the AzureBareMetalStorageInstance.
        :param pulumi.Input[str] azure_bare_metal_storage_instance_size: the SKU type that is provisioned
        :param pulumi.Input[str] billing_mode: the billing mode for the storage instance
        """
        if azure_bare_metal_storage_instance_size is not None:
            pulumi.set(__self__, "azure_bare_metal_storage_instance_size", azure_bare_metal_storage_instance_size)
        if billing_mode is not None:
            pulumi.set(__self__, "billing_mode", billing_mode)

    @property
    @pulumi.getter(name="azureBareMetalStorageInstanceSize")
    def azure_bare_metal_storage_instance_size(self) -> Optional[pulumi.Input[str]]:
        """
        the SKU type that is provisioned
        """
        return pulumi.get(self, "azure_bare_metal_storage_instance_size")

    @azure_bare_metal_storage_instance_size.setter
    def azure_bare_metal_storage_instance_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_bare_metal_storage_instance_size", value)

    @property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[pulumi.Input[str]]:
        """
        the billing mode for the storage instance
        """
        return pulumi.get(self, "billing_mode")

    @billing_mode.setter
    def billing_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "billing_mode", value)


@pulumi.input_type
class StoragePropertiesArgs:
    def __init__(__self__, *,
                 generation: Optional[pulumi.Input[str]] = None,
                 hardware_type: Optional[pulumi.Input[str]] = None,
                 offering_type: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 storage_billing_properties: Optional[pulumi.Input['StorageBillingPropertiesArgs']] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 workload_type: Optional[pulumi.Input[str]] = None):
        """
        described the storage properties of the azure baremetalstorage instance
        :param pulumi.Input[str] generation: the kind of storage instance
        :param pulumi.Input[str] hardware_type: the hardware type of the storage instance
        :param pulumi.Input[str] offering_type: the offering type for which the resource is getting provisioned
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: State of provisioning of the AzureBareMetalStorageInstance
        :param pulumi.Input['StorageBillingPropertiesArgs'] storage_billing_properties: the billing related information for the resource
        :param pulumi.Input[str] storage_type: the storage protocol for which the resource is getting provisioned
        :param pulumi.Input[str] workload_type: the workload for which the resource is getting provisioned
        """
        if generation is not None:
            pulumi.set(__self__, "generation", generation)
        if hardware_type is not None:
            pulumi.set(__self__, "hardware_type", hardware_type)
        if offering_type is not None:
            pulumi.set(__self__, "offering_type", offering_type)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if storage_billing_properties is not None:
            pulumi.set(__self__, "storage_billing_properties", storage_billing_properties)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)
        if workload_type is not None:
            pulumi.set(__self__, "workload_type", workload_type)

    @property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[str]]:
        """
        the kind of storage instance
        """
        return pulumi.get(self, "generation")

    @generation.setter
    def generation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "generation", value)

    @property
    @pulumi.getter(name="hardwareType")
    def hardware_type(self) -> Optional[pulumi.Input[str]]:
        """
        the hardware type of the storage instance
        """
        return pulumi.get(self, "hardware_type")

    @hardware_type.setter
    def hardware_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hardware_type", value)

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> Optional[pulumi.Input[str]]:
        """
        the offering type for which the resource is getting provisioned
        """
        return pulumi.get(self, "offering_type")

    @offering_type.setter
    def offering_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "offering_type", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ProvisioningState']]]:
        """
        State of provisioning of the AzureBareMetalStorageInstance
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="storageBillingProperties")
    def storage_billing_properties(self) -> Optional[pulumi.Input['StorageBillingPropertiesArgs']]:
        """
        the billing related information for the resource
        """
        return pulumi.get(self, "storage_billing_properties")

    @storage_billing_properties.setter
    def storage_billing_properties(self, value: Optional[pulumi.Input['StorageBillingPropertiesArgs']]):
        pulumi.set(self, "storage_billing_properties", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        the storage protocol for which the resource is getting provisioned
        """
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)

    @property
    @pulumi.getter(name="workloadType")
    def workload_type(self) -> Optional[pulumi.Input[str]]:
        """
        the workload for which the resource is getting provisioned
        """
        return pulumi.get(self, "workload_type")

    @workload_type.setter
    def workload_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workload_type", value)


