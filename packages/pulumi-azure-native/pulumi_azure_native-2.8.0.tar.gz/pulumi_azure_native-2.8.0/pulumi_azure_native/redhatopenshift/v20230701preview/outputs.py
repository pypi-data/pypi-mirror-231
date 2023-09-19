# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'APIServerProfileResponse',
    'ClusterProfileResponse',
    'ConsoleProfileResponse',
    'EffectiveOutboundIPResponse',
    'IngressProfileResponse',
    'LoadBalancerProfileResponse',
    'ManagedOutboundIPsResponse',
    'MasterProfileResponse',
    'NetworkProfileResponse',
    'OutboundIPPrefixResponse',
    'OutboundIPResponse',
    'ServicePrincipalProfileResponse',
    'SystemDataResponse',
    'WorkerProfileResponse',
]

@pulumi.output_type
class APIServerProfileResponse(dict):
    """
    APIServerProfile represents an API server profile.
    """
    def __init__(__self__, *,
                 ip: Optional[str] = None,
                 url: Optional[str] = None,
                 visibility: Optional[str] = None):
        """
        APIServerProfile represents an API server profile.
        :param str ip: The IP of the cluster API server.
        :param str url: The URL to access the cluster API server.
        :param str visibility: API server visibility.
        """
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if visibility is not None:
            pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter
    def ip(self) -> Optional[str]:
        """
        The IP of the cluster API server.
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        The URL to access the cluster API server.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def visibility(self) -> Optional[str]:
        """
        API server visibility.
        """
        return pulumi.get(self, "visibility")


@pulumi.output_type
class ClusterProfileResponse(dict):
    """
    ClusterProfile represents a cluster profile.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fipsValidatedModules":
            suggest = "fips_validated_modules"
        elif key == "pullSecret":
            suggest = "pull_secret"
        elif key == "resourceGroupId":
            suggest = "resource_group_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 domain: Optional[str] = None,
                 fips_validated_modules: Optional[str] = None,
                 pull_secret: Optional[str] = None,
                 resource_group_id: Optional[str] = None,
                 version: Optional[str] = None):
        """
        ClusterProfile represents a cluster profile.
        :param str domain: The domain for the cluster.
        :param str fips_validated_modules: If FIPS validated crypto modules are used
        :param str pull_secret: The pull secret for the cluster.
        :param str resource_group_id: The ID of the cluster resource group.
        :param str version: The version of the cluster.
        """
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if fips_validated_modules is not None:
            pulumi.set(__self__, "fips_validated_modules", fips_validated_modules)
        if pull_secret is not None:
            pulumi.set(__self__, "pull_secret", pull_secret)
        if resource_group_id is not None:
            pulumi.set(__self__, "resource_group_id", resource_group_id)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        """
        The domain for the cluster.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="fipsValidatedModules")
    def fips_validated_modules(self) -> Optional[str]:
        """
        If FIPS validated crypto modules are used
        """
        return pulumi.get(self, "fips_validated_modules")

    @property
    @pulumi.getter(name="pullSecret")
    def pull_secret(self) -> Optional[str]:
        """
        The pull secret for the cluster.
        """
        return pulumi.get(self, "pull_secret")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        """
        The ID of the cluster resource group.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version of the cluster.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class ConsoleProfileResponse(dict):
    """
    ConsoleProfile represents a console profile.
    """
    def __init__(__self__, *,
                 url: Optional[str] = None):
        """
        ConsoleProfile represents a console profile.
        :param str url: The URL to access the cluster console.
        """
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        The URL to access the cluster console.
        """
        return pulumi.get(self, "url")


@pulumi.output_type
class EffectiveOutboundIPResponse(dict):
    """
    EffectiveOutboundIP represents an effective outbound IP resource of the cluster public load balancer.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None):
        """
        EffectiveOutboundIP represents an effective outbound IP resource of the cluster public load balancer.
        :param str id: The fully qualified Azure resource id of an IP address resource.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The fully qualified Azure resource id of an IP address resource.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class IngressProfileResponse(dict):
    """
    IngressProfile represents an ingress profile.
    """
    def __init__(__self__, *,
                 ip: Optional[str] = None,
                 name: Optional[str] = None,
                 visibility: Optional[str] = None):
        """
        IngressProfile represents an ingress profile.
        :param str ip: The IP of the ingress.
        :param str name: The ingress profile name.
        :param str visibility: Ingress visibility.
        """
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if visibility is not None:
            pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter
    def ip(self) -> Optional[str]:
        """
        The IP of the ingress.
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The ingress profile name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def visibility(self) -> Optional[str]:
        """
        Ingress visibility.
        """
        return pulumi.get(self, "visibility")


