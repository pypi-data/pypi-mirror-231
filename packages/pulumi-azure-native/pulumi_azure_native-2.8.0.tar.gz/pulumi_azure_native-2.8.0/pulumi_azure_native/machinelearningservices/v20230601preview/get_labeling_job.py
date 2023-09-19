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

__all__ = [
    'GetLabelingJobResult',
    'AwaitableGetLabelingJobResult',
    'get_labeling_job',
    'get_labeling_job_output',
]

@pulumi.output_type
class GetLabelingJobResult:
    """
    Azure Resource Manager resource envelope.
    """
    def __init__(__self__, id=None, labeling_job_properties=None, name=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labeling_job_properties and not isinstance(labeling_job_properties, dict):
            raise TypeError("Expected argument 'labeling_job_properties' to be a dict")
        pulumi.set(__self__, "labeling_job_properties", labeling_job_properties)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="labelingJobProperties")
    def labeling_job_properties(self) -> 'outputs.LabelingJobResponse':
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "labeling_job_properties")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetLabelingJobResult(GetLabelingJobResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLabelingJobResult(
            id=self.id,
            labeling_job_properties=self.labeling_job_properties,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_labeling_job(id: Optional[str] = None,
                     include_job_instructions: Optional[bool] = None,
                     include_label_categories: Optional[bool] = None,
                     resource_group_name: Optional[str] = None,
                     workspace_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLabelingJobResult:
    """
    Azure Resource Manager resource envelope.


    :param str id: The name and identifier for the LabelingJob.
    :param bool include_job_instructions: Boolean value to indicate whether to include JobInstructions in response.
    :param bool include_label_categories: Boolean value to indicate Whether to include LabelCategories in response.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['includeJobInstructions'] = include_job_instructions
    __args__['includeLabelCategories'] = include_label_categories
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20230601preview:getLabelingJob', __args__, opts=opts, typ=GetLabelingJobResult).value

    return AwaitableGetLabelingJobResult(
        id=pulumi.get(__ret__, 'id'),
        labeling_job_properties=pulumi.get(__ret__, 'labeling_job_properties'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_labeling_job)
def get_labeling_job_output(id: Optional[pulumi.Input[str]] = None,
                            include_job_instructions: Optional[pulumi.Input[Optional[bool]]] = None,
                            include_label_categories: Optional[pulumi.Input[Optional[bool]]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            workspace_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLabelingJobResult]:
    """
    Azure Resource Manager resource envelope.


    :param str id: The name and identifier for the LabelingJob.
    :param bool include_job_instructions: Boolean value to indicate whether to include JobInstructions in response.
    :param bool include_label_categories: Boolean value to indicate Whether to include LabelCategories in response.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
