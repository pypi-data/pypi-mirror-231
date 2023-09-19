# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ClusterType',
    'IpAllocationType',
    'ValidationThresholdGrouping',
    'ValidationThresholdType',
]


class ClusterType(str, Enum):
    """
    The type of rack configuration for the cluster.
    """
    SINGLE_RACK = "SingleRack"
    MULTI_RACK = "MultiRack"


class IpAllocationType(str, Enum):
    """
    The type of the IP address allocation.
    """
    IPV4 = "IPV4"
    IPV6 = "IPV6"
    DUAL_STACK = "DualStack"


class ValidationThresholdGrouping(str, Enum):
    """
    Selection of how the type evaluation is applied to the cluster calculation.
    """
    PER_CLUSTER = "PerCluster"
    PER_RACK = "PerRack"


class ValidationThresholdType(str, Enum):
    """
    Selection of how the threshold should be evaluated.
    """
    COUNT_SUCCESS = "CountSuccess"
    PERCENT_SUCCESS = "PercentSuccess"
