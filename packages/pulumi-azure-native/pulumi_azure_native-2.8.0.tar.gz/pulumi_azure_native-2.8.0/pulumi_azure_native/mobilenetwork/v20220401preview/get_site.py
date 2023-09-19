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
    'GetSiteResult',
    'AwaitableGetSiteResult',
    'get_site',
    'get_site_output',
]

@pulumi.output_type
class GetSiteResult:
    """
    Site resource.
    """
    def __init__(__self__, created_at=None, created_by=None, created_by_type=None, id=None, last_modified_at=None, last_modified_by=None, last_modified_by_type=None, location=None, name=None, network_functions=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if created_by_type and not isinstance(created_by_type, str):
            raise TypeError("Expected argument 'created_by_type' to be a str")
        pulumi.set(__self__, "created_by_type", created_by_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_at and not isinstance(last_modified_at, str):
            raise TypeError("Expected argument 'last_modified_at' to be a str")
        pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by and not isinstance(last_modified_by, str):
            raise TypeError("Expected argument 'last_modified_by' to be a str")
        pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type and not isinstance(last_modified_by_type, str):
            raise TypeError("Expected argument 'last_modified_by_type' to be a str")
        pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_functions and not isinstance(network_functions, list):
            raise TypeError("Expected argument 'network_functions' to be a list")
        pulumi.set(__self__, "network_functions", network_functions)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
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
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

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
    @pulumi.getter(name="networkFunctions")
    def network_functions(self) -> Optional[Sequence['outputs.SubResourceResponse']]:
        """
        An array of IDs of the network functions deployed on the site, maintained by the user.
        """
        return pulumi.get(self, "network_functions")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the site resource.
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


class AwaitableGetSiteResult(GetSiteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSiteResult(
            created_at=self.created_at,
            created_by=self.created_by,
            created_by_type=self.created_by_type,
            id=self.id,
            last_modified_at=self.last_modified_at,
            last_modified_by=self.last_modified_by,
            last_modified_by_type=self.last_modified_by_type,
            location=self.location,
            name=self.name,
            network_functions=self.network_functions,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_site(mobile_network_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             site_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSiteResult:
    """
    Gets information about the specified mobile network site.


    :param str mobile_network_name: The name of the mobile network.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: The name of the mobile network site.
    """
    __args__ = dict()
    __args__['mobileNetworkName'] = mobile_network_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['siteName'] = site_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:mobilenetwork/v20220401preview:getSite', __args__, opts=opts, typ=GetSiteResult).value

    return AwaitableGetSiteResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        created_by=pulumi.get(__ret__, 'created_by'),
        created_by_type=pulumi.get(__ret__, 'created_by_type'),
        id=pulumi.get(__ret__, 'id'),
        last_modified_at=pulumi.get(__ret__, 'last_modified_at'),
        last_modified_by=pulumi.get(__ret__, 'last_modified_by'),
        last_modified_by_type=pulumi.get(__ret__, 'last_modified_by_type'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_functions=pulumi.get(__ret__, 'network_functions'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_site)
def get_site_output(mobile_network_name: Optional[pulumi.Input[str]] = None,
                    resource_group_name: Optional[pulumi.Input[str]] = None,
                    site_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSiteResult]:
    """
    Gets information about the specified mobile network site.


    :param str mobile_network_name: The name of the mobile network.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: The name of the mobile network site.
    """
    ...
