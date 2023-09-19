# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AssignmentScopeValidation',
    'ExemptionCategory',
    'SelectorKind',
]


class AssignmentScopeValidation(str, Enum):
    """
    The option whether validate the exemption is at or under the assignment scope.
    """
    DEFAULT = "Default"
    """
    This option will validate the exemption is at or under the assignment scope.
    """
    DO_NOT_VALIDATE = "DoNotValidate"
    """
    This option will bypass the validation the exemption scope is at or under the policy assignment scope.
    """


class ExemptionCategory(str, Enum):
    """
    The policy exemption category. Possible values are Waiver and Mitigated.
    """
    WAIVER = "Waiver"
    """
    This category of exemptions usually means the scope is not applicable for the policy.
    """
    MITIGATED = "Mitigated"
    """
    This category of exemptions usually means the mitigation actions have been applied to the scope.
    """


class SelectorKind(str, Enum):
    """
    The selector kind.
    """
    RESOURCE_LOCATION = "resourceLocation"
    """
    The selector kind to filter policies by the resource location.
    """
    RESOURCE_TYPE = "resourceType"
    """
    The selector kind to filter policies by the resource type.
    """
    RESOURCE_WITHOUT_LOCATION = "resourceWithoutLocation"
    """
    The selector kind to filter policies by the resource without location.
    """
    POLICY_DEFINITION_REFERENCE_ID = "policyDefinitionReferenceId"
    """
    The selector kind to filter policies by the policy definition reference ID.
    """
