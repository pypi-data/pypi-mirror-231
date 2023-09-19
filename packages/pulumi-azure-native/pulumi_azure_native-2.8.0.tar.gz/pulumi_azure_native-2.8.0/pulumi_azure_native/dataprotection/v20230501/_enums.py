# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AbsoluteMarker',
    'AlertsState',
    'CrossRegionRestoreState',
    'CrossSubscriptionRestoreState',
    'DataStoreTypes',
    'DayOfWeek',
    'ImmutabilityState',
    'Month',
    'ResourcePropertiesObjectType',
    'SecretStoreType',
    'SoftDeleteState',
    'StorageSettingStoreTypes',
    'StorageSettingTypes',
    'ValidationType',
    'WeekNumber',
]


class AbsoluteMarker(str, Enum):
    ALL_BACKUP = "AllBackup"
    FIRST_OF_DAY = "FirstOfDay"
    FIRST_OF_MONTH = "FirstOfMonth"
    FIRST_OF_WEEK = "FirstOfWeek"
    FIRST_OF_YEAR = "FirstOfYear"


class AlertsState(str, Enum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class CrossRegionRestoreState(str, Enum):
    """
    CrossRegionRestore state
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class CrossSubscriptionRestoreState(str, Enum):
    """
    CrossSubscriptionRestore state
    """
    DISABLED = "Disabled"
    PERMANENTLY_DISABLED = "PermanentlyDisabled"
    ENABLED = "Enabled"


class DataStoreTypes(str, Enum):
    """
    type of datastore; Operational/Vault/Archive
    """
    OPERATIONAL_STORE = "OperationalStore"
    VAULT_STORE = "VaultStore"
    ARCHIVE_STORE = "ArchiveStore"


class DayOfWeek(str, Enum):
    FRIDAY = "Friday"
    MONDAY = "Monday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    THURSDAY = "Thursday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"


class ImmutabilityState(str, Enum):
    """
    Immutability state
    """
    DISABLED = "Disabled"
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"


class Month(str, Enum):
    APRIL = "April"
    AUGUST = "August"
    DECEMBER = "December"
    FEBRUARY = "February"
    JANUARY = "January"
    JULY = "July"
    JUNE = "June"
    MARCH = "March"
    MAY = "May"
    NOVEMBER = "November"
    OCTOBER = "October"
    SEPTEMBER = "September"


class ResourcePropertiesObjectType(str, Enum):
    """
    Type of the specific object - used for deserializing
    """
    DEFAULT_RESOURCE_PROPERTIES = "DefaultResourceProperties"


class SecretStoreType(str, Enum):
    """
    Gets or sets the type of secret store
    """
    INVALID = "Invalid"
    AZURE_KEY_VAULT = "AzureKeyVault"


class SoftDeleteState(str, Enum):
    """
    State of soft delete
    """
    OFF = "Off"
    """
    Soft Delete is turned off for the BackupVault
    """
    ON = "On"
    """
    Soft Delete is enabled for the BackupVault but can be turned off
    """
    ALWAYS_ON = "AlwaysOn"
    """
    Soft Delete is permanently enabled for the BackupVault and the setting cannot be changed
    """


class StorageSettingStoreTypes(str, Enum):
    """
    Gets or sets the type of the datastore.
    """
    ARCHIVE_STORE = "ArchiveStore"
    OPERATIONAL_STORE = "OperationalStore"
    VAULT_STORE = "VaultStore"


class StorageSettingTypes(str, Enum):
    """
    Gets or sets the type.
    """
    GEO_REDUNDANT = "GeoRedundant"
    LOCALLY_REDUNDANT = "LocallyRedundant"
    ZONE_REDUNDANT = "ZoneRedundant"


class ValidationType(str, Enum):
    """
    Specifies the type of validation. In case of DeepValidation, all validations from /validateForBackup API will run again.
    """
    SHALLOW_VALIDATION = "ShallowValidation"
    DEEP_VALIDATION = "DeepValidation"


class WeekNumber(str, Enum):
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    SECOND = "Second"
    THIRD = "Third"