@pulumi.output_type
class LoadBalancerProfileResponse(dict):
    """
    LoadBalancerProfile represents the profile of the cluster public load balancer.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "effectiveOutboundIps":
            suggest = "effective_outbound_ips"
        elif key == "allocatedOutboundPorts":
            suggest = "allocated_outbound_ports"
        elif key == "managedOutboundIps":
            suggest = "managed_outbound_ips"
        elif key == "outboundIpPrefixes":
            suggest = "outbound_ip_prefixes"
        elif key == "outboundIps":
            suggest = "outbound_ips"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoadBalancerProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoadBalancerProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoadBalancerProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 effective_outbound_ips: Sequence['outputs.EffectiveOutboundIPResponse'],
                 allocated_outbound_ports: Optional[int] = None,
                 managed_outbound_ips: Optional['outputs.ManagedOutboundIPsResponse'] = None,
                 outbound_ip_prefixes: Optional[Sequence['outputs.OutboundIPPrefixResponse']] = None,
                 outbound_ips: Optional[Sequence['outputs.OutboundIPResponse']] = None):
        """
        LoadBalancerProfile represents the profile of the cluster public load balancer.
        :param Sequence['EffectiveOutboundIPResponse'] effective_outbound_ips: The list of effective outbound IP addresses of the public load balancer.
        :param int allocated_outbound_ports: The desired number of allocated SNAT ports per VM. Allowed values are in the range of 0 to 64000 (inclusive). The default value is 1024.
        :param 'ManagedOutboundIPsResponse' managed_outbound_ips: The desired managed outbound IPs for the cluster public load balancer.
        :param Sequence['OutboundIPPrefixResponse'] outbound_ip_prefixes: The desired outbound IP Prefix resources for the cluster load balancer.
        :param Sequence['OutboundIPResponse'] outbound_ips: The desired outbound IP resources for the cluster load balancer.
        """
        pulumi.set(__self__, "effective_outbound_ips", effective_outbound_ips)
        if allocated_outbound_ports is not None:
            pulumi.set(__self__, "allocated_outbound_ports", allocated_outbound_ports)
        if managed_outbound_ips is not None:
            pulumi.set(__self__, "managed_outbound_ips", managed_outbound_ips)
        if outbound_ip_prefixes is not None:
            pulumi.set(__self__, "outbound_ip_prefixes", outbound_ip_prefixes)
        if outbound_ips is not None:
            pulumi.set(__self__, "outbound_ips", outbound_ips)

    @property
    @pulumi.getter(name="effectiveOutboundIps")
    def effective_outbound_ips(self) -> Sequence['outputs.EffectiveOutboundIPResponse']:
        """
        The list of effective outbound IP addresses of the public load balancer.
        """
        return pulumi.get(self, "effective_outbound_ips")

    @property
    @pulumi.getter(name="allocatedOutboundPorts")
    def allocated_outbound_ports(self) -> Optional[int]:
        """
        The desired number of allocated SNAT ports per VM. Allowed values are in the range of 0 to 64000 (inclusive). The default value is 1024.
        """
        return pulumi.get(self, "allocated_outbound_ports")

    @property
    @pulumi.getter(name="managedOutboundIps")
    def managed_outbound_ips(self) -> Optional['outputs.ManagedOutboundIPsResponse']:
        """
        The desired managed outbound IPs for the cluster public load balancer.
        """
        return pulumi.get(self, "managed_outbound_ips")

    @property
    @pulumi.getter(name="outboundIpPrefixes")
    def outbound_ip_prefixes(self) -> Optional[Sequence['outputs.OutboundIPPrefixResponse']]:
        """
        The desired outbound IP Prefix resources for the cluster load balancer.
        """
        return pulumi.get(self, "outbound_ip_prefixes")

    @property
    @pulumi.getter(name="outboundIps")
    def outbound_ips(self) -> Optional[Sequence['outputs.OutboundIPResponse']]:
        """
        The desired outbound IP resources for the cluster load balancer.
        """
        return pulumi.get(self, "outbound_ips")


@pulumi.output_type
class ManagedOutboundIPsResponse(dict):
    """
    ManagedOutboundIPs represents the desired managed outbound IPs for the cluster public load balancer.
    """
    def __init__(__self__, *,
                 count: Optional[int] = None):
        """
        ManagedOutboundIPs represents the desired managed outbound IPs for the cluster public load balancer.
        :param int count: Count represents the desired number of IPv4 outbound IPs created and managed by Azure for the cluster public load balancer.  Allowed values are in the range of 1 - 20.  The default value is 1.
        """
        if count is not None:
            pulumi.set(__self__, "count", count)

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        Count represents the desired number of IPv4 outbound IPs created and managed by Azure for the cluster public load balancer.  Allowed values are in the range of 1 - 20.  The default value is 1.
        """
        return pulumi.get(self, "count")


