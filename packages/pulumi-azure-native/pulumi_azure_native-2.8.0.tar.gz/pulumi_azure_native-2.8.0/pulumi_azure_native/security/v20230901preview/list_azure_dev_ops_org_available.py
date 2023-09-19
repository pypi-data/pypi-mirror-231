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
    'ListAzureDevOpsOrgAvailableResult',
    'AwaitableListAzureDevOpsOrgAvailableResult',
    'list_azure_dev_ops_org_available',
    'list_azure_dev_ops_org_available_output',
]

@pulumi.output_type
class ListAzureDevOpsOrgAvailableResult:
    """
    List of RP resources which supports pagination.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        Gets or sets next link to scroll over the results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.AzureDevOpsOrgResponse']]:
        """
        Gets or sets list of resources.
        """
        return pulumi.get(self, "value")


class AwaitableListAzureDevOpsOrgAvailableResult(ListAzureDevOpsOrgAvailableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAzureDevOpsOrgAvailableResult(
            next_link=self.next_link,
            value=self.value)


def list_azure_dev_ops_org_available(resource_group_name: Optional[str] = None,
                                     security_connector_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAzureDevOpsOrgAvailableResult:
    """
    List of RP resources which supports pagination.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str security_connector_name: The security connector name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['securityConnectorName'] = security_connector_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security/v20230901preview:listAzureDevOpsOrgAvailable', __args__, opts=opts, typ=ListAzureDevOpsOrgAvailableResult).value

    return AwaitableListAzureDevOpsOrgAvailableResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_azure_dev_ops_org_available)
def list_azure_dev_ops_org_available_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                            security_connector_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListAzureDevOpsOrgAvailableResult]:
    """
    List of RP resources which supports pagination.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str security_connector_name: The security connector name.
    """
    ...
