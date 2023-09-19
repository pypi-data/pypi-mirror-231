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

__all__ = ['ExportArgs', 'Export']

@pulumi.input_type
class ExportArgs:
    def __init__(__self__, *,
                 definition: pulumi.Input['ExportDefinitionArgs'],
                 delivery_info: pulumi.Input['ExportDeliveryInfoArgs'],
                 scope: pulumi.Input[str],
                 e_tag: Optional[pulumi.Input[str]] = None,
                 export_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 identity: Optional[pulumi.Input['SystemAssignedServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partition_data: Optional[pulumi.Input[bool]] = None,
                 schedule: Optional[pulumi.Input['ExportScheduleArgs']] = None):
        """
        The set of arguments for constructing a Export resource.
        :param pulumi.Input['ExportDefinitionArgs'] definition: Has the definition for the export.
        :param pulumi.Input['ExportDeliveryInfoArgs'] delivery_info: Has delivery information for the export.
        :param pulumi.Input[str] scope: The scope associated with export operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope, and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' specific for partners.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input[str] export_name: Export Name.
        :param pulumi.Input[Union[str, 'FormatType']] format: The format of the export being delivered. Currently only 'Csv' is supported.
        :param pulumi.Input['SystemAssignedServiceIdentityArgs'] identity: The managed identity associated with Export
        :param pulumi.Input[str] location: The location of the Export's managed identity. Only required when utilizing managed identity.
        :param pulumi.Input[bool] partition_data: If set to true, exported data will be partitioned by size and placed in a blob directory together with a manifest file. Note: this option is currently available only for Microsoft Customer Agreement commerce scopes.
        :param pulumi.Input['ExportScheduleArgs'] schedule: Has schedule information for the export.
        """
        pulumi.set(__self__, "definition", definition)
        pulumi.set(__self__, "delivery_info", delivery_info)
        pulumi.set(__self__, "scope", scope)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if export_name is not None:
            pulumi.set(__self__, "export_name", export_name)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if partition_data is not None:
            pulumi.set(__self__, "partition_data", partition_data)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Input['ExportDefinitionArgs']:
        """
        Has the definition for the export.
        """
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: pulumi.Input['ExportDefinitionArgs']):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Input['ExportDeliveryInfoArgs']:
        """
        Has delivery information for the export.
        """
        return pulumi.get(self, "delivery_info")

    @delivery_info.setter
    def delivery_info(self, value: pulumi.Input['ExportDeliveryInfoArgs']):
        pulumi.set(self, "delivery_info", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope associated with export operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope, and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' specific for partners.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter(name="exportName")
    def export_name(self) -> Optional[pulumi.Input[str]]:
        """
        Export Name.
        """
        return pulumi.get(self, "export_name")

    @export_name.setter
    def export_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "export_name", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[Union[str, 'FormatType']]]:
        """
        The format of the export being delivered. Currently only 'Csv' is supported.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[Union[str, 'FormatType']]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['SystemAssignedServiceIdentityArgs']]:
        """
        The managed identity associated with Export
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['SystemAssignedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the Export's managed identity. Only required when utilizing managed identity.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="partitionData")
    def partition_data(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, exported data will be partitioned by size and placed in a blob directory together with a manifest file. Note: this option is currently available only for Microsoft Customer Agreement commerce scopes.
        """
        return pulumi.get(self, "partition_data")

    @partition_data.setter
    def partition_data(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "partition_data", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['ExportScheduleArgs']]:
        """
        Has schedule information for the export.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['ExportScheduleArgs']]):
        pulumi.set(self, "schedule", value)


