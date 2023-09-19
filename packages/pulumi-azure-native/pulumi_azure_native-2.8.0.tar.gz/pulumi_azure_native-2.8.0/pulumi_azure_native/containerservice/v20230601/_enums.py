# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AgentPoolMode',
    'AgentPoolType',
    'Code',
    'ConnectionStatus',
    'Expander',
    'ExtendedLocationTypes',
    'GPUInstanceProfile',
    'IpFamily',
    'KeyVaultNetworkAccessTypes',
    'KubeletDiskType',
    'KubernetesSupportPlan',
    'LicenseType',
    'LoadBalancerSku',
    'ManagedClusterSKUName',
    'ManagedClusterSKUTier',
    'NetworkDataplane',
    'NetworkMode',
    'NetworkPlugin',
    'NetworkPluginMode',
    'NetworkPolicy',
    'NodeOSUpgradeChannel',
    'OSDiskType',
    'OSSKU',
    'OSType',
    'OutboundType',
    'PublicNetworkAccess',
    'ResourceIdentityType',
    'ScaleDownMode',
    'ScaleSetEvictionPolicy',
    'ScaleSetPriority',
    'SnapshotType',
    'Type',
    'UpgradeChannel',
    'WeekDay',
    'WorkloadRuntime',
]


class AgentPoolMode(str, Enum):
    """
    A cluster must have at least one 'System' Agent Pool at all times. For additional information on agent pool restrictions and best practices, see: https://docs.microsoft.com/azure/aks/use-system-pools
    """
    SYSTEM = "System"
    """
    System agent pools are primarily for hosting critical system pods such as CoreDNS and metrics-server. System agent pools osType must be Linux. System agent pools VM SKU must have at least 2vCPUs and 4GB of memory.
    """
    USER = "User"
    """
    User agent pools are primarily for hosting your application pods.
    """


class AgentPoolType(str, Enum):
    """
    The type of Agent Pool.
    """
    VIRTUAL_MACHINE_SCALE_SETS = "VirtualMachineScaleSets"
    """
    Create an Agent Pool backed by a Virtual Machine Scale Set.
    """
    AVAILABILITY_SET = "AvailabilitySet"
    """
    Use of this is strongly discouraged.
    """


class Code(str, Enum):
    """
    Tells whether the cluster is Running or Stopped
    """
    RUNNING = "Running"
    """
    The cluster is running.
    """
    STOPPED = "Stopped"
    """
    The cluster is stopped.
    """


