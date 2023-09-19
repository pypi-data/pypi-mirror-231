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

__all__ = ['CaCertificateArgs', 'CaCertificate']

@pulumi.input_type
class CaCertificateArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 ca_certificate_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoded_certificate: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CaCertificate resource.
        :param pulumi.Input[str] namespace_name: Name of the namespace.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[str] ca_certificate_name: The CA certificate name.
        :param pulumi.Input[str] description: Description for the CA Certificate resource.
        :param pulumi.Input[str] encoded_certificate: Base64 encoded PEM (Privacy Enhanced Mail) format certificate data.
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if ca_certificate_name is not None:
            pulumi.set(__self__, "ca_certificate_name", ca_certificate_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if encoded_certificate is not None:
            pulumi.set(__self__, "encoded_certificate", encoded_certificate)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        Name of the namespace.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="caCertificateName")
    def ca_certificate_name(self) -> Optional[pulumi.Input[str]]:
        """
        The CA certificate name.
        """
        return pulumi.get(self, "ca_certificate_name")

    @ca_certificate_name.setter
    def ca_certificate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_certificate_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description for the CA Certificate resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="encodedCertificate")
    def encoded_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        Base64 encoded PEM (Privacy Enhanced Mail) format certificate data.
        """
        return pulumi.get(self, "encoded_certificate")

    @encoded_certificate.setter
    def encoded_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoded_certificate", value)


class CaCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ca_certificate_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoded_certificate: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The CA Certificate resource.
        Azure REST API version: 2023-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ca_certificate_name: The CA certificate name.
        :param pulumi.Input[str] description: Description for the CA Certificate resource.
        :param pulumi.Input[str] encoded_certificate: Base64 encoded PEM (Privacy Enhanced Mail) format certificate data.
        :param pulumi.Input[str] namespace_name: Name of the namespace.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CaCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The CA Certificate resource.
        Azure REST API version: 2023-06-01-preview.

        :param str resource_name: The name of the resource.
        :param CaCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CaCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ca_certificate_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoded_certificate: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CaCertificateArgs.__new__(CaCertificateArgs)

            __props__.__dict__["ca_certificate_name"] = ca_certificate_name
            __props__.__dict__["description"] = description
            __props__.__dict__["encoded_certificate"] = encoded_certificate
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["expiry_time_in_utc"] = None
            __props__.__dict__["issue_time_in_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid/v20230601preview:CaCertificate")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CaCertificate, __self__).__init__(
            'azure-native:eventgrid:CaCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CaCertificate':
        """
        Get an existing CaCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CaCertificateArgs.__new__(CaCertificateArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["encoded_certificate"] = None
        __props__.__dict__["expiry_time_in_utc"] = None
        __props__.__dict__["issue_time_in_utc"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return CaCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description for the CA Certificate resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encodedCertificate")
    def encoded_certificate(self) -> pulumi.Output[Optional[str]]:
        """
        Base64 encoded PEM (Privacy Enhanced Mail) format certificate data.
        """
        return pulumi.get(self, "encoded_certificate")

    @property
    @pulumi.getter(name="expiryTimeInUtc")
    def expiry_time_in_utc(self) -> pulumi.Output[str]:
        """
        Certificate expiry time in UTC. This is a read-only field.
        """
        return pulumi.get(self, "expiry_time_in_utc")

    @property
    @pulumi.getter(name="issueTimeInUtc")
    def issue_time_in_utc(self) -> pulumi.Output[str]:
        """
        Certificate issue time in UTC. This is a read-only field.
        """
        return pulumi.get(self, "issue_time_in_utc")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the CA Certificate resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to the CaCertificate resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

