# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AdministratorType',
    'AutoExecuteStatus',
    'BackupStorageRedundancy',
    'BlobAuditingPolicyState',
    'CatalogCollationType',
    'CreateMode',
    'DataMaskingState',
    'DatabaseIdentityType',
    'DatabaseLicenseType',
    'DatabaseReadScale',
    'DayOfWeek',
    'ElasticPoolLicenseType',
    'GeoBackupPolicyState',
    'IdentityType',
    'InstancePoolLicenseType',
    'JobScheduleType',
    'JobStepActionSource',
    'JobStepActionType',
    'JobStepOutputType',
    'JobTargetGroupMembershipType',
    'JobTargetType',
    'ManagedDatabaseCreateMode',
    'ManagedInstanceAdministratorType',
    'ManagedInstanceLicenseType',
    'ManagedInstanceProxyOverride',
    'ManagedServerCreateMode',
    'PrincipalType',
    'PrivateLinkServiceConnectionStateStatus',
    'ReadOnlyEndpointFailoverPolicy',
    'ReadWriteEndpointFailoverPolicy',
    'ReplicationMode',
    'SampleName',
    'SecondaryType',
    'SecurityAlertPolicyEmailAccountAdmins',
    'SecurityAlertPolicyState',
    'SecurityAlertPolicyUseServerDefault',
    'SecurityAlertsPolicyState',
    'SensitivityLabelRank',
    'ServerKeyType',
    'ServerNetworkAccessFlag',
    'ServicePrincipalType',
    'SqlVulnerabilityAssessmentState',
    'SyncConflictResolutionPolicy',
    'SyncDirection',
    'SyncMemberDbType',
    'TransparentDataEncryptionState',
]


class AdministratorType(str, Enum):
    """
    Type of the sever administrator.
    """
    ACTIVE_DIRECTORY = "ActiveDirectory"


class AutoExecuteStatus(str, Enum):
    """
    Gets the auto-execute status (whether to let the system execute the recommendations) of this advisor. Possible values are 'Enabled' and 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    DEFAULT = "Default"


class BackupStorageRedundancy(str, Enum):
    """
    The storage account type to be used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage)
    """
    GEO = "Geo"
    LOCAL = "Local"
    ZONE = "Zone"
    GEO_ZONE = "GeoZone"


class BlobAuditingPolicyState(str, Enum):
    """
    Specifies the state of the audit. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class CatalogCollationType(str, Enum):
    """
    Collation of the metadata catalog.
    """
    DATABAS_E_DEFAULT = "DATABASE_DEFAULT"
    SQ_L_LATIN1_GENERAL_CP1_C_I_AS = "SQL_Latin1_General_CP1_CI_AS"


class CreateMode(str, Enum):
    """
    Specifies the mode of database creation.
    
    Default: regular database creation.
    
    Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.
    
    Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.
    
    PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.
    
    Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.
    
    Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.
    
    RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.
    
    Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition.
    """
    DEFAULT = "Default"
    COPY = "Copy"
    SECONDARY = "Secondary"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    RESTORE = "Restore"
    RECOVERY = "Recovery"
    RESTORE_EXTERNAL_BACKUP = "RestoreExternalBackup"
    RESTORE_EXTERNAL_BACKUP_SECONDARY = "RestoreExternalBackupSecondary"
    RESTORE_LONG_TERM_RETENTION_BACKUP = "RestoreLongTermRetentionBackup"
    ONLINE_SECONDARY = "OnlineSecondary"


class DataMaskingState(str, Enum):
    """
    The state of the data masking policy.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class DatabaseIdentityType(str, Enum):
    """
    The identity type
    """
    NONE = "None"
    USER_ASSIGNED = "UserAssigned"


class DatabaseLicenseType(str, Enum):
    """
    The license type to apply for this database. `LicenseIncluded` if you need a license, or `BasePrice` if you have a license and are eligible for the Azure Hybrid Benefit.
    """
    LICENSE_INCLUDED = "LicenseIncluded"
    BASE_PRICE = "BasePrice"


class DatabaseReadScale(str, Enum):
    """
    The state of read-only routing. If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica in the same region. Not applicable to a Hyperscale database within an elastic pool.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class DayOfWeek(str, Enum):
    """
    Stop day.
    """
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class ElasticPoolLicenseType(str, Enum):
    """
    The license type to apply for this elastic pool.
    """
    LICENSE_INCLUDED = "LicenseIncluded"
    BASE_PRICE = "BasePrice"


class GeoBackupPolicyState(str, Enum):
    """
    The state of the geo backup policy.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class IdentityType(str, Enum):
    """
    The identity type. Set this to 'SystemAssigned' in order to automatically create and assign an Azure Active Directory principal for the resource.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class InstancePoolLicenseType(str, Enum):
    """
    The license type. Possible values are 'LicenseIncluded' (price for SQL license is included) and 'BasePrice' (without SQL license price).
    """
    LICENSE_INCLUDED = "LicenseIncluded"
    BASE_PRICE = "BasePrice"


class JobScheduleType(str, Enum):
    """
    Schedule interval type
    """
    ONCE = "Once"
    RECURRING = "Recurring"


class JobStepActionSource(str, Enum):
    """
    The source of the action to execute.
    """
    INLINE = "Inline"


class JobStepActionType(str, Enum):
    """
    Type of action being executed by the job step.
    """
    T_SQL = "TSql"


class JobStepOutputType(str, Enum):
    """
    The output destination type.
    """
    SQL_DATABASE = "SqlDatabase"


class JobTargetGroupMembershipType(str, Enum):
    """
    Whether the target is included or excluded from the group.
    """
    INCLUDE = "Include"
    EXCLUDE = "Exclude"


