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
    'GetServiceResult',
    'AwaitableGetServiceResult',
    'get_service',
    'get_service_output',
]

@pulumi.output_type
class GetServiceResult:
    """
    A Database Migration Service resource
    """
    def __init__(__self__, etag=None, id=None, kind=None, location=None, name=None, provisioning_state=None, public_key=None, sku=None, system_data=None, tags=None, type=None, virtual_nic_id=None, virtual_subnet_id=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_nic_id and not isinstance(virtual_nic_id, str):
            raise TypeError("Expected argument 'virtual_nic_id' to be a str")
        pulumi.set(__self__, "virtual_nic_id", virtual_nic_id)
        if virtual_subnet_id and not isinstance(virtual_subnet_id, str):
            raise TypeError("Expected argument 'virtual_subnet_id' to be a str")
        pulumi.set(__self__, "virtual_subnet_id", virtual_subnet_id)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        HTTP strong entity tag value. Ignored if submitted
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The resource kind. Only 'vm' (the default) is supported.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The resource's provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[str]:
        """
        The public key of the service, used to encrypt secrets sent to the service
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.ServiceSkuResponse']:
        """
        Service SKU
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
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
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNicId")
    def virtual_nic_id(self) -> Optional[str]:
        """
        The ID of the Microsoft.Network/networkInterfaces resource which the service have
        """
        return pulumi.get(self, "virtual_nic_id")

    @property
    @pulumi.getter(name="virtualSubnetId")
    def virtual_subnet_id(self) -> str:
        """
        The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined
        """
        return pulumi.get(self, "virtual_subnet_id")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            public_key=self.public_key,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            virtual_nic_id=self.virtual_nic_id,
            virtual_subnet_id=self.virtual_subnet_id)


def get_service(group_name: Optional[str] = None,
                service_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    The services resource is the top-level resource that represents the Database Migration Service. The GET method retrieves information about a service instance.


    :param str group_name: Name of the resource group
    :param str service_name: Name of the service
    """
    __args__ = dict()
    __args__['groupName'] = group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datamigration/v20210630:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_key=pulumi.get(__ret__, 'public_key'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        virtual_nic_id=pulumi.get(__ret__, 'virtual_nic_id'),
        virtual_subnet_id=pulumi.get(__ret__, 'virtual_subnet_id'))


@_utilities.lift_output_func(get_service)
def get_service_output(group_name: Optional[pulumi.Input[str]] = None,
                       service_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceResult]:
    """
    The services resource is the top-level resource that represents the Database Migration Service. The GET method retrieves information about a service instance.


    :param str group_name: Name of the resource group
    :param str service_name: Name of the service
    """
    ...
