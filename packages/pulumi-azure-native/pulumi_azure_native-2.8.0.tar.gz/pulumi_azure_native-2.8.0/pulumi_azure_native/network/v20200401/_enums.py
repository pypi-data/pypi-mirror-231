# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AzureFirewallApplicationRuleProtocolType',
    'AzureFirewallNatRCActionType',
    'AzureFirewallNetworkRuleProtocol',
    'AzureFirewallRCActionType',
    'AzureFirewallSkuName',
    'AzureFirewallSkuTier',
    'AzureFirewallThreatIntelMode',
    'FirewallPolicyFilterRuleActionType',
    'FirewallPolicyNatRuleActionType',
    'FirewallPolicyRuleConditionApplicationProtocolType',
    'FirewallPolicyRuleConditionNetworkProtocol',
    'FirewallPolicyRuleConditionType',
    'FirewallPolicyRuleType',
    'ResourceIdentityType',
]


class AzureFirewallApplicationRuleProtocolType(str, Enum):
    """
    Protocol type.
    """
    HTTP = "Http"
    HTTPS = "Https"
    MSSQL = "Mssql"


class AzureFirewallNatRCActionType(str, Enum):
    """
    The type of action.
    """
    SNAT = "Snat"
    DNAT = "Dnat"


class AzureFirewallNetworkRuleProtocol(str, Enum):
    """
    The protocol of a Network Rule resource.
    """
    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"
    ICMP = "ICMP"


class AzureFirewallRCActionType(str, Enum):
    """
    The type of action.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class AzureFirewallSkuName(str, Enum):
    """
    Name of an Azure Firewall SKU.
    """
    AZF_W_V_NET = "AZFW_VNet"
    AZF_W_HUB = "AZFW_Hub"


class AzureFirewallSkuTier(str, Enum):
    """
    Tier of an Azure Firewall.
    """
    STANDARD = "Standard"
    PREMIUM = "Premium"


class AzureFirewallThreatIntelMode(str, Enum):
    """
    The operation mode for Threat Intelligence.
    """
    ALERT = "Alert"
    DENY = "Deny"
    OFF = "Off"


class FirewallPolicyFilterRuleActionType(str, Enum):
    """
    The type of action.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class FirewallPolicyNatRuleActionType(str, Enum):
    """
    The type of action.
    """
    DNAT = "DNAT"


class FirewallPolicyRuleConditionApplicationProtocolType(str, Enum):
    """
    Protocol type.
    """
    HTTP = "Http"
    HTTPS = "Https"


class FirewallPolicyRuleConditionNetworkProtocol(str, Enum):
    """
    The Network protocol of a Rule condition.
    """
    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"
    ICMP = "ICMP"


class FirewallPolicyRuleConditionType(str, Enum):
    """
    Rule Condition Type.
    """
    APPLICATION_RULE_CONDITION = "ApplicationRuleCondition"
    NETWORK_RULE_CONDITION = "NetworkRuleCondition"
    NAT_RULE_CONDITION = "NatRuleCondition"


class FirewallPolicyRuleType(str, Enum):
    """
    The type of the rule.
    """
    FIREWALL_POLICY_NAT_RULE = "FirewallPolicyNatRule"
    FIREWALL_POLICY_FILTER_RULE = "FirewallPolicyFilterRule"


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the virtual machine.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"
