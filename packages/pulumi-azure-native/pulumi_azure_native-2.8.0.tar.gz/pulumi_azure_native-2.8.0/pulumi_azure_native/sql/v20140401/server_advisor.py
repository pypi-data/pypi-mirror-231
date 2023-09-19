# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ServerAdvisorArgs', 'ServerAdvisor']

@pulumi.input_type
class ServerAdvisorArgs:
    def __init__(__self__, *,
                 auto_execute_value: pulumi.Input['AutoExecuteStatus'],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 advisor_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerAdvisor resource.
        :param pulumi.Input['AutoExecuteStatus'] auto_execute_value: Gets the auto-execute status (whether to let the system execute the recommendations) of this advisor. Possible values are 'Enabled' and 'Disabled'
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[str] advisor_name: The name of the Server Advisor.
        """
        pulumi.set(__self__, "auto_execute_value", auto_execute_value)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if advisor_name is not None:
            pulumi.set(__self__, "advisor_name", advisor_name)

    @property
    @pulumi.getter(name="autoExecuteValue")
    def auto_execute_value(self) -> pulumi.Input['AutoExecuteStatus']:
        """
        Gets the auto-execute status (whether to let the system execute the recommendations) of this advisor. Possible values are 'Enabled' and 'Disabled'
        """
        return pulumi.get(self, "auto_execute_value")

    @auto_execute_value.setter
    def auto_execute_value(self, value: pulumi.Input['AutoExecuteStatus']):
        pulumi.set(self, "auto_execute_value", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="advisorName")
    def advisor_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Server Advisor.
        """
        return pulumi.get(self, "advisor_name")

    @advisor_name.setter
    def advisor_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "advisor_name", value)


class ServerAdvisor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advisor_name: Optional[pulumi.Input[str]] = None,
                 auto_execute_value: Optional[pulumi.Input['AutoExecuteStatus']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Database Advisor.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] advisor_name: The name of the Server Advisor.
        :param pulumi.Input['AutoExecuteStatus'] auto_execute_value: Gets the auto-execute status (whether to let the system execute the recommendations) of this advisor. Possible values are 'Enabled' and 'Disabled'
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerAdvisorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Database Advisor.

        :param str resource_name: The name of the resource.
        :param ServerAdvisorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerAdvisorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advisor_name: Optional[pulumi.Input[str]] = None,
                 auto_execute_value: Optional[pulumi.Input['AutoExecuteStatus']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerAdvisorArgs.__new__(ServerAdvisorArgs)

            __props__.__dict__["advisor_name"] = advisor_name
            if auto_execute_value is None and not opts.urn:
                raise TypeError("Missing required property 'auto_execute_value'")
            __props__.__dict__["auto_execute_value"] = auto_execute_value
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["advisor_status"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["last_checked"] = None
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["recommendations_status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20150501preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20200202preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20200801preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20201101preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20210201preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20210501preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20210801preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20211101:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20211101preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20220201preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20220501preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20220801preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20221101preview:ServerAdvisor"), pulumi.Alias(type_="azure-native:sql/v20230201preview:ServerAdvisor")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerAdvisor, __self__).__init__(
            'azure-native:sql/v20140401:ServerAdvisor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerAdvisor':
        """
        Get an existing ServerAdvisor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerAdvisorArgs.__new__(ServerAdvisorArgs)

        __props__.__dict__["advisor_status"] = None
        __props__.__dict__["auto_execute_value"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["last_checked"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["recommendations_status"] = None
        __props__.__dict__["type"] = None
        return ServerAdvisor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="advisorStatus")
    def advisor_status(self) -> pulumi.Output[str]:
        """
        Gets the status of availability of this advisor to customers. Possible values are 'GA', 'PublicPreview', 'LimitedPublicPreview' and 'PrivatePreview'.
        """
        return pulumi.get(self, "advisor_status")

    @property
    @pulumi.getter(name="autoExecuteValue")
    def auto_execute_value(self) -> pulumi.Output[str]:
        """
        Gets the auto-execute status (whether to let the system execute the recommendations) of this advisor. Possible values are 'Enabled' and 'Disabled'
        """
        return pulumi.get(self, "auto_execute_value")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Resource kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastChecked")
    def last_checked(self) -> pulumi.Output[str]:
        """
        Gets the time when the current resource was analyzed for recommendations by this advisor.
        """
        return pulumi.get(self, "last_checked")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recommendationsStatus")
    def recommendations_status(self) -> pulumi.Output[str]:
        """
        Gets that status of recommendations for this advisor and reason for not having any recommendations. Possible values include, but are not limited to, 'Ok' (Recommendations available), LowActivity (not enough workload to analyze), 'DbSeemsTuned' (Database is doing well), etc.
        """
        return pulumi.get(self, "recommendations_status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

