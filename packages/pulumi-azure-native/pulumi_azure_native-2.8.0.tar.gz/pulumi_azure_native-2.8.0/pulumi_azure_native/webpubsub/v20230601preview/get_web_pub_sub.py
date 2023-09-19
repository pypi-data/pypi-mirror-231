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
    'GetWebPubSubResult',
    'AwaitableGetWebPubSubResult',
    'get_web_pub_sub',
    'get_web_pub_sub_output',
]

@pulumi.output_type
class GetWebPubSubResult:
    """
    A class represent a resource.
    """
    def __init__(__self__, disable_aad_auth=None, disable_local_auth=None, external_ip=None, host_name=None, host_name_prefix=None, id=None, identity=None, kind=None, live_trace_configuration=None, location=None, name=None, network_acls=None, private_endpoint_connections=None, provisioning_state=None, public_network_access=None, public_port=None, resource_log_configuration=None, server_port=None, shared_private_link_resources=None, sku=None, system_data=None, tags=None, tls=None, type=None, version=None):
        if disable_aad_auth and not isinstance(disable_aad_auth, bool):
            raise TypeError("Expected argument 'disable_aad_auth' to be a bool")
        pulumi.set(__self__, "disable_aad_auth", disable_aad_auth)
        if disable_local_auth and not isinstance(disable_local_auth, bool):
            raise TypeError("Expected argument 'disable_local_auth' to be a bool")
        pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if external_ip and not isinstance(external_ip, str):
            raise TypeError("Expected argument 'external_ip' to be a str")
        pulumi.set(__self__, "external_ip", external_ip)
        if host_name and not isinstance(host_name, str):
            raise TypeError("Expected argument 'host_name' to be a str")
        pulumi.set(__self__, "host_name", host_name)
        if host_name_prefix and not isinstance(host_name_prefix, str):
            raise TypeError("Expected argument 'host_name_prefix' to be a str")
        pulumi.set(__self__, "host_name_prefix", host_name_prefix)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if live_trace_configuration and not isinstance(live_trace_configuration, dict):
            raise TypeError("Expected argument 'live_trace_configuration' to be a dict")
        pulumi.set(__self__, "live_trace_configuration", live_trace_configuration)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_acls and not isinstance(network_acls, dict):
            raise TypeError("Expected argument 'network_acls' to be a dict")
        pulumi.set(__self__, "network_acls", network_acls)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if public_port and not isinstance(public_port, int):
            raise TypeError("Expected argument 'public_port' to be a int")
        pulumi.set(__self__, "public_port", public_port)
        if resource_log_configuration and not isinstance(resource_log_configuration, dict):
            raise TypeError("Expected argument 'resource_log_configuration' to be a dict")
        pulumi.set(__self__, "resource_log_configuration", resource_log_configuration)
        if server_port and not isinstance(server_port, int):
            raise TypeError("Expected argument 'server_port' to be a int")
        pulumi.set(__self__, "server_port", server_port)
        if shared_private_link_resources and not isinstance(shared_private_link_resources, list):
            raise TypeError("Expected argument 'shared_private_link_resources' to be a list")
        pulumi.set(__self__, "shared_private_link_resources", shared_private_link_resources)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tls and not isinstance(tls, dict):
            raise TypeError("Expected argument 'tls' to be a dict")
        pulumi.set(__self__, "tls", tls)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="disableAadAuth")
    def disable_aad_auth(self) -> Optional[bool]:
        """
        DisableLocalAuth
        Enable or disable aad auth
        When set as true, connection with AuthType=aad won't work.
        """
        return pulumi.get(self, "disable_aad_auth")

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[bool]:
        """
        DisableLocalAuth
        Enable or disable local auth with AccessKey
        When set as true, connection with AccessKey=xxx won't work.
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter(name="externalIP")
    def external_ip(self) -> str:
        """
        The publicly accessible IP of the resource.
        """
        return pulumi.get(self, "external_ip")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        """
        FQDN of the service instance.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="hostNamePrefix")
    def host_name_prefix(self) -> str:
        """
        Deprecated.
        """
        return pulumi.get(self, "host_name_prefix")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedIdentityResponse']:
        """
        A class represent managed identities used for request and response
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The kind of the service
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="liveTraceConfiguration")
    def live_trace_configuration(self) -> Optional['outputs.LiveTraceConfigurationResponse']:
        """
        Live trace configuration of a Microsoft.SignalRService resource.
        """
        return pulumi.get(self, "live_trace_configuration")

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
    @pulumi.getter(name="networkACLs")
    def network_acls(self) -> Optional['outputs.WebPubSubNetworkACLsResponse']:
        """
        Network ACLs for the resource
        """
        return pulumi.get(self, "network_acls")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        Private endpoint connections to the resource.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Enable or disable public network access. Default to "Enabled".
        When it's Enabled, network ACLs still apply.
        When it's Disabled, public network access is always disabled no matter what you set in network ACLs.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="publicPort")
    def public_port(self) -> int:
        """
        The publicly accessible port of the resource which is designed for browser/client side usage.
        """
        return pulumi.get(self, "public_port")

    @property
    @pulumi.getter(name="resourceLogConfiguration")
    def resource_log_configuration(self) -> Optional['outputs.ResourceLogConfigurationResponse']:
        """
        Resource log configuration of a Microsoft.SignalRService resource.
        """
        return pulumi.get(self, "resource_log_configuration")

    @property
    @pulumi.getter(name="serverPort")
    def server_port(self) -> int:
        """
        The publicly accessible port of the resource which is designed for customer server side usage.
        """
        return pulumi.get(self, "server_port")

    @property
    @pulumi.getter(name="sharedPrivateLinkResources")
    def shared_private_link_resources(self) -> Sequence['outputs.SharedPrivateLinkResourceResponse']:
        """
        The list of shared private link resources.
        """
        return pulumi.get(self, "shared_private_link_resources")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.ResourceSkuResponse']:
        """
        The billing information of the resource.
        """
        return pulumi.get(self, "sku")

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
    def tls(self) -> Optional['outputs.WebPubSubTlsSettingsResponse']:
        """
        TLS settings for the resource
        """
        return pulumi.get(self, "tls")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of the resource. Probably you need the same or higher version of client SDKs.
        """
        return pulumi.get(self, "version")


