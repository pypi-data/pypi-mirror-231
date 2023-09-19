# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Access',
    'ClusterUpgradeCadence',
    'ClusterUpgradeMode',
    'Direction',
    'DiskType',
    'EvictionPolicyType',
    'FailureAction',
    'IPAddressType',
    'ManagedClusterAddOnFeature',
    'ManagedIdentityType',
    'MoveCost',
    'NsgProtocol',
    'PartitionScheme',
    'PrivateEndpointNetworkPolicies',
    'PrivateLinkServiceNetworkPolicies',
    'ProbeProtocol',
    'Protocol',
    'RollingUpgradeMode',
    'SecurityType',
    'ServiceCorrelationScheme',
    'ServiceKind',
    'ServiceLoadMetricWeight',
    'ServicePackageActivationMode',
    'ServicePlacementPolicyType',
    'ServiceScalingMechanismKind',
    'ServiceScalingTriggerKind',
    'SkuName',
    'VmSetupAction',
    'ZonalUpdateMode',
]


class Access(str, Enum):
    """
    The network traffic is allowed or denied.
    """
    ALLOW = "allow"
    DENY = "deny"


class ClusterUpgradeCadence(str, Enum):
    """
    Indicates when new cluster runtime version upgrades will be applied after they are released. By default is Wave0. Only applies when **clusterUpgradeMode** is set to 'Automatic'.
    """
    WAVE0 = "Wave0"
    """
    Cluster upgrade starts immediately after a new version is rolled out. Recommended for Test/Dev clusters.
    """
    WAVE1 = "Wave1"
    """
    Cluster upgrade starts 7 days after a new version is rolled out. Recommended for Pre-prod clusters.
    """
    WAVE2 = "Wave2"
    """
    Cluster upgrade starts 14 days after a new version is rolled out. Recommended for Production clusters.
    """


class ClusterUpgradeMode(str, Enum):
    """
    The upgrade mode of the cluster when new Service Fabric runtime version is available.
    """
    AUTOMATIC = "Automatic"
    """
    The cluster will be automatically upgraded to the latest Service Fabric runtime version, **clusterUpgradeCadence** will determine when the upgrade starts after the new version becomes available.
    """
    MANUAL = "Manual"
    """
    The cluster will not be automatically upgraded to the latest Service Fabric runtime version. The cluster is upgraded by setting the **clusterCodeVersion** property in the cluster resource.
    """


class Direction(str, Enum):
    """
    Network security rule direction.
    """
    INBOUND = "inbound"
    OUTBOUND = "outbound"


class DiskType(str, Enum):
    """
    Managed data disk type. Specifies the storage account type for the managed disk
    """
    STANDARD_LRS = "Standard_LRS"
    """
    Standard HDD locally redundant storage. Best for backup, non-critical, and infrequent access.
    """
    STANDARD_SS_D_LRS = "StandardSSD_LRS"
    """
    Standard SSD locally redundant storage. Best for web servers, lightly used enterprise applications and dev/test.
    """
    PREMIUM_LRS = "Premium_LRS"
    """
    Premium SSD locally redundant storage. Best for production and performance sensitive workloads.
    """


class EvictionPolicyType(str, Enum):
    """
    Specifies the eviction policy for virtual machines in a SPOT node type. Default is Delete.
    """
    DELETE = "Delete"
    """
    Eviction policy will be Delete for SPOT vms.
    """
    DEALLOCATE = "Deallocate"
    """
    Eviction policy will be Deallocate for SPOT vms.
    """


class FailureAction(str, Enum):
    """
    The compensating action to perform when a Monitored upgrade encounters monitoring policy or health policy violations. Invalid indicates the failure action is invalid. Rollback specifies that the upgrade will start rolling back automatically. Manual indicates that the upgrade will switch to UnmonitoredManual upgrade mode.
    """
    ROLLBACK = "Rollback"
    """
    Indicates that a rollback of the upgrade will be performed by Service Fabric if the upgrade fails.
    """
    MANUAL = "Manual"
    """
    Indicates that a manual repair will need to be performed by the administrator if the upgrade fails. Service Fabric will not proceed to the next upgrade domain automatically.
    """


class IPAddressType(str, Enum):
    """
    The IP address type of this frontend configuration. If omitted the default value is IPv4.
    """
    I_PV4 = "IPv4"
    """
    IPv4 address type.
    """
    I_PV6 = "IPv6"
    """
    IPv6 address type.
    """


