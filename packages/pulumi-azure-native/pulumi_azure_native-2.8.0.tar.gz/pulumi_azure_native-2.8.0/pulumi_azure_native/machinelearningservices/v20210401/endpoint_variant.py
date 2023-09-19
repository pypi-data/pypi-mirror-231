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

__all__ = ['EndpointVariantArgs', 'EndpointVariant']

@pulumi.input_type
class EndpointVariantArgs:
    def __init__(__self__, *,
                 compute_type: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 environment_image_request: Optional[pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs']] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 keys: Optional[pulumi.Input['CreateServiceRequestKeysArgs']] = None,
                 kv_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 traffic_percentile: Optional[pulumi.Input[float]] = None,
                 type: Optional[pulumi.Input[Union[str, 'VariantType']]] = None):
        """
        The set of arguments for constructing a EndpointVariant resource.
        :param pulumi.Input[str] compute_type: The compute environment type for the service.
               Expected value is 'Custom'.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[str] description: The description of the service.
        :param pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs'] environment_image_request: The Environment, models and assets needed for inferencing.
        :param pulumi.Input[bool] is_default: Is this the default variant.
        :param pulumi.Input['CreateServiceRequestKeysArgs'] keys: The authentication keys.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] kv_tags: The service tag dictionary. Tags are mutable.
        :param pulumi.Input[str] location: The name of the Azure location/region.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The service properties dictionary. Properties are immutable.
        :param pulumi.Input[str] service_name: Name of the Azure Machine Learning service.
        :param pulumi.Input[float] traffic_percentile: The amount of traffic variant receives.
        :param pulumi.Input[Union[str, 'VariantType']] type: The type of the variant.
        """
        pulumi.set(__self__, "compute_type", 'Custom')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if environment_image_request is not None:
            pulumi.set(__self__, "environment_image_request", environment_image_request)
        if is_default is not None:
            pulumi.set(__self__, "is_default", is_default)
        if keys is not None:
            pulumi.set(__self__, "keys", keys)
        if kv_tags is not None:
            pulumi.set(__self__, "kv_tags", kv_tags)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if traffic_percentile is not None:
            pulumi.set(__self__, "traffic_percentile", traffic_percentile)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[str]:
        """
        The compute environment type for the service.
        Expected value is 'Custom'.
        """
        return pulumi.get(self, "compute_type")

    @compute_type.setter
    def compute_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "compute_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group in which workspace is located.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        Name of Azure Machine Learning workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the service.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="environmentImageRequest")
    def environment_image_request(self) -> Optional[pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs']]:
        """
        The Environment, models and assets needed for inferencing.
        """
        return pulumi.get(self, "environment_image_request")

    @environment_image_request.setter
    def environment_image_request(self, value: Optional[pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs']]):
        pulumi.set(self, "environment_image_request", value)

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[bool]]:
        """
        Is this the default variant.
        """
        return pulumi.get(self, "is_default")

    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default", value)

    @property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input['CreateServiceRequestKeysArgs']]:
        """
        The authentication keys.
        """
        return pulumi.get(self, "keys")

    @keys.setter
    def keys(self, value: Optional[pulumi.Input['CreateServiceRequestKeysArgs']]):
        pulumi.set(self, "keys", value)

    @property
    @pulumi.getter(name="kvTags")
    def kv_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The service tag dictionary. Tags are mutable.
        """
        return pulumi.get(self, "kv_tags")

    @kv_tags.setter
    def kv_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "kv_tags", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Azure location/region.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The service properties dictionary. Properties are immutable.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Azure Machine Learning service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="trafficPercentile")
    def traffic_percentile(self) -> Optional[pulumi.Input[float]]:
        """
        The amount of traffic variant receives.
        """
        return pulumi.get(self, "traffic_percentile")

    @traffic_percentile.setter
    def traffic_percentile(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "traffic_percentile", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'VariantType']]]:
        """
        The type of the variant.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'VariantType']]]):
        pulumi.set(self, "type", value)


class EndpointVariant(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_image_request: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestEnvironmentImageRequestArgs']]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 keys: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestKeysArgs']]] = None,
                 kv_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 traffic_percentile: Optional[pulumi.Input[float]] = None,
                 type: Optional[pulumi.Input[Union[str, 'VariantType']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Machine Learning service object wrapped into ARM resource envelope.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_type: The compute environment type for the service.
               Expected value is 'Custom'.
        :param pulumi.Input[str] description: The description of the service.
        :param pulumi.Input[pulumi.InputType['CreateServiceRequestEnvironmentImageRequestArgs']] environment_image_request: The Environment, models and assets needed for inferencing.
        :param pulumi.Input[bool] is_default: Is this the default variant.
        :param pulumi.Input[pulumi.InputType['CreateServiceRequestKeysArgs']] keys: The authentication keys.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] kv_tags: The service tag dictionary. Tags are mutable.
        :param pulumi.Input[str] location: The name of the Azure location/region.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The service properties dictionary. Properties are immutable.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] service_name: Name of the Azure Machine Learning service.
        :param pulumi.Input[float] traffic_percentile: The amount of traffic variant receives.
        :param pulumi.Input[Union[str, 'VariantType']] type: The type of the variant.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EndpointVariantArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Machine Learning service object wrapped into ARM resource envelope.

        :param str resource_name: The name of the resource.
        :param EndpointVariantArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EndpointVariantArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_image_request: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestEnvironmentImageRequestArgs']]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 keys: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestKeysArgs']]] = None,
                 kv_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 traffic_percentile: Optional[pulumi.Input[float]] = None,
                 type: Optional[pulumi.Input[Union[str, 'VariantType']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EndpointVariantArgs.__new__(EndpointVariantArgs)

            if compute_type is None and not opts.urn:
                raise TypeError("Missing required property 'compute_type'")
            __props__.__dict__["compute_type"] = 'Custom'
            __props__.__dict__["description"] = description
            __props__.__dict__["environment_image_request"] = environment_image_request
            __props__.__dict__["is_default"] = is_default
            __props__.__dict__["keys"] = keys
            __props__.__dict__["kv_tags"] = kv_tags
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["traffic_percentile"] = traffic_percentile
            __props__.__dict__["type"] = type
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["identity"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["sku"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["tags"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:machinelearningservices/v20200501preview:EndpointVariant"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200515preview:EndpointVariant"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200901preview:EndpointVariant"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210101:EndpointVariant")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EndpointVariant, __self__).__init__(
            'azure-native:machinelearningservices/v20210401:EndpointVariant',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EndpointVariant':
        """
        Get an existing EndpointVariant resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EndpointVariantArgs.__new__(EndpointVariantArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return EndpointVariant(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        Service properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The sku of the workspace.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Specifies the type of the resource.
        """
        return pulumi.get(self, "type")

