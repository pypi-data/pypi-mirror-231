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
    'GetGovernanceRuleResult',
    'AwaitableGetGovernanceRuleResult',
    'get_governance_rule',
    'get_governance_rule_output',
]

@pulumi.output_type
class GetGovernanceRuleResult:
    """
    Governance rule over a given scope
    """
    def __init__(__self__, description=None, display_name=None, excluded_scopes=None, governance_email_notification=None, id=None, include_member_scopes=None, is_disabled=None, is_grace_period=None, metadata=None, name=None, owner_source=None, remediation_timeframe=None, rule_priority=None, rule_type=None, source_resource_type=None, tenant_id=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if excluded_scopes and not isinstance(excluded_scopes, list):
            raise TypeError("Expected argument 'excluded_scopes' to be a list")
        pulumi.set(__self__, "excluded_scopes", excluded_scopes)
        if governance_email_notification and not isinstance(governance_email_notification, dict):
            raise TypeError("Expected argument 'governance_email_notification' to be a dict")
        pulumi.set(__self__, "governance_email_notification", governance_email_notification)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_member_scopes and not isinstance(include_member_scopes, bool):
            raise TypeError("Expected argument 'include_member_scopes' to be a bool")
        pulumi.set(__self__, "include_member_scopes", include_member_scopes)
        if is_disabled and not isinstance(is_disabled, bool):
            raise TypeError("Expected argument 'is_disabled' to be a bool")
        pulumi.set(__self__, "is_disabled", is_disabled)
        if is_grace_period and not isinstance(is_grace_period, bool):
            raise TypeError("Expected argument 'is_grace_period' to be a bool")
        pulumi.set(__self__, "is_grace_period", is_grace_period)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner_source and not isinstance(owner_source, dict):
            raise TypeError("Expected argument 'owner_source' to be a dict")
        pulumi.set(__self__, "owner_source", owner_source)
        if remediation_timeframe and not isinstance(remediation_timeframe, str):
            raise TypeError("Expected argument 'remediation_timeframe' to be a str")
        pulumi.set(__self__, "remediation_timeframe", remediation_timeframe)
        if rule_priority and not isinstance(rule_priority, int):
            raise TypeError("Expected argument 'rule_priority' to be a int")
        pulumi.set(__self__, "rule_priority", rule_priority)
        if rule_type and not isinstance(rule_type, str):
            raise TypeError("Expected argument 'rule_type' to be a str")
        pulumi.set(__self__, "rule_type", rule_type)
        if source_resource_type and not isinstance(source_resource_type, str):
            raise TypeError("Expected argument 'source_resource_type' to be a str")
        pulumi.set(__self__, "source_resource_type", source_resource_type)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the governance rule
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name of the governance rule
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="excludedScopes")
    def excluded_scopes(self) -> Optional[Sequence[str]]:
        """
        Excluded scopes, filter out the descendants of the scope (on management scopes)
        """
        return pulumi.get(self, "excluded_scopes")

    @property
    @pulumi.getter(name="governanceEmailNotification")
    def governance_email_notification(self) -> Optional['outputs.GovernanceRuleEmailNotificationResponse']:
        """
        The email notifications settings for the governance rule, states whether to disable notifications for mangers and owners
        """
        return pulumi.get(self, "governance_email_notification")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includeMemberScopes")
    def include_member_scopes(self) -> Optional[bool]:
        """
        Defines whether the rule is management scope rule (master connector as a single scope or management scope)
        """
        return pulumi.get(self, "include_member_scopes")

    @property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[bool]:
        """
        Defines whether the rule is active/inactive
        """
        return pulumi.get(self, "is_disabled")

    @property
    @pulumi.getter(name="isGracePeriod")
    def is_grace_period(self) -> Optional[bool]:
        """
        Defines whether there is a grace period on the governance rule
        """
        return pulumi.get(self, "is_grace_period")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['outputs.GovernanceRuleMetadataResponse']:
        """
        The governance rule metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerSource")
    def owner_source(self) -> 'outputs.GovernanceRuleOwnerSourceResponse':
        """
        The owner source for the governance rule - e.g. Manually by user@contoso.com - see example
        """
        return pulumi.get(self, "owner_source")

    @property
    @pulumi.getter(name="remediationTimeframe")
    def remediation_timeframe(self) -> Optional[str]:
        """
        Governance rule remediation timeframe - this is the time that will affect on the grace-period duration e.g. 7.00:00:00 - means 7 days
        """
        return pulumi.get(self, "remediation_timeframe")

    @property
    @pulumi.getter(name="rulePriority")
    def rule_priority(self) -> int:
        """
        The governance rule priority, priority to the lower number. Rules with the same priority on the same scope will not be allowed
        """
        return pulumi.get(self, "rule_priority")

    @property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> str:
        """
        The rule type of the governance rule, defines the source of the rule e.g. Integrated
        """
        return pulumi.get(self, "rule_type")

    @property
    @pulumi.getter(name="sourceResourceType")
    def source_resource_type(self) -> str:
        """
        The governance rule source, what the rule affects, e.g. Assessments
        """
        return pulumi.get(self, "source_resource_type")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenantId (GUID)
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetGovernanceRuleResult(GetGovernanceRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGovernanceRuleResult(
            description=self.description,
            display_name=self.display_name,
            excluded_scopes=self.excluded_scopes,
            governance_email_notification=self.governance_email_notification,
            id=self.id,
            include_member_scopes=self.include_member_scopes,
            is_disabled=self.is_disabled,
            is_grace_period=self.is_grace_period,
            metadata=self.metadata,
            name=self.name,
            owner_source=self.owner_source,
            remediation_timeframe=self.remediation_timeframe,
            rule_priority=self.rule_priority,
            rule_type=self.rule_type,
            source_resource_type=self.source_resource_type,
            tenant_id=self.tenant_id,
            type=self.type)


def get_governance_rule(rule_id: Optional[str] = None,
                        scope: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGovernanceRuleResult:
    """
    Get a specific governance rule for the requested scope by ruleId


    :param str rule_id: The governance rule key - unique key for the standard governance rule (GUID)
    :param str scope: The scope of the Governance rules. Valid scopes are: management group (format: 'providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: 'subscriptions/{subscriptionId}'), or security connector (format: 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'
    """
    __args__ = dict()
    __args__['ruleId'] = rule_id
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security/v20220101preview:getGovernanceRule', __args__, opts=opts, typ=GetGovernanceRuleResult).value

    return AwaitableGetGovernanceRuleResult(
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        excluded_scopes=pulumi.get(__ret__, 'excluded_scopes'),
        governance_email_notification=pulumi.get(__ret__, 'governance_email_notification'),
        id=pulumi.get(__ret__, 'id'),
        include_member_scopes=pulumi.get(__ret__, 'include_member_scopes'),
        is_disabled=pulumi.get(__ret__, 'is_disabled'),
        is_grace_period=pulumi.get(__ret__, 'is_grace_period'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        owner_source=pulumi.get(__ret__, 'owner_source'),
        remediation_timeframe=pulumi.get(__ret__, 'remediation_timeframe'),
        rule_priority=pulumi.get(__ret__, 'rule_priority'),
        rule_type=pulumi.get(__ret__, 'rule_type'),
        source_resource_type=pulumi.get(__ret__, 'source_resource_type'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_governance_rule)
def get_governance_rule_output(rule_id: Optional[pulumi.Input[str]] = None,
                               scope: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGovernanceRuleResult]:
    """
    Get a specific governance rule for the requested scope by ruleId


    :param str rule_id: The governance rule key - unique key for the standard governance rule (GUID)
    :param str scope: The scope of the Governance rules. Valid scopes are: management group (format: 'providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: 'subscriptions/{subscriptionId}'), or security connector (format: 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'
    """
    ...
