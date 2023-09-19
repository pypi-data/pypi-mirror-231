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

__all__ = ['AADDataConnectorArgs', 'AADDataConnector']

@pulumi.input_type
class AADDataConnectorArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 data_connector_id: Optional[pulumi.Input[str]] = None,
                 data_types: Optional[pulumi.Input['AlertsDataTypeOfDataConnectorArgs']] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AADDataConnector resource.
        :param pulumi.Input[str] kind: The kind of the data connector
               Expected value is 'AzureActiveDirectory'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] data_connector_id: Connector ID
        :param pulumi.Input['AlertsDataTypeOfDataConnectorArgs'] data_types: The available data types for the connector.
        :param pulumi.Input[str] tenant_id: The tenant id to connect to, and get the data from.
        """
        pulumi.set(__self__, "kind", 'AzureActiveDirectory')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if data_connector_id is not None:
            pulumi.set(__self__, "data_connector_id", data_connector_id)
        if data_types is not None:
            pulumi.set(__self__, "data_types", data_types)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the data connector
        Expected value is 'AzureActiveDirectory'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="dataConnectorId")
    def data_connector_id(self) -> Optional[pulumi.Input[str]]:
        """
        Connector ID
        """
        return pulumi.get(self, "data_connector_id")

    @data_connector_id.setter
    def data_connector_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_connector_id", value)

    @property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> Optional[pulumi.Input['AlertsDataTypeOfDataConnectorArgs']]:
        """
        The available data types for the connector.
        """
        return pulumi.get(self, "data_types")

    @data_types.setter
    def data_types(self, value: Optional[pulumi.Input['AlertsDataTypeOfDataConnectorArgs']]):
        pulumi.set(self, "data_types", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The tenant id to connect to, and get the data from.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class AADDataConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_connector_id: Optional[pulumi.Input[str]] = None,
                 data_types: Optional[pulumi.Input[pulumi.InputType['AlertsDataTypeOfDataConnectorArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents AAD (Azure Active Directory) data connector.
        Azure REST API version: 2023-02-01. Prior API version in Azure Native 1.x: 2020-01-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_connector_id: Connector ID
        :param pulumi.Input[pulumi.InputType['AlertsDataTypeOfDataConnectorArgs']] data_types: The available data types for the connector.
        :param pulumi.Input[str] kind: The kind of the data connector
               Expected value is 'AzureActiveDirectory'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] tenant_id: The tenant id to connect to, and get the data from.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AADDataConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents AAD (Azure Active Directory) data connector.
        Azure REST API version: 2023-02-01. Prior API version in Azure Native 1.x: 2020-01-01

        :param str resource_name: The name of the resource.
        :param AADDataConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AADDataConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_connector_id: Optional[pulumi.Input[str]] = None,
                 data_types: Optional[pulumi.Input[pulumi.InputType['AlertsDataTypeOfDataConnectorArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AADDataConnectorArgs.__new__(AADDataConnectorArgs)

            __props__.__dict__["data_connector_id"] = data_connector_id
            __props__.__dict__["data_types"] = data_types
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'AzureActiveDirectory'
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tenant_id"] = tenant_id
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20200101:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20211001:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220801:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20221101:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230201:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230201preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230301preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230601preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:AADDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:AADDataConnector")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AADDataConnector, __self__).__init__(
            'azure-native:securityinsights:AADDataConnector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AADDataConnector':
        """
        Get an existing AADDataConnector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AADDataConnectorArgs.__new__(AADDataConnectorArgs)

        __props__.__dict__["data_types"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return AADDataConnector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> pulumi.Output[Optional['outputs.AlertsDataTypeOfDataConnectorResponse']]:
        """
        The available data types for the connector.
        """
        return pulumi.get(self, "data_types")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of the data connector
        Expected value is 'AzureActiveDirectory'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        The tenant id to connect to, and get the data from.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

