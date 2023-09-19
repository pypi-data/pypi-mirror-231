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
    'GetVmmServerResult',
    'AwaitableGetVmmServerResult',
    'get_vmm_server',
    'get_vmm_server_output',
]

@pulumi.output_type
class GetVmmServerResult:
    """
    The VmmServers resource definition.
    """
    def __init__(__self__, connection_status=None, credentials=None, error_message=None, extended_location=None, fqdn=None, id=None, location=None, name=None, port=None, provisioning_state=None, system_data=None, tags=None, type=None, uuid=None, version=None):
        if connection_status and not isinstance(connection_status, str):
            raise TypeError("Expected argument 'connection_status' to be a str")
        pulumi.set(__self__, "connection_status", connection_status)
        if credentials and not isinstance(credentials, dict):
            raise TypeError("Expected argument 'credentials' to be a dict")
        pulumi.set(__self__, "credentials", credentials)
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        pulumi.set(__self__, "error_message", error_message)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
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
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> str:
        """
        Gets or sets the connection status to the vmmServer.
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter
    def credentials(self) -> Optional['outputs.VMMServerPropertiesResponseCredentials']:
        """
        Credentials to connect to VMMServer.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        """
        Gets or sets any error message if connection to vmmServer is having any issue.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> 'outputs.ExtendedLocationResponse':
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        Fqdn is the hostname/ip of the vmmServer.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        Port is the port on which the vmmServer is listening.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        Unique ID of vmmServer.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version is the version of the vmmSever.
        """
        return pulumi.get(self, "version")


class AwaitableGetVmmServerResult(GetVmmServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVmmServerResult(
            connection_status=self.connection_status,
            credentials=self.credentials,
            error_message=self.error_message,
            extended_location=self.extended_location,
            fqdn=self.fqdn,
            id=self.id,
            location=self.location,
            name=self.name,
            port=self.port,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            uuid=self.uuid,
            version=self.version)


def get_vmm_server(resource_group_name: Optional[str] = None,
                   vmm_server_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVmmServerResult:
    """
    Implements VMMServer GET method.
    Azure REST API version: 2022-05-21-preview.


    :param str resource_group_name: The name of the resource group.
    :param str vmm_server_name: Name of the VMMServer.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['vmmServerName'] = vmm_server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:scvmm:getVmmServer', __args__, opts=opts, typ=GetVmmServerResult).value

    return AwaitableGetVmmServerResult(
        connection_status=pulumi.get(__ret__, 'connection_status'),
        credentials=pulumi.get(__ret__, 'credentials'),
        error_message=pulumi.get(__ret__, 'error_message'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        fqdn=pulumi.get(__ret__, 'fqdn'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        port=pulumi.get(__ret__, 'port'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        uuid=pulumi.get(__ret__, 'uuid'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_vmm_server)
def get_vmm_server_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                          vmm_server_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVmmServerResult]:
    """
    Implements VMMServer GET method.
    Azure REST API version: 2022-05-21-preview.


    :param str resource_group_name: The name of the resource group.
    :param str vmm_server_name: Name of the VMMServer.
    """
    ...
