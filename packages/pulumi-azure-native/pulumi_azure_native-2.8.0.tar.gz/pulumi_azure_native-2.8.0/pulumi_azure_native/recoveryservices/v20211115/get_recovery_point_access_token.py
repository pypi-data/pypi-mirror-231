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
    'GetRecoveryPointAccessTokenResult',
    'AwaitableGetRecoveryPointAccessTokenResult',
    'get_recovery_point_access_token',
    'get_recovery_point_access_token_output',
]

@pulumi.output_type
class GetRecoveryPointAccessTokenResult:
    def __init__(__self__, e_tag=None, id=None, location=None, name=None, properties=None, tags=None, type=None):
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[str]:
        """
        Optional ETag.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id represents the complete path to the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name associated with the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.WorkloadCrrAccessTokenResponse':
        """
        CrrAccessTokenResource properties
        """
        return pulumi.get(self, "properties")

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
        Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/...
        """
        return pulumi.get(self, "type")


class AwaitableGetRecoveryPointAccessTokenResult(GetRecoveryPointAccessTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRecoveryPointAccessTokenResult(
            e_tag=self.e_tag,
            id=self.id,
            location=self.location,
            name=self.name,
            properties=self.properties,
            tags=self.tags,
            type=self.type)


def get_recovery_point_access_token(container_name: Optional[str] = None,
                                    e_tag: Optional[str] = None,
                                    fabric_name: Optional[str] = None,
                                    location: Optional[str] = None,
                                    properties: Optional[pulumi.InputType['AADProperties']] = None,
                                    protected_item_name: Optional[str] = None,
                                    recovery_point_id: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    tags: Optional[Mapping[str, str]] = None,
                                    vault_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRecoveryPointAccessTokenResult:
    """
    Use this data source to access information about an existing resource.

    :param str container_name: Name of the container.
    :param str e_tag: Optional ETag.
    :param str fabric_name: Fabric name associated with the container.
    :param str location: Resource location.
    :param pulumi.InputType['AADProperties'] properties: AADPropertiesResource properties
    :param str protected_item_name: Name of the Protected Item.
    :param str recovery_point_id: Recovery Point Id
    :param str resource_group_name: The name of the resource group where the recovery services vault is present.
    :param Mapping[str, str] tags: Resource tags.
    :param str vault_name: The name of the recovery services vault.
    """
    __args__ = dict()
    __args__['containerName'] = container_name
    __args__['eTag'] = e_tag
    __args__['fabricName'] = fabric_name
    __args__['location'] = location
    __args__['properties'] = properties
    __args__['protectedItemName'] = protected_item_name
    __args__['recoveryPointId'] = recovery_point_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['tags'] = tags
    __args__['vaultName'] = vault_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:recoveryservices/v20211115:getRecoveryPointAccessToken', __args__, opts=opts, typ=GetRecoveryPointAccessTokenResult).value

    return AwaitableGetRecoveryPointAccessTokenResult(
        e_tag=pulumi.get(__ret__, 'e_tag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_recovery_point_access_token)
def get_recovery_point_access_token_output(container_name: Optional[pulumi.Input[str]] = None,
                                           e_tag: Optional[pulumi.Input[Optional[str]]] = None,
                                           fabric_name: Optional[pulumi.Input[str]] = None,
                                           location: Optional[pulumi.Input[Optional[str]]] = None,
                                           properties: Optional[pulumi.Input[Optional[pulumi.InputType['AADProperties']]]] = None,
                                           protected_item_name: Optional[pulumi.Input[str]] = None,
                                           recovery_point_id: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                           vault_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRecoveryPointAccessTokenResult]:
    """
    Use this data source to access information about an existing resource.

    :param str container_name: Name of the container.
    :param str e_tag: Optional ETag.
    :param str fabric_name: Fabric name associated with the container.
    :param str location: Resource location.
    :param pulumi.InputType['AADProperties'] properties: AADPropertiesResource properties
    :param str protected_item_name: Name of the Protected Item.
    :param str recovery_point_id: Recovery Point Id
    :param str resource_group_name: The name of the resource group where the recovery services vault is present.
    :param Mapping[str, str] tags: Resource tags.
    :param str vault_name: The name of the recovery services vault.
    """
    ...
