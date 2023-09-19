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
    'GetEncryptionProtectorResult',
    'AwaitableGetEncryptionProtectorResult',
    'get_encryption_protector',
    'get_encryption_protector_output',
]

@pulumi.output_type
class GetEncryptionProtectorResult:
    """
    The server encryption protector.
    """
    def __init__(__self__, auto_rotation_enabled=None, id=None, kind=None, location=None, name=None, server_key_name=None, server_key_type=None, subregion=None, thumbprint=None, type=None, uri=None):
        if auto_rotation_enabled and not isinstance(auto_rotation_enabled, bool):
            raise TypeError("Expected argument 'auto_rotation_enabled' to be a bool")
        pulumi.set(__self__, "auto_rotation_enabled", auto_rotation_enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if server_key_name and not isinstance(server_key_name, str):
            raise TypeError("Expected argument 'server_key_name' to be a str")
        pulumi.set(__self__, "server_key_name", server_key_name)
        if server_key_type and not isinstance(server_key_type, str):
            raise TypeError("Expected argument 'server_key_type' to be a str")
        pulumi.set(__self__, "server_key_type", server_key_type)
        if subregion and not isinstance(subregion, str):
            raise TypeError("Expected argument 'subregion' to be a str")
        pulumi.set(__self__, "subregion", subregion)
        if thumbprint and not isinstance(thumbprint, str):
            raise TypeError("Expected argument 'thumbprint' to be a str")
        pulumi.set(__self__, "thumbprint", thumbprint)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uri and not isinstance(uri, str):
            raise TypeError("Expected argument 'uri' to be a str")
        pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="autoRotationEnabled")
    def auto_rotation_enabled(self) -> Optional[bool]:
        """
        Key auto rotation opt-in flag. Either true or false.
        """
        return pulumi.get(self, "auto_rotation_enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of encryption protector. This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serverKeyName")
    def server_key_name(self) -> Optional[str]:
        """
        The name of the server key.
        """
        return pulumi.get(self, "server_key_name")

    @property
    @pulumi.getter(name="serverKeyType")
    def server_key_type(self) -> str:
        """
        The encryption protector type like 'ServiceManaged', 'AzureKeyVault'.
        """
        return pulumi.get(self, "server_key_type")

    @property
    @pulumi.getter
    def subregion(self) -> str:
        """
        Subregion of the encryption protector.
        """
        return pulumi.get(self, "subregion")

    @property
    @pulumi.getter
    def thumbprint(self) -> str:
        """
        Thumbprint of the server key.
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uri(self) -> str:
        """
        The URI of the server key.
        """
        return pulumi.get(self, "uri")


class AwaitableGetEncryptionProtectorResult(GetEncryptionProtectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEncryptionProtectorResult(
            auto_rotation_enabled=self.auto_rotation_enabled,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            server_key_name=self.server_key_name,
            server_key_type=self.server_key_type,
            subregion=self.subregion,
            thumbprint=self.thumbprint,
            type=self.type,
            uri=self.uri)


def get_encryption_protector(encryption_protector_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             server_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEncryptionProtectorResult:
    """
    Gets a server encryption protector.


    :param str encryption_protector_name: The name of the encryption protector to be retrieved.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['encryptionProtectorName'] = encryption_protector_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20221101preview:getEncryptionProtector', __args__, opts=opts, typ=GetEncryptionProtectorResult).value

    return AwaitableGetEncryptionProtectorResult(
        auto_rotation_enabled=pulumi.get(__ret__, 'auto_rotation_enabled'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        server_key_name=pulumi.get(__ret__, 'server_key_name'),
        server_key_type=pulumi.get(__ret__, 'server_key_type'),
        subregion=pulumi.get(__ret__, 'subregion'),
        thumbprint=pulumi.get(__ret__, 'thumbprint'),
        type=pulumi.get(__ret__, 'type'),
        uri=pulumi.get(__ret__, 'uri'))


@_utilities.lift_output_func(get_encryption_protector)
def get_encryption_protector_output(encryption_protector_name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    server_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEncryptionProtectorResult]:
    """
    Gets a server encryption protector.


    :param str encryption_protector_name: The name of the encryption protector to be retrieved.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
