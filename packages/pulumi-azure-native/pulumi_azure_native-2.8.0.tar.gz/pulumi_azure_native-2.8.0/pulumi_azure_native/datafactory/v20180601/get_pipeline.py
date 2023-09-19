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
    'GetPipelineResult',
    'AwaitableGetPipelineResult',
    'get_pipeline',
    'get_pipeline_output',
]

@pulumi.output_type
class GetPipelineResult:
    """
    Pipeline resource type.
    """
    def __init__(__self__, activities=None, annotations=None, concurrency=None, description=None, etag=None, folder=None, id=None, name=None, parameters=None, policy=None, run_dimensions=None, type=None, variables=None):
        if activities and not isinstance(activities, list):
            raise TypeError("Expected argument 'activities' to be a list")
        pulumi.set(__self__, "activities", activities)
        if annotations and not isinstance(annotations, list):
            raise TypeError("Expected argument 'annotations' to be a list")
        pulumi.set(__self__, "annotations", annotations)
        if concurrency and not isinstance(concurrency, int):
            raise TypeError("Expected argument 'concurrency' to be a int")
        pulumi.set(__self__, "concurrency", concurrency)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if folder and not isinstance(folder, dict):
            raise TypeError("Expected argument 'folder' to be a dict")
        pulumi.set(__self__, "folder", folder)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if policy and not isinstance(policy, dict):
            raise TypeError("Expected argument 'policy' to be a dict")
        pulumi.set(__self__, "policy", policy)
        if run_dimensions and not isinstance(run_dimensions, dict):
            raise TypeError("Expected argument 'run_dimensions' to be a dict")
        pulumi.set(__self__, "run_dimensions", run_dimensions)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if variables and not isinstance(variables, dict):
            raise TypeError("Expected argument 'variables' to be a dict")
        pulumi.set(__self__, "variables", variables)

    @property
    @pulumi.getter
    def activities(self) -> Optional[Sequence[Any]]:
        """
        List of activities in pipeline.
        """
        return pulumi.get(self, "activities")

    @property
    @pulumi.getter
    def annotations(self) -> Optional[Sequence[Any]]:
        """
        List of tags that can be used for describing the Pipeline.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def concurrency(self) -> Optional[int]:
        """
        The max number of concurrent runs for the pipeline.
        """
        return pulumi.get(self, "concurrency")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the pipeline.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Etag identifies change in the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def folder(self) -> Optional['outputs.PipelineResponseFolder']:
        """
        The folder that this Pipeline is in. If not specified, Pipeline will appear at the root level.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, 'outputs.ParameterSpecificationResponse']]:
        """
        List of parameters for pipeline.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def policy(self) -> Optional['outputs.PipelinePolicyResponse']:
        """
        Pipeline Policy.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="runDimensions")
    def run_dimensions(self) -> Optional[Mapping[str, Any]]:
        """
        Dimensions emitted by Pipeline.
        """
        return pulumi.get(self, "run_dimensions")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def variables(self) -> Optional[Mapping[str, 'outputs.VariableSpecificationResponse']]:
        """
        List of variables for pipeline.
        """
        return pulumi.get(self, "variables")


class AwaitableGetPipelineResult(GetPipelineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPipelineResult(
            activities=self.activities,
            annotations=self.annotations,
            concurrency=self.concurrency,
            description=self.description,
            etag=self.etag,
            folder=self.folder,
            id=self.id,
            name=self.name,
            parameters=self.parameters,
            policy=self.policy,
            run_dimensions=self.run_dimensions,
            type=self.type,
            variables=self.variables)


def get_pipeline(factory_name: Optional[str] = None,
                 pipeline_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPipelineResult:
    """
    Gets a pipeline.


    :param str factory_name: The factory name.
    :param str pipeline_name: The pipeline name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['factoryName'] = factory_name
    __args__['pipelineName'] = pipeline_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datafactory/v20180601:getPipeline', __args__, opts=opts, typ=GetPipelineResult).value

    return AwaitableGetPipelineResult(
        activities=pulumi.get(__ret__, 'activities'),
        annotations=pulumi.get(__ret__, 'annotations'),
        concurrency=pulumi.get(__ret__, 'concurrency'),
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        folder=pulumi.get(__ret__, 'folder'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        parameters=pulumi.get(__ret__, 'parameters'),
        policy=pulumi.get(__ret__, 'policy'),
        run_dimensions=pulumi.get(__ret__, 'run_dimensions'),
        type=pulumi.get(__ret__, 'type'),
        variables=pulumi.get(__ret__, 'variables'))


@_utilities.lift_output_func(get_pipeline)
def get_pipeline_output(factory_name: Optional[pulumi.Input[str]] = None,
                        pipeline_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPipelineResult]:
    """
    Gets a pipeline.


    :param str factory_name: The factory name.
    :param str pipeline_name: The pipeline name.
    :param str resource_group_name: The resource group name.
    """
    ...
