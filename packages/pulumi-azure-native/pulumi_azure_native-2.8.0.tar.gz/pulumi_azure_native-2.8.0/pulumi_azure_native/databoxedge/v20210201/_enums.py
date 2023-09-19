# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DataBoxEdgeDeviceKind',
    'DataBoxEdgeDeviceStatus',
    'DataResidencyType',
    'MsiIdentityType',
    'SkuName',
    'SkuTier',
]


class DataBoxEdgeDeviceKind(str, Enum):
    """
    The kind of the device.
    """
    AZURE_DATA_BOX_GATEWAY = "AzureDataBoxGateway"
    AZURE_STACK_EDGE = "AzureStackEdge"
    AZURE_STACK_HUB = "AzureStackHub"
    AZURE_MODULAR_DATA_CENTRE = "AzureModularDataCentre"


class DataBoxEdgeDeviceStatus(str, Enum):
    """
    The status of the Data Box Edge/Gateway device.
    """
    READY_TO_SETUP = "ReadyToSetup"
    ONLINE = "Online"
    OFFLINE = "Offline"
    NEEDS_ATTENTION = "NeedsAttention"
    DISCONNECTED = "Disconnected"
    PARTIALLY_DISCONNECTED = "PartiallyDisconnected"
    MAINTENANCE = "Maintenance"


class DataResidencyType(str, Enum):
    """
    DataResidencyType enum
    """
    GEO_ZONE_REPLICATION = "GeoZoneReplication"
    ZONE_REPLICATION = "ZoneReplication"


class MsiIdentityType(str, Enum):
    """
    Identity type
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class SkuName(str, Enum):
    """
    SKU name.
    """
    GATEWAY = "Gateway"
    EDGE = "Edge"
    TE_A_1_NODE = "TEA_1Node"
    TE_A_1_NODE_UPS = "TEA_1Node_UPS"
    TE_A_1_NODE_HEATER = "TEA_1Node_Heater"
    TE_A_1_NODE_UP_S_HEATER = "TEA_1Node_UPS_Heater"
    TE_A_4_NODE_HEATER = "TEA_4Node_Heater"
    TE_A_4_NODE_UP_S_HEATER = "TEA_4Node_UPS_Heater"
    TMA = "TMA"
    TDC = "TDC"
    TC_A_SMALL = "TCA_Small"
    GPU = "GPU"
    TC_A_LARGE = "TCA_Large"
    EDGE_P_BASE = "EdgeP_Base"
    EDGE_P_HIGH = "EdgeP_High"
    EDGE_P_R_BASE = "EdgePR_Base"
    EDGE_P_R_BASE_UPS = "EdgePR_Base_UPS"
    EP2_64_1_VP_U_W = "EP2_64_1VPU_W"
    EP2_128_1_T4_MX1_W = "EP2_128_1T4_Mx1_W"
    EP2_256_2_T4_W = "EP2_256_2T4_W"
    EDGE_M_R_MINI = "EdgeMR_Mini"
    RC_A_SMALL = "RCA_Small"
    RC_A_LARGE = "RCA_Large"
    RDC = "RDC"
    MANAGEMENT = "Management"


class SkuTier(str, Enum):
    """
    The SKU tier. This is based on the SKU name.
    """
    STANDARD = "Standard"
