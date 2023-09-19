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
from ._inputs import *

__all__ = ['UpdateRunArgs', 'UpdateRun']

@pulumi.input_type
class UpdateRunArgs:
    def __init__(__self__, *,
                 fleet_name: pulumi.Input[str],
                 managed_cluster_update: pulumi.Input['ManagedClusterUpdateArgs'],
                 resource_group_name: pulumi.Input[str],
                 strategy: Optional[pulumi.Input['UpdateRunStrategyArgs']] = None,
                 update_run_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UpdateRun resource.
        :param pulumi.Input[str] fleet_name: The name of the Fleet resource.
        :param pulumi.Input['ManagedClusterUpdateArgs'] managed_cluster_update: The update to be applied to all clusters in the UpdateRun. The managedClusterUpdate can be modified until the run is started.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['UpdateRunStrategyArgs'] strategy: The strategy defines the order in which the clusters will be updated. 
               If not set, all members will be updated sequentially. The UpdateRun status will show a single UpdateStage and a single UpdateGroup targeting all members.
               The strategy of the UpdateRun can be modified until the run is started.
        :param pulumi.Input[str] update_run_name: The name of the UpdateRun resource.
        """
        pulumi.set(__self__, "fleet_name", fleet_name)
        pulumi.set(__self__, "managed_cluster_update", managed_cluster_update)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if strategy is not None:
            pulumi.set(__self__, "strategy", strategy)
        if update_run_name is not None:
            pulumi.set(__self__, "update_run_name", update_run_name)

    @property
    @pulumi.getter(name="fleetName")
    def fleet_name(self) -> pulumi.Input[str]:
        """
        The name of the Fleet resource.
        """
        return pulumi.get(self, "fleet_name")

    @fleet_name.setter
    def fleet_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "fleet_name", value)

    @property
    @pulumi.getter(name="managedClusterUpdate")
    def managed_cluster_update(self) -> pulumi.Input['ManagedClusterUpdateArgs']:
        """
        The update to be applied to all clusters in the UpdateRun. The managedClusterUpdate can be modified until the run is started.
        """
        return pulumi.get(self, "managed_cluster_update")

    @managed_cluster_update.setter
    def managed_cluster_update(self, value: pulumi.Input['ManagedClusterUpdateArgs']):
        pulumi.set(self, "managed_cluster_update", value)

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
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input['UpdateRunStrategyArgs']]:
        """
        The strategy defines the order in which the clusters will be updated. 
        If not set, all members will be updated sequentially. The UpdateRun status will show a single UpdateStage and a single UpdateGroup targeting all members.
        The strategy of the UpdateRun can be modified until the run is started.
        """
        return pulumi.get(self, "strategy")

    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input['UpdateRunStrategyArgs']]):
        pulumi.set(self, "strategy", value)

    @property
    @pulumi.getter(name="updateRunName")
    def update_run_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the UpdateRun resource.
        """
        return pulumi.get(self, "update_run_name")

    @update_run_name.setter
    def update_run_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_run_name", value)


class UpdateRun(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fleet_name: Optional[pulumi.Input[str]] = None,
                 managed_cluster_update: Optional[pulumi.Input[pulumi.InputType['ManagedClusterUpdateArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 strategy: Optional[pulumi.Input[pulumi.InputType['UpdateRunStrategyArgs']]] = None,
                 update_run_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An UpdateRun is a multi-stage process to perform update operations across members of a Fleet.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fleet_name: The name of the Fleet resource.
        :param pulumi.Input[pulumi.InputType['ManagedClusterUpdateArgs']] managed_cluster_update: The update to be applied to all clusters in the UpdateRun. The managedClusterUpdate can be modified until the run is started.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['UpdateRunStrategyArgs']] strategy: The strategy defines the order in which the clusters will be updated. 
               If not set, all members will be updated sequentially. The UpdateRun status will show a single UpdateStage and a single UpdateGroup targeting all members.
               The strategy of the UpdateRun can be modified until the run is started.
        :param pulumi.Input[str] update_run_name: The name of the UpdateRun resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UpdateRunArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An UpdateRun is a multi-stage process to perform update operations across members of a Fleet.

        :param str resource_name: The name of the resource.
        :param UpdateRunArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UpdateRunArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fleet_name: Optional[pulumi.Input[str]] = None,
                 managed_cluster_update: Optional[pulumi.Input[pulumi.InputType['ManagedClusterUpdateArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 strategy: Optional[pulumi.Input[pulumi.InputType['UpdateRunStrategyArgs']]] = None,
                 update_run_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UpdateRunArgs.__new__(UpdateRunArgs)

            if fleet_name is None and not opts.urn:
                raise TypeError("Missing required property 'fleet_name'")
            __props__.__dict__["fleet_name"] = fleet_name
            if managed_cluster_update is None and not opts.urn:
                raise TypeError("Missing required property 'managed_cluster_update'")
            __props__.__dict__["managed_cluster_update"] = managed_cluster_update
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["strategy"] = strategy
            __props__.__dict__["update_run_name"] = update_run_name
            __props__.__dict__["e_tag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerservice:UpdateRun"), pulumi.Alias(type_="azure-native:containerservice/v20230315preview:UpdateRun")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(UpdateRun, __self__).__init__(
            'azure-native:containerservice/v20230615preview:UpdateRun',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UpdateRun':
        """
        Get an existing UpdateRun resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UpdateRunArgs.__new__(UpdateRunArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["managed_cluster_update"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["strategy"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return UpdateRun(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[str]:
        """
        If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="managedClusterUpdate")
    def managed_cluster_update(self) -> pulumi.Output['outputs.ManagedClusterUpdateResponse']:
        """
        The update to be applied to all clusters in the UpdateRun. The managedClusterUpdate can be modified until the run is started.
        """
        return pulumi.get(self, "managed_cluster_update")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the UpdateRun resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.UpdateRunStatusResponse']:
        """
        The status of the UpdateRun.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def strategy(self) -> pulumi.Output[Optional['outputs.UpdateRunStrategyResponse']]:
        """
        The strategy defines the order in which the clusters will be updated. 
        If not set, all members will be updated sequentially. The UpdateRun status will show a single UpdateStage and a single UpdateGroup targeting all members.
        The strategy of the UpdateRun can be modified until the run is started.
        """
        return pulumi.get(self, "strategy")

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

