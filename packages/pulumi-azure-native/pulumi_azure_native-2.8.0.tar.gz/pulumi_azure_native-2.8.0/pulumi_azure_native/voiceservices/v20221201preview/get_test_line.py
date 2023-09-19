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
    'GetTestLineResult',
    'AwaitableGetTestLineResult',
    'get_test_line',
    'get_test_line_output',
]

@pulumi.output_type
class GetTestLineResult:
    """
    A TestLine resource
    """
    def __init__(__self__, id=None, location=None, name=None, phone_number=None, provisioning_state=None, purpose=None, system_data=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if phone_number and not isinstance(phone_number, str):
            raise TypeError("Expected argument 'phone_number' to be a str")
        pulumi.set(__self__, "phone_number", phone_number)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if purpose and not isinstance(purpose, str):
            raise TypeError("Expected argument 'purpose' to be a str")
        pulumi.set(__self__, "purpose", purpose)
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
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> str:
        """
        The phone number
        """
        return pulumi.get(self, "phone_number")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def purpose(self) -> str:
        """
        Purpose of this test line, e.g. automated or manual testing
        """
        return pulumi.get(self, "purpose")

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


class AwaitableGetTestLineResult(GetTestLineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTestLineResult(
            id=self.id,
            location=self.location,
            name=self.name,
            phone_number=self.phone_number,
            provisioning_state=self.provisioning_state,
            purpose=self.purpose,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_test_line(communications_gateway_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  test_line_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTestLineResult:
    """
    Get a TestLine


    :param str communications_gateway_name: Unique identifier for this deployment
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_line_name: Unique identifier for this test line
    """
    __args__ = dict()
    __args__['communicationsGatewayName'] = communications_gateway_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['testLineName'] = test_line_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:voiceservices/v20221201preview:getTestLine', __args__, opts=opts, typ=GetTestLineResult).value

    return AwaitableGetTestLineResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        phone_number=pulumi.get(__ret__, 'phone_number'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        purpose=pulumi.get(__ret__, 'purpose'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_test_line)
def get_test_line_output(communications_gateway_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         test_line_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTestLineResult]:
    """
    Get a TestLine


    :param str communications_gateway_name: Unique identifier for this deployment
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_line_name: Unique identifier for this test line
    """
    ...
