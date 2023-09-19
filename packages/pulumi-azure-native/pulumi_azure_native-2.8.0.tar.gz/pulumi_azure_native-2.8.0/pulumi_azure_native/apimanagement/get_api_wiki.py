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
    'GetApiWikiResult',
    'AwaitableGetApiWikiResult',
    'get_api_wiki',
    'get_api_wiki_output',
]

@pulumi.output_type
class GetApiWikiResult:
    """
    Wiki properties
    """
    def __init__(__self__, documents=None, id=None, name=None, type=None):
        if documents and not isinstance(documents, list):
            raise TypeError("Expected argument 'documents' to be a list")
        pulumi.set(__self__, "documents", documents)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def documents(self) -> Optional[Sequence['outputs.WikiDocumentationContractResponse']]:
        """
        Collection wiki documents included into this wiki.
        """
        return pulumi.get(self, "documents")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetApiWikiResult(GetApiWikiResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiWikiResult(
            documents=self.documents,
            id=self.id,
            name=self.name,
            type=self.type)


def get_api_wiki(api_id: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 service_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiWikiResult:
    """
    Gets the details of the Wiki for an API specified by its identifier.
    Azure REST API version: 2022-08-01.


    :param str api_id: API identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement:getApiWiki', __args__, opts=opts, typ=GetApiWikiResult).value

    return AwaitableGetApiWikiResult(
        documents=pulumi.get(__ret__, 'documents'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_api_wiki)
def get_api_wiki_output(api_id: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        service_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiWikiResult]:
    """
    Gets the details of the Wiki for an API specified by its identifier.
    Azure REST API version: 2022-08-01.


    :param str api_id: API identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