class Export(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['ExportDefinitionArgs']]] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['ExportDeliveryInfoArgs']]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 export_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['SystemAssignedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partition_data: Optional[pulumi.Input[bool]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ExportScheduleArgs']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An export resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExportDefinitionArgs']] definition: Has the definition for the export.
        :param pulumi.Input[pulumi.InputType['ExportDeliveryInfoArgs']] delivery_info: Has delivery information for the export.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input[str] export_name: Export Name.
        :param pulumi.Input[Union[str, 'FormatType']] format: The format of the export being delivered. Currently only 'Csv' is supported.
        :param pulumi.Input[pulumi.InputType['SystemAssignedServiceIdentityArgs']] identity: The managed identity associated with Export
        :param pulumi.Input[str] location: The location of the Export's managed identity. Only required when utilizing managed identity.
        :param pulumi.Input[bool] partition_data: If set to true, exported data will be partitioned by size and placed in a blob directory together with a manifest file. Note: this option is currently available only for Microsoft Customer Agreement commerce scopes.
        :param pulumi.Input[pulumi.InputType['ExportScheduleArgs']] schedule: Has schedule information for the export.
        :param pulumi.Input[str] scope: The scope associated with export operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope, and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' specific for partners.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExportArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An export resource.

        :param str resource_name: The name of the resource.
        :param ExportArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExportArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['ExportDefinitionArgs']]] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['ExportDeliveryInfoArgs']]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 export_name: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['SystemAssignedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partition_data: Optional[pulumi.Input[bool]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ExportScheduleArgs']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExportArgs.__new__(ExportArgs)

            if definition is None and not opts.urn:
                raise TypeError("Missing required property 'definition'")
            __props__.__dict__["definition"] = definition
            if delivery_info is None and not opts.urn:
                raise TypeError("Missing required property 'delivery_info'")
            __props__.__dict__["delivery_info"] = delivery_info
            __props__.__dict__["e_tag"] = e_tag
            __props__.__dict__["export_name"] = export_name
            __props__.__dict__["format"] = format
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["partition_data"] = partition_data
            __props__.__dict__["schedule"] = schedule
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["name"] = None
            __props__.__dict__["next_run_time_estimate"] = None
            __props__.__dict__["run_history"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:costmanagement:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20190101:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20190901:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20191001:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20191101:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20200601:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20201201preview:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20210101:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20211001:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20221001:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20230301:Export"), pulumi.Alias(type_="azure-native:costmanagement/v20230801:Export")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Export, __self__).__init__(
            'azure-native:costmanagement/v20230401preview:Export',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Export':
        """
        Get an existing Export resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExportArgs.__new__(ExportArgs)

        __props__.__dict__["definition"] = None
        __props__.__dict__["delivery_info"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["format"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["next_run_time_estimate"] = None
        __props__.__dict__["partition_data"] = None
        __props__.__dict__["run_history"] = None
        __props__.__dict__["schedule"] = None
        __props__.__dict__["type"] = None
        return Export(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output['outputs.ExportDefinitionResponse']:
        """
        Has the definition for the export.
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Output['outputs.ExportDeliveryInfoResponse']:
        """
        Has delivery information for the export.
        """
        return pulumi.get(self, "delivery_info")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional[str]]:
        """
        The format of the export being delivered. Currently only 'Csv' is supported.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.SystemAssignedServiceIdentityResponse']]:
        """
        The managed identity associated with Export
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the Export's managed identity. Only required when utilizing managed identity.
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
    @pulumi.getter(name="nextRunTimeEstimate")
    def next_run_time_estimate(self) -> pulumi.Output[str]:
        """
        If the export has an active schedule, provides an estimate of the next run time.
        """
        return pulumi.get(self, "next_run_time_estimate")

    @property
    @pulumi.getter(name="partitionData")
    def partition_data(self) -> pulumi.Output[Optional[bool]]:
        """
        If set to true, exported data will be partitioned by size and placed in a blob directory together with a manifest file. Note: this option is currently available only for Microsoft Customer Agreement commerce scopes.
        """
        return pulumi.get(self, "partition_data")

    @property
    @pulumi.getter(name="runHistory")
    def run_history(self) -> pulumi.Output[Optional['outputs.ExportExecutionListResultResponse']]:
        """
        If requested, has the most recent run history for the export.
        """
        return pulumi.get(self, "run_history")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional['outputs.ExportScheduleResponse']]:
        """
        Has schedule information for the export.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