@pulumi.output_type
class MasterProfileResponse(dict):
    """
    MasterProfile represents a master profile.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "diskEncryptionSetId":
            suggest = "disk_encryption_set_id"
        elif key == "encryptionAtHost":
            suggest = "encryption_at_host"
        elif key == "subnetId":
            suggest = "subnet_id"
        elif key == "vmSize":
            suggest = "vm_size"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MasterProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MasterProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MasterProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 disk_encryption_set_id: Optional[str] = None,
                 encryption_at_host: Optional[str] = None,
                 subnet_id: Optional[str] = None,
                 vm_size: Optional[str] = None):
        """
        MasterProfile represents a master profile.
        :param str disk_encryption_set_id: The resource ID of an associated DiskEncryptionSet, if applicable.
        :param str encryption_at_host: Whether master virtual machines are encrypted at host.
        :param str subnet_id: The Azure resource ID of the master subnet.
        :param str vm_size: The size of the master VMs.
        """
        if disk_encryption_set_id is not None:
            pulumi.set(__self__, "disk_encryption_set_id", disk_encryption_set_id)
        if encryption_at_host is not None:
            pulumi.set(__self__, "encryption_at_host", encryption_at_host)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if vm_size is not None:
            pulumi.set(__self__, "vm_size", vm_size)

    @property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[str]:
        """
        The resource ID of an associated DiskEncryptionSet, if applicable.
        """
        return pulumi.get(self, "disk_encryption_set_id")

    @property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[str]:
        """
        Whether master virtual machines are encrypted at host.
        """
        return pulumi.get(self, "encryption_at_host")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[str]:
        """
        The Azure resource ID of the master subnet.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[str]:
        """
        The size of the master VMs.
        """
        return pulumi.get(self, "vm_size")


