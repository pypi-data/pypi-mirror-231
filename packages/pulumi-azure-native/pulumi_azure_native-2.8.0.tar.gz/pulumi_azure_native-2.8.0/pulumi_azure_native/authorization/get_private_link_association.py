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
    'GetPrivateLinkAssociationResult',
    'AwaitableGetPrivateLinkAssociationResult',
    'get_private_link_association',
    'get_private_link_association_output',
]

@pulumi.output_type
class GetPrivateLinkAssociationResult:
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The plaResourceID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The pla name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.PrivateLinkAssociationPropertiesExpandedResponse':
        """
        The private link association properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The operation type.
        """
        return pulumi.get(self, "type")


class AwaitableGetPrivateLinkAssociationResult(GetPrivateLinkAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateLinkAssociationResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_private_link_association(group_id: Optional[str] = None,
                                 pla_id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateLinkAssociationResult:
    """
    Get a single private link association
    Azure REST API version: 2020-05-01.


    :param str group_id: The management group ID.
    :param str pla_id: The ID of the PLA
    """
    __args__ = dict()
    __args__['groupId'] = group_id
    __args__['plaId'] = pla_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:authorization:getPrivateLinkAssociation', __args__, opts=opts, typ=GetPrivateLinkAssociationResult).value

    return AwaitableGetPrivateLinkAssociationResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_private_link_association)
def get_private_link_association_output(group_id: Optional[pulumi.Input[str]] = None,
                                        pla_id: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateLinkAssociationResult]:
    """
    Get a single private link association
    Azure REST API version: 2020-05-01.


    :param str group_id: The management group ID.
    :param str pla_id: The ID of the PLA
    """
    ...
