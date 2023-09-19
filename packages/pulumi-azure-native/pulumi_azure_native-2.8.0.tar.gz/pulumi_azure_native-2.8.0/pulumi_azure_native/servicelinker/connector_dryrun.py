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

__all__ = ['ConnectorDryrunArgs', 'ConnectorDryrun']

@pulumi.input_type
class ConnectorDryrunArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 dryrun_name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input['CreateOrUpdateDryrunParametersArgs']] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConnectorDryrun resource.
        :param pulumi.Input[str] location: The name of Azure region.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] dryrun_name: The name of dryrun.
        :param pulumi.Input['CreateOrUpdateDryrunParametersArgs'] parameters: The parameters of the dryrun
        :param pulumi.Input[str] subscription_id: The ID of the target subscription.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if dryrun_name is not None:
            pulumi.set(__self__, "dryrun_name", dryrun_name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The name of Azure region.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

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
    @pulumi.getter(name="dryrunName")
    def dryrun_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of dryrun.
        """
        return pulumi.get(self, "dryrun_name")

    @dryrun_name.setter
    def dryrun_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dryrun_name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input['CreateOrUpdateDryrunParametersArgs']]:
        """
        The parameters of the dryrun
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input['CreateOrUpdateDryrunParametersArgs']]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the target subscription.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)


class ConnectorDryrun(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dryrun_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['CreateOrUpdateDryrunParametersArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        a dryrun job resource
        Azure REST API version: 2022-11-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dryrun_name: The name of dryrun.
        :param pulumi.Input[str] location: The name of Azure region.
        :param pulumi.Input[pulumi.InputType['CreateOrUpdateDryrunParametersArgs']] parameters: The parameters of the dryrun
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] subscription_id: The ID of the target subscription.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectorDryrunArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        a dryrun job resource
        Azure REST API version: 2022-11-01-preview.

        :param str resource_name: The name of the resource.
        :param ConnectorDryrunArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectorDryrunArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dryrun_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['CreateOrUpdateDryrunParametersArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectorDryrunArgs.__new__(ConnectorDryrunArgs)

            __props__.__dict__["dryrun_name"] = dryrun_name
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["parameters"] = parameters
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["name"] = None
            __props__.__dict__["operation_previews"] = None
            __props__.__dict__["prerequisite_results"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicelinker/v20221101preview:ConnectorDryrun")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConnectorDryrun, __self__).__init__(
            'azure-native:servicelinker:ConnectorDryrun',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectorDryrun':
        """
        Get an existing ConnectorDryrun resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectorDryrunArgs.__new__(ConnectorDryrunArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["operation_previews"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["prerequisite_results"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ConnectorDryrun(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationPreviews")
    def operation_previews(self) -> pulumi.Output[Sequence['outputs.DryrunOperationPreviewResponse']]:
        """
        the preview of the operations for creation
        """
        return pulumi.get(self, "operation_previews")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional['outputs.CreateOrUpdateDryrunParametersResponse']]:
        """
        The parameters of the dryrun
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="prerequisiteResults")
    def prerequisite_results(self) -> pulumi.Output[Sequence[Any]]:
        """
        the result of the dryrun
        """
        return pulumi.get(self, "prerequisite_results")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state. 
        """
        return pulumi.get(self, "provisioning_state")

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