@pulumi.output_type
class NetworkProfileResponse(dict):
    """
    NetworkProfile represents a network profile.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "loadBalancerProfile":
            suggest = "load_balancer_profile"
        elif key == "outboundType":
            suggest = "outbound_type"
        elif key == "podCidr":
            suggest = "pod_cidr"
        elif key == "serviceCidr":
            suggest = "service_cidr"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NetworkProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NetworkProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NetworkProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 load_balancer_profile: Optional['outputs.LoadBalancerProfileResponse'] = None,
                 outbound_type: Optional[str] = None,
                 pod_cidr: Optional[str] = None,
                 service_cidr: Optional[str] = None):
        """
        NetworkProfile represents a network profile.
        :param 'LoadBalancerProfileResponse' load_balancer_profile: The cluster load balancer profile.
        :param str outbound_type: The OutboundType used for egress traffic.
        :param str pod_cidr: The CIDR used for OpenShift/Kubernetes Pods.
        :param str service_cidr: The CIDR used for OpenShift/Kubernetes Services.
        """
        if load_balancer_profile is not None:
            pulumi.set(__self__, "load_balancer_profile", load_balancer_profile)
        if outbound_type is not None:
            pulumi.set(__self__, "outbound_type", outbound_type)
        if pod_cidr is not None:
            pulumi.set(__self__, "pod_cidr", pod_cidr)
        if service_cidr is not None:
            pulumi.set(__self__, "service_cidr", service_cidr)

    @property
    @pulumi.getter(name="loadBalancerProfile")
    def load_balancer_profile(self) -> Optional['outputs.LoadBalancerProfileResponse']:
        """
        The cluster load balancer profile.
        """
        return pulumi.get(self, "load_balancer_profile")

    @property
    @pulumi.getter(name="outboundType")
    def outbound_type(self) -> Optional[str]:
        """
        The OutboundType used for egress traffic.
        """
        return pulumi.get(self, "outbound_type")

    @property
    @pulumi.getter(name="podCidr")
    def pod_cidr(self) -> Optional[str]:
        """
        The CIDR used for OpenShift/Kubernetes Pods.
        """
        return pulumi.get(self, "pod_cidr")

    @property
    @pulumi.getter(name="serviceCidr")
    def service_cidr(self) -> Optional[str]:
        """
        The CIDR used for OpenShift/Kubernetes Services.
        """
        return pulumi.get(self, "service_cidr")


@pulumi.output_type
class OutboundIPPrefixResponse(dict):
    """
    OutboundIPPrefix represents a desired outbound IP Prefix resource for the cluster load balancer.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None):
        """
        OutboundIPPrefix represents a desired outbound IP Prefix resource for the cluster load balancer.
        :param str id: The fully qualified Azure resource id of an IP Prefix resource.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The fully qualified Azure resource id of an IP Prefix resource.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class OutboundIPResponse(dict):
    """
    OutboundIP represents a desired outbound IP resource for the cluster load balancer.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None):
        """
        OutboundIP represents a desired outbound IP resource for the cluster load balancer.
        :param str id: The fully qualified Azure resource id of the IP address resource.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The fully qualified Azure resource id of the IP address resource.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class ServicePrincipalProfileResponse(dict):
    """
    ServicePrincipalProfile represents a service principal profile.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "clientSecret":
            suggest = "client_secret"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServicePrincipalProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServicePrincipalProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServicePrincipalProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: Optional[str] = None,
                 client_secret: Optional[str] = None):
        """
        ServicePrincipalProfile represents a service principal profile.
        :param str client_id: The client ID used for the cluster.
        :param str client_secret: The client secret used for the cluster.
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_secret is not None:
            pulumi.set(__self__, "client_secret", client_secret)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[str]:
        """
        The client ID used for the cluster.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[str]:
        """
        The client secret used for the cluster.
        """
        return pulumi.get(self, "client_secret")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


@pulumi.output_type
class WorkerProfileResponse(dict):
    """
    WorkerProfile represents a worker profile.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "diskEncryptionSetId":
            suggest = "disk_encryption_set_id"
        elif key == "diskSizeGB":
            suggest = "disk_size_gb"
        elif key == "encryptionAtHost":
            suggest = "encryption_at_host"
        elif key == "subnetId":
            suggest = "subnet_id"
        elif key == "vmSize":
            suggest = "vm_size"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkerProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkerProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkerProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 count: Optional[int] = None,
                 disk_encryption_set_id: Optional[str] = None,
                 disk_size_gb: Optional[int] = None,
                 encryption_at_host: Optional[str] = None,
                 name: Optional[str] = None,
                 subnet_id: Optional[str] = None,
                 vm_size: Optional[str] = None):
        """
        WorkerProfile represents a worker profile.
        :param int count: The number of worker VMs.
        :param str disk_encryption_set_id: The resource ID of an associated DiskEncryptionSet, if applicable.
        :param int disk_size_gb: The disk size of the worker VMs.
        :param str encryption_at_host: Whether master virtual machines are encrypted at host.
        :param str name: The worker profile name.
        :param str subnet_id: The Azure resource ID of the worker subnet.
        :param str vm_size: The size of the worker VMs.
        """
        if count is not None:
            pulumi.set(__self__, "count", count)
        if disk_encryption_set_id is not None:
            pulumi.set(__self__, "disk_encryption_set_id", disk_encryption_set_id)
        if disk_size_gb is not None:
            pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if encryption_at_host is not None:
            pulumi.set(__self__, "encryption_at_host", encryption_at_host)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if vm_size is not None:
            pulumi.set(__self__, "vm_size", vm_size)

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        The number of worker VMs.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[str]:
        """
        The resource ID of an associated DiskEncryptionSet, if applicable.
        """
        return pulumi.get(self, "disk_encryption_set_id")

    @property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[int]:
        """
        The disk size of the worker VMs.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="encryptionAtHost")
    def encryption_at_host(self) -> Optional[str]:
        """
        Whether master virtual machines are encrypted at host.
        """
        return pulumi.get(self, "encryption_at_host")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The worker profile name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[str]:
        """
        The Azure resource ID of the worker subnet.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[str]:
        """
        The size of the worker VMs.
        """
        return pulumi.get(self, "vm_size")


