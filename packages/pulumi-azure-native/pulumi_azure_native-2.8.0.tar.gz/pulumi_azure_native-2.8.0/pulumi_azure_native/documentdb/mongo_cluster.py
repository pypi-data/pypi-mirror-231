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
from ._inputs import *

__all__ = ['MongoClusterArgs', 'MongoCluster']

@pulumi.input_type
class MongoClusterArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mongo_cluster_name: Optional[pulumi.Input[str]] = None,
                 node_group_specs: Optional[pulumi.Input[Sequence[pulumi.Input['NodeGroupSpecArgs']]]] = None,
                 restore_parameters: Optional[pulumi.Input['MongoClusterRestoreParametersArgs']] = None,
                 server_version: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MongoCluster resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] administrator_login: The administrator's login for the mongo cluster.
        :param pulumi.Input[str] administrator_login_password: The password of the administrator login.
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: The mode to create a mongo cluster.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] mongo_cluster_name: The name of the mongo cluster.
        :param pulumi.Input[Sequence[pulumi.Input['NodeGroupSpecArgs']]] node_group_specs: The list of node group specs in the cluster.
        :param pulumi.Input['MongoClusterRestoreParametersArgs'] restore_parameters: Parameters used for restore operations
        :param pulumi.Input[str] server_version: The Mongo DB server version. Defaults to the latest available version if not specified.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if administrator_login is not None:
            pulumi.set(__self__, "administrator_login", administrator_login)
        if administrator_login_password is not None:
            pulumi.set(__self__, "administrator_login_password", administrator_login_password)
        if create_mode is None:
            create_mode = 'Default'
        if create_mode is not None:
            pulumi.set(__self__, "create_mode", create_mode)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mongo_cluster_name is not None:
            pulumi.set(__self__, "mongo_cluster_name", mongo_cluster_name)
        if node_group_specs is not None:
            pulumi.set(__self__, "node_group_specs", node_group_specs)
        if restore_parameters is not None:
            pulumi.set(__self__, "restore_parameters", restore_parameters)
        if server_version is not None:
            pulumi.set(__self__, "server_version", server_version)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[pulumi.Input[str]]:
        """
        The administrator's login for the mongo cluster.
        """
        return pulumi.get(self, "administrator_login")

    @administrator_login.setter
    def administrator_login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_login", value)

    @property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the administrator login.
        """
        return pulumi.get(self, "administrator_login_password")

    @administrator_login_password.setter
    def administrator_login_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_login_password", value)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[str, 'CreateMode']]]:
        """
        The mode to create a mongo cluster.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[str, 'CreateMode']]]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mongoClusterName")
    def mongo_cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the mongo cluster.
        """
        return pulumi.get(self, "mongo_cluster_name")

    @mongo_cluster_name.setter
    def mongo_cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mongo_cluster_name", value)

    @property
    @pulumi.getter(name="nodeGroupSpecs")
    def node_group_specs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NodeGroupSpecArgs']]]]:
        """
        The list of node group specs in the cluster.
        """
        return pulumi.get(self, "node_group_specs")

    @node_group_specs.setter
    def node_group_specs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NodeGroupSpecArgs']]]]):
        pulumi.set(self, "node_group_specs", value)

    @property
    @pulumi.getter(name="restoreParameters")
    def restore_parameters(self) -> Optional[pulumi.Input['MongoClusterRestoreParametersArgs']]:
        """
        Parameters used for restore operations
        """
        return pulumi.get(self, "restore_parameters")

    @restore_parameters.setter
    def restore_parameters(self, value: Optional[pulumi.Input['MongoClusterRestoreParametersArgs']]):
        pulumi.set(self, "restore_parameters", value)

    @property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[str]]:
        """
        The Mongo DB server version. Defaults to the latest available version if not specified.
        """
        return pulumi.get(self, "server_version")

    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_version", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class MongoCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mongo_cluster_name: Optional[pulumi.Input[str]] = None,
                 node_group_specs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NodeGroupSpecArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restore_parameters: Optional[pulumi.Input[pulumi.InputType['MongoClusterRestoreParametersArgs']]] = None,
                 server_version: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents a mongo cluster resource.
        Azure REST API version: 2023-03-15-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administrator_login: The administrator's login for the mongo cluster.
        :param pulumi.Input[str] administrator_login_password: The password of the administrator login.
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: The mode to create a mongo cluster.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] mongo_cluster_name: The name of the mongo cluster.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NodeGroupSpecArgs']]]] node_group_specs: The list of node group specs in the cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['MongoClusterRestoreParametersArgs']] restore_parameters: Parameters used for restore operations
        :param pulumi.Input[str] server_version: The Mongo DB server version. Defaults to the latest available version if not specified.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MongoClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a mongo cluster resource.
        Azure REST API version: 2023-03-15-preview.

        :param str resource_name: The name of the resource.
        :param MongoClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MongoClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mongo_cluster_name: Optional[pulumi.Input[str]] = None,
                 node_group_specs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NodeGroupSpecArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restore_parameters: Optional[pulumi.Input[pulumi.InputType['MongoClusterRestoreParametersArgs']]] = None,
                 server_version: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MongoClusterArgs.__new__(MongoClusterArgs)

            __props__.__dict__["administrator_login"] = administrator_login
            __props__.__dict__["administrator_login_password"] = administrator_login_password
            if create_mode is None:
                create_mode = 'Default'
            __props__.__dict__["create_mode"] = create_mode
            __props__.__dict__["location"] = location
            __props__.__dict__["mongo_cluster_name"] = mongo_cluster_name
            __props__.__dict__["node_group_specs"] = node_group_specs
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["restore_parameters"] = restore_parameters
            __props__.__dict__["server_version"] = server_version
            __props__.__dict__["tags"] = tags
            __props__.__dict__["cluster_status"] = None
            __props__.__dict__["connection_string"] = None
            __props__.__dict__["earliest_restore_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:documentdb/v20230301preview:MongoCluster"), pulumi.Alias(type_="azure-native:documentdb/v20230315preview:MongoCluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MongoCluster, __self__).__init__(
            'azure-native:documentdb:MongoCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MongoCluster':
        """
        Get an existing MongoCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MongoClusterArgs.__new__(MongoClusterArgs)

        __props__.__dict__["administrator_login"] = None
        __props__.__dict__["cluster_status"] = None
        __props__.__dict__["connection_string"] = None
        __props__.__dict__["earliest_restore_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["node_group_specs"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["server_version"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return MongoCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Output[Optional[str]]:
        """
        The administrator's login for the mongo cluster.
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="clusterStatus")
    def cluster_status(self) -> pulumi.Output[str]:
        """
        A status of the mongo cluster.
        """
        return pulumi.get(self, "cluster_status")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Output[str]:
        """
        The default mongo connection string for the cluster.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="earliestRestoreTime")
    def earliest_restore_time(self) -> pulumi.Output[str]:
        """
        Earliest restore timestamp in UTC ISO8601 format.
        """
        return pulumi.get(self, "earliest_restore_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeGroupSpecs")
    def node_group_specs(self) -> pulumi.Output[Optional[Sequence['outputs.NodeGroupSpecResponse']]]:
        """
        The list of node group specs in the cluster.
        """
        return pulumi.get(self, "node_group_specs")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        A provisioning state of the mongo cluster.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> pulumi.Output[Optional[str]]:
        """
        The Mongo DB server version. Defaults to the latest available version if not specified.
        """
        return pulumi.get(self, "server_version")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

