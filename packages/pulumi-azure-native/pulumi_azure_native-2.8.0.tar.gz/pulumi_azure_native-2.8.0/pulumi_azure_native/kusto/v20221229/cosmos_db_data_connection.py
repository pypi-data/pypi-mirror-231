# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['CosmosDbDataConnectionArgs', 'CosmosDbDataConnection']

@pulumi.input_type
class CosmosDbDataConnectionArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 cosmos_db_account_resource_id: pulumi.Input[str],
                 cosmos_db_container: pulumi.Input[str],
                 cosmos_db_database: pulumi.Input[str],
                 database_name: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 managed_identity_resource_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 table_name: pulumi.Input[str],
                 data_connection_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 retrieval_start_date: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CosmosDbDataConnection resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] cosmos_db_account_resource_id: The resource ID of the Cosmos DB account used to create the data connection.
        :param pulumi.Input[str] cosmos_db_container: The name of an existing container in the Cosmos DB database.
        :param pulumi.Input[str] cosmos_db_database: The name of an existing database in the Cosmos DB account.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto cluster.
        :param pulumi.Input[str] kind: Kind of the endpoint for the data connection
               Expected value is 'CosmosDb'.
        :param pulumi.Input[str] managed_identity_resource_id: The resource ID of a managed system or user-assigned identity. The identity is used to authenticate with Cosmos DB.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        :param pulumi.Input[str] table_name: The case-sensitive name of the existing target table in your cluster. Retrieved data is ingested into this table.
        :param pulumi.Input[str] data_connection_name: The name of the data connection.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] mapping_rule_name: The name of an existing mapping rule to use when ingesting the retrieved data.
        :param pulumi.Input[str] retrieval_start_date: Optional. If defined, the data connection retrieves Cosmos DB documents created or updated after the specified retrieval start date.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "cosmos_db_account_resource_id", cosmos_db_account_resource_id)
        pulumi.set(__self__, "cosmos_db_container", cosmos_db_container)
        pulumi.set(__self__, "cosmos_db_database", cosmos_db_database)
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "kind", 'CosmosDb')
        pulumi.set(__self__, "managed_identity_resource_id", managed_identity_resource_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "table_name", table_name)
        if data_connection_name is not None:
            pulumi.set(__self__, "data_connection_name", data_connection_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mapping_rule_name is not None:
            pulumi.set(__self__, "mapping_rule_name", mapping_rule_name)
        if retrieval_start_date is not None:
            pulumi.set(__self__, "retrieval_start_date", retrieval_start_date)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the Kusto cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="cosmosDbAccountResourceId")
    def cosmos_db_account_resource_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Cosmos DB account used to create the data connection.
        """
        return pulumi.get(self, "cosmos_db_account_resource_id")

    @cosmos_db_account_resource_id.setter
    def cosmos_db_account_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cosmos_db_account_resource_id", value)

    @property
    @pulumi.getter(name="cosmosDbContainer")
    def cosmos_db_container(self) -> pulumi.Input[str]:
        """
        The name of an existing container in the Cosmos DB database.
        """
        return pulumi.get(self, "cosmos_db_container")

    @cosmos_db_container.setter
    def cosmos_db_container(self, value: pulumi.Input[str]):
        pulumi.set(self, "cosmos_db_container", value)

    @property
    @pulumi.getter(name="cosmosDbDatabase")
    def cosmos_db_database(self) -> pulumi.Input[str]:
        """
        The name of an existing database in the Cosmos DB account.
        """
        return pulumi.get(self, "cosmos_db_database")

    @cosmos_db_database.setter
    def cosmos_db_database(self, value: pulumi.Input[str]):
        pulumi.set(self, "cosmos_db_database", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the database in the Kusto cluster.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Kind of the endpoint for the data connection
        Expected value is 'CosmosDb'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="managedIdentityResourceId")
    def managed_identity_resource_id(self) -> pulumi.Input[str]:
        """
        The resource ID of a managed system or user-assigned identity. The identity is used to authenticate with Cosmos DB.
        """
        return pulumi.get(self, "managed_identity_resource_id")

    @managed_identity_resource_id.setter
    def managed_identity_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_identity_resource_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group containing the Kusto cluster.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[str]:
        """
        The case-sensitive name of the existing target table in your cluster. Retrieved data is ingested into this table.
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "table_name", value)

    @property
    @pulumi.getter(name="dataConnectionName")
    def data_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the data connection.
        """
        return pulumi.get(self, "data_connection_name")

    @data_connection_name.setter
    def data_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_connection_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of an existing mapping rule to use when ingesting the retrieved data.
        """
        return pulumi.get(self, "mapping_rule_name")

    @mapping_rule_name.setter
    def mapping_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mapping_rule_name", value)

    @property
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. If defined, the data connection retrieves Cosmos DB documents created or updated after the specified retrieval start date.
        """
        return pulumi.get(self, "retrieval_start_date")

    @retrieval_start_date.setter
    def retrieval_start_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retrieval_start_date", value)


class CosmosDbDataConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cosmos_db_account_resource_id: Optional[pulumi.Input[str]] = None,
                 cosmos_db_container: Optional[pulumi.Input[str]] = None,
                 cosmos_db_database: Optional[pulumi.Input[str]] = None,
                 data_connection_name: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_identity_resource_id: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retrieval_start_date: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing a CosmosDb data connection.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] cosmos_db_account_resource_id: The resource ID of the Cosmos DB account used to create the data connection.
        :param pulumi.Input[str] cosmos_db_container: The name of an existing container in the Cosmos DB database.
        :param pulumi.Input[str] cosmos_db_database: The name of an existing database in the Cosmos DB account.
        :param pulumi.Input[str] data_connection_name: The name of the data connection.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto cluster.
        :param pulumi.Input[str] kind: Kind of the endpoint for the data connection
               Expected value is 'CosmosDb'.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] managed_identity_resource_id: The resource ID of a managed system or user-assigned identity. The identity is used to authenticate with Cosmos DB.
        :param pulumi.Input[str] mapping_rule_name: The name of an existing mapping rule to use when ingesting the retrieved data.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        :param pulumi.Input[str] retrieval_start_date: Optional. If defined, the data connection retrieves Cosmos DB documents created or updated after the specified retrieval start date.
        :param pulumi.Input[str] table_name: The case-sensitive name of the existing target table in your cluster. Retrieved data is ingested into this table.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CosmosDbDataConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a CosmosDb data connection.

        :param str resource_name: The name of the resource.
        :param CosmosDbDataConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CosmosDbDataConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cosmos_db_account_resource_id: Optional[pulumi.Input[str]] = None,
                 cosmos_db_container: Optional[pulumi.Input[str]] = None,
                 cosmos_db_database: Optional[pulumi.Input[str]] = None,
                 data_connection_name: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_identity_resource_id: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retrieval_start_date: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CosmosDbDataConnectionArgs.__new__(CosmosDbDataConnectionArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if cosmos_db_account_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'cosmos_db_account_resource_id'")
            __props__.__dict__["cosmos_db_account_resource_id"] = cosmos_db_account_resource_id
            if cosmos_db_container is None and not opts.urn:
                raise TypeError("Missing required property 'cosmos_db_container'")
            __props__.__dict__["cosmos_db_container"] = cosmos_db_container
            if cosmos_db_database is None and not opts.urn:
                raise TypeError("Missing required property 'cosmos_db_database'")
            __props__.__dict__["cosmos_db_database"] = cosmos_db_database
            __props__.__dict__["data_connection_name"] = data_connection_name
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'CosmosDb'
            __props__.__dict__["location"] = location
            if managed_identity_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'managed_identity_resource_id'")
            __props__.__dict__["managed_identity_resource_id"] = managed_identity_resource_id
            __props__.__dict__["mapping_rule_name"] = mapping_rule_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["retrieval_start_date"] = retrieval_start_date
            if table_name is None and not opts.urn:
                raise TypeError("Missing required property 'table_name'")
            __props__.__dict__["table_name"] = table_name
            __props__.__dict__["managed_identity_object_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:kusto:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20190121:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20190515:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20190907:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20191109:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20200215:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20200614:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20200918:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20210101:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20210827:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20220201:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20220707:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20221111:CosmosDbDataConnection"), pulumi.Alias(type_="azure-native:kusto/v20230502:CosmosDbDataConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CosmosDbDataConnection, __self__).__init__(
            'azure-native:kusto/v20221229:CosmosDbDataConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CosmosDbDataConnection':
        """
        Get an existing CosmosDbDataConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CosmosDbDataConnectionArgs.__new__(CosmosDbDataConnectionArgs)

        __props__.__dict__["cosmos_db_account_resource_id"] = None
        __props__.__dict__["cosmos_db_container"] = None
        __props__.__dict__["cosmos_db_database"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_identity_object_id"] = None
        __props__.__dict__["managed_identity_resource_id"] = None
        __props__.__dict__["mapping_rule_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["retrieval_start_date"] = None
        __props__.__dict__["table_name"] = None
        __props__.__dict__["type"] = None
        return CosmosDbDataConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cosmosDbAccountResourceId")
    def cosmos_db_account_resource_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Cosmos DB account used to create the data connection.
        """
        return pulumi.get(self, "cosmos_db_account_resource_id")

    @property
    @pulumi.getter(name="cosmosDbContainer")
    def cosmos_db_container(self) -> pulumi.Output[str]:
        """
        The name of an existing container in the Cosmos DB database.
        """
        return pulumi.get(self, "cosmos_db_container")

    @property
    @pulumi.getter(name="cosmosDbDatabase")
    def cosmos_db_database(self) -> pulumi.Output[str]:
        """
        The name of an existing database in the Cosmos DB account.
        """
        return pulumi.get(self, "cosmos_db_database")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of the endpoint for the data connection
        Expected value is 'CosmosDb'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedIdentityObjectId")
    def managed_identity_object_id(self) -> pulumi.Output[str]:
        """
        The object ID of the managed identity resource.
        """
        return pulumi.get(self, "managed_identity_object_id")

    @property
    @pulumi.getter(name="managedIdentityResourceId")
    def managed_identity_resource_id(self) -> pulumi.Output[str]:
        """
        The resource ID of a managed system or user-assigned identity. The identity is used to authenticate with Cosmos DB.
        """
        return pulumi.get(self, "managed_identity_resource_id")

    @property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of an existing mapping rule to use when ingesting the retrieved data.
        """
        return pulumi.get(self, "mapping_rule_name")

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
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> pulumi.Output[Optional[str]]:
        """
        Optional. If defined, the data connection retrieves Cosmos DB documents created or updated after the specified retrieval start date.
        """
        return pulumi.get(self, "retrieval_start_date")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[str]:
        """
        The case-sensitive name of the existing target table in your cluster. Retrieved data is ingested into this table.
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

