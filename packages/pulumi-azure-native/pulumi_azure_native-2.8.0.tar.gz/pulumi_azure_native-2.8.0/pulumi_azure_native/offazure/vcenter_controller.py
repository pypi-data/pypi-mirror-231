# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = ['VcenterControllerArgs', 'VcenterController']

@pulumi.input_type
class VcenterControllerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 site_name: pulumi.Input[str],
                 fqdn: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 run_as_account_id: Optional[pulumi.Input[str]] = None,
                 vcenter_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VcenterController resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] site_name: Site name
        :param pulumi.Input[str] fqdn: Gets or sets the FQDN/IPAddress of the vCenter.
        :param pulumi.Input[str] friendly_name: Gets or sets the friendly name of the vCenter.
        :param pulumi.Input[str] port: Gets or sets the port of the vCenter.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the last operation.
        :param pulumi.Input[str] run_as_account_id: Gets or sets the run as account ID of the vCenter.
        :param pulumi.Input[str] vcenter_name:  VCenters name
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "site_name", site_name)
        if fqdn is not None:
            pulumi.set(__self__, "fqdn", fqdn)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if run_as_account_id is not None:
            pulumi.set(__self__, "run_as_account_id", run_as_account_id)
        if vcenter_name is not None:
            pulumi.set(__self__, "vcenter_name", vcenter_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Input[str]:
        """
        Site name
        """
        return pulumi.get(self, "site_name")

    @site_name.setter
    def site_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "site_name", value)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the FQDN/IPAddress of the vCenter.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the friendly name of the vCenter.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the port of the vCenter.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ProvisioningState']]]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the run as account ID of the vCenter.
        """
        return pulumi.get(self, "run_as_account_id")

    @run_as_account_id.setter
    def run_as_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_as_account_id", value)

    @property
    @pulumi.getter(name="vcenterName")
    def vcenter_name(self) -> Optional[pulumi.Input[str]]:
        """
         VCenters name
        """
        return pulumi.get(self, "vcenter_name")

    @vcenter_name.setter
    def vcenter_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vcenter_name", value)


class VcenterController(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_as_account_id: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 vcenter_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A vcenter resource belonging to a site resource.
        Azure REST API version: 2023-06-06.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fqdn: Gets or sets the FQDN/IPAddress of the vCenter.
        :param pulumi.Input[str] friendly_name: Gets or sets the friendly name of the vCenter.
        :param pulumi.Input[str] port: Gets or sets the port of the vCenter.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the last operation.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] run_as_account_id: Gets or sets the run as account ID of the vCenter.
        :param pulumi.Input[str] site_name: Site name
        :param pulumi.Input[str] vcenter_name:  VCenters name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VcenterControllerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A vcenter resource belonging to a site resource.
        Azure REST API version: 2023-06-06.

        :param str resource_name: The name of the resource.
        :param VcenterControllerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VcenterControllerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_as_account_id: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 vcenter_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VcenterControllerArgs.__new__(VcenterControllerArgs)

            __props__.__dict__["fqdn"] = fqdn
            __props__.__dict__["friendly_name"] = friendly_name
            __props__.__dict__["port"] = port
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["run_as_account_id"] = run_as_account_id
            if site_name is None and not opts.urn:
                raise TypeError("Missing required property 'site_name'")
            __props__.__dict__["site_name"] = site_name
            __props__.__dict__["vcenter_name"] = vcenter_name
            __props__.__dict__["created_timestamp"] = None
            __props__.__dict__["errors"] = None
            __props__.__dict__["instance_uuid"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["perf_statistics_level"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_timestamp"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:offazure/v20200101:VcenterController"), pulumi.Alias(type_="azure-native:offazure/v20200707:VcenterController"), pulumi.Alias(type_="azure-native:offazure/v20230606:VcenterController")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VcenterController, __self__).__init__(
            'azure-native:offazure:VcenterController',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VcenterController':
        """
        Get an existing VcenterController resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VcenterControllerArgs.__new__(VcenterControllerArgs)

        __props__.__dict__["created_timestamp"] = None
        __props__.__dict__["errors"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["friendly_name"] = None
        __props__.__dict__["instance_uuid"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["perf_statistics_level"] = None
        __props__.__dict__["port"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["run_as_account_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_timestamp"] = None
        __props__.__dict__["version"] = None
        return VcenterController(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[str]:
        """
        Gets the timestamp marking vCenter creation.
        """
        return pulumi.get(self, "created_timestamp")

    @property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence['outputs.HealthErrorDetailsResponse']]:
        """
        Gets the errors.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the FQDN/IPAddress of the vCenter.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the friendly name of the vCenter.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="instanceUuid")
    def instance_uuid(self) -> pulumi.Output[str]:
        """
        Gets the instance UUID of the vCenter.
        """
        return pulumi.get(self, "instance_uuid")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="perfStatisticsLevel")
    def perf_statistics_level(self) -> pulumi.Output[str]:
        """
        Gets the performance statistics enabled on the vCenter.
        """
        return pulumi.get(self, "perf_statistics_level")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the port of the vCenter.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the run as account ID of the vCenter.
        """
        return pulumi.get(self, "run_as_account_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> pulumi.Output[str]:
        """
        Gets the timestamp marking last updated on the vCenter.
        """
        return pulumi.get(self, "updated_timestamp")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Gets the version of the vCenter.
        """
        return pulumi.get(self, "version")

