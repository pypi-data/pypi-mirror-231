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

__all__ = [
    'GetServerEndpointResult',
    'AwaitableGetServerEndpointResult',
    'get_server_endpoint',
    'get_server_endpoint_output',
]

@pulumi.output_type
class GetServerEndpointResult:
    """
    Server Endpoint object.
    """
    def __init__(__self__, cloud_tiering=None, cloud_tiering_status=None, friendly_name=None, id=None, initial_download_policy=None, initial_upload_policy=None, last_operation_name=None, last_workflow_id=None, local_cache_mode=None, name=None, offline_data_transfer=None, offline_data_transfer_share_name=None, offline_data_transfer_storage_account_resource_id=None, offline_data_transfer_storage_account_tenant_id=None, provisioning_state=None, recall_status=None, server_local_path=None, server_name=None, server_resource_id=None, sync_status=None, system_data=None, tier_files_older_than_days=None, type=None, volume_free_space_percent=None):
        if cloud_tiering and not isinstance(cloud_tiering, str):
            raise TypeError("Expected argument 'cloud_tiering' to be a str")
        pulumi.set(__self__, "cloud_tiering", cloud_tiering)
        if cloud_tiering_status and not isinstance(cloud_tiering_status, dict):
            raise TypeError("Expected argument 'cloud_tiering_status' to be a dict")
        pulumi.set(__self__, "cloud_tiering_status", cloud_tiering_status)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if initial_download_policy and not isinstance(initial_download_policy, str):
            raise TypeError("Expected argument 'initial_download_policy' to be a str")
        pulumi.set(__self__, "initial_download_policy", initial_download_policy)
        if initial_upload_policy and not isinstance(initial_upload_policy, str):
            raise TypeError("Expected argument 'initial_upload_policy' to be a str")
        pulumi.set(__self__, "initial_upload_policy", initial_upload_policy)
        if last_operation_name and not isinstance(last_operation_name, str):
            raise TypeError("Expected argument 'last_operation_name' to be a str")
        pulumi.set(__self__, "last_operation_name", last_operation_name)
        if last_workflow_id and not isinstance(last_workflow_id, str):
            raise TypeError("Expected argument 'last_workflow_id' to be a str")
        pulumi.set(__self__, "last_workflow_id", last_workflow_id)
        if local_cache_mode and not isinstance(local_cache_mode, str):
            raise TypeError("Expected argument 'local_cache_mode' to be a str")
        pulumi.set(__self__, "local_cache_mode", local_cache_mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if offline_data_transfer and not isinstance(offline_data_transfer, str):
            raise TypeError("Expected argument 'offline_data_transfer' to be a str")
        pulumi.set(__self__, "offline_data_transfer", offline_data_transfer)
        if offline_data_transfer_share_name and not isinstance(offline_data_transfer_share_name, str):
            raise TypeError("Expected argument 'offline_data_transfer_share_name' to be a str")
        pulumi.set(__self__, "offline_data_transfer_share_name", offline_data_transfer_share_name)
        if offline_data_transfer_storage_account_resource_id and not isinstance(offline_data_transfer_storage_account_resource_id, str):
            raise TypeError("Expected argument 'offline_data_transfer_storage_account_resource_id' to be a str")
        pulumi.set(__self__, "offline_data_transfer_storage_account_resource_id", offline_data_transfer_storage_account_resource_id)
        if offline_data_transfer_storage_account_tenant_id and not isinstance(offline_data_transfer_storage_account_tenant_id, str):
            raise TypeError("Expected argument 'offline_data_transfer_storage_account_tenant_id' to be a str")
        pulumi.set(__self__, "offline_data_transfer_storage_account_tenant_id", offline_data_transfer_storage_account_tenant_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if recall_status and not isinstance(recall_status, dict):
            raise TypeError("Expected argument 'recall_status' to be a dict")
        pulumi.set(__self__, "recall_status", recall_status)
        if server_local_path and not isinstance(server_local_path, str):
            raise TypeError("Expected argument 'server_local_path' to be a str")
        pulumi.set(__self__, "server_local_path", server_local_path)
        if server_name and not isinstance(server_name, str):
            raise TypeError("Expected argument 'server_name' to be a str")
        pulumi.set(__self__, "server_name", server_name)
        if server_resource_id and not isinstance(server_resource_id, str):
            raise TypeError("Expected argument 'server_resource_id' to be a str")
        pulumi.set(__self__, "server_resource_id", server_resource_id)
        if sync_status and not isinstance(sync_status, dict):
            raise TypeError("Expected argument 'sync_status' to be a dict")
        pulumi.set(__self__, "sync_status", sync_status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tier_files_older_than_days and not isinstance(tier_files_older_than_days, int):
            raise TypeError("Expected argument 'tier_files_older_than_days' to be a int")
        pulumi.set(__self__, "tier_files_older_than_days", tier_files_older_than_days)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volume_free_space_percent and not isinstance(volume_free_space_percent, int):
            raise TypeError("Expected argument 'volume_free_space_percent' to be a int")
        pulumi.set(__self__, "volume_free_space_percent", volume_free_space_percent)

    @property
    @pulumi.getter(name="cloudTiering")
    def cloud_tiering(self) -> Optional[str]:
        """
        Cloud Tiering.
        """
        return pulumi.get(self, "cloud_tiering")

    @property
    @pulumi.getter(name="cloudTieringStatus")
    def cloud_tiering_status(self) -> 'outputs.ServerEndpointCloudTieringStatusResponse':
        """
        Cloud tiering status. Only populated if cloud tiering is enabled.
        """
        return pulumi.get(self, "cloud_tiering_status")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        Friendly Name
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="initialDownloadPolicy")
    def initial_download_policy(self) -> Optional[str]:
        """
        Policy for how namespace and files are recalled during FastDr.
        """
        return pulumi.get(self, "initial_download_policy")

    @property
    @pulumi.getter(name="initialUploadPolicy")
    def initial_upload_policy(self) -> Optional[str]:
        """
        Policy for how the initial upload sync session is performed.
        """
        return pulumi.get(self, "initial_upload_policy")

    @property
    @pulumi.getter(name="lastOperationName")
    def last_operation_name(self) -> str:
        """
        Resource Last Operation Name
        """
        return pulumi.get(self, "last_operation_name")

    @property
    @pulumi.getter(name="lastWorkflowId")
    def last_workflow_id(self) -> str:
        """
        ServerEndpoint lastWorkflowId
        """
        return pulumi.get(self, "last_workflow_id")

    @property
    @pulumi.getter(name="localCacheMode")
    def local_cache_mode(self) -> Optional[str]:
        """
        Policy for enabling follow-the-sun business models: link local cache to cloud behavior to pre-populate before local access.
        """
        return pulumi.get(self, "local_cache_mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="offlineDataTransfer")
    def offline_data_transfer(self) -> Optional[str]:
        """
        Offline data transfer
        """
        return pulumi.get(self, "offline_data_transfer")

    @property
    @pulumi.getter(name="offlineDataTransferShareName")
    def offline_data_transfer_share_name(self) -> Optional[str]:
        """
        Offline data transfer share name
        """
        return pulumi.get(self, "offline_data_transfer_share_name")

    @property
    @pulumi.getter(name="offlineDataTransferStorageAccountResourceId")
    def offline_data_transfer_storage_account_resource_id(self) -> str:
        """
        Offline data transfer storage account resource ID
        """
        return pulumi.get(self, "offline_data_transfer_storage_account_resource_id")

    @property
    @pulumi.getter(name="offlineDataTransferStorageAccountTenantId")
    def offline_data_transfer_storage_account_tenant_id(self) -> str:
        """
        Offline data transfer storage account tenant ID
        """
        return pulumi.get(self, "offline_data_transfer_storage_account_tenant_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        ServerEndpoint Provisioning State
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="recallStatus")
    def recall_status(self) -> 'outputs.ServerEndpointRecallStatusResponse':
        """
        Recall status. Only populated if cloud tiering is enabled.
        """
        return pulumi.get(self, "recall_status")

    @property
    @pulumi.getter(name="serverLocalPath")
    def server_local_path(self) -> Optional[str]:
        """
        Server Local path.
        """
        return pulumi.get(self, "server_local_path")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> str:
        """
        Server name
        """
        return pulumi.get(self, "server_name")

    @property
    @pulumi.getter(name="serverResourceId")
    def server_resource_id(self) -> Optional[str]:
        """
        Server Resource Id.
        """
        return pulumi.get(self, "server_resource_id")

    @property
    @pulumi.getter(name="syncStatus")
    def sync_status(self) -> 'outputs.ServerEndpointSyncStatusResponse':
        """
        Server Endpoint sync status
        """
        return pulumi.get(self, "sync_status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tierFilesOlderThanDays")
    def tier_files_older_than_days(self) -> Optional[int]:
        """
        Tier files older than days.
        """
        return pulumi.get(self, "tier_files_older_than_days")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeFreeSpacePercent")
    def volume_free_space_percent(self) -> Optional[int]:
        """
        Level of free space to be maintained by Cloud Tiering if it is enabled.
        """
        return pulumi.get(self, "volume_free_space_percent")


class AwaitableGetServerEndpointResult(GetServerEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerEndpointResult(
            cloud_tiering=self.cloud_tiering,
            cloud_tiering_status=self.cloud_tiering_status,
            friendly_name=self.friendly_name,
            id=self.id,
            initial_download_policy=self.initial_download_policy,
            initial_upload_policy=self.initial_upload_policy,
            last_operation_name=self.last_operation_name,
            last_workflow_id=self.last_workflow_id,
            local_cache_mode=self.local_cache_mode,
            name=self.name,
            offline_data_transfer=self.offline_data_transfer,
            offline_data_transfer_share_name=self.offline_data_transfer_share_name,
            offline_data_transfer_storage_account_resource_id=self.offline_data_transfer_storage_account_resource_id,
            offline_data_transfer_storage_account_tenant_id=self.offline_data_transfer_storage_account_tenant_id,
            provisioning_state=self.provisioning_state,
            recall_status=self.recall_status,
            server_local_path=self.server_local_path,
            server_name=self.server_name,
            server_resource_id=self.server_resource_id,
            sync_status=self.sync_status,
            system_data=self.system_data,
            tier_files_older_than_days=self.tier_files_older_than_days,
            type=self.type,
            volume_free_space_percent=self.volume_free_space_percent)


def get_server_endpoint(resource_group_name: Optional[str] = None,
                        server_endpoint_name: Optional[str] = None,
                        storage_sync_service_name: Optional[str] = None,
                        sync_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerEndpointResult:
    """
    Get a ServerEndpoint.
    Azure REST API version: 2022-06-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_endpoint_name: Name of Server Endpoint object.
    :param str storage_sync_service_name: Name of Storage Sync Service resource.
    :param str sync_group_name: Name of Sync Group resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverEndpointName'] = server_endpoint_name
    __args__['storageSyncServiceName'] = storage_sync_service_name
    __args__['syncGroupName'] = sync_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storagesync:getServerEndpoint', __args__, opts=opts, typ=GetServerEndpointResult).value

    return AwaitableGetServerEndpointResult(
        cloud_tiering=pulumi.get(__ret__, 'cloud_tiering'),
        cloud_tiering_status=pulumi.get(__ret__, 'cloud_tiering_status'),
        friendly_name=pulumi.get(__ret__, 'friendly_name'),
        id=pulumi.get(__ret__, 'id'),
        initial_download_policy=pulumi.get(__ret__, 'initial_download_policy'),
        initial_upload_policy=pulumi.get(__ret__, 'initial_upload_policy'),
        last_operation_name=pulumi.get(__ret__, 'last_operation_name'),
        last_workflow_id=pulumi.get(__ret__, 'last_workflow_id'),
        local_cache_mode=pulumi.get(__ret__, 'local_cache_mode'),
        name=pulumi.get(__ret__, 'name'),
        offline_data_transfer=pulumi.get(__ret__, 'offline_data_transfer'),
        offline_data_transfer_share_name=pulumi.get(__ret__, 'offline_data_transfer_share_name'),
        offline_data_transfer_storage_account_resource_id=pulumi.get(__ret__, 'offline_data_transfer_storage_account_resource_id'),
        offline_data_transfer_storage_account_tenant_id=pulumi.get(__ret__, 'offline_data_transfer_storage_account_tenant_id'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        recall_status=pulumi.get(__ret__, 'recall_status'),
        server_local_path=pulumi.get(__ret__, 'server_local_path'),
        server_name=pulumi.get(__ret__, 'server_name'),
        server_resource_id=pulumi.get(__ret__, 'server_resource_id'),
        sync_status=pulumi.get(__ret__, 'sync_status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tier_files_older_than_days=pulumi.get(__ret__, 'tier_files_older_than_days'),
        type=pulumi.get(__ret__, 'type'),
        volume_free_space_percent=pulumi.get(__ret__, 'volume_free_space_percent'))


@_utilities.lift_output_func(get_server_endpoint)
def get_server_endpoint_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                               server_endpoint_name: Optional[pulumi.Input[str]] = None,
                               storage_sync_service_name: Optional[pulumi.Input[str]] = None,
                               sync_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerEndpointResult]:
    """
    Get a ServerEndpoint.
    Azure REST API version: 2022-06-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_endpoint_name: Name of Server Endpoint object.
    :param str storage_sync_service_name: Name of Storage Sync Service resource.
    :param str sync_group_name: Name of Sync Group resource.
    """
    ...
