# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ActiveDirectoryAuthEnum',
    'ArmServerKeyType',
    'CancelEnum',
    'CreateMode',
    'GeoRedundantBackupEnum',
    'HighAvailabilityMode',
    'IdentityType',
    'LogicalReplicationOnSourceDbEnum',
    'MigrationMode',
    'OverwriteDbsInTargetEnum',
    'PasswordAuthEnum',
    'PrincipalType',
    'PrivateEndpointServiceConnectionStatus',
    'ReplicationRole',
    'ServerVersion',
    'SkuTier',
    'StartDataMigrationEnum',
    'TriggerCutoverEnum',
]


class ActiveDirectoryAuthEnum(str, Enum):
    """
    If Enabled, Azure Active Directory authentication is enabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ArmServerKeyType(str, Enum):
    """
    Data encryption type to depict if it is System Managed vs Azure Key vault.
    """
    SYSTEM_MANAGED = "SystemManaged"
    AZURE_KEY_VAULT = "AzureKeyVault"


class CancelEnum(str, Enum):
    """
    To trigger cancel for entire migration we need to send this flag as True
    """
    TRUE = "True"
    FALSE = "False"


class CreateMode(str, Enum):
    """
    The mode to create a new PostgreSQL server.
    """
    DEFAULT = "Default"
    CREATE = "Create"
    UPDATE = "Update"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    GEO_RESTORE = "GeoRestore"
    REPLICA = "Replica"


class GeoRedundantBackupEnum(str, Enum):
    """
    A value indicating whether Geo-Redundant backup is enabled on the server.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class HighAvailabilityMode(str, Enum):
    """
    The HA mode for the server.
    """
    DISABLED = "Disabled"
    ZONE_REDUNDANT = "ZoneRedundant"
    SAME_ZONE = "SameZone"


class IdentityType(str, Enum):
    """
    the types of identities associated with this resource; currently restricted to 'None and UserAssigned'
    """
    NONE = "None"
    USER_ASSIGNED = "UserAssigned"


class LogicalReplicationOnSourceDbEnum(str, Enum):
    """
    Indicates whether to setup LogicalReplicationOnSourceDb, if needed
    """
    TRUE = "True"
    FALSE = "False"


class MigrationMode(str, Enum):
    """
    There are two types of migration modes Online and Offline
    """
    OFFLINE = "Offline"
    ONLINE = "Online"


class OverwriteDbsInTargetEnum(str, Enum):
    """
    Indicates whether the databases on the target server can be overwritten, if already present. If set to False, the migration workflow will wait for a confirmation, if it detects that the database already exists.
    """
    TRUE = "True"
    FALSE = "False"


class PasswordAuthEnum(str, Enum):
    """
    If Enabled, Password authentication is enabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class PrincipalType(str, Enum):
    """
    The principal type used to represent the type of Active Directory Administrator.
    """
    UNKNOWN = "Unknown"
    USER = "User"
    GROUP = "Group"
    SERVICE_PRINCIPAL = "ServicePrincipal"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class ReplicationRole(str, Enum):
    """
    Replication role of the server
    """
    NONE = "None"
    PRIMARY = "Primary"
    ASYNC_REPLICA = "AsyncReplica"
    GEO_ASYNC_REPLICA = "GeoAsyncReplica"


class ServerVersion(str, Enum):
    """
    PostgreSQL Server version.
    """
    SERVER_VERSION_14 = "14"
    SERVER_VERSION_13 = "13"
    SERVER_VERSION_12 = "12"
    SERVER_VERSION_11 = "11"


class SkuTier(str, Enum):
    """
    The tier of the particular SKU, e.g. Burstable.
    """
    BURSTABLE = "Burstable"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"


class StartDataMigrationEnum(str, Enum):
    """
    Indicates whether the data migration should start right away
    """
    TRUE = "True"
    FALSE = "False"


class TriggerCutoverEnum(str, Enum):
    """
    To trigger cutover for entire migration we need to send this flag as True
    """
    TRUE = "True"
    FALSE = "False"
