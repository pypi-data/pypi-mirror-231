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
    'GetOrganizationElasticToAzureSubscriptionMappingResult',
    'AwaitableGetOrganizationElasticToAzureSubscriptionMappingResult',
    'get_organization_elastic_to_azure_subscription_mapping',
]

@pulumi.output_type
class GetOrganizationElasticToAzureSubscriptionMappingResult:
    """
    The Azure Subscription ID to which the Organization of the logged in user belongs and gets billed into.
    """
    def __init__(__self__, properties=None):
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ElasticOrganizationToAzureSubscriptionMappingResponsePropertiesResponse':
        """
        The properties of Azure Subscription ID to which the Organization of the logged in user belongs and gets billed into.
        """
        return pulumi.get(self, "properties")


class AwaitableGetOrganizationElasticToAzureSubscriptionMappingResult(GetOrganizationElasticToAzureSubscriptionMappingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationElasticToAzureSubscriptionMappingResult(
            properties=self.properties)


def get_organization_elastic_to_azure_subscription_mapping(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationElasticToAzureSubscriptionMappingResult:
    """
    Get Elastic Organization To Azure Subscription Mapping details for the logged-in user.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elastic/v20230701preview:getOrganizationElasticToAzureSubscriptionMapping', __args__, opts=opts, typ=GetOrganizationElasticToAzureSubscriptionMappingResult).value

    return AwaitableGetOrganizationElasticToAzureSubscriptionMappingResult(
        properties=pulumi.get(__ret__, 'properties'))
