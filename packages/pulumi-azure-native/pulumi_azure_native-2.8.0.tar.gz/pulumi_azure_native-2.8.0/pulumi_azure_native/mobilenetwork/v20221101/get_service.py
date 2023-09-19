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
    Service resource. Must be created in the same location as its parent mobile network.
    """
    def __init__(__self__, id=None, location=None, name=None, pcc_rules=None, provisioning_state=None, service_precedence=None, service_qos_policy=None, system_data=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pcc_rules and not isinstance(pcc_rules, list):
            raise TypeError("Expected argument 'pcc_rules' to be a list")
        pulumi.set(__self__, "pcc_rules", pcc_rules)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_precedence and not isinstance(service_precedence, int):
            raise TypeError("Expected argument 'service_precedence' to be a int")
        pulumi.set(__self__, "service_precedence", service_precedence)
        if service_qos_policy and not isinstance(service_qos_policy, dict):
            raise TypeError("Expected argument 'service_qos_policy' to be a dict")
        pulumi.set(__self__, "service_qos_policy", service_qos_policy)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

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
    @pulumi.getter(name="pccRules")
    def pcc_rules(self) -> Sequence['outputs.PccRuleConfigurationResponse']:
        """
        The set of data flow policy rules that make up this service.
        """
        return pulumi.get(self, "pcc_rules")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the service resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="servicePrecedence")
    def service_precedence(self) -> int:
        """
        A precedence value that is used to decide between services when identifying the QoS values to use for a particular SIM. A lower value means a higher priority. This value should be unique among all services configured in the mobile network.
        """
        return pulumi.get(self, "service_precedence")

    @property
    @pulumi.getter(name="serviceQosPolicy")
    def service_qos_policy(self) -> Optional['outputs.QosPolicyResponse']:
        """
        The QoS policy to use for packets matching this service. This can be overridden for particular flows using the ruleQosPolicy field in a PccRuleConfiguration. If this field is null then the UE's SIM policy will define the QoS settings.
        """
        return pulumi.get(self, "service_qos_policy")

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
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            id=self.id,
            location=self.location,
            name=self.name,
            pcc_rules=self.pcc_rules,
            provisioning_state=self.provisioning_state,
            service_precedence=self.service_precedence,
            service_qos_policy=self.service_qos_policy,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_service(mobile_network_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                service_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    Gets information about the specified service.


    :param str mobile_network_name: The name of the mobile network.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the service. You must not use any of the following reserved strings - `default`, `requested` or `service`
    """
    __args__ = dict()
    __args__['mobileNetworkName'] = mobile_network_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:mobilenetwork/v20221101:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        pcc_rules=pulumi.get(__ret__, 'pcc_rules'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        service_precedence=pulumi.get(__ret__, 'service_precedence'),
        service_qos_policy=pulumi.get(__ret__, 'service_qos_policy'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_service)
def get_service_output(mobile_network_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       service_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceResult]:
    """
    Gets information about the specified service.


    :param str mobile_network_name: The name of the mobile network.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the service. You must not use any of the following reserved strings - `default`, `requested` or `service`
    """
    ...
