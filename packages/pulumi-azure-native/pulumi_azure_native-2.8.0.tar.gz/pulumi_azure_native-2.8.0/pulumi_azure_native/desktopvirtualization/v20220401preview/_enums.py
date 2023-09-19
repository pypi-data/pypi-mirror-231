# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApplicationGroupType',
    'DayOfWeek',
    'HostPoolType',
    'HostpoolPublicNetworkAccess',
    'LoadBalancerType',
    'Operation',
    'PersonalDesktopAssignmentType',
    'PreferredAppGroupType',
    'RegistrationTokenOperation',
    'ResourceIdentityType',
    'SSOSecretType',
    'SessionHostComponentUpdateType',
    'SkuTier',
]


class ApplicationGroupType(str, Enum):
    """
    Resource Type of ApplicationGroup.
    """
    REMOTE_APP = "RemoteApp"
    DESKTOP = "Desktop"


class DayOfWeek(str, Enum):
    """
    Day of the week.
    """
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class HostPoolType(str, Enum):
    """
    HostPool type for desktop.
    """
    PERSONAL = "Personal"
    """
    Users will be assigned a SessionHost either by administrators (PersonalDesktopAssignmentType = Direct) or upon connecting to the pool (PersonalDesktopAssignmentType = Automatic). They will always be redirected to their assigned SessionHost.
    """
    POOLED = "Pooled"
    """
    Users get a new (random) SessionHost every time it connects to the HostPool.
    """
    BYO_DESKTOP = "BYODesktop"
    """
    Users assign their own machines, load balancing logic remains the same as Personal. PersonalDesktopAssignmentType must be Direct.
    """


class HostpoolPublicNetworkAccess(str, Enum):
    """
    Enabled allows this resource to be accessed from both public and private networks, Disabled allows this resource to only be accessed via private endpoints
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    ENABLED_FOR_SESSION_HOSTS_ONLY = "EnabledForSessionHostsOnly"
    ENABLED_FOR_CLIENTS_ONLY = "EnabledForClientsOnly"


class LoadBalancerType(str, Enum):
    """
    The type of the load balancer.
    """
    BREADTH_FIRST = "BreadthFirst"
    DEPTH_FIRST = "DepthFirst"
    PERSISTENT = "Persistent"


class Operation(str, Enum):
    """
    The type of operation for migration.
    """
    START = "Start"
    """
    Start the migration.
    """
    REVOKE = "Revoke"
    """
    Revoke the migration.
    """
    COMPLETE = "Complete"
    """
    Complete the migration.
    """
    HIDE = "Hide"
    """
    Hide the hostpool.
    """
    UNHIDE = "Unhide"
    """
    Unhide the hostpool.
    """


class PersonalDesktopAssignmentType(str, Enum):
    """
    PersonalDesktopAssignment type for HostPool.
    """
    AUTOMATIC = "Automatic"
    DIRECT = "Direct"


class PreferredAppGroupType(str, Enum):
    """
    The type of preferred application group type, default to Desktop Application Group
    """
    NONE = "None"
    DESKTOP = "Desktop"
    RAIL_APPLICATIONS = "RailApplications"


class RegistrationTokenOperation(str, Enum):
    """
    The type of resetting the token.
    """
    DELETE = "Delete"
    NONE = "None"
    UPDATE = "Update"


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"


class SSOSecretType(str, Enum):
    """
    The type of single sign on Secret Type.
    """
    SHARED_KEY = "SharedKey"
    CERTIFICATE = "Certificate"
    SHARED_KEY_IN_KEY_VAULT = "SharedKeyInKeyVault"
    CERTIFICATE_IN_KEY_VAULT = "CertificateInKeyVault"


class SessionHostComponentUpdateType(str, Enum):
    """
    The type of maintenance for session host components.
    """
    DEFAULT = "Default"
    """
    Agent and other agent side components are delivery schedule is controlled by WVD Infra.
    """
    SCHEDULED = "Scheduled"
    """
    TenantAdmin have opted in for Scheduled Component Update feature.
    """


class SkuTier(str, Enum):
    """
    This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
    """
    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
