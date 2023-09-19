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

__all__ = [
    'GetVendorSkuPreviewResult',
    'AwaitableGetVendorSkuPreviewResult',
    'get_vendor_sku_preview',
    'get_vendor_sku_preview_output',
]

@pulumi.output_type
class GetVendorSkuPreviewResult:
    """
    Customer subscription which can use a sku.
    """
    def __init__(__self__, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
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

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The preview subscription ID.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the PreviewSubscription resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetVendorSkuPreviewResult(GetVendorSkuPreviewResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVendorSkuPreviewResult(
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_vendor_sku_preview(preview_subscription: Optional[str] = None,
                           sku_name: Optional[str] = None,
                           vendor_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVendorSkuPreviewResult:
    """
    Gets the preview information of a vendor sku.


    :param str preview_subscription: Preview subscription ID.
    :param str sku_name: The name of the vendor sku.
    :param str vendor_name: The name of the vendor.
    """
    __args__ = dict()
    __args__['previewSubscription'] = preview_subscription
    __args__['skuName'] = sku_name
    __args__['vendorName'] = vendor_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridnetwork/v20220101preview:getVendorSkuPreview', __args__, opts=opts, typ=GetVendorSkuPreviewResult).value

    return AwaitableGetVendorSkuPreviewResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_vendor_sku_preview)
def get_vendor_sku_preview_output(preview_subscription: Optional[pulumi.Input[str]] = None,
                                  sku_name: Optional[pulumi.Input[str]] = None,
                                  vendor_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVendorSkuPreviewResult]:
    """
    Gets the preview information of a vendor sku.


    :param str preview_subscription: Preview subscription ID.
    :param str sku_name: The name of the vendor sku.
    :param str vendor_name: The name of the vendor.
    """
    ...
