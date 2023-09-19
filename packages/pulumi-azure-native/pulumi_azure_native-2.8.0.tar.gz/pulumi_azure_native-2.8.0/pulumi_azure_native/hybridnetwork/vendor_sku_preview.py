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

__all__ = ['VendorSkuPreviewArgs', 'VendorSkuPreview']

@pulumi.input_type
class VendorSkuPreviewArgs:
    def __init__(__self__, *,
                 sku_name: pulumi.Input[str],
                 vendor_name: pulumi.Input[str],
                 preview_subscription: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VendorSkuPreview resource.
        :param pulumi.Input[str] sku_name: The name of the vendor sku.
        :param pulumi.Input[str] vendor_name: The name of the vendor.
        :param pulumi.Input[str] preview_subscription: Preview subscription ID.
        """
        pulumi.set(__self__, "sku_name", sku_name)
        pulumi.set(__self__, "vendor_name", vendor_name)
        if preview_subscription is not None:
            pulumi.set(__self__, "preview_subscription", preview_subscription)

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> pulumi.Input[str]:
        """
        The name of the vendor sku.
        """
        return pulumi.get(self, "sku_name")

    @sku_name.setter
    def sku_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sku_name", value)

    @property
    @pulumi.getter(name="vendorName")
    def vendor_name(self) -> pulumi.Input[str]:
        """
        The name of the vendor.
        """
        return pulumi.get(self, "vendor_name")

    @vendor_name.setter
    def vendor_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vendor_name", value)

    @property
    @pulumi.getter(name="previewSubscription")
    def preview_subscription(self) -> Optional[pulumi.Input[str]]:
        """
        Preview subscription ID.
        """
        return pulumi.get(self, "preview_subscription")

    @preview_subscription.setter
    def preview_subscription(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preview_subscription", value)


class VendorSkuPreview(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 preview_subscription: Optional[pulumi.Input[str]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 vendor_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Customer subscription which can use a sku.
        Azure REST API version: 2022-01-01-preview. Prior API version in Azure Native 1.x: 2020-01-01-preview

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] preview_subscription: Preview subscription ID.
        :param pulumi.Input[str] sku_name: The name of the vendor sku.
        :param pulumi.Input[str] vendor_name: The name of the vendor.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VendorSkuPreviewArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Customer subscription which can use a sku.
        Azure REST API version: 2022-01-01-preview. Prior API version in Azure Native 1.x: 2020-01-01-preview

        :param str resource_name: The name of the resource.
        :param VendorSkuPreviewArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VendorSkuPreviewArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 preview_subscription: Optional[pulumi.Input[str]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 vendor_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VendorSkuPreviewArgs.__new__(VendorSkuPreviewArgs)

            __props__.__dict__["preview_subscription"] = preview_subscription
            if sku_name is None and not opts.urn:
                raise TypeError("Missing required property 'sku_name'")
            __props__.__dict__["sku_name"] = sku_name
            if vendor_name is None and not opts.urn:
                raise TypeError("Missing required property 'vendor_name'")
            __props__.__dict__["vendor_name"] = vendor_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hybridnetwork/v20200101preview:VendorSkuPreview"), pulumi.Alias(type_="azure-native:hybridnetwork/v20210501:VendorSkuPreview"), pulumi.Alias(type_="azure-native:hybridnetwork/v20220101preview:VendorSkuPreview")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VendorSkuPreview, __self__).__init__(
            'azure-native:hybridnetwork:VendorSkuPreview',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VendorSkuPreview':
        """
        Get an existing VendorSkuPreview resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VendorSkuPreviewArgs.__new__(VendorSkuPreviewArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return VendorSkuPreview(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The preview subscription ID.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the PreviewSubscription resource.
        """
        return pulumi.get(self, "provisioning_state")

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
        The type of the resource.
        """
        return pulumi.get(self, "type")

