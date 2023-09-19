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

__all__ = [
    'GetInventoryItemResult',
    'AwaitableGetInventoryItemResult',
    'get_inventory_item',
    'get_inventory_item_output',
]

@pulumi.output_type
class GetInventoryItemResult:
    """
    Defines the inventory item.
    """
    def __init__(__self__, id=None, inventory_item_name=None, inventory_type=None, kind=None, managed_resource_id=None, name=None, provisioning_state=None, system_data=None, type=None, uuid=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inventory_item_name and not isinstance(inventory_item_name, str):
            raise TypeError("Expected argument 'inventory_item_name' to be a str")
        pulumi.set(__self__, "inventory_item_name", inventory_item_name)
        if inventory_type and not isinstance(inventory_type, str):
            raise TypeError("Expected argument 'inventory_type' to be a str")
        pulumi.set(__self__, "inventory_type", inventory_type)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if managed_resource_id and not isinstance(managed_resource_id, str):
            raise TypeError("Expected argument 'managed_resource_id' to be a str")
        pulumi.set(__self__, "managed_resource_id", managed_resource_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inventoryItemName")
    def inventory_item_name(self) -> str:
        """
        Gets the Managed Object name in VMM for the inventory item.
        """
        return pulumi.get(self, "inventory_item_name")

    @property
    @pulumi.getter(name="inventoryType")
    def inventory_type(self) -> str:
        """
        They inventory type.
        """
        return pulumi.get(self, "inventory_type")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="managedResourceId")
    def managed_resource_id(self) -> str:
        """
        Gets the tracked resource id corresponding to the inventory resource.
        """
        return pulumi.get(self, "managed_resource_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        Gets the UUID (which is assigned by VMM) for the inventory item.
        """
        return pulumi.get(self, "uuid")


class AwaitableGetInventoryItemResult(GetInventoryItemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInventoryItemResult(
            id=self.id,
            inventory_item_name=self.inventory_item_name,
            inventory_type=self.inventory_type,
            kind=self.kind,
            managed_resource_id=self.managed_resource_id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type,
            uuid=self.uuid)


def get_inventory_item(inventory_item_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       vmm_server_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInventoryItemResult:
    """
    Shows an inventory item.
    Azure REST API version: 2022-05-21-preview.


    :param str inventory_item_name: Name of the inventoryItem.
    :param str resource_group_name: The name of the resource group.
    :param str vmm_server_name: Name of the VMMServer.
    """
    __args__ = dict()
    __args__['inventoryItemName'] = inventory_item_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['vmmServerName'] = vmm_server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:scvmm:getInventoryItem', __args__, opts=opts, typ=GetInventoryItemResult).value

    return AwaitableGetInventoryItemResult(
        id=pulumi.get(__ret__, 'id'),
        inventory_item_name=pulumi.get(__ret__, 'inventory_item_name'),
        inventory_type=pulumi.get(__ret__, 'inventory_type'),
        kind=pulumi.get(__ret__, 'kind'),
        managed_resource_id=pulumi.get(__ret__, 'managed_resource_id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        uuid=pulumi.get(__ret__, 'uuid'))


@_utilities.lift_output_func(get_inventory_item)
def get_inventory_item_output(inventory_item_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              vmm_server_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInventoryItemResult]:
    """
    Shows an inventory item.
    Azure REST API version: 2022-05-21-preview.


    :param str inventory_item_name: Name of the inventoryItem.
    :param str resource_group_name: The name of the resource group.
    :param str vmm_server_name: Name of the VMMServer.
    """
    ...