class AwaitableGetWebPubSubResult(GetWebPubSubResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebPubSubResult(
            disable_aad_auth=self.disable_aad_auth,
            disable_local_auth=self.disable_local_auth,
            external_ip=self.external_ip,
            host_name=self.host_name,
            host_name_prefix=self.host_name_prefix,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            live_trace_configuration=self.live_trace_configuration,
            location=self.location,
            name=self.name,
            network_acls=self.network_acls,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            public_port=self.public_port,
            resource_log_configuration=self.resource_log_configuration,
            server_port=self.server_port,
            shared_private_link_resources=self.shared_private_link_resources,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            tls=self.tls,
            type=self.type,
            version=self.version)


def get_web_pub_sub(resource_group_name: Optional[str] = None,
                    resource_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebPubSubResult:
    """
    Get the resource and its properties.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:webpubsub/v20230601preview:getWebPubSub', __args__, opts=opts, typ=GetWebPubSubResult).value

    return AwaitableGetWebPubSubResult(
        disable_aad_auth=pulumi.get(__ret__, 'disable_aad_auth'),
        disable_local_auth=pulumi.get(__ret__, 'disable_local_auth'),
        external_ip=pulumi.get(__ret__, 'external_ip'),
        host_name=pulumi.get(__ret__, 'host_name'),
        host_name_prefix=pulumi.get(__ret__, 'host_name_prefix'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        kind=pulumi.get(__ret__, 'kind'),
        live_trace_configuration=pulumi.get(__ret__, 'live_trace_configuration'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_acls=pulumi.get(__ret__, 'network_acls'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        public_port=pulumi.get(__ret__, 'public_port'),
        resource_log_configuration=pulumi.get(__ret__, 'resource_log_configuration'),
        server_port=pulumi.get(__ret__, 'server_port'),
        shared_private_link_resources=pulumi.get(__ret__, 'shared_private_link_resources'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        tls=pulumi.get(__ret__, 'tls'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_web_pub_sub)
def get_web_pub_sub_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                           resource_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebPubSubResult]:
    """
    Get the resource and its properties.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource.
    """
    ...
