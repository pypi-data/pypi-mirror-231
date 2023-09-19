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

__all__ = [
    'GetSAPDiskConfigurationsResult',
    'AwaitableGetSAPDiskConfigurationsResult',
    'get_sap_disk_configurations',
    'get_sap_disk_configurations_output',
]

@pulumi.output_type
class GetSAPDiskConfigurationsResult:
    """
    The list of disk configuration for vmSku which are part of SAP deployment.
    """
    def __init__(__self__, volume_configurations=None):
        if volume_configurations and not isinstance(volume_configurations, dict):
            raise TypeError("Expected argument 'volume_configurations' to be a dict")
        pulumi.set(__self__, "volume_configurations", volume_configurations)

    @property
    @pulumi.getter(name="volumeConfigurations")
    def volume_configurations(self) -> Optional[Mapping[str, 'outputs.SAPDiskConfigurationResponse']]:
        """
        The disk configuration for the db volume. For HANA, Required volumes are: ['hana/data', 'hana/log', hana/shared', 'usr/sap', 'os'], Optional volume : ['backup'].
        """
        return pulumi.get(self, "volume_configurations")


class AwaitableGetSAPDiskConfigurationsResult(GetSAPDiskConfigurationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSAPDiskConfigurationsResult(
            volume_configurations=self.volume_configurations)


def get_sap_disk_configurations(app_location: Optional[str] = None,
                                database_type: Optional[Union[str, 'SAPDatabaseType']] = None,
                                db_vm_sku: Optional[str] = None,
                                deployment_type: Optional[Union[str, 'SAPDeploymentType']] = None,
                                environment: Optional[Union[str, 'SAPEnvironmentType']] = None,
                                location: Optional[str] = None,
                                sap_product: Optional[Union[str, 'SAPProductType']] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSAPDiskConfigurationsResult:
    """
    Get the SAP Disk Configuration Layout prod/non-prod SAP System.


    :param str app_location: The geo-location where the SAP resources will be created.
    :param Union[str, 'SAPDatabaseType'] database_type: The database type. Eg: HANA, DB2, etc
    :param str db_vm_sku: The VM SKU for database instance.
    :param Union[str, 'SAPDeploymentType'] deployment_type: The deployment type. Eg: SingleServer/ThreeTier
    :param Union[str, 'SAPEnvironmentType'] environment: Defines the environment type - Production/Non Production.
    :param str location: The name of Azure region.
    :param Union[str, 'SAPProductType'] sap_product: Defines the SAP Product type.
    """
    __args__ = dict()
    __args__['appLocation'] = app_location
    __args__['databaseType'] = database_type
    __args__['dbVmSku'] = db_vm_sku
    __args__['deploymentType'] = deployment_type
    __args__['environment'] = environment
    __args__['location'] = location
    __args__['sapProduct'] = sap_product
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:workloads/v20230401:getSAPDiskConfigurations', __args__, opts=opts, typ=GetSAPDiskConfigurationsResult).value

    return AwaitableGetSAPDiskConfigurationsResult(
        volume_configurations=pulumi.get(__ret__, 'volume_configurations'))


@_utilities.lift_output_func(get_sap_disk_configurations)
def get_sap_disk_configurations_output(app_location: Optional[pulumi.Input[str]] = None,
                                       database_type: Optional[pulumi.Input[Union[str, 'SAPDatabaseType']]] = None,
                                       db_vm_sku: Optional[pulumi.Input[str]] = None,
                                       deployment_type: Optional[pulumi.Input[Union[str, 'SAPDeploymentType']]] = None,
                                       environment: Optional[pulumi.Input[Union[str, 'SAPEnvironmentType']]] = None,
                                       location: Optional[pulumi.Input[str]] = None,
                                       sap_product: Optional[pulumi.Input[Union[str, 'SAPProductType']]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSAPDiskConfigurationsResult]:
    """
    Get the SAP Disk Configuration Layout prod/non-prod SAP System.


    :param str app_location: The geo-location where the SAP resources will be created.
    :param Union[str, 'SAPDatabaseType'] database_type: The database type. Eg: HANA, DB2, etc
    :param str db_vm_sku: The VM SKU for database instance.
    :param Union[str, 'SAPDeploymentType'] deployment_type: The deployment type. Eg: SingleServer/ThreeTier
    :param Union[str, 'SAPEnvironmentType'] environment: Defines the environment type - Production/Non Production.
    :param str location: The name of Azure region.
    :param Union[str, 'SAPProductType'] sap_product: Defines the SAP Product type.
    """
    ...
