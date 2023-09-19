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
    'GetIntegrationAccountResult',
    'AwaitableGetIntegrationAccountResult',
    'get_integration_account',
    'get_integration_account_output',
]

@pulumi.output_type
class GetIntegrationAccountResult:
    """
    The integration account.
    """
    def __init__(__self__, id=None, integration_service_environment=None, location=None, name=None, sku=None, state=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if integration_service_environment and not isinstance(integration_service_environment, dict):
            raise TypeError("Expected argument 'integration_service_environment' to be a dict")
        pulumi.set(__self__, "integration_service_environment", integration_service_environment)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(self) -> Optional['outputs.ResourceReferenceResponse']:
        """
        The integration service environment.
        """
        return pulumi.get(self, "integration_service_environment")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.IntegrationAccountSkuResponse']:
        """
        The sku.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The workflow state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetIntegrationAccountResult(GetIntegrationAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIntegrationAccountResult(
            id=self.id,
            integration_service_environment=self.integration_service_environment,
            location=self.location,
            name=self.name,
            sku=self.sku,
            state=self.state,
            tags=self.tags,
            type=self.type)


def get_integration_account(integration_account_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIntegrationAccountResult:
    """
    Gets an integration account.


    :param str integration_account_name: The integration account name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['integrationAccountName'] = integration_account_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:logic/v20190501:getIntegrationAccount', __args__, opts=opts, typ=GetIntegrationAccountResult).value

    return AwaitableGetIntegrationAccountResult(
        id=pulumi.get(__ret__, 'id'),
        integration_service_environment=pulumi.get(__ret__, 'integration_service_environment'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        sku=pulumi.get(__ret__, 'sku'),
        state=pulumi.get(__ret__, 'state'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_integration_account)
def get_integration_account_output(integration_account_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIntegrationAccountResult]:
    """
    Gets an integration account.


    :param str integration_account_name: The integration account name.
    :param str resource_group_name: The resource group name.
    """
    ...
