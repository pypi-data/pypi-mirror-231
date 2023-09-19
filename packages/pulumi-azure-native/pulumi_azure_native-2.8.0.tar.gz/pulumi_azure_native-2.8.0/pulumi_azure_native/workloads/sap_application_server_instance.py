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

__all__ = ['SAPApplicationServerInstanceArgs', 'SAPApplicationServerInstance']

@pulumi.input_type
class SAPApplicationServerInstanceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sap_virtual_instance_name: pulumi.Input[str],
                 application_instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SAPApplicationServerInstance resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sap_virtual_instance_name: The name of the Virtual Instances for SAP solutions resource
        :param pulumi.Input[str] application_instance_name: The name of SAP Application Server instance resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sap_virtual_instance_name", sap_virtual_instance_name)
        if application_instance_name is not None:
            pulumi.set(__self__, "application_instance_name", application_instance_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="sapVirtualInstanceName")
    def sap_virtual_instance_name(self) -> pulumi.Input[str]:
        """
        The name of the Virtual Instances for SAP solutions resource
        """
        return pulumi.get(self, "sap_virtual_instance_name")

    @sap_virtual_instance_name.setter
    def sap_virtual_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sap_virtual_instance_name", value)

    @property
    @pulumi.getter(name="applicationInstanceName")
    def application_instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of SAP Application Server instance resource.
        """
        return pulumi.get(self, "application_instance_name")

    @application_instance_name.setter
    def application_instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_instance_name", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class SAPApplicationServerInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sap_virtual_instance_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Define the SAP Application Server Instance resource.
        Azure REST API version: 2023-04-01. Prior API version in Azure Native 1.x: 2021-12-01-preview

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_instance_name: The name of SAP Application Server instance resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sap_virtual_instance_name: The name of the Virtual Instances for SAP solutions resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SAPApplicationServerInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Define the SAP Application Server Instance resource.
        Azure REST API version: 2023-04-01. Prior API version in Azure Native 1.x: 2021-12-01-preview

        :param str resource_name: The name of the resource.
        :param SAPApplicationServerInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SAPApplicationServerInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sap_virtual_instance_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SAPApplicationServerInstanceArgs.__new__(SAPApplicationServerInstanceArgs)

            __props__.__dict__["application_instance_name"] = application_instance_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sap_virtual_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'sap_virtual_instance_name'")
            __props__.__dict__["sap_virtual_instance_name"] = sap_virtual_instance_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["errors"] = None
            __props__.__dict__["gateway_port"] = None
            __props__.__dict__["health"] = None
            __props__.__dict__["hostname"] = None
            __props__.__dict__["icm_http_port"] = None
            __props__.__dict__["icm_https_port"] = None
            __props__.__dict__["instance_no"] = None
            __props__.__dict__["ip_address"] = None
            __props__.__dict__["kernel_patch"] = None
            __props__.__dict__["kernel_version"] = None
            __props__.__dict__["load_balancer_details"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["subnet"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["vm_details"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:workloads/v20211201preview:SAPApplicationServerInstance"), pulumi.Alias(type_="azure-native:workloads/v20221101preview:SAPApplicationServerInstance"), pulumi.Alias(type_="azure-native:workloads/v20230401:SAPApplicationServerInstance")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SAPApplicationServerInstance, __self__).__init__(
            'azure-native:workloads:SAPApplicationServerInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SAPApplicationServerInstance':
        """
        Get an existing SAPApplicationServerInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SAPApplicationServerInstanceArgs.__new__(SAPApplicationServerInstanceArgs)

        __props__.__dict__["errors"] = None
        __props__.__dict__["gateway_port"] = None
        __props__.__dict__["health"] = None
        __props__.__dict__["hostname"] = None
        __props__.__dict__["icm_http_port"] = None
        __props__.__dict__["icm_https_port"] = None
        __props__.__dict__["instance_no"] = None
        __props__.__dict__["ip_address"] = None
        __props__.__dict__["kernel_patch"] = None
        __props__.__dict__["kernel_version"] = None
        __props__.__dict__["load_balancer_details"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subnet"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vm_details"] = None
        return SAPApplicationServerInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def errors(self) -> pulumi.Output['outputs.SAPVirtualInstanceErrorResponse']:
        """
        Defines the Application Instance errors.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter(name="gatewayPort")
    def gateway_port(self) -> pulumi.Output[float]:
        """
        Application server instance gateway Port.
        """
        return pulumi.get(self, "gateway_port")

    @property
    @pulumi.getter
    def health(self) -> pulumi.Output[str]:
        """
        Defines the health of SAP Instances.
        """
        return pulumi.get(self, "health")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        Application server instance SAP hostname.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="icmHttpPort")
    def icm_http_port(self) -> pulumi.Output[float]:
        """
        Application server instance ICM HTTP Port.
        """
        return pulumi.get(self, "icm_http_port")

    @property
    @pulumi.getter(name="icmHttpsPort")
    def icm_https_port(self) -> pulumi.Output[float]:
        """
        Application server instance ICM HTTPS Port.
        """
        return pulumi.get(self, "icm_https_port")

    @property
    @pulumi.getter(name="instanceNo")
    def instance_no(self) -> pulumi.Output[str]:
        """
        Application server Instance Number.
        """
        return pulumi.get(self, "instance_no")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
         Application server instance SAP IP Address.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="kernelPatch")
    def kernel_patch(self) -> pulumi.Output[str]:
        """
        Application server instance SAP Kernel Patch level.
        """
        return pulumi.get(self, "kernel_patch")

    @property
    @pulumi.getter(name="kernelVersion")
    def kernel_version(self) -> pulumi.Output[str]:
        """
         Application server instance SAP Kernel Version.
        """
        return pulumi.get(self, "kernel_version")

    @property
    @pulumi.getter(name="loadBalancerDetails")
    def load_balancer_details(self) -> pulumi.Output['outputs.LoadBalancerDetailsResponse']:
        """
        The Load Balancer details such as LoadBalancer ID attached to Application Server Virtual Machines
        """
        return pulumi.get(self, "load_balancer_details")

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
        Defines the provisioning states.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Defines the SAP Instance status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[str]:
        """
        Application server Subnet.
        """
        return pulumi.get(self, "subnet")

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

    @property
    @pulumi.getter(name="vmDetails")
    def vm_details(self) -> pulumi.Output[Sequence['outputs.ApplicationServerVmDetailsResponse']]:
        """
        The list of virtual machines.
        """
        return pulumi.get(self, "vm_details")

