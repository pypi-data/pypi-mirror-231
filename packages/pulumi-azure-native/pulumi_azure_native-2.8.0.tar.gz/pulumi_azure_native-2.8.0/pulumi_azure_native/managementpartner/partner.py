# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PartnerArgs', 'Partner']

@pulumi.input_type
class PartnerArgs:
    def __init__(__self__, *,
                 partner_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Partner resource.
        :param pulumi.Input[str] partner_id: Id of the Partner
        """
        if partner_id is not None:
            pulumi.set(__self__, "partner_id", partner_id)

    @property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the Partner
        """
        return pulumi.get(self, "partner_id")

    @partner_id.setter
    def partner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_id", value)


class Partner(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 partner_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        this is the management partner operations response
        Azure REST API version: 2018-02-01. Prior API version in Azure Native 1.x: 2018-02-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] partner_id: Id of the Partner
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PartnerArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        this is the management partner operations response
        Azure REST API version: 2018-02-01. Prior API version in Azure Native 1.x: 2018-02-01

        :param str resource_name: The name of the resource.
        :param PartnerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PartnerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 partner_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PartnerArgs.__new__(PartnerArgs)

            __props__.__dict__["partner_id"] = partner_id
            __props__.__dict__["created_time"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["object_id"] = None
            __props__.__dict__["partner_name"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_time"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managementpartner/v20180201:Partner")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Partner, __self__).__init__(
            'azure-native:managementpartner:Partner',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Partner':
        """
        Get an existing Partner resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PartnerArgs.__new__(PartnerArgs)

        __props__.__dict__["created_time"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["object_id"] = None
        __props__.__dict__["partner_id"] = None
        __props__.__dict__["partner_name"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_time"] = None
        __props__.__dict__["version"] = None
        return Partner(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[Optional[str]]:
        """
        This is the DateTime when the partner was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[int]]:
        """
        Type of the partner
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the partner
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[Optional[str]]:
        """
        This is the object id.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> pulumi.Output[Optional[str]]:
        """
        This is the partner id
        """
        return pulumi.get(self, "partner_id")

    @property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> pulumi.Output[Optional[str]]:
        """
        This is the partner name
        """
        return pulumi.get(self, "partner_name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        This is the tenant id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of resource. "Microsoft.ManagementPartner/partners"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> pulumi.Output[Optional[str]]:
        """
        This is the DateTime when the partner was updated.
        """
        return pulumi.get(self, "updated_time")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[int]]:
        """
        This is the version.
        """
        return pulumi.get(self, "version")

