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
from ._inputs import *

__all__ = ['GCPDataConnectorArgs', 'GCPDataConnector']

@pulumi.input_type
class GCPDataConnectorArgs:
    def __init__(__self__, *,
                 auth: pulumi.Input['GCPAuthPropertiesArgs'],
                 connector_definition_name: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 request: pulumi.Input['GCPRequestPropertiesArgs'],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 data_connector_id: Optional[pulumi.Input[str]] = None,
                 dcr_config: Optional[pulumi.Input['DCRConfigurationArgs']] = None):
        """
        The set of arguments for constructing a GCPDataConnector resource.
        :param pulumi.Input['GCPAuthPropertiesArgs'] auth: The auth section of the connector.
        :param pulumi.Input[str] connector_definition_name: The name of the connector definition that represents the UI config.
        :param pulumi.Input[str] kind: The kind of the data connector
               Expected value is 'GCP'.
        :param pulumi.Input['GCPRequestPropertiesArgs'] request: The request section of the connector.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] data_connector_id: Connector ID
        :param pulumi.Input['DCRConfigurationArgs'] dcr_config: The configuration of the destination of the data.
        """
        pulumi.set(__self__, "auth", auth)
        pulumi.set(__self__, "connector_definition_name", connector_definition_name)
        pulumi.set(__self__, "kind", 'GCP')
        pulumi.set(__self__, "request", request)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if data_connector_id is not None:
            pulumi.set(__self__, "data_connector_id", data_connector_id)
        if dcr_config is not None:
            pulumi.set(__self__, "dcr_config", dcr_config)

    @property
    @pulumi.getter
    def auth(self) -> pulumi.Input['GCPAuthPropertiesArgs']:
        """
        The auth section of the connector.
        """
        return pulumi.get(self, "auth")

    @auth.setter
    def auth(self, value: pulumi.Input['GCPAuthPropertiesArgs']):
        pulumi.set(self, "auth", value)

    @property
    @pulumi.getter(name="connectorDefinitionName")
    def connector_definition_name(self) -> pulumi.Input[str]:
        """
        The name of the connector definition that represents the UI config.
        """
        return pulumi.get(self, "connector_definition_name")

    @connector_definition_name.setter
    def connector_definition_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "connector_definition_name", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the data connector
        Expected value is 'GCP'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def request(self) -> pulumi.Input['GCPRequestPropertiesArgs']:
        """
        The request section of the connector.
        """
        return pulumi.get(self, "request")

    @request.setter
    def request(self, value: pulumi.Input['GCPRequestPropertiesArgs']):
        pulumi.set(self, "request", value)

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
    @pulumi.getter(name="dcrConfig")
    def dcr_config(self) -> Optional[pulumi.Input['DCRConfigurationArgs']]:
        """
        The configuration of the destination of the data.
        """
        return pulumi.get(self, "dcr_config")

    @dcr_config.setter
    def dcr_config(self, value: Optional[pulumi.Input['DCRConfigurationArgs']]):
        pulumi.set(self, "dcr_config", value)


class GCPDataConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth: Optional[pulumi.Input[pulumi.InputType['GCPAuthPropertiesArgs']]] = None,
                 connector_definition_name: Optional[pulumi.Input[str]] = None,
                 data_connector_id: Optional[pulumi.Input[str]] = None,
                 dcr_config: Optional[pulumi.Input[pulumi.InputType['DCRConfigurationArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 request: Optional[pulumi.Input[pulumi.InputType['GCPRequestPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents Google Cloud Platform data connector.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GCPAuthPropertiesArgs']] auth: The auth section of the connector.
        :param pulumi.Input[str] connector_definition_name: The name of the connector definition that represents the UI config.
        :param pulumi.Input[str] data_connector_id: Connector ID
        :param pulumi.Input[pulumi.InputType['DCRConfigurationArgs']] dcr_config: The configuration of the destination of the data.
        :param pulumi.Input[str] kind: The kind of the data connector
               Expected value is 'GCP'.
        :param pulumi.Input[pulumi.InputType['GCPRequestPropertiesArgs']] request: The request section of the connector.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GCPDataConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents Google Cloud Platform data connector.

        :param str resource_name: The name of the resource.
        :param GCPDataConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GCPDataConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth: Optional[pulumi.Input[pulumi.InputType['GCPAuthPropertiesArgs']]] = None,
                 connector_definition_name: Optional[pulumi.Input[str]] = None,
                 data_connector_id: Optional[pulumi.Input[str]] = None,
                 dcr_config: Optional[pulumi.Input[pulumi.InputType['DCRConfigurationArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 request: Optional[pulumi.Input[pulumi.InputType['GCPRequestPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GCPDataConnectorArgs.__new__(GCPDataConnectorArgs)

            if auth is None and not opts.urn:
                raise TypeError("Missing required property 'auth'")
            __props__.__dict__["auth"] = auth
            if connector_definition_name is None and not opts.urn:
                raise TypeError("Missing required property 'connector_definition_name'")
            __props__.__dict__["connector_definition_name"] = connector_definition_name
            __props__.__dict__["data_connector_id"] = data_connector_id
            __props__.__dict__["dcr_config"] = dcr_config
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'GCP'
            if request is None and not opts.urn:
                raise TypeError("Missing required property 'request'")
            __props__.__dict__["request"] = request
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20200101:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20211001:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220801:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20221101:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230201:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230201preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230301preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:GCPDataConnector"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:GCPDataConnector")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GCPDataConnector, __self__).__init__(
            'azure-native:securityinsights/v20230601preview:GCPDataConnector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GCPDataConnector':
        """
        Get an existing GCPDataConnector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GCPDataConnectorArgs.__new__(GCPDataConnectorArgs)

        __props__.__dict__["auth"] = None
        __props__.__dict__["connector_definition_name"] = None
        __props__.__dict__["dcr_config"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["request"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return GCPDataConnector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def auth(self) -> pulumi.Output['outputs.GCPAuthPropertiesResponse']:
        """
        The auth section of the connector.
        """
        return pulumi.get(self, "auth")

    @property
    @pulumi.getter(name="connectorDefinitionName")
    def connector_definition_name(self) -> pulumi.Output[str]:
        """
        The name of the connector definition that represents the UI config.
        """
        return pulumi.get(self, "connector_definition_name")

    @property
    @pulumi.getter(name="dcrConfig")
    def dcr_config(self) -> pulumi.Output[Optional['outputs.DCRConfigurationResponse']]:
        """
        The configuration of the destination of the data.
        """
        return pulumi.get(self, "dcr_config")

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
        Expected value is 'GCP'.
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
    @pulumi.getter
    def request(self) -> pulumi.Output['outputs.GCPRequestPropertiesResponse']:
        """
        The request section of the connector.
        """
        return pulumi.get(self, "request")

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

