# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DeploymentMode',
    'ExpressionEvaluationOptionsScopeType',
    'ExtendedLocationType',
    'OnErrorDeploymentType',
    'ResourceIdentityType',
]


class DeploymentMode(str, Enum):
    """
    The mode that is used to deploy resources. This value can be either Incremental or Complete. In Incremental mode, resources are deployed without deleting existing resources that are not included in the template. In Complete mode, resources are deployed and existing resources in the resource group that are not included in the template are deleted. Be careful when using Complete mode as you may unintentionally delete resources.
    """
    INCREMENTAL = "Incremental"
    COMPLETE = "Complete"


class ExpressionEvaluationOptionsScopeType(str, Enum):
    """
    The scope to be used for evaluation of parameters, variables and functions in a nested template.
    """
    NOT_SPECIFIED = "NotSpecified"
    OUTER = "Outer"
    INNER = "Inner"


class ExtendedLocationType(str, Enum):
    """
    The extended location type.
    """
    EDGE_ZONE = "EdgeZone"


class OnErrorDeploymentType(str, Enum):
    """
    The deployment on error behavior type. Possible values are LastSuccessful and SpecificDeployment.
    """
    LAST_SUCCESSFUL = "LastSuccessful"
    SPECIFIC_DEPLOYMENT = "SpecificDeployment"


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"