class JobTargetType(str, Enum):
    """
    The target type.
    """
    TARGET_GROUP = "TargetGroup"
    SQL_DATABASE = "SqlDatabase"
    SQL_ELASTIC_POOL = "SqlElasticPool"
    SQL_SHARD_MAP = "SqlShardMap"
    SQL_SERVER = "SqlServer"


class ManagedDatabaseCreateMode(str, Enum):
    """
    Managed database create mode. PointInTimeRestore: Create a database by restoring a point in time backup of an existing database. SourceDatabaseName, SourceManagedInstanceName and PointInTime must be specified. RestoreExternalBackup: Create a database by restoring from external backup files. Collation, StorageContainerUri and StorageContainerSasToken must be specified. Recovery: Creates a database by restoring a geo-replicated backup. RecoverableDatabaseId must be specified as the recoverable database resource ID to restore. RestoreLongTermRetentionBackup: Create a database by restoring from a long term retention backup (longTermRetentionBackupResourceId required).
    """
    DEFAULT = "Default"
    RESTORE_EXTERNAL_BACKUP = "RestoreExternalBackup"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    RECOVERY = "Recovery"
    RESTORE_LONG_TERM_RETENTION_BACKUP = "RestoreLongTermRetentionBackup"


class ManagedInstanceAdministratorType(str, Enum):
    """
    Type of the managed instance administrator.
    """
    ACTIVE_DIRECTORY = "ActiveDirectory"


class ManagedInstanceLicenseType(str, Enum):
    """
    The license type. Possible values are 'LicenseIncluded' (regular price inclusive of a new SQL license) and 'BasePrice' (discounted AHB price for bringing your own SQL licenses).
    """
    LICENSE_INCLUDED = "LicenseIncluded"
    BASE_PRICE = "BasePrice"


class ManagedInstanceProxyOverride(str, Enum):
    """
    Connection type used for connecting to the instance.
    """
    PROXY = "Proxy"
    REDIRECT = "Redirect"
    DEFAULT = "Default"


class ManagedServerCreateMode(str, Enum):
    """
    Specifies the mode of database creation.
    
    Default: Regular instance creation.
    
    Restore: Creates an instance by restoring a set of backups to specific point in time. RestorePointInTime and SourceManagedInstanceId must be specified.
    """
    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"


class PrincipalType(str, Enum):
    """
    Principal Type of the sever administrator.
    """
    USER = "User"
    GROUP = "Group"
    APPLICATION = "Application"


class PrivateLinkServiceConnectionStateStatus(str, Enum):
    """
    The private link service connection status.
    """
    APPROVED = "Approved"
    PENDING = "Pending"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class ReadOnlyEndpointFailoverPolicy(str, Enum):
    """
    Failover policy of the read-only endpoint for the failover group.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ReadWriteEndpointFailoverPolicy(str, Enum):
    """
    Failover policy of the read-write endpoint for the failover group. If failoverPolicy is Automatic then failoverWithDataLossGracePeriodMinutes is required.
    """
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


class ReplicationMode(str, Enum):
    """
    The replication mode of a distributed availability group. Parameter will be ignored during link creation.
    """
    ASYNC_ = "Async"
    SYNC = "Sync"


class SampleName(str, Enum):
    """
    The name of the sample schema to apply when creating this database.
    """
    ADVENTURE_WORKS_LT = "AdventureWorksLT"
    WIDE_WORLD_IMPORTERS_STD = "WideWorldImportersStd"
    WIDE_WORLD_IMPORTERS_FULL = "WideWorldImportersFull"


class SecondaryType(str, Enum):
    """
    The secondary type of the database if it is a secondary.  Valid values are Geo and Named.
    """
    GEO = "Geo"
    NAMED = "Named"


class SecurityAlertPolicyEmailAccountAdmins(str, Enum):
    """
    Specifies that the alert is sent to the account administrators.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SecurityAlertPolicyState(str, Enum):
    """
    Specifies the state of the policy. If state is Enabled, storageEndpoint and storageAccountAccessKey are required.
    """
    NEW = "New"
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SecurityAlertPolicyUseServerDefault(str, Enum):
    """
    Specifies whether to use the default server policy.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SecurityAlertsPolicyState(str, Enum):
    """
    Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SensitivityLabelRank(str, Enum):
    NONE = "None"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class ServerKeyType(str, Enum):
    """
    The server key type like 'ServiceManaged', 'AzureKeyVault'.
    """
    SERVICE_MANAGED = "ServiceManaged"
    AZURE_KEY_VAULT = "AzureKeyVault"


class ServerNetworkAccessFlag(str, Enum):
    """
    Whether or not to restrict outbound network access for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ServicePrincipalType(str, Enum):
    """
    Service principal type.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"


class SqlVulnerabilityAssessmentState(str, Enum):
    """
    Specifies the state of the SQL Vulnerability Assessment, whether it is enabled or disabled or a state has not been applied yet on the specific database or server.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SyncConflictResolutionPolicy(str, Enum):
    """
    Conflict resolution policy of the sync group.
    """
    HUB_WIN = "HubWin"
    MEMBER_WIN = "MemberWin"


class SyncDirection(str, Enum):
    """
    Sync direction of the sync member.
    """
    BIDIRECTIONAL = "Bidirectional"
    ONE_WAY_MEMBER_TO_HUB = "OneWayMemberToHub"
    ONE_WAY_HUB_TO_MEMBER = "OneWayHubToMember"


class SyncMemberDbType(str, Enum):
    """
    Database type of the sync member.
    """
    AZURE_SQL_DATABASE = "AzureSqlDatabase"
    SQL_SERVER_DATABASE = "SqlServerDatabase"


class TransparentDataEncryptionState(str, Enum):
    """
    Specifies the state of the transparent data encryption.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
