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
    'GetNetworkSecurityGroupResult',
    'AwaitableGetNetworkSecurityGroupResult',
    'get_network_security_group',
    'get_network_security_group_output',
]

@pulumi.output_type
class GetNetworkSecurityGroupResult:
    """
    NetworkSecurityGroup resource.
    """
    def __init__(__self__, default_security_rules=None, etag=None, flow_logs=None, flush_connection=None, id=None, location=None, name=None, network_interfaces=None, provisioning_state=None, resource_guid=None, security_rules=None, subnets=None, tags=None, type=None):
        if default_security_rules and not isinstance(default_security_rules, list):
            raise TypeError("Expected argument 'default_security_rules' to be a list")
        pulumi.set(__self__, "default_security_rules", default_security_rules)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if flow_logs and not isinstance(flow_logs, list):
            raise TypeError("Expected argument 'flow_logs' to be a list")
        pulumi.set(__self__, "flow_logs", flow_logs)
        if flush_connection and not isinstance(flush_connection, bool):
            raise TypeError("Expected argument 'flush_connection' to be a bool")
        pulumi.set(__self__, "flush_connection", flush_connection)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_interfaces and not isinstance(network_interfaces, list):
            raise TypeError("Expected argument 'network_interfaces' to be a list")
        pulumi.set(__self__, "network_interfaces", network_interfaces)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if security_rules and not isinstance(security_rules, list):
            raise TypeError("Expected argument 'security_rules' to be a list")
        pulumi.set(__self__, "security_rules", security_rules)
        if subnets and not isinstance(subnets, list):
            raise TypeError("Expected argument 'subnets' to be a list")
        pulumi.set(__self__, "subnets", subnets)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="defaultSecurityRules")
    def default_security_rules(self) -> Sequence['outputs.SecurityRuleResponse']:
        """
        The default security rules of network security group.
        """
        return pulumi.get(self, "default_security_rules")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="flowLogs")
    def flow_logs(self) -> Sequence['outputs.FlowLogResponse']:
        """
        A collection of references to flow log resources.
        """
        return pulumi.get(self, "flow_logs")

    @property
    @pulumi.getter(name="flushConnection")
    def flush_connection(self) -> Optional[bool]:
        """
        When enabled, flows created from Network Security Group connections will be re-evaluated when rules are updates. Initial enablement will trigger re-evaluation.
        """
        return pulumi.get(self, "flush_connection")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
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
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence['outputs.NetworkInterfaceResponse']:
        """
        A collection of references to network interfaces.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the network security group resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> str:
        """
        The resource GUID property of the network security group resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="securityRules")
    def security_rules(self) -> Optional[Sequence['outputs.SecurityRuleResponse']]:
        """
        A collection of security rules of the network security group.
        """
        return pulumi.get(self, "security_rules")

    @property
    @pulumi.getter
    def subnets(self) -> Sequence['outputs.SubnetResponse']:
        """
        A collection of references to subnets.
        """
        return pulumi.get(self, "subnets")

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


class AwaitableGetNetworkSecurityGroupResult(GetNetworkSecurityGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkSecurityGroupResult(
            default_security_rules=self.default_security_rules,
            etag=self.etag,
            flow_logs=self.flow_logs,
            flush_connection=self.flush_connection,
            id=self.id,
            location=self.location,
            name=self.name,
            network_interfaces=self.network_interfaces,
            provisioning_state=self.provisioning_state,
            resource_guid=self.resource_guid,
            security_rules=self.security_rules,
            subnets=self.subnets,
            tags=self.tags,
            type=self.type)


def get_network_security_group(expand: Optional[str] = None,
                               network_security_group_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkSecurityGroupResult:
    """
    Gets the specified network security group.


    :param str expand: Expands referenced resources.
    :param str network_security_group_name: The name of the network security group.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['networkSecurityGroupName'] = network_security_group_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230501:getNetworkSecurityGroup', __args__, opts=opts, typ=GetNetworkSecurityGroupResult).value

    return AwaitableGetNetworkSecurityGroupResult(
        default_security_rules=pulumi.get(__ret__, 'default_security_rules'),
        etag=pulumi.get(__ret__, 'etag'),
        flow_logs=pulumi.get(__ret__, 'flow_logs'),
        flush_connection=pulumi.get(__ret__, 'flush_connection'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_interfaces=pulumi.get(__ret__, 'network_interfaces'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_guid=pulumi.get(__ret__, 'resource_guid'),
        security_rules=pulumi.get(__ret__, 'security_rules'),
        subnets=pulumi.get(__ret__, 'subnets'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_network_security_group)
def get_network_security_group_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                                      network_security_group_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkSecurityGroupResult]:
    """
    Gets the specified network security group.


    :param str expand: Expands referenced resources.
    :param str network_security_group_name: The name of the network security group.
    :param str resource_group_name: The name of the resource group.
    """
    ...
