# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApplicationSharingPolicy',
    'ClusterPurpose',
    'ComputeEnvironmentType',
    'ComputeInstanceAuthorizationType',
    'ComputeType',
    'LoadBalancerType',
    'OsType',
    'RemoteLoginPortPublicAccess',
    'ResourceIdentityType',
    'SshPublicAccess',
    'ValueFormat',
    'VariantType',
    'VmPriority',
]


class ApplicationSharingPolicy(str, Enum):
    """
    Policy for sharing applications on this compute instance among users of parent workspace. If Personal, only the creator can access applications on this compute instance. When Shared, any workspace user can access applications on this instance depending on his/her assigned role.
    """
    PERSONAL = "Personal"
    SHARED = "Shared"


class ClusterPurpose(str, Enum):
    """
    Intended usage of the cluster
    """
    FAST_PROD = "FastProd"
    DENSE_PROD = "DenseProd"
    DEV_TEST = "DevTest"


class ComputeEnvironmentType(str, Enum):
    """
    The compute environment type for the service.
    """
    ACI = "ACI"
    AKS = "AKS"


class ComputeInstanceAuthorizationType(str, Enum):
    """
    The Compute Instance Authorization type. Available values are personal (default).
    """
    PERSONAL = "personal"


class ComputeType(str, Enum):
    """
    The type of compute
    """
    AKS = "AKS"
    AML_COMPUTE = "AmlCompute"
    COMPUTE_INSTANCE = "ComputeInstance"
    DATA_FACTORY = "DataFactory"
    VIRTUAL_MACHINE = "VirtualMachine"
    HD_INSIGHT = "HDInsight"
    DATABRICKS = "Databricks"
    DATA_LAKE_ANALYTICS = "DataLakeAnalytics"
    SYNAPSE_SPARK = "SynapseSpark"


class LoadBalancerType(str, Enum):
    """
    Load Balancer Type
    """
    PUBLIC_IP = "PublicIp"
    INTERNAL_LOAD_BALANCER = "InternalLoadBalancer"


class OsType(str, Enum):
    """
    Compute OS Type
    """
    LINUX = "Linux"
    WINDOWS = "Windows"


class RemoteLoginPortPublicAccess(str, Enum):
    """
    State of the public SSH port. Possible values are: Disabled - Indicates that the public ssh port is closed on all nodes of the cluster. Enabled - Indicates that the public ssh port is open on all nodes of the cluster. NotSpecified - Indicates that the public ssh port is closed on all nodes of the cluster if VNet is defined, else is open all public nodes. It can be default only during cluster creation time, after creation it will be either enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    NOT_SPECIFIED = "NotSpecified"


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"


class SshPublicAccess(str, Enum):
    """
    State of the public SSH port. Possible values are: Disabled - Indicates that the public ssh port is closed on this instance. Enabled - Indicates that the public ssh port is open and accessible according to the VNet/subnet policy if applicable.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ValueFormat(str, Enum):
    """
    format for the workspace connection value
    """
    JSON = "JSON"


class VariantType(str, Enum):
    """
    The type of the variant.
    """
    CONTROL = "Control"
    TREATMENT = "Treatment"


class VmPriority(str, Enum):
    """
    Virtual Machine priority
    """
    DEDICATED = "Dedicated"
    LOW_PRIORITY = "LowPriority"
