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
    'GetTenantConfigurationResult',
    'AwaitableGetTenantConfigurationResult',
    'get_tenant_configuration',
    'get_tenant_configuration_output',
]

@pulumi.output_type
class GetTenantConfigurationResult:
    """
    Tenant configuration.
    """
    def __init__(__self__, enforce_private_markdown_storage=None, id=None, name=None, type=None):
        if enforce_private_markdown_storage and not isinstance(enforce_private_markdown_storage, bool):
            raise TypeError("Expected argument 'enforce_private_markdown_storage' to be a bool")
        pulumi.set(__self__, "enforce_private_markdown_storage", enforce_private_markdown_storage)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="enforcePrivateMarkdownStorage")
    def enforce_private_markdown_storage(self) -> Optional[bool]:
        """
        When flag is set to true Markdown tile will require external storage configuration (URI). The inline content configuration will be prohibited.
        """
        return pulumi.get(self, "enforce_private_markdown_storage")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetTenantConfigurationResult(GetTenantConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTenantConfigurationResult(
            enforce_private_markdown_storage=self.enforce_private_markdown_storage,
            id=self.id,
            name=self.name,
            type=self.type)


def get_tenant_configuration(configuration_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTenantConfigurationResult:
    """
    Gets the tenant configuration.


    :param str configuration_name: The configuration name. Value must be 'default'
    """
    __args__ = dict()
    __args__['configurationName'] = configuration_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:portal/v20200901preview:getTenantConfiguration', __args__, opts=opts, typ=GetTenantConfigurationResult).value

    return AwaitableGetTenantConfigurationResult(
        enforce_private_markdown_storage=pulumi.get(__ret__, 'enforce_private_markdown_storage'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_tenant_configuration)
def get_tenant_configuration_output(configuration_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTenantConfigurationResult]:
    """
    Gets the tenant configuration.


    :param str configuration_name: The configuration name. Value must be 'default'
    """
    ...
