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
    'GetPipelineRunResult',
    'AwaitableGetPipelineRunResult',
    'get_pipeline_run',
    'get_pipeline_run_output',
]

@pulumi.output_type
class GetPipelineRunResult:
    """
    An object that represents a pipeline run for a container registry.
    """
    def __init__(__self__, force_update_tag=None, id=None, name=None, provisioning_state=None, request=None, response=None, system_data=None, type=None):
        if force_update_tag and not isinstance(force_update_tag, str):
            raise TypeError("Expected argument 'force_update_tag' to be a str")
        pulumi.set(__self__, "force_update_tag", force_update_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if request and not isinstance(request, dict):
            raise TypeError("Expected argument 'request' to be a dict")
        pulumi.set(__self__, "request", request)
        if response and not isinstance(response, dict):
            raise TypeError("Expected argument 'response' to be a dict")
        pulumi.set(__self__, "response", response)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[str]:
        """
        How the pipeline run should be forced to recreate even if the pipeline run configuration has not changed.
        """
        return pulumi.get(self, "force_update_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of a pipeline run.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def request(self) -> Optional['outputs.PipelineRunRequestResponse']:
        """
        The request parameters for a pipeline run.
        """
        return pulumi.get(self, "request")

    @property
    @pulumi.getter
    def response(self) -> 'outputs.PipelineRunResponseResponse':
        """
        The response of a pipeline run.
        """
        return pulumi.get(self, "response")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetPipelineRunResult(GetPipelineRunResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPipelineRunResult(
            force_update_tag=self.force_update_tag,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            request=self.request,
            response=self.response,
            system_data=self.system_data,
            type=self.type)


def get_pipeline_run(pipeline_run_name: Optional[str] = None,
                     registry_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPipelineRunResult:
    """
    Gets the detailed information for a given pipeline run.


    :param str pipeline_run_name: The name of the pipeline run.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['pipelineRunName'] = pipeline_run_name
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20230601preview:getPipelineRun', __args__, opts=opts, typ=GetPipelineRunResult).value

    return AwaitableGetPipelineRunResult(
        force_update_tag=pulumi.get(__ret__, 'force_update_tag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        request=pulumi.get(__ret__, 'request'),
        response=pulumi.get(__ret__, 'response'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_pipeline_run)
def get_pipeline_run_output(pipeline_run_name: Optional[pulumi.Input[str]] = None,
                            registry_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPipelineRunResult]:
    """
    Gets the detailed information for a given pipeline run.


    :param str pipeline_run_name: The name of the pipeline run.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
