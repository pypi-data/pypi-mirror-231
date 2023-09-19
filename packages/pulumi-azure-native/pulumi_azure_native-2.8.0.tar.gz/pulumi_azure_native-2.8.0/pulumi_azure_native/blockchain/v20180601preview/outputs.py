# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'ApiKeyResponse',
    'BlockchainMemberNodesSkuResponse',
    'ConsortiumResponse',
    'FirewallRuleResponse',
    'SkuResponse',
]

@pulumi.output_type
class ApiKeyResponse(dict):
    """
    API key payload which is exposed in the request/response of the resource provider.
    """
    def __init__(__self__, *,
                 key_name: Optional[str] = None,
                 value: Optional[str] = None):
        """
        API key payload which is exposed in the request/response of the resource provider.
        :param str key_name: Gets or sets the API key name.
        :param str value: Gets or sets the API key value.
        """
        if key_name is not None:
            pulumi.set(__self__, "key_name", key_name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[str]:
        """
        Gets or sets the API key name.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Gets or sets the API key value.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class BlockchainMemberNodesSkuResponse(dict):
    """
    Payload of the blockchain member nodes Sku for a blockchain member.
    """
    def __init__(__self__, *,
                 capacity: Optional[int] = None):
        """
        Payload of the blockchain member nodes Sku for a blockchain member.
        :param int capacity: Gets or sets the nodes capacity.
        """
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        Gets or sets the nodes capacity.
        """
        return pulumi.get(self, "capacity")


@pulumi.output_type
class ConsortiumResponse(dict):
    """
    Consortium payload
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 protocol: Optional[str] = None):
        """
        Consortium payload
        :param str name: Gets or sets the blockchain member name.
        :param str protocol: Gets or sets the protocol for the consortium.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Gets or sets the blockchain member name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        """
        Gets or sets the protocol for the consortium.
        """
        return pulumi.get(self, "protocol")


@pulumi.output_type
class FirewallRuleResponse(dict):
    """
    Ip range for firewall rules
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endIpAddress":
            suggest = "end_ip_address"
        elif key == "ruleName":
            suggest = "rule_name"
        elif key == "startIpAddress":
            suggest = "start_ip_address"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FirewallRuleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FirewallRuleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FirewallRuleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 end_ip_address: Optional[str] = None,
                 rule_name: Optional[str] = None,
                 start_ip_address: Optional[str] = None):
        """
        Ip range for firewall rules
        :param str end_ip_address: Gets or sets the end IP address of the firewall rule range.
        :param str rule_name: Gets or sets the name of the firewall rules.
        :param str start_ip_address: Gets or sets the start IP address of the firewall rule range.
        """
        if end_ip_address is not None:
            pulumi.set(__self__, "end_ip_address", end_ip_address)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)
        if start_ip_address is not None:
            pulumi.set(__self__, "start_ip_address", start_ip_address)

    @property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> Optional[str]:
        """
        Gets or sets the end IP address of the firewall rule range.
        """
        return pulumi.get(self, "end_ip_address")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[str]:
        """
        Gets or sets the name of the firewall rules.
        """
        return pulumi.get(self, "rule_name")

    @property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> Optional[str]:
        """
        Gets or sets the start IP address of the firewall rule range.
        """
        return pulumi.get(self, "start_ip_address")


@pulumi.output_type
class SkuResponse(dict):
    """
    Blockchain member Sku in payload
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 tier: Optional[str] = None):
        """
        Blockchain member Sku in payload
        :param str name: Gets or sets Sku name
        :param str tier: Gets or sets Sku tier
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Gets or sets Sku name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        Gets or sets Sku tier
        """
        return pulumi.get(self, "tier")


