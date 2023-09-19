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
    'GetClientGroupResult',
    'AwaitableGetClientGroupResult',
    'get_client_group',
    'get_client_group_output',
]

@pulumi.output_type
class GetClientGroupResult:
    """
    The Client group resource.
    """
    def __init__(__self__, description=None, id=None, name=None, provisioning_state=None, query=None, system_data=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if query and not isinstance(query, str):
            raise TypeError("Expected argument 'query' to be a str")
        pulumi.set(__self__, "query", query)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description for the Client Group resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the ClientGroup resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def query(self) -> Optional[str]:
        """
        The grouping query for the clients.
        Example : attributes.keyName IN ['a', 'b', 'c'].
        """
        return pulumi.get(self, "query")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to the ClientGroup resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetClientGroupResult(GetClientGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientGroupResult(
            description=self.description,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            query=self.query,
            system_data=self.system_data,
            type=self.type)


def get_client_group(client_group_name: Optional[str] = None,
                     namespace_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientGroupResult:
    """
    Get properties of a client group.


    :param str client_group_name: Name of the client group.
    :param str namespace_name: Name of the namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    __args__ = dict()
    __args__['clientGroupName'] = client_group_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid/v20230601preview:getClientGroup', __args__, opts=opts, typ=GetClientGroupResult).value

    return AwaitableGetClientGroupResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        query=pulumi.get(__ret__, 'query'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_client_group)
def get_client_group_output(client_group_name: Optional[pulumi.Input[str]] = None,
                            namespace_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClientGroupResult]:
    """
    Get properties of a client group.


    :param str client_group_name: Name of the client group.
    :param str namespace_name: Name of the namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    ...
