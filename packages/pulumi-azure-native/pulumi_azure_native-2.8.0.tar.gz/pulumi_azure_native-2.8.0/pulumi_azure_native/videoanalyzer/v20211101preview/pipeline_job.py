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

__all__ = ['PipelineJobArgs', 'PipelineJob']

@pulumi.input_type
class PipelineJobArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 topology_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['ParameterDefinitionArgs']]]] = None,
                 pipeline_job_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PipelineJob resource.
        :param pulumi.Input[str] account_name: The Azure Video Analyzer account name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] topology_name: Reference to an existing pipeline topology. When activated, this pipeline job will process content according to the pipeline topology definition.
        :param pulumi.Input[str] description: An optional description for the pipeline.
        :param pulumi.Input[Sequence[pulumi.Input['ParameterDefinitionArgs']]] parameters: List of the instance level parameter values for the user-defined topology parameters. A pipeline can only define or override parameters values for parameters which have been declared in the referenced topology. Topology parameters without a default value must be defined. Topology parameters with a default value can be optionally be overridden.
        :param pulumi.Input[str] pipeline_job_name: The pipeline job name.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "topology_name", topology_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if pipeline_job_name is not None:
            pulumi.set(__self__, "pipeline_job_name", pipeline_job_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The Azure Video Analyzer account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

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
    @pulumi.getter(name="topologyName")
    def topology_name(self) -> pulumi.Input[str]:
        """
        Reference to an existing pipeline topology. When activated, this pipeline job will process content according to the pipeline topology definition.
        """
        return pulumi.get(self, "topology_name")

    @topology_name.setter
    def topology_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "topology_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description for the pipeline.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ParameterDefinitionArgs']]]]:
        """
        List of the instance level parameter values for the user-defined topology parameters. A pipeline can only define or override parameters values for parameters which have been declared in the referenced topology. Topology parameters without a default value must be defined. Topology parameters with a default value can be optionally be overridden.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ParameterDefinitionArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="pipelineJobName")
    def pipeline_job_name(self) -> Optional[pulumi.Input[str]]:
        """
        The pipeline job name.
        """
        return pulumi.get(self, "pipeline_job_name")

    @pipeline_job_name.setter
    def pipeline_job_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_job_name", value)


class PipelineJob(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterDefinitionArgs']]]]] = None,
                 pipeline_job_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 topology_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Pipeline job represents a unique instance of a batch topology, used for offline processing of selected portions of archived content.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The Azure Video Analyzer account name.
        :param pulumi.Input[str] description: An optional description for the pipeline.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterDefinitionArgs']]]] parameters: List of the instance level parameter values for the user-defined topology parameters. A pipeline can only define or override parameters values for parameters which have been declared in the referenced topology. Topology parameters without a default value must be defined. Topology parameters with a default value can be optionally be overridden.
        :param pulumi.Input[str] pipeline_job_name: The pipeline job name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] topology_name: Reference to an existing pipeline topology. When activated, this pipeline job will process content according to the pipeline topology definition.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineJobArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Pipeline job represents a unique instance of a batch topology, used for offline processing of selected portions of archived content.

        :param str resource_name: The name of the resource.
        :param PipelineJobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineJobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterDefinitionArgs']]]]] = None,
                 pipeline_job_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 topology_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PipelineJobArgs.__new__(PipelineJobArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["description"] = description
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["pipeline_job_name"] = pipeline_job_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if topology_name is None and not opts.urn:
                raise TypeError("Missing required property 'topology_name'")
            __props__.__dict__["topology_name"] = topology_name
            __props__.__dict__["error"] = None
            __props__.__dict__["expiration"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:videoanalyzer:PipelineJob")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PipelineJob, __self__).__init__(
            'azure-native:videoanalyzer/v20211101preview:PipelineJob',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PipelineJob':
        """
        Get an existing PipelineJob resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PipelineJobArgs.__new__(PipelineJobArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["error"] = None
        __props__.__dict__["expiration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["topology_name"] = None
        __props__.__dict__["type"] = None
        return PipelineJob(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description for the pipeline.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output['outputs.PipelineJobErrorResponse']:
        """
        Details about the error, in case the pipeline job fails.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def expiration(self) -> pulumi.Output[str]:
        """
        The date-time by when this pipeline job will be automatically deleted from your account.
        """
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence['outputs.ParameterDefinitionResponse']]]:
        """
        List of the instance level parameter values for the user-defined topology parameters. A pipeline can only define or override parameters values for parameters which have been declared in the referenced topology. Topology parameters without a default value must be defined. Topology parameters with a default value can be optionally be overridden.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Current state of the pipeline (read-only).
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="topologyName")
    def topology_name(self) -> pulumi.Output[str]:
        """
        Reference to an existing pipeline topology. When activated, this pipeline job will process content according to the pipeline topology definition.
        """
        return pulumi.get(self, "topology_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

