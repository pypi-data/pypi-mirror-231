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
    'GetOrchestratorInstanceServiceDetailsResult',
    'AwaitableGetOrchestratorInstanceServiceDetailsResult',
    'get_orchestrator_instance_service_details',
    'get_orchestrator_instance_service_details_output',
]

@pulumi.output_type
class GetOrchestratorInstanceServiceDetailsResult:
    """
    Represents an instance of a orchestrator.
    """
    def __init__(__self__, api_server_endpoint=None, cluster_root_ca=None, controller_details=None, id=None, identity=None, kind=None, location=None, name=None, orchestrator_app_id=None, orchestrator_tenant_id=None, private_link_resource_id=None, provisioning_state=None, resource_guid=None, tags=None, type=None):
        if api_server_endpoint and not isinstance(api_server_endpoint, str):
            raise TypeError("Expected argument 'api_server_endpoint' to be a str")
        pulumi.set(__self__, "api_server_endpoint", api_server_endpoint)
        if cluster_root_ca and not isinstance(cluster_root_ca, str):
            raise TypeError("Expected argument 'cluster_root_ca' to be a str")
        pulumi.set(__self__, "cluster_root_ca", cluster_root_ca)
        if controller_details and not isinstance(controller_details, dict):
            raise TypeError("Expected argument 'controller_details' to be a dict")
        pulumi.set(__self__, "controller_details", controller_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if orchestrator_app_id and not isinstance(orchestrator_app_id, str):
            raise TypeError("Expected argument 'orchestrator_app_id' to be a str")
        pulumi.set(__self__, "orchestrator_app_id", orchestrator_app_id)
        if orchestrator_tenant_id and not isinstance(orchestrator_tenant_id, str):
            raise TypeError("Expected argument 'orchestrator_tenant_id' to be a str")
        pulumi.set(__self__, "orchestrator_tenant_id", orchestrator_tenant_id)
        if private_link_resource_id and not isinstance(private_link_resource_id, str):
            raise TypeError("Expected argument 'private_link_resource_id' to be a str")
        pulumi.set(__self__, "private_link_resource_id", private_link_resource_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_guid and not isinstance(resource_guid, str):
            raise TypeError("Expected argument 'resource_guid' to be a str")
        pulumi.set(__self__, "resource_guid", resource_guid)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="apiServerEndpoint")
    def api_server_endpoint(self) -> Optional[str]:
        """
        K8s APIServer url. Either one of apiServerEndpoint or privateLinkResourceId can be specified
        """
        return pulumi.get(self, "api_server_endpoint")

    @property
    @pulumi.getter(name="clusterRootCA")
    def cluster_root_ca(self) -> Optional[str]:
        """
        RootCA certificate of kubernetes cluster base64 encoded
        """
        return pulumi.get(self, "cluster_root_ca")

    @property
    @pulumi.getter(name="controllerDetails")
    def controller_details(self) -> 'outputs.ControllerDetailsResponse':
        """
        Properties of the controller.
        """
        return pulumi.get(self, "controller_details")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        An identifier that represents the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.OrchestratorIdentityResponse']:
        """
        The identity of the orchestrator
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of workbook. Choices are user and shared.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orchestratorAppId")
    def orchestrator_app_id(self) -> Optional[str]:
        """
        AAD ID used with apiserver
        """
        return pulumi.get(self, "orchestrator_app_id")

    @property
    @pulumi.getter(name="orchestratorTenantId")
    def orchestrator_tenant_id(self) -> Optional[str]:
        """
        TenantID of server App ID
        """
        return pulumi.get(self, "orchestrator_tenant_id")

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[str]:
        """
        private link arm resource id. Either one of apiServerEndpoint or privateLinkResourceId can be specified
        """
        return pulumi.get(self, "private_link_resource_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current state of orchestratorInstance resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> str:
        """
        Resource guid.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetOrchestratorInstanceServiceDetailsResult(GetOrchestratorInstanceServiceDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrchestratorInstanceServiceDetailsResult(
            api_server_endpoint=self.api_server_endpoint,
            cluster_root_ca=self.cluster_root_ca,
            controller_details=self.controller_details,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            location=self.location,
            name=self.name,
            orchestrator_app_id=self.orchestrator_app_id,
            orchestrator_tenant_id=self.orchestrator_tenant_id,
            private_link_resource_id=self.private_link_resource_id,
            provisioning_state=self.provisioning_state,
            resource_guid=self.resource_guid,
            tags=self.tags,
            type=self.type)


def get_orchestrator_instance_service_details(resource_group_name: Optional[str] = None,
                                              resource_name: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrchestratorInstanceServiceDetailsResult:
    """
    Gets details about the orchestrator instance.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource. It must be a minimum of 3 characters, and a maximum of 63.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:delegatednetwork/v20230627preview:getOrchestratorInstanceServiceDetails', __args__, opts=opts, typ=GetOrchestratorInstanceServiceDetailsResult).value

    return AwaitableGetOrchestratorInstanceServiceDetailsResult(
        api_server_endpoint=pulumi.get(__ret__, 'api_server_endpoint'),
        cluster_root_ca=pulumi.get(__ret__, 'cluster_root_ca'),
        controller_details=pulumi.get(__ret__, 'controller_details'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        orchestrator_app_id=pulumi.get(__ret__, 'orchestrator_app_id'),
        orchestrator_tenant_id=pulumi.get(__ret__, 'orchestrator_tenant_id'),
        private_link_resource_id=pulumi.get(__ret__, 'private_link_resource_id'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_guid=pulumi.get(__ret__, 'resource_guid'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_orchestrator_instance_service_details)
def get_orchestrator_instance_service_details_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                     resource_name: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrchestratorInstanceServiceDetailsResult]:
    """
    Gets details about the orchestrator instance.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource. It must be a minimum of 3 characters, and a maximum of 63.
    """
    ...
