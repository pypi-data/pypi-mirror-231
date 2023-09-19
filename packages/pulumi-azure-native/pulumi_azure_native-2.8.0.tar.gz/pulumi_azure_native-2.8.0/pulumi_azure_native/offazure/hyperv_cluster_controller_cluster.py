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

__all__ = ['HypervClusterControllerClusterArgs', 'HypervClusterControllerCluster']

@pulumi.input_type
class HypervClusterControllerClusterArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 site_name: pulumi.Input[str],
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 host_fqdn_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 run_as_account_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a HypervClusterControllerCluster resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] site_name: Site name
        :param pulumi.Input[str] cluster_name:  Cluster ARM name
        :param pulumi.Input[str] fqdn: Gets or sets the FQDN/IPAddress of the Hyper-V cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_fqdn_list: Gets or sets list of hosts (FQDN) currently being tracked by the cluster.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the last operation.
        :param pulumi.Input[str] run_as_account_id: Gets or sets Run as account ID of the Hyper-V cluster.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "site_name", site_name)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if fqdn is not None:
            pulumi.set(__self__, "fqdn", fqdn)
        if host_fqdn_list is not None:
            pulumi.set(__self__, "host_fqdn_list", host_fqdn_list)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if run_as_account_id is not None:
            pulumi.set(__self__, "run_as_account_id", run_as_account_id)

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
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
         Cluster ARM name
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the FQDN/IPAddress of the Hyper-V cluster.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter(name="hostFqdnList")
    def host_fqdn_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Gets or sets list of hosts (FQDN) currently being tracked by the cluster.
        """
        return pulumi.get(self, "host_fqdn_list")

    @host_fqdn_list.setter
    def host_fqdn_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "host_fqdn_list", value)

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
        Gets or sets Run as account ID of the Hyper-V cluster.
        """
        return pulumi.get(self, "run_as_account_id")

    @run_as_account_id.setter
    def run_as_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_as_account_id", value)


class HypervClusterControllerCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 host_fqdn_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_as_account_id: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A cluster resource belonging to a site resource.
        Azure REST API version: 2023-06-06.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name:  Cluster ARM name
        :param pulumi.Input[str] fqdn: Gets or sets the FQDN/IPAddress of the Hyper-V cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_fqdn_list: Gets or sets list of hosts (FQDN) currently being tracked by the cluster.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the last operation.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] run_as_account_id: Gets or sets Run as account ID of the Hyper-V cluster.
        :param pulumi.Input[str] site_name: Site name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HypervClusterControllerClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A cluster resource belonging to a site resource.
        Azure REST API version: 2023-06-06.

        :param str resource_name: The name of the resource.
        :param HypervClusterControllerClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HypervClusterControllerClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 host_fqdn_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_as_account_id: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HypervClusterControllerClusterArgs.__new__(HypervClusterControllerClusterArgs)

            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["fqdn"] = fqdn
            __props__.__dict__["host_fqdn_list"] = host_fqdn_list
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["run_as_account_id"] = run_as_account_id
            if site_name is None and not opts.urn:
                raise TypeError("Missing required property 'site_name'")
            __props__.__dict__["site_name"] = site_name
            __props__.__dict__["created_timestamp"] = None
            __props__.__dict__["errors"] = None
            __props__.__dict__["functional_level"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_timestamp"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:offazure/v20230606:HypervClusterControllerCluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(HypervClusterControllerCluster, __self__).__init__(
            'azure-native:offazure:HypervClusterControllerCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HypervClusterControllerCluster':
        """
        Get an existing HypervClusterControllerCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HypervClusterControllerClusterArgs.__new__(HypervClusterControllerClusterArgs)

        __props__.__dict__["created_timestamp"] = None
        __props__.__dict__["errors"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["functional_level"] = None
        __props__.__dict__["host_fqdn_list"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["run_as_account_id"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_timestamp"] = None
        return HypervClusterControllerCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> pulumi.Output[str]:
        """
        Gets the timestamp marking Hyper-V cluster creation.
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
        Gets or sets the FQDN/IPAddress of the Hyper-V cluster.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="functionalLevel")
    def functional_level(self) -> pulumi.Output[int]:
        """
        Gets the functional level of the Hyper-V cluster.
        """
        return pulumi.get(self, "functional_level")

    @property
    @pulumi.getter(name="hostFqdnList")
    def host_fqdn_list(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Gets or sets list of hosts (FQDN) currently being tracked by the cluster.
        """
        return pulumi.get(self, "host_fqdn_list")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

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
        Gets or sets Run as account ID of the Hyper-V cluster.
        """
        return pulumi.get(self, "run_as_account_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Gets the status of the Hyper-V cluster.
        """
        return pulumi.get(self, "status")

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
        Gets the timestamp marking last updated on the Hyper-V cluster.
        """
        return pulumi.get(self, "updated_timestamp")

