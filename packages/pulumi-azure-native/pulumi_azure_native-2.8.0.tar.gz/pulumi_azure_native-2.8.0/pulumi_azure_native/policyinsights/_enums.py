# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ComplianceState',
    'ResourceDiscoveryMode',
]


class ComplianceState(str, Enum):
    """
    The compliance state that should be set on the resource.
    """
    COMPLIANT = "Compliant"
    """
    The resource is in compliance with the policy.
    """
    NON_COMPLIANT = "NonCompliant"
    """
    The resource is not in compliance with the policy.
    """
    UNKNOWN = "Unknown"
    """
    The compliance state of the resource is not known.
    """


class ResourceDiscoveryMode(str, Enum):
    """
    The way resources to remediate are discovered. Defaults to ExistingNonCompliant if not specified.
    """
    EXISTING_NON_COMPLIANT = "ExistingNonCompliant"
    """
    Remediate resources that are already known to be non-compliant.
    """
    RE_EVALUATE_COMPLIANCE = "ReEvaluateCompliance"
    """
    Re-evaluate the compliance state of resources and then remediate the resources found to be non-compliant.
    """
