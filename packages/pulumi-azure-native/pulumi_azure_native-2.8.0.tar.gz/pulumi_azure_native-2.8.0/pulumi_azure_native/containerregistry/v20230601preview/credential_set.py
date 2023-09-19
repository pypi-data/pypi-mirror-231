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
from ._enums import *
from ._inputs import *

__all__ = ['CredentialSetArgs', 'CredentialSet']

@pulumi.input_type
class CredentialSetArgs:
    def __init__(__self__, *,
                 registry_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 auth_credentials: Optional[pulumi.Input[Sequence[pulumi.Input['AuthCredentialArgs']]]] = None,
                 credential_set_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['IdentityPropertiesArgs']] = None,
                 login_server: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CredentialSet resource.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['AuthCredentialArgs']]] auth_credentials: List of authentication credentials stored for an upstream.
               Usually consists of a primary and an optional secondary credential.
        :param pulumi.Input[str] credential_set_name: The name of the credential set.
        :param pulumi.Input['IdentityPropertiesArgs'] identity: Identities associated with the resource. This is used to access the KeyVault secrets.
        :param pulumi.Input[str] login_server: The credentials are stored for this upstream or login server.
        """
        pulumi.set(__self__, "registry_name", registry_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auth_credentials is not None:
            pulumi.set(__self__, "auth_credentials", auth_credentials)
        if credential_set_name is not None:
            pulumi.set(__self__, "credential_set_name", credential_set_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if login_server is not None:
            pulumi.set(__self__, "login_server", login_server)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @registry_name.setter
    def registry_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_name", value)

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
    @pulumi.getter(name="authCredentials")
    def auth_credentials(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AuthCredentialArgs']]]]:
        """
        List of authentication credentials stored for an upstream.
        Usually consists of a primary and an optional secondary credential.
        """
        return pulumi.get(self, "auth_credentials")

    @auth_credentials.setter
    def auth_credentials(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AuthCredentialArgs']]]]):
        pulumi.set(self, "auth_credentials", value)

    @property
    @pulumi.getter(name="credentialSetName")
    def credential_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the credential set.
        """
        return pulumi.get(self, "credential_set_name")

    @credential_set_name.setter
    def credential_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credential_set_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityPropertiesArgs']]:
        """
        Identities associated with the resource. This is used to access the KeyVault secrets.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityPropertiesArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="loginServer")
    def login_server(self) -> Optional[pulumi.Input[str]]:
        """
        The credentials are stored for this upstream or login server.
        """
        return pulumi.get(self, "login_server")

    @login_server.setter
    def login_server(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "login_server", value)


class CredentialSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_credentials: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AuthCredentialArgs']]]]] = None,
                 credential_set_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityPropertiesArgs']]] = None,
                 login_server: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An object that represents a credential set resource for a container registry.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AuthCredentialArgs']]]] auth_credentials: List of authentication credentials stored for an upstream.
               Usually consists of a primary and an optional secondary credential.
        :param pulumi.Input[str] credential_set_name: The name of the credential set.
        :param pulumi.Input[pulumi.InputType['IdentityPropertiesArgs']] identity: Identities associated with the resource. This is used to access the KeyVault secrets.
        :param pulumi.Input[str] login_server: The credentials are stored for this upstream or login server.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CredentialSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object that represents a credential set resource for a container registry.

        :param str resource_name: The name of the resource.
        :param CredentialSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CredentialSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_credentials: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AuthCredentialArgs']]]]] = None,
                 credential_set_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityPropertiesArgs']]] = None,
                 login_server: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CredentialSetArgs.__new__(CredentialSetArgs)

            __props__.__dict__["auth_credentials"] = auth_credentials
            __props__.__dict__["credential_set_name"] = credential_set_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["login_server"] = login_server
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__.__dict__["registry_name"] = registry_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerregistry:CredentialSet"), pulumi.Alias(type_="azure-native:containerregistry/v20230101preview:CredentialSet"), pulumi.Alias(type_="azure-native:containerregistry/v20230701:CredentialSet"), pulumi.Alias(type_="azure-native:containerregistry/v20230801preview:CredentialSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CredentialSet, __self__).__init__(
            'azure-native:containerregistry/v20230601preview:CredentialSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CredentialSet':
        """
        Get an existing CredentialSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CredentialSetArgs.__new__(CredentialSetArgs)

        __props__.__dict__["auth_credentials"] = None
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["login_server"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return CredentialSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authCredentials")
    def auth_credentials(self) -> pulumi.Output[Optional[Sequence['outputs.AuthCredentialResponse']]]:
        """
        List of authentication credentials stored for an upstream.
        Usually consists of a primary and an optional secondary credential.
        """
        return pulumi.get(self, "auth_credentials")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The creation date of credential store resource.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityPropertiesResponse']]:
        """
        Identities associated with the resource. This is used to access the KeyVault secrets.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="loginServer")
    def login_server(self) -> pulumi.Output[Optional[str]]:
        """
        The credentials are stored for this upstream or login server.
        """
        return pulumi.get(self, "login_server")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
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
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

