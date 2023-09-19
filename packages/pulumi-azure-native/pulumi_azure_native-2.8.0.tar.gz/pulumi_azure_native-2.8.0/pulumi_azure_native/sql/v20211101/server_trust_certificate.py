# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ServerTrustCertificateArgs', 'ServerTrustCertificate']

@pulumi.input_type
class ServerTrustCertificateArgs:
    def __init__(__self__, *,
                 managed_instance_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 public_blob: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerTrustCertificate resource.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] certificate_name: Name of of the certificate to upload.
        :param pulumi.Input[str] public_blob: The certificate public blob
        """
        pulumi.set(__self__, "managed_instance_name", managed_instance_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if certificate_name is not None:
            pulumi.set(__self__, "certificate_name", certificate_name)
        if public_blob is not None:
            pulumi.set(__self__, "public_blob", public_blob)

    @property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[str]:
        """
        The name of the managed instance.
        """
        return pulumi.get(self, "managed_instance_name")

    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_instance_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of of the certificate to upload.
        """
        return pulumi.get(self, "certificate_name")

    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_name", value)

    @property
    @pulumi.getter(name="publicBlob")
    def public_blob(self) -> Optional[pulumi.Input[str]]:
        """
        The certificate public blob
        """
        return pulumi.get(self, "public_blob")

    @public_blob.setter
    def public_blob(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_blob", value)


class ServerTrustCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 public_blob: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Server trust certificate imported from box to enable connection between box and Sql Managed Instance.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_name: Name of of the certificate to upload.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] public_blob: The certificate public blob
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerTrustCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Server trust certificate imported from box to enable connection between box and Sql Managed Instance.

        :param str resource_name: The name of the resource.
        :param ServerTrustCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerTrustCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 public_blob: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerTrustCertificateArgs.__new__(ServerTrustCertificateArgs)

            __props__.__dict__["certificate_name"] = certificate_name
            if managed_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_name'")
            __props__.__dict__["managed_instance_name"] = managed_instance_name
            __props__.__dict__["public_blob"] = public_blob
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["thumbprint"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:ServerTrustCertificate"), pulumi.Alias(type_="azure-native:sql/v20210501preview:ServerTrustCertificate"), pulumi.Alias(type_="azure-native:sql/v20210801preview:ServerTrustCertificate"), pulumi.Alias(type_="azure-native:sql/v20211101preview:ServerTrustCertificate"), pulumi.Alias(type_="azure-native:sql/v20220201preview:ServerTrustCertificate"), pulumi.Alias(type_="azure-native:sql/v20220501preview:ServerTrustCertificate"), pulumi.Alias(type_="azure-native:sql/v20220801preview:ServerTrustCertificate"), pulumi.Alias(type_="azure-native:sql/v20221101preview:ServerTrustCertificate"), pulumi.Alias(type_="azure-native:sql/v20230201preview:ServerTrustCertificate")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerTrustCertificate, __self__).__init__(
            'azure-native:sql/v20211101:ServerTrustCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerTrustCertificate':
        """
        Get an existing ServerTrustCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerTrustCertificateArgs.__new__(ServerTrustCertificateArgs)

        __props__.__dict__["certificate_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["public_blob"] = None
        __props__.__dict__["thumbprint"] = None
        __props__.__dict__["type"] = None
        return ServerTrustCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> pulumi.Output[str]:
        """
        The certificate name
        """
        return pulumi.get(self, "certificate_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicBlob")
    def public_blob(self) -> pulumi.Output[Optional[str]]:
        """
        The certificate public blob
        """
        return pulumi.get(self, "public_blob")

    @property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Output[str]:
        """
        The certificate thumbprint
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

