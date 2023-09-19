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
    'ListPolicyFragmentReferencesResult',
    'AwaitableListPolicyFragmentReferencesResult',
    'list_policy_fragment_references',
    'list_policy_fragment_references_output',
]

@pulumi.output_type
class ListPolicyFragmentReferencesResult:
    """
    A collection of resources.
    """
    def __init__(__self__, count=None, next_link=None, value=None):
        if count and not isinstance(count, float):
            raise TypeError("Expected argument 'count' to be a float")
        pulumi.set(__self__, "count", count)
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def count(self) -> Optional[float]:
        """
        Total record count number.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        Next page link if any.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.ResourceCollectionResponseValue']]:
        """
        A collection of resources.
        """
        return pulumi.get(self, "value")


class AwaitableListPolicyFragmentReferencesResult(ListPolicyFragmentReferencesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListPolicyFragmentReferencesResult(
            count=self.count,
            next_link=self.next_link,
            value=self.value)


def list_policy_fragment_references(id: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    service_name: Optional[str] = None,
                                    skip: Optional[int] = None,
                                    top: Optional[int] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListPolicyFragmentReferencesResult:
    """
    Lists policy resources that reference the policy fragment.
    Azure REST API version: 2022-08-01.


    :param str id: A resource identifier.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param int skip: Number of records to skip.
    :param int top: Number of records to return.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['skip'] = skip
    __args__['top'] = top
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement:listPolicyFragmentReferences', __args__, opts=opts, typ=ListPolicyFragmentReferencesResult).value

    return AwaitableListPolicyFragmentReferencesResult(
        count=pulumi.get(__ret__, 'count'),
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_policy_fragment_references)
def list_policy_fragment_references_output(id: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           service_name: Optional[pulumi.Input[str]] = None,
                                           skip: Optional[pulumi.Input[Optional[int]]] = None,
                                           top: Optional[pulumi.Input[Optional[int]]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListPolicyFragmentReferencesResult]:
    """
    Lists policy resources that reference the policy fragment.
    Azure REST API version: 2022-08-01.


    :param str id: A resource identifier.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param int skip: Number of records to skip.
    :param int top: Number of records to return.
    """
    ...
