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

__all__ = ['MetricsConfigurationArgs', 'MetricsConfiguration']

@pulumi.input_type
class MetricsConfigurationArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 collection_interval: pulumi.Input[float],
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 resource_group_name: pulumi.Input[str],
                 enabled_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metrics_configuration_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MetricsConfiguration resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[float] collection_interval: The interval in minutes by which metrics will be collected.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_metrics: The list of metric names that have been chosen to be enabled in addition to the core set of enabled metrics.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] metrics_configuration_name: The name of the metrics configuration for the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "collection_interval", collection_interval)
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if enabled_metrics is not None:
            pulumi.set(__self__, "enabled_metrics", enabled_metrics)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metrics_configuration_name is not None:
            pulumi.set(__self__, "metrics_configuration_name", metrics_configuration_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="collectionInterval")
    def collection_interval(self) -> pulumi.Input[float]:
        """
        The interval in minutes by which metrics will be collected.
        """
        return pulumi.get(self, "collection_interval")

    @collection_interval.setter
    def collection_interval(self, value: pulumi.Input[float]):
        pulumi.set(self, "collection_interval", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

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
    @pulumi.getter(name="enabledMetrics")
    def enabled_metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of metric names that have been chosen to be enabled in addition to the core set of enabled metrics.
        """
        return pulumi.get(self, "enabled_metrics")

    @enabled_metrics.setter
    def enabled_metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enabled_metrics", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="metricsConfigurationName")
    def metrics_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the metrics configuration for the cluster.
        """
        return pulumi.get(self, "metrics_configuration_name")

    @metrics_configuration_name.setter
    def metrics_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metrics_configuration_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class MetricsConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 collection_interval: Optional[pulumi.Input[float]] = None,
                 enabled_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metrics_configuration_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a MetricsConfiguration resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[float] collection_interval: The interval in minutes by which metrics will be collected.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] enabled_metrics: The list of metric names that have been chosen to be enabled in addition to the core set of enabled metrics.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] metrics_configuration_name: The name of the metrics configuration for the cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetricsConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a MetricsConfiguration resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MetricsConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetricsConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 collection_interval: Optional[pulumi.Input[float]] = None,
                 enabled_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metrics_configuration_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MetricsConfigurationArgs.__new__(MetricsConfigurationArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if collection_interval is None and not opts.urn:
                raise TypeError("Missing required property 'collection_interval'")
            __props__.__dict__["collection_interval"] = collection_interval
            __props__.__dict__["enabled_metrics"] = enabled_metrics
            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            __props__.__dict__["metrics_configuration_name"] = metrics_configuration_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["detailed_status"] = None
            __props__.__dict__["detailed_status_message"] = None
            __props__.__dict__["disabled_metrics"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkcloud:MetricsConfiguration"), pulumi.Alias(type_="azure-native:networkcloud/v20221212preview:MetricsConfiguration"), pulumi.Alias(type_="azure-native:networkcloud/v20230701:MetricsConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MetricsConfiguration, __self__).__init__(
            'azure-native:networkcloud/v20230501preview:MetricsConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MetricsConfiguration':
        """
        Get an existing MetricsConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MetricsConfigurationArgs.__new__(MetricsConfigurationArgs)

        __props__.__dict__["collection_interval"] = None
        __props__.__dict__["detailed_status"] = None
        __props__.__dict__["detailed_status_message"] = None
        __props__.__dict__["disabled_metrics"] = None
        __props__.__dict__["enabled_metrics"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return MetricsConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="collectionInterval")
    def collection_interval(self) -> pulumi.Output[float]:
        """
        The interval in minutes by which metrics will be collected.
        """
        return pulumi.get(self, "collection_interval")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[str]:
        """
        The more detailed status of the metrics configuration.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[str]:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="disabledMetrics")
    def disabled_metrics(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of metrics that are available for the cluster but disabled at the moment.
        """
        return pulumi.get(self, "disabled_metrics")

    @property
    @pulumi.getter(name="enabledMetrics")
    def enabled_metrics(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of metric names that have been chosen to be enabled in addition to the core set of enabled metrics.
        """
        return pulumi.get(self, "enabled_metrics")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

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
        The provisioning state of the metrics configuration.
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
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

