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
    'GetLabPlanResult',
    'AwaitableGetLabPlanResult',
    'get_lab_plan',
    'get_lab_plan_output',
]

@pulumi.output_type
class GetLabPlanResult:
    """
    Lab Plans act as a permission container for creating labs via labs.azure.com. Additionally, they can provide a set of default configurations that will apply at the time of creating a lab, but these defaults can still be overwritten.
    """
    def __init__(__self__, allowed_regions=None, default_auto_shutdown_profile=None, default_connection_profile=None, default_network_profile=None, id=None, identity=None, linked_lms_instance=None, location=None, name=None, provisioning_state=None, resource_operation_error=None, shared_gallery_id=None, support_info=None, system_data=None, tags=None, type=None):
        if allowed_regions and not isinstance(allowed_regions, list):
            raise TypeError("Expected argument 'allowed_regions' to be a list")
        pulumi.set(__self__, "allowed_regions", allowed_regions)
        if default_auto_shutdown_profile and not isinstance(default_auto_shutdown_profile, dict):
            raise TypeError("Expected argument 'default_auto_shutdown_profile' to be a dict")
        pulumi.set(__self__, "default_auto_shutdown_profile", default_auto_shutdown_profile)
        if default_connection_profile and not isinstance(default_connection_profile, dict):
            raise TypeError("Expected argument 'default_connection_profile' to be a dict")
        pulumi.set(__self__, "default_connection_profile", default_connection_profile)
        if default_network_profile and not isinstance(default_network_profile, dict):
            raise TypeError("Expected argument 'default_network_profile' to be a dict")
        pulumi.set(__self__, "default_network_profile", default_network_profile)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if linked_lms_instance and not isinstance(linked_lms_instance, str):
            raise TypeError("Expected argument 'linked_lms_instance' to be a str")
        pulumi.set(__self__, "linked_lms_instance", linked_lms_instance)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_operation_error and not isinstance(resource_operation_error, dict):
            raise TypeError("Expected argument 'resource_operation_error' to be a dict")
        pulumi.set(__self__, "resource_operation_error", resource_operation_error)
        if shared_gallery_id and not isinstance(shared_gallery_id, str):
            raise TypeError("Expected argument 'shared_gallery_id' to be a str")
        pulumi.set(__self__, "shared_gallery_id", shared_gallery_id)
        if support_info and not isinstance(support_info, dict):
            raise TypeError("Expected argument 'support_info' to be a dict")
        pulumi.set(__self__, "support_info", support_info)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(self) -> Optional[Sequence[str]]:
        """
        The allowed regions for the lab creator to use when creating labs using this lab plan.
        """
        return pulumi.get(self, "allowed_regions")

    @property
    @pulumi.getter(name="defaultAutoShutdownProfile")
    def default_auto_shutdown_profile(self) -> Optional['outputs.AutoShutdownProfileResponse']:
        """
        The default lab shutdown profile. This can be changed on a lab resource and only provides a default profile.
        """
        return pulumi.get(self, "default_auto_shutdown_profile")

    @property
    @pulumi.getter(name="defaultConnectionProfile")
    def default_connection_profile(self) -> Optional['outputs.ConnectionProfileResponse']:
        """
        The default lab connection profile. This can be changed on a lab resource and only provides a default profile.
        """
        return pulumi.get(self, "default_connection_profile")

    @property
    @pulumi.getter(name="defaultNetworkProfile")
    def default_network_profile(self) -> Optional['outputs.LabPlanNetworkProfileResponse']:
        """
        The lab plan network profile. To enforce lab network policies they must be defined here and cannot be changed when there are existing labs associated with this lab plan.
        """
        return pulumi.get(self, "default_network_profile")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        Managed Identity Information
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="linkedLmsInstance")
    def linked_lms_instance(self) -> Optional[str]:
        """
        Base Url of the lms instance this lab plan can link lab rosters against.
        """
        return pulumi.get(self, "linked_lms_instance")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Current provisioning state of the lab plan.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceOperationError")
    def resource_operation_error(self) -> 'outputs.ResourceOperationErrorResponse':
        """
        Error details of last operation done on lab plan.
        """
        return pulumi.get(self, "resource_operation_error")

    @property
    @pulumi.getter(name="sharedGalleryId")
    def shared_gallery_id(self) -> Optional[str]:
        """
        Resource ID of the Shared Image Gallery attached to this lab plan. When saving a lab template virtual machine image it will be persisted in this gallery. Shared images from the gallery can be made available to use when creating new labs.
        """
        return pulumi.get(self, "shared_gallery_id")

    @property
    @pulumi.getter(name="supportInfo")
    def support_info(self) -> Optional['outputs.SupportInfoResponse']:
        """
        Support contact information and instructions for users of the lab plan. This information is displayed to lab owners and virtual machine users for all labs in the lab plan.
        """
        return pulumi.get(self, "support_info")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the lab plan.
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


class AwaitableGetLabPlanResult(GetLabPlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLabPlanResult(
            allowed_regions=self.allowed_regions,
            default_auto_shutdown_profile=self.default_auto_shutdown_profile,
            default_connection_profile=self.default_connection_profile,
            default_network_profile=self.default_network_profile,
            id=self.id,
            identity=self.identity,
            linked_lms_instance=self.linked_lms_instance,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            resource_operation_error=self.resource_operation_error,
            shared_gallery_id=self.shared_gallery_id,
            support_info=self.support_info,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_lab_plan(lab_plan_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLabPlanResult:
    """
    Retrieves the properties of a Lab Plan.


    :param str lab_plan_name: The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['labPlanName'] = lab_plan_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:labservices/v20230607:getLabPlan', __args__, opts=opts, typ=GetLabPlanResult).value

    return AwaitableGetLabPlanResult(
        allowed_regions=pulumi.get(__ret__, 'allowed_regions'),
        default_auto_shutdown_profile=pulumi.get(__ret__, 'default_auto_shutdown_profile'),
        default_connection_profile=pulumi.get(__ret__, 'default_connection_profile'),
        default_network_profile=pulumi.get(__ret__, 'default_network_profile'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        linked_lms_instance=pulumi.get(__ret__, 'linked_lms_instance'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_operation_error=pulumi.get(__ret__, 'resource_operation_error'),
        shared_gallery_id=pulumi.get(__ret__, 'shared_gallery_id'),
        support_info=pulumi.get(__ret__, 'support_info'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_lab_plan)
def get_lab_plan_output(lab_plan_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLabPlanResult]:
    """
    Retrieves the properties of a Lab Plan.


    :param str lab_plan_name: The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
