# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ColumnDataTypeHintEnum',
    'ColumnTypeEnum',
    'IdentityType',
    'PublicNetworkAccessType',
    'TablePlanEnum',
    'WorkspaceSkuNameEnum',
]


class ColumnDataTypeHintEnum(str, Enum):
    """
    Column data type logical hint.
    """
    URI = "uri"
    """
    A string that matches the pattern of a URI, for example, scheme://username:password@host:1234/this/is/a/path?k1=v1&k2=v2#fragment
    """
    GUID = "guid"
    """
    A standard 128-bit GUID following the standard shape, xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    """
    ARM_PATH = "armPath"
    """
    An Azure Resource Model (ARM) path: /subscriptions/{...}/resourceGroups/{...}/providers/Microsoft.{...}/{...}/{...}/{...}...
    """
    IP = "ip"
    """
    A standard V4/V6 ip address following the standard shape, x.x.x.x/y:y:y:y:y:y:y:y
    """


class ColumnTypeEnum(str, Enum):
    """
    Column data type.
    """
    STRING = "string"
    INT = "int"
    LONG = "long"
    REAL = "real"
    BOOLEAN = "boolean"
    DATE_TIME = "dateTime"
    GUID = "guid"
    DYNAMIC = "dynamic"


class IdentityType(str, Enum):
    """
    Type of managed service identity.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"


class PublicNetworkAccessType(str, Enum):
    """
    The network access type for accessing Log Analytics query.
    """
    ENABLED = "Enabled"
    """
    Enables connectivity to Log Analytics through public DNS.
    """
    DISABLED = "Disabled"
    """
    Disables public connectivity to Log Analytics through public DNS.
    """


class TablePlanEnum(str, Enum):
    """
    Instruct the system how to handle and charge the logs ingested to this table.
    """
    BASIC = "Basic"
    """
    Logs  that are adjusted to support high volume low value verbose logs.
    """
    ANALYTICS = "Analytics"
    """
    Logs  that allow monitoring and analytics.
    """


class WorkspaceSkuNameEnum(str, Enum):
    """
    The name of the SKU.
    """
    FREE = "Free"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PER_NODE = "PerNode"
    PER_GB2018 = "PerGB2018"
    STANDALONE = "Standalone"
    CAPACITY_RESERVATION = "CapacityReservation"
    LA_CLUSTER = "LACluster"
