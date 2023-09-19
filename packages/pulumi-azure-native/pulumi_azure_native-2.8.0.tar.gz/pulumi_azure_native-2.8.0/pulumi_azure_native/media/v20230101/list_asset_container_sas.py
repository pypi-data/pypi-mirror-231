# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'ListAssetContainerSasResult',
    'AwaitableListAssetContainerSasResult',
    'list_asset_container_sas',
    'list_asset_container_sas_output',
]

@pulumi.output_type
class ListAssetContainerSasResult:
    """
    The Asset Storage container SAS URLs.
    """
    def __init__(__self__, asset_container_sas_urls=None):
        if asset_container_sas_urls and not isinstance(asset_container_sas_urls, list):
            raise TypeError("Expected argument 'asset_container_sas_urls' to be a list")
        pulumi.set(__self__, "asset_container_sas_urls", asset_container_sas_urls)

    @property
    @pulumi.getter(name="assetContainerSasUrls")
    def asset_container_sas_urls(self) -> Optional[Sequence[str]]:
        """
        The list of Asset container SAS URLs.
        """
        return pulumi.get(self, "asset_container_sas_urls")


class AwaitableListAssetContainerSasResult(ListAssetContainerSasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAssetContainerSasResult(
            asset_container_sas_urls=self.asset_container_sas_urls)


def list_asset_container_sas(account_name: Optional[str] = None,
                             asset_name: Optional[str] = None,
                             expiry_time: Optional[str] = None,
                             permissions: Optional[Union[str, 'AssetContainerPermission']] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAssetContainerSasResult:
    """
    Lists storage container URLs with shared access signatures (SAS) for uploading and downloading Asset content. The signatures are derived from the storage account keys.


    :param str account_name: The Media Services account name.
    :param str asset_name: The Asset name.
    :param str expiry_time: The SAS URL expiration time.  This must be less than 24 hours from the current time.
    :param Union[str, 'AssetContainerPermission'] permissions: The permissions to set on the SAS URL.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['assetName'] = asset_name
    __args__['expiryTime'] = expiry_time
    __args__['permissions'] = permissions
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media/v20230101:listAssetContainerSas', __args__, opts=opts, typ=ListAssetContainerSasResult).value

    return AwaitableListAssetContainerSasResult(
        asset_container_sas_urls=pulumi.get(__ret__, 'asset_container_sas_urls'))


@_utilities.lift_output_func(list_asset_container_sas)
def list_asset_container_sas_output(account_name: Optional[pulumi.Input[str]] = None,
                                    asset_name: Optional[pulumi.Input[str]] = None,
                                    expiry_time: Optional[pulumi.Input[Optional[str]]] = None,
                                    permissions: Optional[pulumi.Input[Optional[Union[str, 'AssetContainerPermission']]]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListAssetContainerSasResult]:
    """
    Lists storage container URLs with shared access signatures (SAS) for uploading and downloading Asset content. The signatures are derived from the storage account keys.


    :param str account_name: The Media Services account name.
    :param str asset_name: The Asset name.
    :param str expiry_time: The SAS URL expiration time.  This must be less than 24 hours from the current time.
    :param Union[str, 'AssetContainerPermission'] permissions: The permissions to set on the SAS URL.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    ...
