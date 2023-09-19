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

__all__ = ['KustoPoolArgs', 'KustoPool']

@pulumi.input_type
class KustoPoolArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['AzureSkuArgs'],
                 workspace_name: pulumi.Input[str],
                 engine_type: Optional[pulumi.Input[Union[str, 'EngineType']]] = None,
                 kusto_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_uid: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KustoPool resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['AzureSkuArgs'] sku: The SKU of the kusto pool.
        :param pulumi.Input[str] workspace_name: The name of the workspace
        :param pulumi.Input[Union[str, 'EngineType']] engine_type: The engine type
        :param pulumi.Input[str] kusto_pool_name: The name of the Kusto pool.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_uid: The workspace unique identifier.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if engine_type is not None:
            pulumi.set(__self__, "engine_type", engine_type)
        if kusto_pool_name is not None:
            pulumi.set(__self__, "kusto_pool_name", kusto_pool_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workspace_uid is not None:
            pulumi.set(__self__, "workspace_uid", workspace_uid)

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
    def sku(self) -> pulumi.Input['AzureSkuArgs']:
        """
        The SKU of the kusto pool.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['AzureSkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> Optional[pulumi.Input[Union[str, 'EngineType']]]:
        """
        The engine type
        """
        return pulumi.get(self, "engine_type")

    @engine_type.setter
    def engine_type(self, value: Optional[pulumi.Input[Union[str, 'EngineType']]]):
        pulumi.set(self, "engine_type", value)

    @property
    @pulumi.getter(name="kustoPoolName")
    def kusto_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kusto pool.
        """
        return pulumi.get(self, "kusto_pool_name")

    @kusto_pool_name.setter
    def kusto_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kusto_pool_name", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workspaceUid")
    def workspace_uid(self) -> Optional[pulumi.Input[str]]:
        """
        The workspace unique identifier.
        """
        return pulumi.get(self, "workspace_uid")

    @workspace_uid.setter
    def workspace_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_uid", value)


class KustoPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 engine_type: Optional[pulumi.Input[Union[str, 'EngineType']]] = None,
                 kusto_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['AzureSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 workspace_uid: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing a Kusto kusto pool.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'EngineType']] engine_type: The engine type
        :param pulumi.Input[str] kusto_pool_name: The name of the Kusto pool.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['AzureSkuArgs']] sku: The SKU of the kusto pool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_name: The name of the workspace
        :param pulumi.Input[str] workspace_uid: The workspace unique identifier.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KustoPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a Kusto kusto pool.

        :param str resource_name: The name of the resource.
        :param KustoPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KustoPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 engine_type: Optional[pulumi.Input[Union[str, 'EngineType']]] = None,
                 kusto_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['AzureSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 workspace_uid: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KustoPoolArgs.__new__(KustoPoolArgs)

            __props__.__dict__["engine_type"] = engine_type
            __props__.__dict__["kusto_pool_name"] = kusto_pool_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["workspace_uid"] = workspace_uid
            __props__.__dict__["data_ingestion_uri"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["state_reason"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["uri"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:synapse/v20210401preview:kustoPool"), pulumi.Alias(type_="azure-native:synapse:KustoPool"), pulumi.Alias(type_="azure-native:synapse:kustoPool"), pulumi.Alias(type_="azure-native:synapse/v20210601preview:KustoPool"), pulumi.Alias(type_="azure-native:synapse/v20210601preview:kustoPool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(KustoPool, __self__).__init__(
            'azure-native:synapse/v20210401preview:KustoPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'KustoPool':
        """
        Get an existing KustoPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = KustoPoolArgs.__new__(KustoPoolArgs)

        __props__.__dict__["data_ingestion_uri"] = None
        __props__.__dict__["engine_type"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["state_reason"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uri"] = None
        __props__.__dict__["workspace_uid"] = None
        return KustoPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataIngestionUri")
    def data_ingestion_uri(self) -> pulumi.Output[str]:
        """
        The Kusto Pool data ingestion URI.
        """
        return pulumi.get(self, "data_ingestion_uri")

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> pulumi.Output[Optional[str]]:
        """
        The engine type
        """
        return pulumi.get(self, "engine_type")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.AzureSkuResponse']:
        """
        The SKU of the kusto pool.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> pulumi.Output[str]:
        """
        The reason for the Kusto Pool's current state.
        """
        return pulumi.get(self, "state_reason")

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

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[str]:
        """
        The Kusto Pool URI.
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter(name="workspaceUid")
    def workspace_uid(self) -> pulumi.Output[Optional[str]]:
        """
        The workspace unique identifier.
        """
        return pulumi.get(self, "workspace_uid")

