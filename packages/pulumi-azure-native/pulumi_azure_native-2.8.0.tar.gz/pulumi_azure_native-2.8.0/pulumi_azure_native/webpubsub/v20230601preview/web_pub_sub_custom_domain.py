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

__all__ = ['WebPubSubCustomDomainArgs', 'WebPubSubCustomDomain']

@pulumi.input_type
class WebPubSubCustomDomainArgs:
    def __init__(__self__, *,
                 custom_certificate: pulumi.Input['ResourceReferenceArgs'],
                 domain_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebPubSubCustomDomain resource.
        :param pulumi.Input['ResourceReferenceArgs'] custom_certificate: Reference to a resource.
        :param pulumi.Input[str] domain_name: The custom domain name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name: The name of the resource.
        :param pulumi.Input[str] name: Custom domain name.
        """
        pulumi.set(__self__, "custom_certificate", custom_certificate)
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="customCertificate")
    def custom_certificate(self) -> pulumi.Input['ResourceReferenceArgs']:
        """
        Reference to a resource.
        """
        return pulumi.get(self, "custom_certificate")

    @custom_certificate.setter
    def custom_certificate(self, value: pulumi.Input['ResourceReferenceArgs']):
        pulumi.set(self, "custom_certificate", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The custom domain name.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Custom domain name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class WebPubSubCustomDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_certificate: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A custom domain

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ResourceReferenceArgs']] custom_certificate: Reference to a resource.
        :param pulumi.Input[str] domain_name: The custom domain name.
        :param pulumi.Input[str] name: Custom domain name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebPubSubCustomDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A custom domain

        :param str resource_name: The name of the resource.
        :param WebPubSubCustomDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebPubSubCustomDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_certificate: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebPubSubCustomDomainArgs.__new__(WebPubSubCustomDomainArgs)

            if custom_certificate is None and not opts.urn:
                raise TypeError("Missing required property 'custom_certificate'")
            __props__.__dict__["custom_certificate"] = custom_certificate
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:webpubsub:WebPubSubCustomDomain"), pulumi.Alias(type_="azure-native:webpubsub/v20220801preview:WebPubSubCustomDomain"), pulumi.Alias(type_="azure-native:webpubsub/v20230201:WebPubSubCustomDomain"), pulumi.Alias(type_="azure-native:webpubsub/v20230301preview:WebPubSubCustomDomain"), pulumi.Alias(type_="azure-native:webpubsub/v20230801preview:WebPubSubCustomDomain")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WebPubSubCustomDomain, __self__).__init__(
            'azure-native:webpubsub/v20230601preview:WebPubSubCustomDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebPubSubCustomDomain':
        """
        Get an existing WebPubSubCustomDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebPubSubCustomDomainArgs.__new__(WebPubSubCustomDomainArgs)

        __props__.__dict__["custom_certificate"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return WebPubSubCustomDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customCertificate")
    def custom_certificate(self) -> pulumi.Output['outputs.ResourceReferenceResponse']:
        """
        Reference to a resource.
        """
        return pulumi.get(self, "custom_certificate")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The custom domain name.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

