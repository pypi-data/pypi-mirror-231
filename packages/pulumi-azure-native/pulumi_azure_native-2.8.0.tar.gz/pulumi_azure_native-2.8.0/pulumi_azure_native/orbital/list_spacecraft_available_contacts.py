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
from ._inputs import *

__all__ = [
    'ListSpacecraftAvailableContactsResult',
    'AwaitableListSpacecraftAvailableContactsResult',
    'list_spacecraft_available_contacts',
    'list_spacecraft_available_contacts_output',
]

@pulumi.output_type
class ListSpacecraftAvailableContactsResult:
    """
    Response for the ListAvailableContacts API service call.
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
    def next_link(self) -> str:
        """
        The URL to get the next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.AvailableContactsResponse']]:
        """
        A list of available contacts.
        """
        return pulumi.get(self, "value")


class AwaitableListSpacecraftAvailableContactsResult(ListSpacecraftAvailableContactsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListSpacecraftAvailableContactsResult(
            next_link=self.next_link,
            value=self.value)


def list_spacecraft_available_contacts(contact_profile: Optional[pulumi.InputType['ContactParametersContactProfile']] = None,
                                       end_time: Optional[str] = None,
                                       ground_station_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       spacecraft_name: Optional[str] = None,
                                       start_time: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSpacecraftAvailableContactsResult:
    """
    Returns list of available contacts. A contact is available if the spacecraft is visible from the ground station for more than the minimum viable contact duration provided in the contact profile.
    Azure REST API version: 2022-11-01.


    :param pulumi.InputType['ContactParametersContactProfile'] contact_profile: The reference to the contact profile resource.
    :param str end_time: End time of a contact (ISO 8601 UTC standard).
    :param str ground_station_name: Name of Azure Ground Station.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str spacecraft_name: Spacecraft ID.
    :param str start_time: Start time of a contact (ISO 8601 UTC standard).
    """
    __args__ = dict()
    __args__['contactProfile'] = contact_profile
    __args__['endTime'] = end_time
    __args__['groundStationName'] = ground_station_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['spacecraftName'] = spacecraft_name
    __args__['startTime'] = start_time
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:orbital:listSpacecraftAvailableContacts', __args__, opts=opts, typ=ListSpacecraftAvailableContactsResult).value

    return AwaitableListSpacecraftAvailableContactsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_spacecraft_available_contacts)
def list_spacecraft_available_contacts_output(contact_profile: Optional[pulumi.Input[pulumi.InputType['ContactParametersContactProfile']]] = None,
                                              end_time: Optional[pulumi.Input[str]] = None,
                                              ground_station_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              spacecraft_name: Optional[pulumi.Input[str]] = None,
                                              start_time: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListSpacecraftAvailableContactsResult]:
    """
    Returns list of available contacts. A contact is available if the spacecraft is visible from the ground station for more than the minimum viable contact duration provided in the contact profile.
    Azure REST API version: 2022-11-01.


    :param pulumi.InputType['ContactParametersContactProfile'] contact_profile: The reference to the contact profile resource.
    :param str end_time: End time of a contact (ISO 8601 UTC standard).
    :param str ground_station_name: Name of Azure Ground Station.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str spacecraft_name: Spacecraft ID.
    :param str start_time: Start time of a contact (ISO 8601 UTC standard).
    """
    ...
