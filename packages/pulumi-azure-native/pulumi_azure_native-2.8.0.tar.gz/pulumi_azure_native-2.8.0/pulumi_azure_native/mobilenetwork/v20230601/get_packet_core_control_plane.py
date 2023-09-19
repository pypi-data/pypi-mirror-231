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
    'GetPacketCoreControlPlaneResult',
    'AwaitableGetPacketCoreControlPlaneResult',
    'get_packet_core_control_plane',
    'get_packet_core_control_plane_output',
]

@pulumi.output_type
class GetPacketCoreControlPlaneResult:
    """
    Packet core control plane resource.
    """
    def __init__(__self__, control_plane_access_interface=None, core_network_technology=None, diagnostics_upload=None, id=None, identity=None, installation=None, installed_version=None, interop_settings=None, local_diagnostics_access=None, location=None, name=None, platform=None, provisioning_state=None, rollback_version=None, sites=None, sku=None, system_data=None, tags=None, type=None, ue_mtu=None, version=None):
        if control_plane_access_interface and not isinstance(control_plane_access_interface, dict):
            raise TypeError("Expected argument 'control_plane_access_interface' to be a dict")
        pulumi.set(__self__, "control_plane_access_interface", control_plane_access_interface)
        if core_network_technology and not isinstance(core_network_technology, str):
            raise TypeError("Expected argument 'core_network_technology' to be a str")
        pulumi.set(__self__, "core_network_technology", core_network_technology)
        if diagnostics_upload and not isinstance(diagnostics_upload, dict):
            raise TypeError("Expected argument 'diagnostics_upload' to be a dict")
        pulumi.set(__self__, "diagnostics_upload", diagnostics_upload)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if installation and not isinstance(installation, dict):
            raise TypeError("Expected argument 'installation' to be a dict")
        pulumi.set(__self__, "installation", installation)
        if installed_version and not isinstance(installed_version, str):
            raise TypeError("Expected argument 'installed_version' to be a str")
        pulumi.set(__self__, "installed_version", installed_version)
        if interop_settings and not isinstance(interop_settings, dict):
            raise TypeError("Expected argument 'interop_settings' to be a dict")
        pulumi.set(__self__, "interop_settings", interop_settings)
        if local_diagnostics_access and not isinstance(local_diagnostics_access, dict):
            raise TypeError("Expected argument 'local_diagnostics_access' to be a dict")
        pulumi.set(__self__, "local_diagnostics_access", local_diagnostics_access)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if platform and not isinstance(platform, dict):
            raise TypeError("Expected argument 'platform' to be a dict")
        pulumi.set(__self__, "platform", platform)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rollback_version and not isinstance(rollback_version, str):
            raise TypeError("Expected argument 'rollback_version' to be a str")
        pulumi.set(__self__, "rollback_version", rollback_version)
        if sites and not isinstance(sites, list):
            raise TypeError("Expected argument 'sites' to be a list")
        pulumi.set(__self__, "sites", sites)
        if sku and not isinstance(sku, str):
            raise TypeError("Expected argument 'sku' to be a str")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if ue_mtu and not isinstance(ue_mtu, int):
            raise TypeError("Expected argument 'ue_mtu' to be a int")
        pulumi.set(__self__, "ue_mtu", ue_mtu)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="controlPlaneAccessInterface")
    def control_plane_access_interface(self) -> 'outputs.InterfacePropertiesResponse':
        """
        The control plane interface on the access network. For 5G networks, this is the N2 interface. For 4G networks, this is the S1-MME interface.
        """
        return pulumi.get(self, "control_plane_access_interface")

    @property
    @pulumi.getter(name="coreNetworkTechnology")
    def core_network_technology(self) -> Optional[str]:
        """
        The core network technology generation (5G core or EPC / 4G core).
        """
        return pulumi.get(self, "core_network_technology")

    @property
    @pulumi.getter(name="diagnosticsUpload")
    def diagnostics_upload(self) -> Optional['outputs.DiagnosticsUploadConfigurationResponse']:
        """
        Configuration for uploading packet core diagnostics
        """
        return pulumi.get(self, "diagnostics_upload")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        The identity used to retrieve the ingress certificate from Azure key vault.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def installation(self) -> Optional['outputs.InstallationResponse']:
        """
        The installation state of the packet core control plane resource.
        """
        return pulumi.get(self, "installation")

    @property
    @pulumi.getter(name="installedVersion")
    def installed_version(self) -> str:
        """
        The currently installed version of the packet core software.
        """
        return pulumi.get(self, "installed_version")

    @property
    @pulumi.getter(name="interopSettings")
    def interop_settings(self) -> Optional[Any]:
        """
        Settings to allow interoperability with third party components e.g. RANs and UEs.
        """
        return pulumi.get(self, "interop_settings")

    @property
    @pulumi.getter(name="localDiagnosticsAccess")
    def local_diagnostics_access(self) -> 'outputs.LocalDiagnosticsAccessConfigurationResponse':
        """
        The kubernetes ingress configuration to control access to packet core diagnostics over local APIs.
        """
        return pulumi.get(self, "local_diagnostics_access")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def platform(self) -> 'outputs.PlatformConfigurationResponse':
        """
        The platform where the packet core is deployed.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the packet core control plane resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rollbackVersion")
    def rollback_version(self) -> str:
        """
        The previous version of the packet core software that was deployed. Used when performing the rollback action.
        """
        return pulumi.get(self, "rollback_version")

    @property
    @pulumi.getter
    def sites(self) -> Sequence['outputs.SiteResourceIdResponse']:
        """
        Site(s) under which this packet core control plane should be deployed. The sites must be in the same location as the packet core control plane.
        """
        return pulumi.get(self, "sites")

    @property
    @pulumi.getter
    def sku(self) -> str:
        """
        The SKU defining the throughput and SIM allowances for this packet core control plane deployment.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="ueMtu")
    def ue_mtu(self) -> Optional[int]:
        """
        The MTU (in bytes) signaled to the UE. The same MTU is set on the user plane data links for all data networks. The MTU set on the user plane access link is calculated to be 60 bytes greater than this value to allow for GTP encapsulation.
        """
        return pulumi.get(self, "ue_mtu")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The desired version of the packet core software.
        """
        return pulumi.get(self, "version")


class AwaitableGetPacketCoreControlPlaneResult(GetPacketCoreControlPlaneResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPacketCoreControlPlaneResult(
            control_plane_access_interface=self.control_plane_access_interface,
            core_network_technology=self.core_network_technology,
            diagnostics_upload=self.diagnostics_upload,
            id=self.id,
            identity=self.identity,
            installation=self.installation,
            installed_version=self.installed_version,
            interop_settings=self.interop_settings,
            local_diagnostics_access=self.local_diagnostics_access,
            location=self.location,
            name=self.name,
            platform=self.platform,
            provisioning_state=self.provisioning_state,
            rollback_version=self.rollback_version,
            sites=self.sites,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            ue_mtu=self.ue_mtu,
            version=self.version)


def get_packet_core_control_plane(packet_core_control_plane_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPacketCoreControlPlaneResult:
    """
    Gets information about the specified packet core control plane.


    :param str packet_core_control_plane_name: The name of the packet core control plane.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['packetCoreControlPlaneName'] = packet_core_control_plane_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:mobilenetwork/v20230601:getPacketCoreControlPlane', __args__, opts=opts, typ=GetPacketCoreControlPlaneResult).value

    return AwaitableGetPacketCoreControlPlaneResult(
        control_plane_access_interface=pulumi.get(__ret__, 'control_plane_access_interface'),
        core_network_technology=pulumi.get(__ret__, 'core_network_technology'),
        diagnostics_upload=pulumi.get(__ret__, 'diagnostics_upload'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        installation=pulumi.get(__ret__, 'installation'),
        installed_version=pulumi.get(__ret__, 'installed_version'),
        interop_settings=pulumi.get(__ret__, 'interop_settings'),
        local_diagnostics_access=pulumi.get(__ret__, 'local_diagnostics_access'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        platform=pulumi.get(__ret__, 'platform'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        rollback_version=pulumi.get(__ret__, 'rollback_version'),
        sites=pulumi.get(__ret__, 'sites'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        ue_mtu=pulumi.get(__ret__, 'ue_mtu'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_packet_core_control_plane)
def get_packet_core_control_plane_output(packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPacketCoreControlPlaneResult]:
    """
    Gets information about the specified packet core control plane.


    :param str packet_core_control_plane_name: The name of the packet core control plane.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
