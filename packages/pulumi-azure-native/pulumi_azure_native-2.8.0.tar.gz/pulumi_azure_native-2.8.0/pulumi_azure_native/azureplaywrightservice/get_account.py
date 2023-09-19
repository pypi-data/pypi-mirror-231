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

__all__ = [
    'GetAccountResult',
    'AwaitableGetAccountResult',
    'get_account',
    'get_account_output',
]

@pulumi.output_type
class GetAccountResult:
    """
    An account resource
    """
    def __init__(__self__, dashboard_uri=None, id=None, location=None, name=None, provisioning_state=None, regional_affinity=None, reporting=None, scalable_execution=None, system_data=None, tags=None, type=None):
        if dashboard_uri and not isinstance(dashboard_uri, str):
            raise TypeError("Expected argument 'dashboard_uri' to be a str")
        pulumi.set(__self__, "dashboard_uri", dashboard_uri)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if regional_affinity and not isinstance(regional_affinity, str):
            raise TypeError("Expected argument 'regional_affinity' to be a str")
        pulumi.set(__self__, "regional_affinity", regional_affinity)
        if reporting and not isinstance(reporting, str):
            raise TypeError("Expected argument 'reporting' to be a str")
        pulumi.set(__self__, "reporting", reporting)
        if scalable_execution and not isinstance(scalable_execution, str):
            raise TypeError("Expected argument 'scalable_execution' to be a str")
        pulumi.set(__self__, "scalable_execution", scalable_execution)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dashboardUri")
    def dashboard_uri(self) -> str:
        """
        The Playwright testing dashboard URI for the account resource.
        """
        return pulumi.get(self, "dashboard_uri")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

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
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="regionalAffinity")
    def regional_affinity(self) -> Optional[str]:
        """
        This property sets the connection region for Playwright client workers to cloud-hosted browsers. If enabled, workers connect to browsers in the closest Azure region, ensuring lower latency. If disabled, workers connect to browsers in the Azure region in which the workspace was initially created.
        """
        return pulumi.get(self, "regional_affinity")

    @property
    @pulumi.getter
    def reporting(self) -> Optional[str]:
        """
        When enabled, this feature allows the workspace to upload and display test results, including artifacts like traces and screenshots, in the Playwright portal. This enables faster and more efficient troubleshooting.
        """
        return pulumi.get(self, "reporting")

    @property
    @pulumi.getter(name="scalableExecution")
    def scalable_execution(self) -> Optional[str]:
        """
        When enabled, Playwright client workers can connect to cloud-hosted browsers. This can increase the number of parallel workers for a test run, significantly minimizing test completion durations.
        """
        return pulumi.get(self, "scalable_execution")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            dashboard_uri=self.dashboard_uri,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            regional_affinity=self.regional_affinity,
            reporting=self.reporting,
            scalable_execution=self.scalable_execution,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_account(name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountResult:
    """
    Get a Account
    Azure REST API version: 2023-10-01-preview.


    :param str name: Name of account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azureplaywrightservice:getAccount', __args__, opts=opts, typ=GetAccountResult).value

    return AwaitableGetAccountResult(
        dashboard_uri=pulumi.get(__ret__, 'dashboard_uri'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        regional_affinity=pulumi.get(__ret__, 'regional_affinity'),
        reporting=pulumi.get(__ret__, 'reporting'),
        scalable_execution=pulumi.get(__ret__, 'scalable_execution'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_account)
def get_account_output(name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountResult]:
    """
    Get a Account
    Azure REST API version: 2023-10-01-preview.


    :param str name: Name of account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
