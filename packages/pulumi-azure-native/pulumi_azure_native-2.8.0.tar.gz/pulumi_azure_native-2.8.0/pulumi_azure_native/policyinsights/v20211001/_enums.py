# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ResourceDiscoveryMode',
]


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
