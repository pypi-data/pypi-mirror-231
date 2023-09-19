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
    'GetMarketplaceImageSasTokenSASTokenResult',
    'AwaitableGetMarketplaceImageSasTokenSASTokenResult',
    'get_marketplace_image_sas_token_sas_token',
    'get_marketplace_image_sas_token_sas_token_output',
]

@pulumi.output_type
class GetMarketplaceImageSasTokenSASTokenResult:
    def __init__(__self__, sas_uri=None, status=None):
        if sas_uri and not isinstance(sas_uri, str):
            raise TypeError("Expected argument 'sas_uri' to be a str")
        pulumi.set(__self__, "sas_uri", sas_uri)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="sasUri")
    def sas_uri(self) -> Optional[str]:
        return pulumi.get(self, "sas_uri")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetMarketplaceImageSasTokenSASTokenResult(GetMarketplaceImageSasTokenSASTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMarketplaceImageSasTokenSASTokenResult(
            sas_uri=self.sas_uri,
            status=self.status)


def get_marketplace_image_sas_token_sas_token(device_name: Optional[str] = None,
                                              offer_name: Optional[str] = None,
                                              publisher_name: Optional[str] = None,
                                              resource_group_name: Optional[str] = None,
                                              sku_name: Optional[str] = None,
                                              version_name: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMarketplaceImageSasTokenSASTokenResult:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['offerName'] = offer_name
    __args__['publisherName'] = publisher_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['skuName'] = sku_name
    __args__['versionName'] = version_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20230101preview:getMarketplaceImageSasTokenSASToken', __args__, opts=opts, typ=GetMarketplaceImageSasTokenSASTokenResult).value

    return AwaitableGetMarketplaceImageSasTokenSASTokenResult(
        sas_uri=pulumi.get(__ret__, 'sas_uri'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_marketplace_image_sas_token_sas_token)
def get_marketplace_image_sas_token_sas_token_output(device_name: Optional[pulumi.Input[str]] = None,
                                                     offer_name: Optional[pulumi.Input[str]] = None,
                                                     publisher_name: Optional[pulumi.Input[str]] = None,
                                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                                     sku_name: Optional[pulumi.Input[str]] = None,
                                                     version_name: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMarketplaceImageSasTokenSASTokenResult]:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: The resource group name.
    """
    ...
