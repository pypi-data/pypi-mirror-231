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

__all__ = [
    'GetPrivateCloudResult',
    'AwaitableGetPrivateCloudResult',
    'get_private_cloud',
    'get_private_cloud_output',
]

@pulumi.output_type
class GetPrivateCloudResult:
    """
    A private cloud resource
    """
    def __init__(__self__, availability=None, circuit=None, encryption=None, endpoints=None, external_cloud_links=None, id=None, identity=None, identity_sources=None, internet=None, location=None, management_cluster=None, management_network=None, name=None, network_block=None, nsx_public_ip_quota_raised=None, nsxt_certificate_thumbprint=None, nsxt_password=None, provisioning_network=None, provisioning_state=None, secondary_circuit=None, sku=None, tags=None, type=None, vcenter_certificate_thumbprint=None, vcenter_password=None, vmotion_network=None):
        if availability and not isinstance(availability, dict):
            raise TypeError("Expected argument 'availability' to be a dict")
        pulumi.set(__self__, "availability", availability)
        if circuit and not isinstance(circuit, dict):
            raise TypeError("Expected argument 'circuit' to be a dict")
        pulumi.set(__self__, "circuit", circuit)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if endpoints and not isinstance(endpoints, dict):
            raise TypeError("Expected argument 'endpoints' to be a dict")
        pulumi.set(__self__, "endpoints", endpoints)
        if external_cloud_links and not isinstance(external_cloud_links, list):
            raise TypeError("Expected argument 'external_cloud_links' to be a list")
        pulumi.set(__self__, "external_cloud_links", external_cloud_links)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if identity_sources and not isinstance(identity_sources, list):
            raise TypeError("Expected argument 'identity_sources' to be a list")
        pulumi.set(__self__, "identity_sources", identity_sources)
        if internet and not isinstance(internet, str):
            raise TypeError("Expected argument 'internet' to be a str")
        pulumi.set(__self__, "internet", internet)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if management_cluster and not isinstance(management_cluster, dict):
            raise TypeError("Expected argument 'management_cluster' to be a dict")
        pulumi.set(__self__, "management_cluster", management_cluster)
        if management_network and not isinstance(management_network, str):
            raise TypeError("Expected argument 'management_network' to be a str")
        pulumi.set(__self__, "management_network", management_network)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_block and not isinstance(network_block, str):
            raise TypeError("Expected argument 'network_block' to be a str")
        pulumi.set(__self__, "network_block", network_block)
        if nsx_public_ip_quota_raised and not isinstance(nsx_public_ip_quota_raised, str):
            raise TypeError("Expected argument 'nsx_public_ip_quota_raised' to be a str")
        pulumi.set(__self__, "nsx_public_ip_quota_raised", nsx_public_ip_quota_raised)
        if nsxt_certificate_thumbprint and not isinstance(nsxt_certificate_thumbprint, str):
            raise TypeError("Expected argument 'nsxt_certificate_thumbprint' to be a str")
        pulumi.set(__self__, "nsxt_certificate_thumbprint", nsxt_certificate_thumbprint)
        if nsxt_password and not isinstance(nsxt_password, str):
            raise TypeError("Expected argument 'nsxt_password' to be a str")
        pulumi.set(__self__, "nsxt_password", nsxt_password)
        if provisioning_network and not isinstance(provisioning_network, str):
            raise TypeError("Expected argument 'provisioning_network' to be a str")
        pulumi.set(__self__, "provisioning_network", provisioning_network)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if secondary_circuit and not isinstance(secondary_circuit, dict):
            raise TypeError("Expected argument 'secondary_circuit' to be a dict")
        pulumi.set(__self__, "secondary_circuit", secondary_circuit)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vcenter_certificate_thumbprint and not isinstance(vcenter_certificate_thumbprint, str):
            raise TypeError("Expected argument 'vcenter_certificate_thumbprint' to be a str")
        pulumi.set(__self__, "vcenter_certificate_thumbprint", vcenter_certificate_thumbprint)
        if vcenter_password and not isinstance(vcenter_password, str):
            raise TypeError("Expected argument 'vcenter_password' to be a str")
        pulumi.set(__self__, "vcenter_password", vcenter_password)
        if vmotion_network and not isinstance(vmotion_network, str):
            raise TypeError("Expected argument 'vmotion_network' to be a str")
        pulumi.set(__self__, "vmotion_network", vmotion_network)

    @property
    @pulumi.getter
    def availability(self) -> Optional['outputs.AvailabilityPropertiesResponse']:
        """
        Properties describing how the cloud is distributed across availability zones
        """
        return pulumi.get(self, "availability")

    @property
    @pulumi.getter
    def circuit(self) -> Optional['outputs.CircuitResponse']:
        """
        An ExpressRoute Circuit
        """
        return pulumi.get(self, "circuit")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.EncryptionResponse']:
        """
        Customer managed key encryption, can be enabled or disabled
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def endpoints(self) -> 'outputs.EndpointsResponse':
        """
        The endpoints
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="externalCloudLinks")
    def external_cloud_links(self) -> Sequence[str]:
        """
        Array of cloud link IDs from other clouds that connect to this one
        """
        return pulumi.get(self, "external_cloud_links")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.PrivateCloudIdentityResponse']:
        """
        The identity of the private cloud, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="identitySources")
    def identity_sources(self) -> Optional[Sequence['outputs.IdentitySourceResponse']]:
        """
        vCenter Single Sign On Identity Sources
        """
        return pulumi.get(self, "identity_sources")

    @property
    @pulumi.getter
    def internet(self) -> Optional[str]:
        """
        Connectivity to internet is enabled or disabled
        """
        return pulumi.get(self, "internet")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementCluster")
    def management_cluster(self) -> 'outputs.ManagementClusterResponse':
        """
        The default cluster used for management
        """
        return pulumi.get(self, "management_cluster")

    @property
    @pulumi.getter(name="managementNetwork")
    def management_network(self) -> str:
        """
        Network used to access vCenter Server and NSX-T Manager
        """
        return pulumi.get(self, "management_network")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkBlock")
    def network_block(self) -> str:
        """
        The block of addresses should be unique across VNet in your subscription as well as on-premise. Make sure the CIDR format is conformed to (A.B.C.D/X) where A,B,C,D are between 0 and 255, and X is between 0 and 22
        """
        return pulumi.get(self, "network_block")

    @property
    @pulumi.getter(name="nsxPublicIpQuotaRaised")
    def nsx_public_ip_quota_raised(self) -> str:
        """
        Flag to indicate whether the private cloud has the quota for provisioned NSX Public IP count raised from 64 to 1024
        """
        return pulumi.get(self, "nsx_public_ip_quota_raised")

    @property
    @pulumi.getter(name="nsxtCertificateThumbprint")
    def nsxt_certificate_thumbprint(self) -> str:
        """
        Thumbprint of the NSX-T Manager SSL certificate
        """
        return pulumi.get(self, "nsxt_certificate_thumbprint")

    @property
    @pulumi.getter(name="nsxtPassword")
    def nsxt_password(self) -> Optional[str]:
        """
        Optionally, set the NSX-T Manager password when the private cloud is created
        """
        return pulumi.get(self, "nsxt_password")

    @property
    @pulumi.getter(name="provisioningNetwork")
    def provisioning_network(self) -> str:
        """
        Used for virtual machine cold migration, cloning, and snapshot migration
        """
        return pulumi.get(self, "provisioning_network")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="secondaryCircuit")
    def secondary_circuit(self) -> Optional['outputs.CircuitResponse']:
        """
        A secondary expressRoute circuit from a separate AZ. Only present in a stretched private cloud
        """
        return pulumi.get(self, "secondary_circuit")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        The private cloud SKU
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vcenterCertificateThumbprint")
    def vcenter_certificate_thumbprint(self) -> str:
        """
        Thumbprint of the vCenter Server SSL certificate
        """
        return pulumi.get(self, "vcenter_certificate_thumbprint")

    @property
    @pulumi.getter(name="vcenterPassword")
    def vcenter_password(self) -> Optional[str]:
        """
        Optionally, set the vCenter admin password when the private cloud is created
        """
        return pulumi.get(self, "vcenter_password")

    @property
    @pulumi.getter(name="vmotionNetwork")
    def vmotion_network(self) -> str:
        """
        Used for live migration of virtual machines
        """
        return pulumi.get(self, "vmotion_network")


class AwaitableGetPrivateCloudResult(GetPrivateCloudResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateCloudResult(
            availability=self.availability,
            circuit=self.circuit,
            encryption=self.encryption,
            endpoints=self.endpoints,
            external_cloud_links=self.external_cloud_links,
            id=self.id,
            identity=self.identity,
            identity_sources=self.identity_sources,
            internet=self.internet,
            location=self.location,
            management_cluster=self.management_cluster,
            management_network=self.management_network,
            name=self.name,
            network_block=self.network_block,
            nsx_public_ip_quota_raised=self.nsx_public_ip_quota_raised,
            nsxt_certificate_thumbprint=self.nsxt_certificate_thumbprint,
            nsxt_password=self.nsxt_password,
            provisioning_network=self.provisioning_network,
            provisioning_state=self.provisioning_state,
            secondary_circuit=self.secondary_circuit,
            sku=self.sku,
            tags=self.tags,
            type=self.type,
            vcenter_certificate_thumbprint=self.vcenter_certificate_thumbprint,
            vcenter_password=self.vcenter_password,
            vmotion_network=self.vmotion_network)


def get_private_cloud(private_cloud_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateCloudResult:
    """
    A private cloud resource


    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['privateCloudName'] = private_cloud_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:avs/v20220501:getPrivateCloud', __args__, opts=opts, typ=GetPrivateCloudResult).value

    return AwaitableGetPrivateCloudResult(
        availability=pulumi.get(__ret__, 'availability'),
        circuit=pulumi.get(__ret__, 'circuit'),
        encryption=pulumi.get(__ret__, 'encryption'),
        endpoints=pulumi.get(__ret__, 'endpoints'),
        external_cloud_links=pulumi.get(__ret__, 'external_cloud_links'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        identity_sources=pulumi.get(__ret__, 'identity_sources'),
        internet=pulumi.get(__ret__, 'internet'),
        location=pulumi.get(__ret__, 'location'),
        management_cluster=pulumi.get(__ret__, 'management_cluster'),
        management_network=pulumi.get(__ret__, 'management_network'),
        name=pulumi.get(__ret__, 'name'),
        network_block=pulumi.get(__ret__, 'network_block'),
        nsx_public_ip_quota_raised=pulumi.get(__ret__, 'nsx_public_ip_quota_raised'),
        nsxt_certificate_thumbprint=pulumi.get(__ret__, 'nsxt_certificate_thumbprint'),
        nsxt_password=pulumi.get(__ret__, 'nsxt_password'),
        provisioning_network=pulumi.get(__ret__, 'provisioning_network'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        secondary_circuit=pulumi.get(__ret__, 'secondary_circuit'),
        sku=pulumi.get(__ret__, 'sku'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        vcenter_certificate_thumbprint=pulumi.get(__ret__, 'vcenter_certificate_thumbprint'),
        vcenter_password=pulumi.get(__ret__, 'vcenter_password'),
        vmotion_network=pulumi.get(__ret__, 'vmotion_network'))


@_utilities.lift_output_func(get_private_cloud)
def get_private_cloud_output(private_cloud_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateCloudResult]:
    """
    A private cloud resource


    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
