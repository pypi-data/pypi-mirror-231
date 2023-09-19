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
    'ListContainerAppSecretsResult',
    'AwaitableListContainerAppSecretsResult',
    'list_container_app_secrets',
    'list_container_app_secrets_output',
]

@pulumi.output_type
class ListContainerAppSecretsResult:
    """
    Container App Secrets Collection ARM resource.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.ContainerAppSecretResponse']:
        """
        Collection of resources.
        """
        return pulumi.get(self, "value")


class AwaitableListContainerAppSecretsResult(ListContainerAppSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListContainerAppSecretsResult(
            value=self.value)


def list_container_app_secrets(container_app_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListContainerAppSecretsResult:
    """
    Container App Secrets Collection ARM resource.


    :param str container_app_name: Name of the Container App.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['containerAppName'] = container_app_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20230401preview:listContainerAppSecrets', __args__, opts=opts, typ=ListContainerAppSecretsResult).value

    return AwaitableListContainerAppSecretsResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_container_app_secrets)
def list_container_app_secrets_output(container_app_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListContainerAppSecretsResult]:
    """
    Container App Secrets Collection ARM resource.


    :param str container_app_name: Name of the Container App.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