class ConnectionStatus(str, Enum):
    """
    The private link service connection status.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class Expander(str, Enum):
    """
    If not specified, the default is 'random'. See [expanders](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-are-expanders) for more information.
    """
    LEAST_WASTE = "least-waste"
    """
    Selects the node group that will have the least idle CPU (if tied, unused memory) after scale-up. This is useful when you have different classes of nodes, for example, high CPU or high memory nodes, and only want to expand those when there are pending pods that need a lot of those resources.
    """
    MOST_PODS = "most-pods"
    """
    Selects the node group that would be able to schedule the most pods when scaling up. This is useful when you are using nodeSelector to make sure certain pods land on certain nodes. Note that this won't cause the autoscaler to select bigger nodes vs. smaller, as it can add multiple smaller nodes at once.
    """
    PRIORITY = "priority"
    """
    Selects the node group that has the highest priority assigned by the user. It's configuration is described in more details [here](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/expander/priority/readme.md).
    """
    RANDOM = "random"
    """
    Used when you don't have a particular need for the node groups to scale differently.
    """


class ExtendedLocationTypes(str, Enum):
    """
    The type of the extended location.
    """
    EDGE_ZONE = "EdgeZone"


class GPUInstanceProfile(str, Enum):
    """
    GPUInstanceProfile to be used to specify GPU MIG instance profile for supported GPU VM SKU.
    """
    MIG1G = "MIG1g"
    MIG2G = "MIG2g"
    MIG3G = "MIG3g"
    MIG4G = "MIG4g"
    MIG7G = "MIG7g"


class IpFamily(str, Enum):
    """
    The IP version to use for cluster networking and IP assignment.
    """
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class KeyVaultNetworkAccessTypes(str, Enum):
    """
    Network access of key vault. The possible values are `Public` and `Private`. `Public` means the key vault allows public access from all networks. `Private` means the key vault disables public access and enables private link. The default value is `Public`.
    """
    PUBLIC = "Public"
    PRIVATE = "Private"


class KubeletDiskType(str, Enum):
    """
    Determines the placement of emptyDir volumes, container runtime data root, and Kubelet ephemeral storage.
    """
    OS = "OS"
    """
    Kubelet will use the OS disk for its data.
    """
    TEMPORARY = "Temporary"
    """
    Kubelet will use the temporary disk for its data.
    """


class KubernetesSupportPlan(str, Enum):
    """
    The support plan for the Managed Cluster. If unspecified, the default is 'KubernetesOfficial'.
    """
    KUBERNETES_OFFICIAL = "KubernetesOfficial"
    """
    Support for the version is the same as for the open source Kubernetes offering. Official Kubernetes open source community support versions for 1 year after release.
    """
    AKS_LONG_TERM_SUPPORT = "AKSLongTermSupport"
    """
    Support for the version extended past the KubernetesOfficial support of 1 year. AKS continues to patch CVEs for another 1 year, for a total of 2 years of support.
    """


class LicenseType(str, Enum):
    """
    The license type to use for Windows VMs. See [Azure Hybrid User Benefits](https://azure.microsoft.com/pricing/hybrid-benefit/faq/) for more details.
    """
    NONE = "None"
    """
    No additional licensing is applied.
    """
    WINDOWS_SERVER = "Windows_Server"
    """
    Enables Azure Hybrid User Benefits for Windows VMs.
    """


class LoadBalancerSku(str, Enum):
    """
    The default is 'standard'. See [Azure Load Balancer SKUs](https://docs.microsoft.com/azure/load-balancer/skus) for more information about the differences between load balancer SKUs.
    """
    STANDARD = "standard"
    """
    Use a a standard Load Balancer. This is the recommended Load Balancer SKU. For more information about on working with the load balancer in the managed cluster, see the [standard Load Balancer](https://docs.microsoft.com/azure/aks/load-balancer-standard) article.
    """
    BASIC = "basic"
    """
    Use a basic Load Balancer with limited functionality.
    """


class ManagedClusterSKUName(str, Enum):
    """
    The name of a managed cluster SKU.
    """
    BASE = "Base"
    """
    Base option for the AKS control plane.
    """


class ManagedClusterSKUTier(str, Enum):
    """
    If not specified, the default is 'Free'. See [AKS Pricing Tier](https://learn.microsoft.com/azure/aks/free-standard-pricing-tiers) for more details.
    """
    PREMIUM = "Premium"
    """
    Cluster has premium capabilities in addition to all of the capabilities included in 'Standard'. Premium enables selection of LongTermSupport (aka.ms/aks/lts) for certain Kubernetes versions.
    """
    STANDARD = "Standard"
    """
    Recommended for mission-critical and production workloads. Includes Kubernetes control plane autoscaling, workload-intensive testing, and up to 5,000 nodes per cluster. Guarantees 99.95% availability of the Kubernetes API server endpoint for clusters that use Availability Zones and 99.9% of availability for clusters that don't use Availability Zones.
    """
    FREE = "Free"
    """
    The cluster management is free, but charged for VM, storage, and networking usage. Best for experimenting, learning, simple testing, or workloads with fewer than 10 nodes. Not recommended for production use cases.
    """


class NetworkDataplane(str, Enum):
    """
    Network dataplane used in the Kubernetes cluster.
    """
    AZURE = "azure"
    """
    Use Azure network dataplane.
    """
    CILIUM = "cilium"
    """
    Use Cilium network dataplane. See [Azure CNI Powered by Cilium](https://learn.microsoft.com/azure/aks/azure-cni-powered-by-cilium) for more information.
    """


class NetworkMode(str, Enum):
    """
    This cannot be specified if networkPlugin is anything other than 'azure'.
    """
    TRANSPARENT = "transparent"
    """
    No bridge is created. Intra-VM Pod to Pod communication is through IP routes created by Azure CNI. See [Transparent Mode](https://docs.microsoft.com/azure/aks/faq#transparent-mode) for more information.
    """
    BRIDGE = "bridge"
    """
    This is no longer supported
    """


class NetworkPlugin(str, Enum):
    """
    Network plugin used for building the Kubernetes network.
    """
    AZURE = "azure"
    """
    Use the Azure CNI network plugin. See [Azure CNI (advanced) networking](https://docs.microsoft.com/azure/aks/concepts-network#azure-cni-advanced-networking) for more information.
    """
    KUBENET = "kubenet"
    """
    Use the Kubenet network plugin. See [Kubenet (basic) networking](https://docs.microsoft.com/azure/aks/concepts-network#kubenet-basic-networking) for more information.
    """
    NONE = "none"
    """
    No CNI plugin is pre-installed. See [BYO CNI](https://docs.microsoft.com/en-us/azure/aks/use-byo-cni) for more information.
    """


class NetworkPluginMode(str, Enum):
    """
    The mode the network plugin should use.
    """
    OVERLAY = "overlay"
    """
    Used with networkPlugin=azure, pods are given IPs from the PodCIDR address space but use Azure Routing Domains rather than Kubenet's method of route tables. For more information visit https://aka.ms/aks/azure-cni-overlay.
    """


class NetworkPolicy(str, Enum):
    """
    Network policy used for building the Kubernetes network.
    """
    CALICO = "calico"
    """
    Use Calico network policies. See [differences between Azure and Calico policies](https://docs.microsoft.com/azure/aks/use-network-policies#differences-between-azure-and-calico-policies-and-their-capabilities) for more information.
    """
    AZURE = "azure"
    """
    Use Azure network policies. See [differences between Azure and Calico policies](https://docs.microsoft.com/azure/aks/use-network-policies#differences-between-azure-and-calico-policies-and-their-capabilities) for more information.
    """
    CILIUM = "cilium"
    """
    Use Cilium to enforce network policies. This requires networkDataplane to be 'cilium'.
    """


class NodeOSUpgradeChannel(str, Enum):
    """
    Manner in which the OS on your nodes is updated. The default is NodeImage.
    """
    NONE = "None"
    """
    No attempt to update your machines OS will be made either by OS or by rolling VHDs. This means you are responsible for your security updates
    """
    UNMANAGED = "Unmanaged"
    """
    OS updates will be applied automatically through the OS built-in patching infrastructure. Newly scaled in machines will be unpatched initially and will be patched at some point by the OS's infrastructure. Behavior of this option depends on the OS in question. Ubuntu and Mariner apply security patches through unattended upgrade roughly once a day around 06:00 UTC. Windows does not apply security patches automatically and so for them this option is equivalent to None till further notice
    """
    NODE_IMAGE = "NodeImage"
    """
    AKS will update the nodes with a newly patched VHD containing security fixes and bugfixes on a weekly cadence. With the VHD update machines will be rolling reimaged to that VHD following maintenance windows and surge settings. No extra VHD cost is incurred when choosing this option as AKS hosts the images.
    """


class OSDiskType(str, Enum):
    """
    The default is 'Ephemeral' if the VM supports it and has a cache disk larger than the requested OSDiskSizeGB. Otherwise, defaults to 'Managed'. May not be changed after creation. For more information see [Ephemeral OS](https://docs.microsoft.com/azure/aks/cluster-configuration#ephemeral-os).
    """
    MANAGED = "Managed"
    """
    Azure replicates the operating system disk for a virtual machine to Azure storage to avoid data loss should the VM need to be relocated to another host. Since containers aren't designed to have local state persisted, this behavior offers limited value while providing some drawbacks, including slower node provisioning and higher read/write latency.
    """
    EPHEMERAL = "Ephemeral"
    """
    Ephemeral OS disks are stored only on the host machine, just like a temporary disk. This provides lower read/write latency, along with faster node scaling and cluster upgrades.
    """


class OSSKU(str, Enum):
    """
    Specifies the OS SKU used by the agent pool. The default is Ubuntu if OSType is Linux. The default is Windows2019 when Kubernetes <= 1.24 or Windows2022 when Kubernetes >= 1.25 if OSType is Windows.
    """
    UBUNTU = "Ubuntu"
    """
    Use Ubuntu as the OS for node images.
    """
    AZURE_LINUX = "AzureLinux"
    """
    Use AzureLinux as the OS for node images. Azure Linux is a container-optimized Linux distro built by Microsoft, visit https://aka.ms/azurelinux for more information.
    """
    CBL_MARINER = "CBLMariner"
    """
    Deprecated OSSKU. Microsoft recommends that new deployments choose 'AzureLinux' instead.
    """
    WINDOWS2019 = "Windows2019"
    """
    Use Windows2019 as the OS for node images. Unsupported for system node pools. Windows2019 only supports Windows2019 containers; it cannot run Windows2022 containers and vice versa.
    """
    WINDOWS2022 = "Windows2022"
    """
    Use Windows2022 as the OS for node images. Unsupported for system node pools. Windows2022 only supports Windows2022 containers; it cannot run Windows2019 containers and vice versa.
    """


class OSType(str, Enum):
    """
    The operating system type. The default is Linux.
    """
    LINUX = "Linux"
    """
    Use Linux.
    """
    WINDOWS = "Windows"
    """
    Use Windows.
    """


class OutboundType(str, Enum):
    """
    This can only be set at cluster creation time and cannot be changed later. For more information see [egress outbound type](https://docs.microsoft.com/azure/aks/egress-outboundtype).
    """
    LOAD_BALANCER = "loadBalancer"
    """
    The load balancer is used for egress through an AKS assigned public IP. This supports Kubernetes services of type 'loadBalancer'. For more information see [outbound type loadbalancer](https://docs.microsoft.com/azure/aks/egress-outboundtype#outbound-type-of-loadbalancer).
    """
    USER_DEFINED_ROUTING = "userDefinedRouting"
    """
    Egress paths must be defined by the user. This is an advanced scenario and requires proper network configuration. For more information see [outbound type userDefinedRouting](https://docs.microsoft.com/azure/aks/egress-outboundtype#outbound-type-of-userdefinedrouting).
    """
    MANAGED_NAT_GATEWAY = "managedNATGateway"
    """
    The AKS-managed NAT gateway is used for egress.
    """
    USER_ASSIGNED_NAT_GATEWAY = "userAssignedNATGateway"
    """
    The user-assigned NAT gateway associated to the cluster subnet is used for egress. This is an advanced scenario and requires proper network configuration.
    """


class PublicNetworkAccess(str, Enum):
    """
    Allow or deny public network access for AKS
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ResourceIdentityType(str, Enum):
    """
    For more information see [use managed identities in AKS](https://docs.microsoft.com/azure/aks/use-managed-identity).
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    """
    Use an implicitly created system assigned managed identity to manage cluster resources. Master components in the control plane such as kube-controller-manager will use the system assigned managed identity to manipulate Azure resources.
    """
    USER_ASSIGNED = "UserAssigned"
    """
    Use a user-specified identity to manage cluster resources. Master components in the control plane such as kube-controller-manager will use the specified user assigned managed identity to manipulate Azure resources.
    """
    NONE = "None"
    """
    Do not use a managed identity for the Managed Cluster, service principal will be used instead.
    """


class ScaleDownMode(str, Enum):
    """
    This also effects the cluster autoscaler behavior. If not specified, it defaults to Delete.
    """
    DELETE = "Delete"
    """
    Create new instances during scale up and remove instances during scale down.
    """
    DEALLOCATE = "Deallocate"
    """
    Attempt to start deallocated instances (if they exist) during scale up and deallocate instances during scale down.
    """


class ScaleSetEvictionPolicy(str, Enum):
    """
    This cannot be specified unless the scaleSetPriority is 'Spot'. If not specified, the default is 'Delete'.
    """
    DELETE = "Delete"
    """
    Nodes in the underlying Scale Set of the node pool are deleted when they're evicted.
    """
    DEALLOCATE = "Deallocate"
    """
    Nodes in the underlying Scale Set of the node pool are set to the stopped-deallocated state upon eviction. Nodes in the stopped-deallocated state count against your compute quota and can cause issues with cluster scaling or upgrading.
    """


class ScaleSetPriority(str, Enum):
    """
    The Virtual Machine Scale Set priority. If not specified, the default is 'Regular'.
    """
    SPOT = "Spot"
    """
    Spot priority VMs will be used. There is no SLA for spot nodes. See [spot on AKS](https://docs.microsoft.com/azure/aks/spot-node-pool) for more information.
    """
    REGULAR = "Regular"
    """
    Regular VMs will be used.
    """


class SnapshotType(str, Enum):
    """
    The type of a snapshot. The default is NodePool.
    """
    NODE_POOL = "NodePool"
    """
    The snapshot is a snapshot of a node pool.
    """


class Type(str, Enum):
    """
    Specifies on which week of the month the dayOfWeek applies.
    """
    FIRST = "First"
    """
    First week of the month.
    """
    SECOND = "Second"
    """
    Second week of the month.
    """
    THIRD = "Third"
    """
    Third week of the month.
    """
    FOURTH = "Fourth"
    """
    Fourth week of the month.
    """
    LAST = "Last"
    """
    Last week of the month.
    """


class UpgradeChannel(str, Enum):
    """
    For more information see [setting the AKS cluster auto-upgrade channel](https://docs.microsoft.com/azure/aks/upgrade-cluster#set-auto-upgrade-channel).
    """
    RAPID = "rapid"
    """
    Automatically upgrade the cluster to the latest supported patch release on the latest supported minor version. In cases where the cluster is at a version of Kubernetes that is at an N-2 minor version where N is the latest supported minor version, the cluster first upgrades to the latest supported patch version on N-1 minor version. For example, if a cluster is running version 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster first is upgraded to 1.18.6, then is upgraded to 1.19.1.
    """
    STABLE = "stable"
    """
    Automatically upgrade the cluster to the latest supported patch release on minor version N-1, where N is the latest supported minor version. For example, if a cluster is running version 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster is upgraded to 1.18.6.
    """
    PATCH = "patch"
    """
    Automatically upgrade the cluster to the latest supported patch version when it becomes available while keeping the minor version the same. For example, if a cluster is running version 1.17.7 and versions 1.17.9, 1.18.4, 1.18.6, and 1.19.1 are available, your cluster is upgraded to 1.17.9.
    """
    NODE_IMAGE = "node-image"
    """
    Automatically upgrade the node image to the latest version available. Consider using nodeOSUpgradeChannel instead as that allows you to configure node OS patching separate from Kubernetes version patching
    """
    NONE = "none"
    """
    Disables auto-upgrades and keeps the cluster at its current version of Kubernetes.
    """


class WeekDay(str, Enum):
    """
    The day of the week.
    """
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class WorkloadRuntime(str, Enum):
    """
    Determines the type of workload a node can run.
    """
    OCI_CONTAINER = "OCIContainer"
    """
    Nodes will use Kubelet to run standard OCI container workloads.
    """
    WASM_WASI = "WasmWasi"
    """
    Nodes will use Krustlet to run WASM workloads using the WASI provider (Preview).
    """
