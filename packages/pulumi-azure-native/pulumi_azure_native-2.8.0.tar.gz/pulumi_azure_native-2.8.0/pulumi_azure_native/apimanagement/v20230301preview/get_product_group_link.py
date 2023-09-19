# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetProductGroupLinkResult',
    'AwaitableGetProductGroupLinkResult',
    'get_product_group_link',
    'get_product_group_link_output',
]

@pulumi.output_type
class GetProductGroupLinkResult:
    """
    Product-group link details.
    """
    def __init__(__self__, group_id=None, id=None, name=None, type=None):
        if group_id and not isinstance(group_id, str):
            raise TypeError("Expected argument 'group_id' to be a str")
        pulumi.set(__self__, "group_id", group_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> str:
        """
        Full resource Id of a group.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetProductGroupLinkResult(GetProductGroupLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProductGroupLinkResult(
            group_id=self.group_id,
            id=self.id,
            name=self.name,
            type=self.type)


def get_product_group_link(group_link_id: Optional[str] = None,
                           product_id: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           service_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProductGroupLinkResult:
    """
    Gets the group link for the product.


    :param str group_link_id: Product-Group link identifier. Must be unique in the current API Management service instance.
    :param str product_id: Product identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['groupLinkId'] = group_link_id
    __args__['productId'] = product_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230301preview:getProductGroupLink', __args__, opts=opts, typ=GetProductGroupLinkResult).value

    return AwaitableGetProductGroupLinkResult(
        group_id=pulumi.get(__ret__, 'group_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_product_group_link)
def get_product_group_link_output(group_link_id: Optional[pulumi.Input[str]] = None,
                                  product_id: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  service_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProductGroupLinkResult]:
    """
    Gets the group link for the product.


    :param str group_link_id: Product-Group link identifier. Must be unique in the current API Management service instance.
    :param str product_id: Product identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