class ManagedClusterAddOnFeature(str, Enum):
    """
    Available cluster add-on features
    """
    DNS_SERVICE = "DnsService"
    """
    Dns service
    """
    BACKUP_RESTORE_SERVICE = "BackupRestoreService"
    """
    Backup and restore service
    """
    RESOURCE_MONITOR_SERVICE = "ResourceMonitorService"
    """
    Resource monitor service
    """


class ManagedIdentityType(str, Enum):
    """
    The type of managed identity for the resource.
    """
    NONE = "None"
    """
    Indicates that no identity is associated with the resource.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    """
    Indicates that system assigned identity is associated with the resource.
    """
    USER_ASSIGNED = "UserAssigned"
    """
    Indicates that user assigned identity is associated with the resource.
    """
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    """
    Indicates that both system assigned and user assigned identity are associated with the resource.
    """


class MoveCost(str, Enum):
    """
    Specifies the move cost for the service.
    """
    ZERO = "Zero"
    """
    Zero move cost. This value is zero.
    """
    LOW = "Low"
    """
    Specifies the move cost of the service as Low. The value is 1.
    """
    MEDIUM = "Medium"
    """
    Specifies the move cost of the service as Medium. The value is 2.
    """
    HIGH = "High"
    """
    Specifies the move cost of the service as High. The value is 3.
    """


class NsgProtocol(str, Enum):
    """
    Network protocol this rule applies to.
    """
    HTTP = "http"
    HTTPS = "https"
    TCP = "tcp"
    UDP = "udp"
    ICMP = "icmp"
    AH = "ah"
    ESP = "esp"


class PartitionScheme(str, Enum):
    """
    Specifies how the service is partitioned.
    """
    SINGLETON = "Singleton"
    """
    Indicates that the partition is based on string names, and is a SingletonPartitionScheme object, The value is 0.
    """
    UNIFORM_INT64_RANGE = "UniformInt64Range"
    """
    Indicates that the partition is based on Int64 key ranges, and is a UniformInt64RangePartitionScheme object. The value is 1.
    """
    NAMED = "Named"
    """
    Indicates that the partition is based on string names, and is a NamedPartitionScheme object. The value is 2.
    """


class PrivateEndpointNetworkPolicies(str, Enum):
    """
    Enable or Disable apply network policies on private end point in the subnet.
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class PrivateLinkServiceNetworkPolicies(str, Enum):
    """
    Enable or Disable apply network policies on private link service in the subnet.
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class ProbeProtocol(str, Enum):
    """
    the reference to the load balancer probe used by the load balancing rule.
    """
    TCP = "tcp"
    HTTP = "http"
    HTTPS = "https"


class Protocol(str, Enum):
    """
    The reference to the transport protocol used by the load balancing rule.
    """
    TCP = "tcp"
    UDP = "udp"


class RollingUpgradeMode(str, Enum):
    """
    The mode used to monitor health during a rolling upgrade. The values are Monitored, and UnmonitoredAuto.
    """
    MONITORED = "Monitored"
    """
    The upgrade will stop after completing each upgrade domain and automatically monitor health before proceeding. The value is 0.
    """
    UNMONITORED_AUTO = "UnmonitoredAuto"
    """
    The upgrade will proceed automatically without performing any health monitoring. The value is 1.
    """


class SecurityType(str, Enum):
    """
    Specifies the security type of the nodeType. Only TrustedLaunch is currently supported
    """
    TRUSTED_LAUNCH = "TrustedLaunch"
    """
    Trusted Launch is a security type that secures generation 2 virtual machines.
    """


class ServiceCorrelationScheme(str, Enum):
    """
    The ServiceCorrelationScheme which describes the relationship between this service and the service specified via ServiceName.
    """
    ALIGNED_AFFINITY = "AlignedAffinity"
    """
    Aligned affinity ensures that the primaries of the partitions of the affinitized services are collocated on the same nodes. This is the default and is the same as selecting the Affinity scheme. The value is 0.
    """
    NON_ALIGNED_AFFINITY = "NonAlignedAffinity"
    """
    Non-Aligned affinity guarantees that all replicas of each service will be placed on the same nodes. Unlike Aligned Affinity, this does not guarantee that replicas of particular role will be collocated. The value is 1.
    """


class ServiceKind(str, Enum):
    """
    The kind of service (Stateless or Stateful).
    """
    STATELESS = "Stateless"
    """
    Does not use Service Fabric to make its state highly available or reliable. The value is 0.
    """
    STATEFUL = "Stateful"
    """
    Uses Service Fabric to make its state or part of its state highly available and reliable. The value is 1.
    """


class ServiceLoadMetricWeight(str, Enum):
    """
    The service load metric relative weight, compared to other metrics configured for this service, as a number.
    """
    ZERO = "Zero"
    """
    Disables resource balancing for this metric. This value is zero.
    """
    LOW = "Low"
    """
    Specifies the metric weight of the service load as Low. The value is 1.
    """
    MEDIUM = "Medium"
    """
    Specifies the metric weight of the service load as Medium. The value is 2.
    """
    HIGH = "High"
    """
    Specifies the metric weight of the service load as High. The value is 3.
    """


class ServicePackageActivationMode(str, Enum):
    """
    The activation Mode of the service package
    """
    SHARED_PROCESS = "SharedProcess"
    """
    Indicates the application package activation mode will use shared process.
    """
    EXCLUSIVE_PROCESS = "ExclusiveProcess"
    """
    Indicates the application package activation mode will use exclusive process.
    """


class ServicePlacementPolicyType(str, Enum):
    """
    The type of placement policy for a service fabric service. Following are the possible values.
    """
    INVALID_DOMAIN = "InvalidDomain"
    """
    Indicates that the ServicePlacementPolicyDescription is of type ServicePlacementInvalidDomainPolicyDescription, which indicates that a particular fault or upgrade domain cannot be used for placement of this service. The value is 0.
    """
    REQUIRED_DOMAIN = "RequiredDomain"
    """
    Indicates that the ServicePlacementPolicyDescription is of type ServicePlacementRequireDomainDistributionPolicyDescription indicating that the replicas of the service must be placed in a specific domain. The value is 1.
    """
    PREFERRED_PRIMARY_DOMAIN = "PreferredPrimaryDomain"
    """
    Indicates that the ServicePlacementPolicyDescription is of type ServicePlacementPreferPrimaryDomainPolicyDescription, which indicates that if possible the Primary replica for the partitions of the service should be located in a particular domain as an optimization. The value is 2.
    """
    REQUIRED_DOMAIN_DISTRIBUTION = "RequiredDomainDistribution"
    """
    Indicates that the ServicePlacementPolicyDescription is of type ServicePlacementRequireDomainDistributionPolicyDescription, indicating that the system will disallow placement of any two replicas from the same partition in the same domain at any time. The value is 3.
    """
    NON_PARTIALLY_PLACE_SERVICE = "NonPartiallyPlaceService"
    """
    Indicates that the ServicePlacementPolicyDescription is of type ServicePlacementNonPartiallyPlaceServicePolicyDescription, which indicates that if possible all replicas of a particular partition of the service should be placed atomically. The value is 4.
    """


class ServiceScalingMechanismKind(str, Enum):
    """
    Specifies the mechanism associated with this scaling policy.
    """
    SCALE_PARTITION_INSTANCE_COUNT = "ScalePartitionInstanceCount"
    """
    Represents a scaling mechanism for adding or removing instances of stateless service partition. The value is 0.
    """
    ADD_REMOVE_INCREMENTAL_NAMED_PARTITION = "AddRemoveIncrementalNamedPartition"
    """
    Represents a scaling mechanism for adding or removing named partitions of a stateless service. The value is 1.
    """


class ServiceScalingTriggerKind(str, Enum):
    """
    Specifies the trigger associated with this scaling policy.
    """
    AVERAGE_PARTITION_LOAD_TRIGGER = "AveragePartitionLoadTrigger"
    """
    Represents a scaling trigger related to an average load of a metric/resource of a partition. The value is 0.
    """
    AVERAGE_SERVICE_LOAD_TRIGGER = "AverageServiceLoadTrigger"
    """
    Represents a scaling policy related to an average load of a metric/resource of a service. The value is 1.
    """


class SkuName(str, Enum):
    """
    Sku Name.
    """
    BASIC = "Basic"
    """
    Basic requires a minimum of 3 nodes and allows only 1 node type.
    """
    STANDARD = "Standard"
    """
    Requires a minimum of 5 nodes and allows 1 or more node type.
    """


class VmSetupAction(str, Enum):
    """
    action to be performed on the vms before bootstrapping the service fabric runtime.
    """
    ENABLE_CONTAINERS = "EnableContainers"
    """
    Enable windows containers feature.
    """
    ENABLE_HYPER_V = "EnableHyperV"
    """
    Enables windows HyperV feature.
    """


class ZonalUpdateMode(str, Enum):
    """
    Indicates the update mode for Cross Az clusters.
    """
    STANDARD = "Standard"
    """
    The cluster will use 5 upgrade domains for Cross Az Node types.
    """
    FAST = "Fast"
    """
    The cluster will use a maximum of 3 upgrade domains per zone instead of 5 for Cross Az Node types for faster deployments.
    """
