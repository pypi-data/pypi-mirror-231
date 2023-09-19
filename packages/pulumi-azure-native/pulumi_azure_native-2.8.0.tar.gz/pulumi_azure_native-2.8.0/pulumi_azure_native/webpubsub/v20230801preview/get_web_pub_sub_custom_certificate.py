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
    'GetWebPubSubCustomCertificateResult',
    'AwaitableGetWebPubSubCustomCertificateResult',
    'get_web_pub_sub_custom_certificate',
    'get_web_pub_sub_custom_certificate_output',
]

@pulumi.output_type
class GetWebPubSubCustomCertificateResult:
    """
    A custom certificate.
    """
    def __init__(__self__, id=None, key_vault_base_uri=None, key_vault_secret_name=None, key_vault_secret_version=None, name=None, provisioning_state=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_vault_base_uri and not isinstance(key_vault_base_uri, str):
            raise TypeError("Expected argument 'key_vault_base_uri' to be a str")
        pulumi.set(__self__, "key_vault_base_uri", key_vault_base_uri)
        if key_vault_secret_name and not isinstance(key_vault_secret_name, str):
            raise TypeError("Expected argument 'key_vault_secret_name' to be a str")
        pulumi.set(__self__, "key_vault_secret_name", key_vault_secret_name)
        if key_vault_secret_version and not isinstance(key_vault_secret_version, str):
            raise TypeError("Expected argument 'key_vault_secret_version' to be a str")
        pulumi.set(__self__, "key_vault_secret_version", key_vault_secret_version)
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
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyVaultBaseUri")
    def key_vault_base_uri(self) -> str:
        """
        Base uri of the KeyVault that stores certificate.
        """
        return pulumi.get(self, "key_vault_base_uri")

    @property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> str:
        """
        Certificate secret name.
        """
        return pulumi.get(self, "key_vault_secret_name")

    @property
    @pulumi.getter(name="keyVaultSecretVersion")
    def key_vault_secret_version(self) -> Optional[str]:
        """
        Certificate secret version.
        """
        return pulumi.get(self, "key_vault_secret_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWebPubSubCustomCertificateResult(GetWebPubSubCustomCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebPubSubCustomCertificateResult(
            id=self.id,
            key_vault_base_uri=self.key_vault_base_uri,
            key_vault_secret_name=self.key_vault_secret_name,
            key_vault_secret_version=self.key_vault_secret_version,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_web_pub_sub_custom_certificate(certificate_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       resource_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebPubSubCustomCertificateResult:
    """
    Get a custom certificate.


    :param str certificate_name: Custom certificate name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource.
    """
    __args__ = dict()
    __args__['certificateName'] = certificate_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:webpubsub/v20230801preview:getWebPubSubCustomCertificate', __args__, opts=opts, typ=GetWebPubSubCustomCertificateResult).value

    return AwaitableGetWebPubSubCustomCertificateResult(
        id=pulumi.get(__ret__, 'id'),
        key_vault_base_uri=pulumi.get(__ret__, 'key_vault_base_uri'),
        key_vault_secret_name=pulumi.get(__ret__, 'key_vault_secret_name'),
        key_vault_secret_version=pulumi.get(__ret__, 'key_vault_secret_version'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_web_pub_sub_custom_certificate)
def get_web_pub_sub_custom_certificate_output(certificate_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              resource_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebPubSubCustomCertificateResult]:
    """
    Get a custom certificate.


    :param str certificate_name: Custom certificate name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource.
    """
    ...
