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
    'GetVCenterResult',
    'AwaitableGetVCenterResult',
    'get_v_center',
    'get_v_center_output',
]

@pulumi.output_type
class GetVCenterResult:
    """
    Defines the vCenter.
    """
    def __init__(__self__, connection_status=None, credentials=None, custom_resource_name=None, extended_location=None, fqdn=None, id=None, instance_uuid=None, kind=None, location=None, name=None, port=None, provisioning_state=None, statuses=None, system_data=None, tags=None, type=None, uuid=None, version=None):
        if connection_status and not isinstance(connection_status, str):
            raise TypeError("Expected argument 'connection_status' to be a str")
        pulumi.set(__self__, "connection_status", connection_status)
        if credentials and not isinstance(credentials, dict):
            raise TypeError("Expected argument 'credentials' to be a dict")
        pulumi.set(__self__, "credentials", credentials)
        if custom_resource_name and not isinstance(custom_resource_name, str):
            raise TypeError("Expected argument 'custom_resource_name' to be a str")
        pulumi.set(__self__, "custom_resource_name", custom_resource_name)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_uuid and not isinstance(instance_uuid, str):
            raise TypeError("Expected argument 'instance_uuid' to be a str")
        pulumi.set(__self__, "instance_uuid", instance_uuid)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
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
        if statuses and not isinstance(statuses, list):
            raise TypeError("Expected argument 'statuses' to be a list")
        pulumi.set(__self__, "statuses", statuses)
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
        Gets or sets the connection status to the vCenter.
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter
    def credentials(self) -> Optional['outputs.VICredentialResponse']:
        """
        Username / Password Credentials to connect to vcenter.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> str:
        """
        Gets the name of the corresponding resource in Kubernetes.
        """
        return pulumi.get(self, "custom_resource_name")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        Gets or sets the extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        Gets or sets the FQDN/IPAddress of the vCenter.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Gets or sets the Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceUuid")
    def instance_uuid(self) -> str:
        """
        Gets or sets the instance UUID of the vCenter.
        """
        return pulumi.get(self, "instance_uuid")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

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
        Gets or sets the name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        Gets or sets the port of the vCenter.
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
    @pulumi.getter
    def statuses(self) -> Sequence['outputs.ResourceStatusResponse']:
        """
        The resource status information.
        """
        return pulumi.get(self, "statuses")

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
        Gets or sets the Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets or sets the type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        Gets or sets a unique identifier for this resource.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Gets or sets the version of the vCenter.
        """
        return pulumi.get(self, "version")


class AwaitableGetVCenterResult(GetVCenterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVCenterResult(
            connection_status=self.connection_status,
            credentials=self.credentials,
            custom_resource_name=self.custom_resource_name,
            extended_location=self.extended_location,
            fqdn=self.fqdn,
            id=self.id,
            instance_uuid=self.instance_uuid,
            kind=self.kind,
            location=self.location,
            name=self.name,
            port=self.port,
            provisioning_state=self.provisioning_state,
            statuses=self.statuses,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            uuid=self.uuid,
            version=self.version)


def get_v_center(resource_group_name: Optional[str] = None,
                 vcenter_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVCenterResult:
    """
    Implements vCenter GET method.


    :param str resource_group_name: The Resource Group Name.
    :param str vcenter_name: Name of the vCenter.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['vcenterName'] = vcenter_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:connectedvmwarevsphere/v20220715preview:getVCenter', __args__, opts=opts, typ=GetVCenterResult).value

    return AwaitableGetVCenterResult(
        connection_status=pulumi.get(__ret__, 'connection_status'),
        credentials=pulumi.get(__ret__, 'credentials'),
        custom_resource_name=pulumi.get(__ret__, 'custom_resource_name'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        fqdn=pulumi.get(__ret__, 'fqdn'),
        id=pulumi.get(__ret__, 'id'),
        instance_uuid=pulumi.get(__ret__, 'instance_uuid'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        port=pulumi.get(__ret__, 'port'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        statuses=pulumi.get(__ret__, 'statuses'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        uuid=pulumi.get(__ret__, 'uuid'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_v_center)
def get_v_center_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                        vcenter_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVCenterResult]:
    """
    Implements vCenter GET method.


    :param str resource_group_name: The Resource Group Name.
    :param str vcenter_name: Name of the vCenter.
    """
    ...
