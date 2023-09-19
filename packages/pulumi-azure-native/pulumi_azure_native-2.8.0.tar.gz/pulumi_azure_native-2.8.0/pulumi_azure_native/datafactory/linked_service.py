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

__all__ = ['LinkedServiceArgs', 'LinkedService']

@pulumi.input_type
class LinkedServiceArgs:
    def __init__(__self__, *,
                 factory_name: pulumi.Input[str],
                 properties: pulumi.Input[Union['AmazonMWSLinkedServiceArgs', 'AmazonRdsForOracleLinkedServiceArgs', 'AmazonRdsForSqlServerLinkedServiceArgs', 'AmazonRedshiftLinkedServiceArgs', 'AmazonS3CompatibleLinkedServiceArgs', 'AmazonS3LinkedServiceArgs', 'AppFiguresLinkedServiceArgs', 'AsanaLinkedServiceArgs', 'AzureBatchLinkedServiceArgs', 'AzureBlobFSLinkedServiceArgs', 'AzureBlobStorageLinkedServiceArgs', 'AzureDataExplorerLinkedServiceArgs', 'AzureDataLakeAnalyticsLinkedServiceArgs', 'AzureDataLakeStoreLinkedServiceArgs', 'AzureDatabricksDeltaLakeLinkedServiceArgs', 'AzureDatabricksLinkedServiceArgs', 'AzureFileStorageLinkedServiceArgs', 'AzureFunctionLinkedServiceArgs', 'AzureKeyVaultLinkedServiceArgs', 'AzureMLLinkedServiceArgs', 'AzureMLServiceLinkedServiceArgs', 'AzureMariaDBLinkedServiceArgs', 'AzureMySqlLinkedServiceArgs', 'AzurePostgreSqlLinkedServiceArgs', 'AzureSearchLinkedServiceArgs', 'AzureSqlDWLinkedServiceArgs', 'AzureSqlDatabaseLinkedServiceArgs', 'AzureSqlMILinkedServiceArgs', 'AzureStorageLinkedServiceArgs', 'AzureSynapseArtifactsLinkedServiceArgs', 'AzureTableStorageLinkedServiceArgs', 'CassandraLinkedServiceArgs', 'CommonDataServiceForAppsLinkedServiceArgs', 'ConcurLinkedServiceArgs', 'CosmosDbLinkedServiceArgs', 'CosmosDbMongoDbApiLinkedServiceArgs', 'CouchbaseLinkedServiceArgs', 'CustomDataSourceLinkedServiceArgs', 'DataworldLinkedServiceArgs', 'Db2LinkedServiceArgs', 'DrillLinkedServiceArgs', 'DynamicsAXLinkedServiceArgs', 'DynamicsCrmLinkedServiceArgs', 'DynamicsLinkedServiceArgs', 'EloquaLinkedServiceArgs', 'FileServerLinkedServiceArgs', 'FtpServerLinkedServiceArgs', 'GoogleAdWordsLinkedServiceArgs', 'GoogleBigQueryLinkedServiceArgs', 'GoogleCloudStorageLinkedServiceArgs', 'GoogleSheetsLinkedServiceArgs', 'GreenplumLinkedServiceArgs', 'HBaseLinkedServiceArgs', 'HDInsightLinkedServiceArgs', 'HDInsightOnDemandLinkedServiceArgs', 'HdfsLinkedServiceArgs', 'HiveLinkedServiceArgs', 'HttpLinkedServiceArgs', 'HubspotLinkedServiceArgs', 'ImpalaLinkedServiceArgs', 'InformixLinkedServiceArgs', 'JiraLinkedServiceArgs', 'MagentoLinkedServiceArgs', 'MariaDBLinkedServiceArgs', 'MarketoLinkedServiceArgs', 'MicrosoftAccessLinkedServiceArgs', 'MongoDbAtlasLinkedServiceArgs', 'MongoDbLinkedServiceArgs', 'MongoDbV2LinkedServiceArgs', 'MySqlLinkedServiceArgs', 'NetezzaLinkedServiceArgs', 'ODataLinkedServiceArgs', 'OdbcLinkedServiceArgs', 'Office365LinkedServiceArgs', 'OracleCloudStorageLinkedServiceArgs', 'OracleLinkedServiceArgs', 'OracleServiceCloudLinkedServiceArgs', 'PaypalLinkedServiceArgs', 'PhoenixLinkedServiceArgs', 'PostgreSqlLinkedServiceArgs', 'PrestoLinkedServiceArgs', 'QuickBooksLinkedServiceArgs', 'QuickbaseLinkedServiceArgs', 'ResponsysLinkedServiceArgs', 'RestServiceLinkedServiceArgs', 'SalesforceLinkedServiceArgs', 'SalesforceMarketingCloudLinkedServiceArgs', 'SalesforceServiceCloudLinkedServiceArgs', 'SapBWLinkedServiceArgs', 'SapCloudForCustomerLinkedServiceArgs', 'SapEccLinkedServiceArgs', 'SapHanaLinkedServiceArgs', 'SapOdpLinkedServiceArgs', 'SapOpenHubLinkedServiceArgs', 'SapTableLinkedServiceArgs', 'ServiceNowLinkedServiceArgs', 'SftpServerLinkedServiceArgs', 'SharePointOnlineListLinkedServiceArgs', 'ShopifyLinkedServiceArgs', 'SmartsheetLinkedServiceArgs', 'SnowflakeLinkedServiceArgs', 'SparkLinkedServiceArgs', 'SqlServerLinkedServiceArgs', 'SquareLinkedServiceArgs', 'SybaseLinkedServiceArgs', 'TeamDeskLinkedServiceArgs', 'TeradataLinkedServiceArgs', 'TwilioLinkedServiceArgs', 'VerticaLinkedServiceArgs', 'WebLinkedServiceArgs', 'XeroLinkedServiceArgs', 'ZendeskLinkedServiceArgs', 'ZohoLinkedServiceArgs']],
                 resource_group_name: pulumi.Input[str],
                 linked_service_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LinkedService resource.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[Union['AmazonMWSLinkedServiceArgs', 'AmazonRdsForOracleLinkedServiceArgs', 'AmazonRdsForSqlServerLinkedServiceArgs', 'AmazonRedshiftLinkedServiceArgs', 'AmazonS3CompatibleLinkedServiceArgs', 'AmazonS3LinkedServiceArgs', 'AppFiguresLinkedServiceArgs', 'AsanaLinkedServiceArgs', 'AzureBatchLinkedServiceArgs', 'AzureBlobFSLinkedServiceArgs', 'AzureBlobStorageLinkedServiceArgs', 'AzureDataExplorerLinkedServiceArgs', 'AzureDataLakeAnalyticsLinkedServiceArgs', 'AzureDataLakeStoreLinkedServiceArgs', 'AzureDatabricksDeltaLakeLinkedServiceArgs', 'AzureDatabricksLinkedServiceArgs', 'AzureFileStorageLinkedServiceArgs', 'AzureFunctionLinkedServiceArgs', 'AzureKeyVaultLinkedServiceArgs', 'AzureMLLinkedServiceArgs', 'AzureMLServiceLinkedServiceArgs', 'AzureMariaDBLinkedServiceArgs', 'AzureMySqlLinkedServiceArgs', 'AzurePostgreSqlLinkedServiceArgs', 'AzureSearchLinkedServiceArgs', 'AzureSqlDWLinkedServiceArgs', 'AzureSqlDatabaseLinkedServiceArgs', 'AzureSqlMILinkedServiceArgs', 'AzureStorageLinkedServiceArgs', 'AzureSynapseArtifactsLinkedServiceArgs', 'AzureTableStorageLinkedServiceArgs', 'CassandraLinkedServiceArgs', 'CommonDataServiceForAppsLinkedServiceArgs', 'ConcurLinkedServiceArgs', 'CosmosDbLinkedServiceArgs', 'CosmosDbMongoDbApiLinkedServiceArgs', 'CouchbaseLinkedServiceArgs', 'CustomDataSourceLinkedServiceArgs', 'DataworldLinkedServiceArgs', 'Db2LinkedServiceArgs', 'DrillLinkedServiceArgs', 'DynamicsAXLinkedServiceArgs', 'DynamicsCrmLinkedServiceArgs', 'DynamicsLinkedServiceArgs', 'EloquaLinkedServiceArgs', 'FileServerLinkedServiceArgs', 'FtpServerLinkedServiceArgs', 'GoogleAdWordsLinkedServiceArgs', 'GoogleBigQueryLinkedServiceArgs', 'GoogleCloudStorageLinkedServiceArgs', 'GoogleSheetsLinkedServiceArgs', 'GreenplumLinkedServiceArgs', 'HBaseLinkedServiceArgs', 'HDInsightLinkedServiceArgs', 'HDInsightOnDemandLinkedServiceArgs', 'HdfsLinkedServiceArgs', 'HiveLinkedServiceArgs', 'HttpLinkedServiceArgs', 'HubspotLinkedServiceArgs', 'ImpalaLinkedServiceArgs', 'InformixLinkedServiceArgs', 'JiraLinkedServiceArgs', 'MagentoLinkedServiceArgs', 'MariaDBLinkedServiceArgs', 'MarketoLinkedServiceArgs', 'MicrosoftAccessLinkedServiceArgs', 'MongoDbAtlasLinkedServiceArgs', 'MongoDbLinkedServiceArgs', 'MongoDbV2LinkedServiceArgs', 'MySqlLinkedServiceArgs', 'NetezzaLinkedServiceArgs', 'ODataLinkedServiceArgs', 'OdbcLinkedServiceArgs', 'Office365LinkedServiceArgs', 'OracleCloudStorageLinkedServiceArgs', 'OracleLinkedServiceArgs', 'OracleServiceCloudLinkedServiceArgs', 'PaypalLinkedServiceArgs', 'PhoenixLinkedServiceArgs', 'PostgreSqlLinkedServiceArgs', 'PrestoLinkedServiceArgs', 'QuickBooksLinkedServiceArgs', 'QuickbaseLinkedServiceArgs', 'ResponsysLinkedServiceArgs', 'RestServiceLinkedServiceArgs', 'SalesforceLinkedServiceArgs', 'SalesforceMarketingCloudLinkedServiceArgs', 'SalesforceServiceCloudLinkedServiceArgs', 'SapBWLinkedServiceArgs', 'SapCloudForCustomerLinkedServiceArgs', 'SapEccLinkedServiceArgs', 'SapHanaLinkedServiceArgs', 'SapOdpLinkedServiceArgs', 'SapOpenHubLinkedServiceArgs', 'SapTableLinkedServiceArgs', 'ServiceNowLinkedServiceArgs', 'SftpServerLinkedServiceArgs', 'SharePointOnlineListLinkedServiceArgs', 'ShopifyLinkedServiceArgs', 'SmartsheetLinkedServiceArgs', 'SnowflakeLinkedServiceArgs', 'SparkLinkedServiceArgs', 'SqlServerLinkedServiceArgs', 'SquareLinkedServiceArgs', 'SybaseLinkedServiceArgs', 'TeamDeskLinkedServiceArgs', 'TeradataLinkedServiceArgs', 'TwilioLinkedServiceArgs', 'VerticaLinkedServiceArgs', 'WebLinkedServiceArgs', 'XeroLinkedServiceArgs', 'ZendeskLinkedServiceArgs', 'ZohoLinkedServiceArgs']] properties: Properties of linked service.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] linked_service_name: The linked service name.
        """
        pulumi.set(__self__, "factory_name", factory_name)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if linked_service_name is not None:
            pulumi.set(__self__, "linked_service_name", linked_service_name)

    @property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[str]:
        """
        The factory name.
        """
        return pulumi.get(self, "factory_name")

    @factory_name.setter
    def factory_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "factory_name", value)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union['AmazonMWSLinkedServiceArgs', 'AmazonRdsForOracleLinkedServiceArgs', 'AmazonRdsForSqlServerLinkedServiceArgs', 'AmazonRedshiftLinkedServiceArgs', 'AmazonS3CompatibleLinkedServiceArgs', 'AmazonS3LinkedServiceArgs', 'AppFiguresLinkedServiceArgs', 'AsanaLinkedServiceArgs', 'AzureBatchLinkedServiceArgs', 'AzureBlobFSLinkedServiceArgs', 'AzureBlobStorageLinkedServiceArgs', 'AzureDataExplorerLinkedServiceArgs', 'AzureDataLakeAnalyticsLinkedServiceArgs', 'AzureDataLakeStoreLinkedServiceArgs', 'AzureDatabricksDeltaLakeLinkedServiceArgs', 'AzureDatabricksLinkedServiceArgs', 'AzureFileStorageLinkedServiceArgs', 'AzureFunctionLinkedServiceArgs', 'AzureKeyVaultLinkedServiceArgs', 'AzureMLLinkedServiceArgs', 'AzureMLServiceLinkedServiceArgs', 'AzureMariaDBLinkedServiceArgs', 'AzureMySqlLinkedServiceArgs', 'AzurePostgreSqlLinkedServiceArgs', 'AzureSearchLinkedServiceArgs', 'AzureSqlDWLinkedServiceArgs', 'AzureSqlDatabaseLinkedServiceArgs', 'AzureSqlMILinkedServiceArgs', 'AzureStorageLinkedServiceArgs', 'AzureSynapseArtifactsLinkedServiceArgs', 'AzureTableStorageLinkedServiceArgs', 'CassandraLinkedServiceArgs', 'CommonDataServiceForAppsLinkedServiceArgs', 'ConcurLinkedServiceArgs', 'CosmosDbLinkedServiceArgs', 'CosmosDbMongoDbApiLinkedServiceArgs', 'CouchbaseLinkedServiceArgs', 'CustomDataSourceLinkedServiceArgs', 'DataworldLinkedServiceArgs', 'Db2LinkedServiceArgs', 'DrillLinkedServiceArgs', 'DynamicsAXLinkedServiceArgs', 'DynamicsCrmLinkedServiceArgs', 'DynamicsLinkedServiceArgs', 'EloquaLinkedServiceArgs', 'FileServerLinkedServiceArgs', 'FtpServerLinkedServiceArgs', 'GoogleAdWordsLinkedServiceArgs', 'GoogleBigQueryLinkedServiceArgs', 'GoogleCloudStorageLinkedServiceArgs', 'GoogleSheetsLinkedServiceArgs', 'GreenplumLinkedServiceArgs', 'HBaseLinkedServiceArgs', 'HDInsightLinkedServiceArgs', 'HDInsightOnDemandLinkedServiceArgs', 'HdfsLinkedServiceArgs', 'HiveLinkedServiceArgs', 'HttpLinkedServiceArgs', 'HubspotLinkedServiceArgs', 'ImpalaLinkedServiceArgs', 'InformixLinkedServiceArgs', 'JiraLinkedServiceArgs', 'MagentoLinkedServiceArgs', 'MariaDBLinkedServiceArgs', 'MarketoLinkedServiceArgs', 'MicrosoftAccessLinkedServiceArgs', 'MongoDbAtlasLinkedServiceArgs', 'MongoDbLinkedServiceArgs', 'MongoDbV2LinkedServiceArgs', 'MySqlLinkedServiceArgs', 'NetezzaLinkedServiceArgs', 'ODataLinkedServiceArgs', 'OdbcLinkedServiceArgs', 'Office365LinkedServiceArgs', 'OracleCloudStorageLinkedServiceArgs', 'OracleLinkedServiceArgs', 'OracleServiceCloudLinkedServiceArgs', 'PaypalLinkedServiceArgs', 'PhoenixLinkedServiceArgs', 'PostgreSqlLinkedServiceArgs', 'PrestoLinkedServiceArgs', 'QuickBooksLinkedServiceArgs', 'QuickbaseLinkedServiceArgs', 'ResponsysLinkedServiceArgs', 'RestServiceLinkedServiceArgs', 'SalesforceLinkedServiceArgs', 'SalesforceMarketingCloudLinkedServiceArgs', 'SalesforceServiceCloudLinkedServiceArgs', 'SapBWLinkedServiceArgs', 'SapCloudForCustomerLinkedServiceArgs', 'SapEccLinkedServiceArgs', 'SapHanaLinkedServiceArgs', 'SapOdpLinkedServiceArgs', 'SapOpenHubLinkedServiceArgs', 'SapTableLinkedServiceArgs', 'ServiceNowLinkedServiceArgs', 'SftpServerLinkedServiceArgs', 'SharePointOnlineListLinkedServiceArgs', 'ShopifyLinkedServiceArgs', 'SmartsheetLinkedServiceArgs', 'SnowflakeLinkedServiceArgs', 'SparkLinkedServiceArgs', 'SqlServerLinkedServiceArgs', 'SquareLinkedServiceArgs', 'SybaseLinkedServiceArgs', 'TeamDeskLinkedServiceArgs', 'TeradataLinkedServiceArgs', 'TwilioLinkedServiceArgs', 'VerticaLinkedServiceArgs', 'WebLinkedServiceArgs', 'XeroLinkedServiceArgs', 'ZendeskLinkedServiceArgs', 'ZohoLinkedServiceArgs']]:
        """
        Properties of linked service.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input[Union['AmazonMWSLinkedServiceArgs', 'AmazonRdsForOracleLinkedServiceArgs', 'AmazonRdsForSqlServerLinkedServiceArgs', 'AmazonRedshiftLinkedServiceArgs', 'AmazonS3CompatibleLinkedServiceArgs', 'AmazonS3LinkedServiceArgs', 'AppFiguresLinkedServiceArgs', 'AsanaLinkedServiceArgs', 'AzureBatchLinkedServiceArgs', 'AzureBlobFSLinkedServiceArgs', 'AzureBlobStorageLinkedServiceArgs', 'AzureDataExplorerLinkedServiceArgs', 'AzureDataLakeAnalyticsLinkedServiceArgs', 'AzureDataLakeStoreLinkedServiceArgs', 'AzureDatabricksDeltaLakeLinkedServiceArgs', 'AzureDatabricksLinkedServiceArgs', 'AzureFileStorageLinkedServiceArgs', 'AzureFunctionLinkedServiceArgs', 'AzureKeyVaultLinkedServiceArgs', 'AzureMLLinkedServiceArgs', 'AzureMLServiceLinkedServiceArgs', 'AzureMariaDBLinkedServiceArgs', 'AzureMySqlLinkedServiceArgs', 'AzurePostgreSqlLinkedServiceArgs', 'AzureSearchLinkedServiceArgs', 'AzureSqlDWLinkedServiceArgs', 'AzureSqlDatabaseLinkedServiceArgs', 'AzureSqlMILinkedServiceArgs', 'AzureStorageLinkedServiceArgs', 'AzureSynapseArtifactsLinkedServiceArgs', 'AzureTableStorageLinkedServiceArgs', 'CassandraLinkedServiceArgs', 'CommonDataServiceForAppsLinkedServiceArgs', 'ConcurLinkedServiceArgs', 'CosmosDbLinkedServiceArgs', 'CosmosDbMongoDbApiLinkedServiceArgs', 'CouchbaseLinkedServiceArgs', 'CustomDataSourceLinkedServiceArgs', 'DataworldLinkedServiceArgs', 'Db2LinkedServiceArgs', 'DrillLinkedServiceArgs', 'DynamicsAXLinkedServiceArgs', 'DynamicsCrmLinkedServiceArgs', 'DynamicsLinkedServiceArgs', 'EloquaLinkedServiceArgs', 'FileServerLinkedServiceArgs', 'FtpServerLinkedServiceArgs', 'GoogleAdWordsLinkedServiceArgs', 'GoogleBigQueryLinkedServiceArgs', 'GoogleCloudStorageLinkedServiceArgs', 'GoogleSheetsLinkedServiceArgs', 'GreenplumLinkedServiceArgs', 'HBaseLinkedServiceArgs', 'HDInsightLinkedServiceArgs', 'HDInsightOnDemandLinkedServiceArgs', 'HdfsLinkedServiceArgs', 'HiveLinkedServiceArgs', 'HttpLinkedServiceArgs', 'HubspotLinkedServiceArgs', 'ImpalaLinkedServiceArgs', 'InformixLinkedServiceArgs', 'JiraLinkedServiceArgs', 'MagentoLinkedServiceArgs', 'MariaDBLinkedServiceArgs', 'MarketoLinkedServiceArgs', 'MicrosoftAccessLinkedServiceArgs', 'MongoDbAtlasLinkedServiceArgs', 'MongoDbLinkedServiceArgs', 'MongoDbV2LinkedServiceArgs', 'MySqlLinkedServiceArgs', 'NetezzaLinkedServiceArgs', 'ODataLinkedServiceArgs', 'OdbcLinkedServiceArgs', 'Office365LinkedServiceArgs', 'OracleCloudStorageLinkedServiceArgs', 'OracleLinkedServiceArgs', 'OracleServiceCloudLinkedServiceArgs', 'PaypalLinkedServiceArgs', 'PhoenixLinkedServiceArgs', 'PostgreSqlLinkedServiceArgs', 'PrestoLinkedServiceArgs', 'QuickBooksLinkedServiceArgs', 'QuickbaseLinkedServiceArgs', 'ResponsysLinkedServiceArgs', 'RestServiceLinkedServiceArgs', 'SalesforceLinkedServiceArgs', 'SalesforceMarketingCloudLinkedServiceArgs', 'SalesforceServiceCloudLinkedServiceArgs', 'SapBWLinkedServiceArgs', 'SapCloudForCustomerLinkedServiceArgs', 'SapEccLinkedServiceArgs', 'SapHanaLinkedServiceArgs', 'SapOdpLinkedServiceArgs', 'SapOpenHubLinkedServiceArgs', 'SapTableLinkedServiceArgs', 'ServiceNowLinkedServiceArgs', 'SftpServerLinkedServiceArgs', 'SharePointOnlineListLinkedServiceArgs', 'ShopifyLinkedServiceArgs', 'SmartsheetLinkedServiceArgs', 'SnowflakeLinkedServiceArgs', 'SparkLinkedServiceArgs', 'SqlServerLinkedServiceArgs', 'SquareLinkedServiceArgs', 'SybaseLinkedServiceArgs', 'TeamDeskLinkedServiceArgs', 'TeradataLinkedServiceArgs', 'TwilioLinkedServiceArgs', 'VerticaLinkedServiceArgs', 'WebLinkedServiceArgs', 'XeroLinkedServiceArgs', 'ZendeskLinkedServiceArgs', 'ZohoLinkedServiceArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="linkedServiceName")
    def linked_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The linked service name.
        """
        return pulumi.get(self, "linked_service_name")

    @linked_service_name.setter
    def linked_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "linked_service_name", value)


class LinkedService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 linked_service_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['AmazonMWSLinkedServiceArgs'], pulumi.InputType['AmazonRdsForOracleLinkedServiceArgs'], pulumi.InputType['AmazonRdsForSqlServerLinkedServiceArgs'], pulumi.InputType['AmazonRedshiftLinkedServiceArgs'], pulumi.InputType['AmazonS3CompatibleLinkedServiceArgs'], pulumi.InputType['AmazonS3LinkedServiceArgs'], pulumi.InputType['AppFiguresLinkedServiceArgs'], pulumi.InputType['AsanaLinkedServiceArgs'], pulumi.InputType['AzureBatchLinkedServiceArgs'], pulumi.InputType['AzureBlobFSLinkedServiceArgs'], pulumi.InputType['AzureBlobStorageLinkedServiceArgs'], pulumi.InputType['AzureDataExplorerLinkedServiceArgs'], pulumi.InputType['AzureDataLakeAnalyticsLinkedServiceArgs'], pulumi.InputType['AzureDataLakeStoreLinkedServiceArgs'], pulumi.InputType['AzureDatabricksDeltaLakeLinkedServiceArgs'], pulumi.InputType['AzureDatabricksLinkedServiceArgs'], pulumi.InputType['AzureFileStorageLinkedServiceArgs'], pulumi.InputType['AzureFunctionLinkedServiceArgs'], pulumi.InputType['AzureKeyVaultLinkedServiceArgs'], pulumi.InputType['AzureMLLinkedServiceArgs'], pulumi.InputType['AzureMLServiceLinkedServiceArgs'], pulumi.InputType['AzureMariaDBLinkedServiceArgs'], pulumi.InputType['AzureMySqlLinkedServiceArgs'], pulumi.InputType['AzurePostgreSqlLinkedServiceArgs'], pulumi.InputType['AzureSearchLinkedServiceArgs'], pulumi.InputType['AzureSqlDWLinkedServiceArgs'], pulumi.InputType['AzureSqlDatabaseLinkedServiceArgs'], pulumi.InputType['AzureSqlMILinkedServiceArgs'], pulumi.InputType['AzureStorageLinkedServiceArgs'], pulumi.InputType['AzureSynapseArtifactsLinkedServiceArgs'], pulumi.InputType['AzureTableStorageLinkedServiceArgs'], pulumi.InputType['CassandraLinkedServiceArgs'], pulumi.InputType['CommonDataServiceForAppsLinkedServiceArgs'], pulumi.InputType['ConcurLinkedServiceArgs'], pulumi.InputType['CosmosDbLinkedServiceArgs'], pulumi.InputType['CosmosDbMongoDbApiLinkedServiceArgs'], pulumi.InputType['CouchbaseLinkedServiceArgs'], pulumi.InputType['CustomDataSourceLinkedServiceArgs'], pulumi.InputType['DataworldLinkedServiceArgs'], pulumi.InputType['Db2LinkedServiceArgs'], pulumi.InputType['DrillLinkedServiceArgs'], pulumi.InputType['DynamicsAXLinkedServiceArgs'], pulumi.InputType['DynamicsCrmLinkedServiceArgs'], pulumi.InputType['DynamicsLinkedServiceArgs'], pulumi.InputType['EloquaLinkedServiceArgs'], pulumi.InputType['FileServerLinkedServiceArgs'], pulumi.InputType['FtpServerLinkedServiceArgs'], pulumi.InputType['GoogleAdWordsLinkedServiceArgs'], pulumi.InputType['GoogleBigQueryLinkedServiceArgs'], pulumi.InputType['GoogleCloudStorageLinkedServiceArgs'], pulumi.InputType['GoogleSheetsLinkedServiceArgs'], pulumi.InputType['GreenplumLinkedServiceArgs'], pulumi.InputType['HBaseLinkedServiceArgs'], pulumi.InputType['HDInsightLinkedServiceArgs'], pulumi.InputType['HDInsightOnDemandLinkedServiceArgs'], pulumi.InputType['HdfsLinkedServiceArgs'], pulumi.InputType['HiveLinkedServiceArgs'], pulumi.InputType['HttpLinkedServiceArgs'], pulumi.InputType['HubspotLinkedServiceArgs'], pulumi.InputType['ImpalaLinkedServiceArgs'], pulumi.InputType['InformixLinkedServiceArgs'], pulumi.InputType['JiraLinkedServiceArgs'], pulumi.InputType['MagentoLinkedServiceArgs'], pulumi.InputType['MariaDBLinkedServiceArgs'], pulumi.InputType['MarketoLinkedServiceArgs'], pulumi.InputType['MicrosoftAccessLinkedServiceArgs'], pulumi.InputType['MongoDbAtlasLinkedServiceArgs'], pulumi.InputType['MongoDbLinkedServiceArgs'], pulumi.InputType['MongoDbV2LinkedServiceArgs'], pulumi.InputType['MySqlLinkedServiceArgs'], pulumi.InputType['NetezzaLinkedServiceArgs'], pulumi.InputType['ODataLinkedServiceArgs'], pulumi.InputType['OdbcLinkedServiceArgs'], pulumi.InputType['Office365LinkedServiceArgs'], pulumi.InputType['OracleCloudStorageLinkedServiceArgs'], pulumi.InputType['OracleLinkedServiceArgs'], pulumi.InputType['OracleServiceCloudLinkedServiceArgs'], pulumi.InputType['PaypalLinkedServiceArgs'], pulumi.InputType['PhoenixLinkedServiceArgs'], pulumi.InputType['PostgreSqlLinkedServiceArgs'], pulumi.InputType['PrestoLinkedServiceArgs'], pulumi.InputType['QuickBooksLinkedServiceArgs'], pulumi.InputType['QuickbaseLinkedServiceArgs'], pulumi.InputType['ResponsysLinkedServiceArgs'], pulumi.InputType['RestServiceLinkedServiceArgs'], pulumi.InputType['SalesforceLinkedServiceArgs'], pulumi.InputType['SalesforceMarketingCloudLinkedServiceArgs'], pulumi.InputType['SalesforceServiceCloudLinkedServiceArgs'], pulumi.InputType['SapBWLinkedServiceArgs'], pulumi.InputType['SapCloudForCustomerLinkedServiceArgs'], pulumi.InputType['SapEccLinkedServiceArgs'], pulumi.InputType['SapHanaLinkedServiceArgs'], pulumi.InputType['SapOdpLinkedServiceArgs'], pulumi.InputType['SapOpenHubLinkedServiceArgs'], pulumi.InputType['SapTableLinkedServiceArgs'], pulumi.InputType['ServiceNowLinkedServiceArgs'], pulumi.InputType['SftpServerLinkedServiceArgs'], pulumi.InputType['SharePointOnlineListLinkedServiceArgs'], pulumi.InputType['ShopifyLinkedServiceArgs'], pulumi.InputType['SmartsheetLinkedServiceArgs'], pulumi.InputType['SnowflakeLinkedServiceArgs'], pulumi.InputType['SparkLinkedServiceArgs'], pulumi.InputType['SqlServerLinkedServiceArgs'], pulumi.InputType['SquareLinkedServiceArgs'], pulumi.InputType['SybaseLinkedServiceArgs'], pulumi.InputType['TeamDeskLinkedServiceArgs'], pulumi.InputType['TeradataLinkedServiceArgs'], pulumi.InputType['TwilioLinkedServiceArgs'], pulumi.InputType['VerticaLinkedServiceArgs'], pulumi.InputType['WebLinkedServiceArgs'], pulumi.InputType['XeroLinkedServiceArgs'], pulumi.InputType['ZendeskLinkedServiceArgs'], pulumi.InputType['ZohoLinkedServiceArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Linked service resource type.
        Azure REST API version: 2018-06-01. Prior API version in Azure Native 1.x: 2018-06-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[str] linked_service_name: The linked service name.
        :param pulumi.Input[Union[pulumi.InputType['AmazonMWSLinkedServiceArgs'], pulumi.InputType['AmazonRdsForOracleLinkedServiceArgs'], pulumi.InputType['AmazonRdsForSqlServerLinkedServiceArgs'], pulumi.InputType['AmazonRedshiftLinkedServiceArgs'], pulumi.InputType['AmazonS3CompatibleLinkedServiceArgs'], pulumi.InputType['AmazonS3LinkedServiceArgs'], pulumi.InputType['AppFiguresLinkedServiceArgs'], pulumi.InputType['AsanaLinkedServiceArgs'], pulumi.InputType['AzureBatchLinkedServiceArgs'], pulumi.InputType['AzureBlobFSLinkedServiceArgs'], pulumi.InputType['AzureBlobStorageLinkedServiceArgs'], pulumi.InputType['AzureDataExplorerLinkedServiceArgs'], pulumi.InputType['AzureDataLakeAnalyticsLinkedServiceArgs'], pulumi.InputType['AzureDataLakeStoreLinkedServiceArgs'], pulumi.InputType['AzureDatabricksDeltaLakeLinkedServiceArgs'], pulumi.InputType['AzureDatabricksLinkedServiceArgs'], pulumi.InputType['AzureFileStorageLinkedServiceArgs'], pulumi.InputType['AzureFunctionLinkedServiceArgs'], pulumi.InputType['AzureKeyVaultLinkedServiceArgs'], pulumi.InputType['AzureMLLinkedServiceArgs'], pulumi.InputType['AzureMLServiceLinkedServiceArgs'], pulumi.InputType['AzureMariaDBLinkedServiceArgs'], pulumi.InputType['AzureMySqlLinkedServiceArgs'], pulumi.InputType['AzurePostgreSqlLinkedServiceArgs'], pulumi.InputType['AzureSearchLinkedServiceArgs'], pulumi.InputType['AzureSqlDWLinkedServiceArgs'], pulumi.InputType['AzureSqlDatabaseLinkedServiceArgs'], pulumi.InputType['AzureSqlMILinkedServiceArgs'], pulumi.InputType['AzureStorageLinkedServiceArgs'], pulumi.InputType['AzureSynapseArtifactsLinkedServiceArgs'], pulumi.InputType['AzureTableStorageLinkedServiceArgs'], pulumi.InputType['CassandraLinkedServiceArgs'], pulumi.InputType['CommonDataServiceForAppsLinkedServiceArgs'], pulumi.InputType['ConcurLinkedServiceArgs'], pulumi.InputType['CosmosDbLinkedServiceArgs'], pulumi.InputType['CosmosDbMongoDbApiLinkedServiceArgs'], pulumi.InputType['CouchbaseLinkedServiceArgs'], pulumi.InputType['CustomDataSourceLinkedServiceArgs'], pulumi.InputType['DataworldLinkedServiceArgs'], pulumi.InputType['Db2LinkedServiceArgs'], pulumi.InputType['DrillLinkedServiceArgs'], pulumi.InputType['DynamicsAXLinkedServiceArgs'], pulumi.InputType['DynamicsCrmLinkedServiceArgs'], pulumi.InputType['DynamicsLinkedServiceArgs'], pulumi.InputType['EloquaLinkedServiceArgs'], pulumi.InputType['FileServerLinkedServiceArgs'], pulumi.InputType['FtpServerLinkedServiceArgs'], pulumi.InputType['GoogleAdWordsLinkedServiceArgs'], pulumi.InputType['GoogleBigQueryLinkedServiceArgs'], pulumi.InputType['GoogleCloudStorageLinkedServiceArgs'], pulumi.InputType['GoogleSheetsLinkedServiceArgs'], pulumi.InputType['GreenplumLinkedServiceArgs'], pulumi.InputType['HBaseLinkedServiceArgs'], pulumi.InputType['HDInsightLinkedServiceArgs'], pulumi.InputType['HDInsightOnDemandLinkedServiceArgs'], pulumi.InputType['HdfsLinkedServiceArgs'], pulumi.InputType['HiveLinkedServiceArgs'], pulumi.InputType['HttpLinkedServiceArgs'], pulumi.InputType['HubspotLinkedServiceArgs'], pulumi.InputType['ImpalaLinkedServiceArgs'], pulumi.InputType['InformixLinkedServiceArgs'], pulumi.InputType['JiraLinkedServiceArgs'], pulumi.InputType['MagentoLinkedServiceArgs'], pulumi.InputType['MariaDBLinkedServiceArgs'], pulumi.InputType['MarketoLinkedServiceArgs'], pulumi.InputType['MicrosoftAccessLinkedServiceArgs'], pulumi.InputType['MongoDbAtlasLinkedServiceArgs'], pulumi.InputType['MongoDbLinkedServiceArgs'], pulumi.InputType['MongoDbV2LinkedServiceArgs'], pulumi.InputType['MySqlLinkedServiceArgs'], pulumi.InputType['NetezzaLinkedServiceArgs'], pulumi.InputType['ODataLinkedServiceArgs'], pulumi.InputType['OdbcLinkedServiceArgs'], pulumi.InputType['Office365LinkedServiceArgs'], pulumi.InputType['OracleCloudStorageLinkedServiceArgs'], pulumi.InputType['OracleLinkedServiceArgs'], pulumi.InputType['OracleServiceCloudLinkedServiceArgs'], pulumi.InputType['PaypalLinkedServiceArgs'], pulumi.InputType['PhoenixLinkedServiceArgs'], pulumi.InputType['PostgreSqlLinkedServiceArgs'], pulumi.InputType['PrestoLinkedServiceArgs'], pulumi.InputType['QuickBooksLinkedServiceArgs'], pulumi.InputType['QuickbaseLinkedServiceArgs'], pulumi.InputType['ResponsysLinkedServiceArgs'], pulumi.InputType['RestServiceLinkedServiceArgs'], pulumi.InputType['SalesforceLinkedServiceArgs'], pulumi.InputType['SalesforceMarketingCloudLinkedServiceArgs'], pulumi.InputType['SalesforceServiceCloudLinkedServiceArgs'], pulumi.InputType['SapBWLinkedServiceArgs'], pulumi.InputType['SapCloudForCustomerLinkedServiceArgs'], pulumi.InputType['SapEccLinkedServiceArgs'], pulumi.InputType['SapHanaLinkedServiceArgs'], pulumi.InputType['SapOdpLinkedServiceArgs'], pulumi.InputType['SapOpenHubLinkedServiceArgs'], pulumi.InputType['SapTableLinkedServiceArgs'], pulumi.InputType['ServiceNowLinkedServiceArgs'], pulumi.InputType['SftpServerLinkedServiceArgs'], pulumi.InputType['SharePointOnlineListLinkedServiceArgs'], pulumi.InputType['ShopifyLinkedServiceArgs'], pulumi.InputType['SmartsheetLinkedServiceArgs'], pulumi.InputType['SnowflakeLinkedServiceArgs'], pulumi.InputType['SparkLinkedServiceArgs'], pulumi.InputType['SqlServerLinkedServiceArgs'], pulumi.InputType['SquareLinkedServiceArgs'], pulumi.InputType['SybaseLinkedServiceArgs'], pulumi.InputType['TeamDeskLinkedServiceArgs'], pulumi.InputType['TeradataLinkedServiceArgs'], pulumi.InputType['TwilioLinkedServiceArgs'], pulumi.InputType['VerticaLinkedServiceArgs'], pulumi.InputType['WebLinkedServiceArgs'], pulumi.InputType['XeroLinkedServiceArgs'], pulumi.InputType['ZendeskLinkedServiceArgs'], pulumi.InputType['ZohoLinkedServiceArgs']]] properties: Properties of linked service.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LinkedServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Linked service resource type.
        Azure REST API version: 2018-06-01. Prior API version in Azure Native 1.x: 2018-06-01

        :param str resource_name: The name of the resource.
        :param LinkedServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LinkedServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 linked_service_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['AmazonMWSLinkedServiceArgs'], pulumi.InputType['AmazonRdsForOracleLinkedServiceArgs'], pulumi.InputType['AmazonRdsForSqlServerLinkedServiceArgs'], pulumi.InputType['AmazonRedshiftLinkedServiceArgs'], pulumi.InputType['AmazonS3CompatibleLinkedServiceArgs'], pulumi.InputType['AmazonS3LinkedServiceArgs'], pulumi.InputType['AppFiguresLinkedServiceArgs'], pulumi.InputType['AsanaLinkedServiceArgs'], pulumi.InputType['AzureBatchLinkedServiceArgs'], pulumi.InputType['AzureBlobFSLinkedServiceArgs'], pulumi.InputType['AzureBlobStorageLinkedServiceArgs'], pulumi.InputType['AzureDataExplorerLinkedServiceArgs'], pulumi.InputType['AzureDataLakeAnalyticsLinkedServiceArgs'], pulumi.InputType['AzureDataLakeStoreLinkedServiceArgs'], pulumi.InputType['AzureDatabricksDeltaLakeLinkedServiceArgs'], pulumi.InputType['AzureDatabricksLinkedServiceArgs'], pulumi.InputType['AzureFileStorageLinkedServiceArgs'], pulumi.InputType['AzureFunctionLinkedServiceArgs'], pulumi.InputType['AzureKeyVaultLinkedServiceArgs'], pulumi.InputType['AzureMLLinkedServiceArgs'], pulumi.InputType['AzureMLServiceLinkedServiceArgs'], pulumi.InputType['AzureMariaDBLinkedServiceArgs'], pulumi.InputType['AzureMySqlLinkedServiceArgs'], pulumi.InputType['AzurePostgreSqlLinkedServiceArgs'], pulumi.InputType['AzureSearchLinkedServiceArgs'], pulumi.InputType['AzureSqlDWLinkedServiceArgs'], pulumi.InputType['AzureSqlDatabaseLinkedServiceArgs'], pulumi.InputType['AzureSqlMILinkedServiceArgs'], pulumi.InputType['AzureStorageLinkedServiceArgs'], pulumi.InputType['AzureSynapseArtifactsLinkedServiceArgs'], pulumi.InputType['AzureTableStorageLinkedServiceArgs'], pulumi.InputType['CassandraLinkedServiceArgs'], pulumi.InputType['CommonDataServiceForAppsLinkedServiceArgs'], pulumi.InputType['ConcurLinkedServiceArgs'], pulumi.InputType['CosmosDbLinkedServiceArgs'], pulumi.InputType['CosmosDbMongoDbApiLinkedServiceArgs'], pulumi.InputType['CouchbaseLinkedServiceArgs'], pulumi.InputType['CustomDataSourceLinkedServiceArgs'], pulumi.InputType['DataworldLinkedServiceArgs'], pulumi.InputType['Db2LinkedServiceArgs'], pulumi.InputType['DrillLinkedServiceArgs'], pulumi.InputType['DynamicsAXLinkedServiceArgs'], pulumi.InputType['DynamicsCrmLinkedServiceArgs'], pulumi.InputType['DynamicsLinkedServiceArgs'], pulumi.InputType['EloquaLinkedServiceArgs'], pulumi.InputType['FileServerLinkedServiceArgs'], pulumi.InputType['FtpServerLinkedServiceArgs'], pulumi.InputType['GoogleAdWordsLinkedServiceArgs'], pulumi.InputType['GoogleBigQueryLinkedServiceArgs'], pulumi.InputType['GoogleCloudStorageLinkedServiceArgs'], pulumi.InputType['GoogleSheetsLinkedServiceArgs'], pulumi.InputType['GreenplumLinkedServiceArgs'], pulumi.InputType['HBaseLinkedServiceArgs'], pulumi.InputType['HDInsightLinkedServiceArgs'], pulumi.InputType['HDInsightOnDemandLinkedServiceArgs'], pulumi.InputType['HdfsLinkedServiceArgs'], pulumi.InputType['HiveLinkedServiceArgs'], pulumi.InputType['HttpLinkedServiceArgs'], pulumi.InputType['HubspotLinkedServiceArgs'], pulumi.InputType['ImpalaLinkedServiceArgs'], pulumi.InputType['InformixLinkedServiceArgs'], pulumi.InputType['JiraLinkedServiceArgs'], pulumi.InputType['MagentoLinkedServiceArgs'], pulumi.InputType['MariaDBLinkedServiceArgs'], pulumi.InputType['MarketoLinkedServiceArgs'], pulumi.InputType['MicrosoftAccessLinkedServiceArgs'], pulumi.InputType['MongoDbAtlasLinkedServiceArgs'], pulumi.InputType['MongoDbLinkedServiceArgs'], pulumi.InputType['MongoDbV2LinkedServiceArgs'], pulumi.InputType['MySqlLinkedServiceArgs'], pulumi.InputType['NetezzaLinkedServiceArgs'], pulumi.InputType['ODataLinkedServiceArgs'], pulumi.InputType['OdbcLinkedServiceArgs'], pulumi.InputType['Office365LinkedServiceArgs'], pulumi.InputType['OracleCloudStorageLinkedServiceArgs'], pulumi.InputType['OracleLinkedServiceArgs'], pulumi.InputType['OracleServiceCloudLinkedServiceArgs'], pulumi.InputType['PaypalLinkedServiceArgs'], pulumi.InputType['PhoenixLinkedServiceArgs'], pulumi.InputType['PostgreSqlLinkedServiceArgs'], pulumi.InputType['PrestoLinkedServiceArgs'], pulumi.InputType['QuickBooksLinkedServiceArgs'], pulumi.InputType['QuickbaseLinkedServiceArgs'], pulumi.InputType['ResponsysLinkedServiceArgs'], pulumi.InputType['RestServiceLinkedServiceArgs'], pulumi.InputType['SalesforceLinkedServiceArgs'], pulumi.InputType['SalesforceMarketingCloudLinkedServiceArgs'], pulumi.InputType['SalesforceServiceCloudLinkedServiceArgs'], pulumi.InputType['SapBWLinkedServiceArgs'], pulumi.InputType['SapCloudForCustomerLinkedServiceArgs'], pulumi.InputType['SapEccLinkedServiceArgs'], pulumi.InputType['SapHanaLinkedServiceArgs'], pulumi.InputType['SapOdpLinkedServiceArgs'], pulumi.InputType['SapOpenHubLinkedServiceArgs'], pulumi.InputType['SapTableLinkedServiceArgs'], pulumi.InputType['ServiceNowLinkedServiceArgs'], pulumi.InputType['SftpServerLinkedServiceArgs'], pulumi.InputType['SharePointOnlineListLinkedServiceArgs'], pulumi.InputType['ShopifyLinkedServiceArgs'], pulumi.InputType['SmartsheetLinkedServiceArgs'], pulumi.InputType['SnowflakeLinkedServiceArgs'], pulumi.InputType['SparkLinkedServiceArgs'], pulumi.InputType['SqlServerLinkedServiceArgs'], pulumi.InputType['SquareLinkedServiceArgs'], pulumi.InputType['SybaseLinkedServiceArgs'], pulumi.InputType['TeamDeskLinkedServiceArgs'], pulumi.InputType['TeradataLinkedServiceArgs'], pulumi.InputType['TwilioLinkedServiceArgs'], pulumi.InputType['VerticaLinkedServiceArgs'], pulumi.InputType['WebLinkedServiceArgs'], pulumi.InputType['XeroLinkedServiceArgs'], pulumi.InputType['ZendeskLinkedServiceArgs'], pulumi.InputType['ZohoLinkedServiceArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LinkedServiceArgs.__new__(LinkedServiceArgs)

            if factory_name is None and not opts.urn:
                raise TypeError("Missing required property 'factory_name'")
            __props__.__dict__["factory_name"] = factory_name
            __props__.__dict__["linked_service_name"] = linked_service_name
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datafactory/v20170901preview:LinkedService"), pulumi.Alias(type_="azure-native:datafactory/v20180601:LinkedService")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LinkedService, __self__).__init__(
            'azure-native:datafactory:LinkedService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LinkedService':
        """
        Get an existing LinkedService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LinkedServiceArgs.__new__(LinkedServiceArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return LinkedService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Etag identifies change in the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        Properties of linked service.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

