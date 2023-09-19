# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AnalyticsConnectorDataDestinationType',
    'AnalyticsConnectorDataSourceType',
    'AnalyticsConnectorMappingType',
    'FhirServiceVersion',
    'ServiceManagedIdentityType',
]


class AnalyticsConnectorDataDestinationType(str, Enum):
    """
    Type of data destination.
    """
    DATALAKE = "datalake"


class AnalyticsConnectorDataSourceType(str, Enum):
    """
    Type of data source.
    """
    FHIRSERVICE = "fhirservice"


class AnalyticsConnectorMappingType(str, Enum):
    """
    Type of data mapping.
    """
    FHIR_TO_PARQUET = "fhirToParquet"


class FhirServiceVersion(str, Enum):
    """
    The kind of FHIR Service.
    """
    STU3 = "STU3"
    R4 = "R4"


class ServiceManagedIdentityType(str, Enum):
    """
    Type of identity being specified, currently SystemAssigned and None are allowed.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
