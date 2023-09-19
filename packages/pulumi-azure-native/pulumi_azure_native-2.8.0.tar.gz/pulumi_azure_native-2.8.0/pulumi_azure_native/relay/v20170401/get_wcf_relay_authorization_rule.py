# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetWCFRelayAuthorizationRuleResult',
    'AwaitableGetWCFRelayAuthorizationRuleResult',
    'get_wcf_relay_authorization_rule',
    'get_wcf_relay_authorization_rule_output',
]

@pulumi.output_type
class GetWCFRelayAuthorizationRuleResult:
    """
    Description of a namespace authorization rule.
    """
    def __init__(__self__, id=None, name=None, rights=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if rights and not isinstance(rights, list):
            raise TypeError("Expected argument 'rights' to be a list")
        pulumi.set(__self__, "rights", rights)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rights(self) -> Sequence[str]:
        """
        The rights associated with the rule.
        """
        return pulumi.get(self, "rights")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetWCFRelayAuthorizationRuleResult(GetWCFRelayAuthorizationRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWCFRelayAuthorizationRuleResult(
            id=self.id,
            name=self.name,
            rights=self.rights,
            type=self.type)


def get_wcf_relay_authorization_rule(authorization_rule_name: Optional[str] = None,
                                     namespace_name: Optional[str] = None,
                                     relay_name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWCFRelayAuthorizationRuleResult:
    """
    Get authorizationRule for a WCF relay by name.


    :param str authorization_rule_name: The authorization rule name.
    :param str namespace_name: The namespace name
    :param str relay_name: The relay name.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['authorizationRuleName'] = authorization_rule_name
    __args__['namespaceName'] = namespace_name
    __args__['relayName'] = relay_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:relay/v20170401:getWCFRelayAuthorizationRule', __args__, opts=opts, typ=GetWCFRelayAuthorizationRuleResult).value

    return AwaitableGetWCFRelayAuthorizationRuleResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        rights=pulumi.get(__ret__, 'rights'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_wcf_relay_authorization_rule)
def get_wcf_relay_authorization_rule_output(authorization_rule_name: Optional[pulumi.Input[str]] = None,
                                            namespace_name: Optional[pulumi.Input[str]] = None,
                                            relay_name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWCFRelayAuthorizationRuleResult]:
    """
    Get authorizationRule for a WCF relay by name.


    :param str authorization_rule_name: The authorization rule name.
    :param str namespace_name: The namespace name
    :param str relay_name: The relay name.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...
