# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'RunLocation',
    'State',
    'SupportedAlgorithm',
    'UserConfirmation',
]


class RunLocation(str, Enum):
    """
    This is the preferred geo location for the job to run.
    """
    NONE = "none"
    AUSTRALIAEAST = "australiaeast"
    AUSTRALIASOUTHEAST = "australiasoutheast"
    BRAZILSOUTH = "brazilsouth"
    CANADACENTRAL = "canadacentral"
    CANADAEAST = "canadaeast"
    CENTRALINDIA = "centralindia"
    CENTRALUS = "centralus"
    EASTASIA = "eastasia"
    EASTUS = "eastus"
    EASTUS2 = "eastus2"
    JAPANEAST = "japaneast"
    JAPANWEST = "japanwest"
    KOREACENTRAL = "koreacentral"
    KOREASOUTH = "koreasouth"
    SOUTHEASTASIA = "southeastasia"
    SOUTHCENTRALUS = "southcentralus"
    SOUTHINDIA = "southindia"
    NORTHCENTRALUS = "northcentralus"
    NORTHEUROPE = "northeurope"
    UKSOUTH = "uksouth"
    UKWEST = "ukwest"
    WESTCENTRALUS = "westcentralus"
    WESTEUROPE = "westeurope"
    WESTINDIA = "westindia"
    WESTUS = "westus"
    WESTUS2 = "westus2"


class State(str, Enum):
    """
    State of the job definition.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    SUPPORTED = "Supported"


class SupportedAlgorithm(str, Enum):
    """
    The encryption algorithm used to encrypt data.
    """
    NONE = "None"
    RSA1_5 = "RSA1_5"
    RS_A_OAEP = "RSA_OAEP"
    PLAIN_TEXT = "PlainText"


class UserConfirmation(str, Enum):
    """
    Enum to detect if user confirmation is required. If not passed will default to NotRequired.
    """
    NOT_REQUIRED = "NotRequired"
    REQUIRED = "Required"
