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

__all__ = [
    'ListIntegrationAccountKeyVaultKeysResult',
    'AwaitableListIntegrationAccountKeyVaultKeysResult',
    'list_integration_account_key_vault_keys',
    'list_integration_account_key_vault_keys_output',
]

@pulumi.output_type
class ListIntegrationAccountKeyVaultKeysResult:
    """
    Collection of key vault keys.
    """
    def __init__(__self__, skip_token=None, value=None):
        if skip_token and not isinstance(skip_token, str):
            raise TypeError("Expected argument 'skip_token' to be a str")
        pulumi.set(__self__, "skip_token", skip_token)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[str]:
        """
        The skip token.
        """
        return pulumi.get(self, "skip_token")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.KeyVaultKeyResponse']]:
        """
        The key vault keys.
        """
        return pulumi.get(self, "value")


class AwaitableListIntegrationAccountKeyVaultKeysResult(ListIntegrationAccountKeyVaultKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListIntegrationAccountKeyVaultKeysResult(
            skip_token=self.skip_token,
            value=self.value)


def list_integration_account_key_vault_keys(integration_account_name: Optional[str] = None,
                                            key_vault: Optional[pulumi.InputType['KeyVaultReference']] = None,
                                            resource_group_name: Optional[str] = None,
                                            skip_token: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListIntegrationAccountKeyVaultKeysResult:
    """
    Gets the integration account's Key Vault keys.


    :param str integration_account_name: The integration account name.
    :param pulumi.InputType['KeyVaultReference'] key_vault: The key vault reference.
    :param str resource_group_name: The resource group name.
    :param str skip_token: The skip token.
    """
    __args__ = dict()
    __args__['integrationAccountName'] = integration_account_name
    __args__['keyVault'] = key_vault
    __args__['resourceGroupName'] = resource_group_name
    __args__['skipToken'] = skip_token
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:logic/v20190501:listIntegrationAccountKeyVaultKeys', __args__, opts=opts, typ=ListIntegrationAccountKeyVaultKeysResult).value

    return AwaitableListIntegrationAccountKeyVaultKeysResult(
        skip_token=pulumi.get(__ret__, 'skip_token'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_integration_account_key_vault_keys)
def list_integration_account_key_vault_keys_output(integration_account_name: Optional[pulumi.Input[str]] = None,
                                                   key_vault: Optional[pulumi.Input[pulumi.InputType['KeyVaultReference']]] = None,
                                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                                   skip_token: Optional[pulumi.Input[Optional[str]]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListIntegrationAccountKeyVaultKeysResult]:
    """
    Gets the integration account's Key Vault keys.


    :param str integration_account_name: The integration account name.
    :param pulumi.InputType['KeyVaultReference'] key_vault: The key vault reference.
    :param str resource_group_name: The resource group name.
    :param str skip_token: The skip token.
    """
    ...
