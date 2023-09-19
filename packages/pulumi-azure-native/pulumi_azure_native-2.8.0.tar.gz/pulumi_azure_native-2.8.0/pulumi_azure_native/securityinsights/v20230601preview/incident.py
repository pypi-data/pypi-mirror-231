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

__all__ = ['IncidentArgs', 'Incident']

@pulumi.input_type
class IncidentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 severity: pulumi.Input[Union[str, 'IncidentSeverity']],
                 status: pulumi.Input[Union[str, 'IncidentStatus']],
                 title: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 classification: Optional[pulumi.Input[Union[str, 'IncidentClassification']]] = None,
                 classification_comment: Optional[pulumi.Input[str]] = None,
                 classification_reason: Optional[pulumi.Input[Union[str, 'IncidentClassificationReason']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 first_activity_time_utc: Optional[pulumi.Input[str]] = None,
                 incident_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input['IncidentLabelArgs']]]] = None,
                 last_activity_time_utc: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input['IncidentOwnerInfoArgs']] = None):
        """
        The set of arguments for constructing a Incident resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'IncidentSeverity']] severity: The severity of the incident
        :param pulumi.Input[Union[str, 'IncidentStatus']] status: The status of the incident
        :param pulumi.Input[str] title: The title of the incident
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[Union[str, 'IncidentClassification']] classification: The reason the incident was closed
        :param pulumi.Input[str] classification_comment: Describes the reason the incident was closed
        :param pulumi.Input[Union[str, 'IncidentClassificationReason']] classification_reason: The classification reason the incident was closed with
        :param pulumi.Input[str] description: The description of the incident
        :param pulumi.Input[str] first_activity_time_utc: The time of the first activity in the incident
        :param pulumi.Input[str] incident_id: Incident ID
        :param pulumi.Input[Sequence[pulumi.Input['IncidentLabelArgs']]] labels: List of labels relevant to this incident
        :param pulumi.Input[str] last_activity_time_utc: The time of the last activity in the incident
        :param pulumi.Input['IncidentOwnerInfoArgs'] owner: Describes a user that the incident is assigned to
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "severity", severity)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if classification is not None:
            pulumi.set(__self__, "classification", classification)
        if classification_comment is not None:
            pulumi.set(__self__, "classification_comment", classification_comment)
        if classification_reason is not None:
            pulumi.set(__self__, "classification_reason", classification_reason)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if first_activity_time_utc is not None:
            pulumi.set(__self__, "first_activity_time_utc", first_activity_time_utc)
        if incident_id is not None:
            pulumi.set(__self__, "incident_id", incident_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if last_activity_time_utc is not None:
            pulumi.set(__self__, "last_activity_time_utc", last_activity_time_utc)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)

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
    @pulumi.getter
    def severity(self) -> pulumi.Input[Union[str, 'IncidentSeverity']]:
        """
        The severity of the incident
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: pulumi.Input[Union[str, 'IncidentSeverity']]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[str, 'IncidentStatus']]:
        """
        The status of the incident
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[Union[str, 'IncidentStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The title of the incident
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter
    def classification(self) -> Optional[pulumi.Input[Union[str, 'IncidentClassification']]]:
        """
        The reason the incident was closed
        """
        return pulumi.get(self, "classification")

    @classification.setter
    def classification(self, value: Optional[pulumi.Input[Union[str, 'IncidentClassification']]]):
        pulumi.set(self, "classification", value)

    @property
    @pulumi.getter(name="classificationComment")
    def classification_comment(self) -> Optional[pulumi.Input[str]]:
        """
        Describes the reason the incident was closed
        """
        return pulumi.get(self, "classification_comment")

    @classification_comment.setter
    def classification_comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "classification_comment", value)

    @property
    @pulumi.getter(name="classificationReason")
    def classification_reason(self) -> Optional[pulumi.Input[Union[str, 'IncidentClassificationReason']]]:
        """
        The classification reason the incident was closed with
        """
        return pulumi.get(self, "classification_reason")

    @classification_reason.setter
    def classification_reason(self, value: Optional[pulumi.Input[Union[str, 'IncidentClassificationReason']]]):
        pulumi.set(self, "classification_reason", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the incident
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="firstActivityTimeUtc")
    def first_activity_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        The time of the first activity in the incident
        """
        return pulumi.get(self, "first_activity_time_utc")

    @first_activity_time_utc.setter
    def first_activity_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_activity_time_utc", value)

    @property
    @pulumi.getter(name="incidentId")
    def incident_id(self) -> Optional[pulumi.Input[str]]:
        """
        Incident ID
        """
        return pulumi.get(self, "incident_id")

    @incident_id.setter
    def incident_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "incident_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IncidentLabelArgs']]]]:
        """
        List of labels relevant to this incident
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IncidentLabelArgs']]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="lastActivityTimeUtc")
    def last_activity_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        The time of the last activity in the incident
        """
        return pulumi.get(self, "last_activity_time_utc")

    @last_activity_time_utc.setter
    def last_activity_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_activity_time_utc", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input['IncidentOwnerInfoArgs']]:
        """
        Describes a user that the incident is assigned to
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input['IncidentOwnerInfoArgs']]):
        pulumi.set(self, "owner", value)


class Incident(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 classification: Optional[pulumi.Input[Union[str, 'IncidentClassification']]] = None,
                 classification_comment: Optional[pulumi.Input[str]] = None,
                 classification_reason: Optional[pulumi.Input[Union[str, 'IncidentClassificationReason']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 first_activity_time_utc: Optional[pulumi.Input[str]] = None,
                 incident_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IncidentLabelArgs']]]]] = None,
                 last_activity_time_utc: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[pulumi.InputType['IncidentOwnerInfoArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[Union[str, 'IncidentSeverity']]] = None,
                 status: Optional[pulumi.Input[Union[str, 'IncidentStatus']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Incident resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'IncidentClassification']] classification: The reason the incident was closed
        :param pulumi.Input[str] classification_comment: Describes the reason the incident was closed
        :param pulumi.Input[Union[str, 'IncidentClassificationReason']] classification_reason: The classification reason the incident was closed with
        :param pulumi.Input[str] description: The description of the incident
        :param pulumi.Input[str] first_activity_time_utc: The time of the first activity in the incident
        :param pulumi.Input[str] incident_id: Incident ID
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IncidentLabelArgs']]]] labels: List of labels relevant to this incident
        :param pulumi.Input[str] last_activity_time_utc: The time of the last activity in the incident
        :param pulumi.Input[pulumi.InputType['IncidentOwnerInfoArgs']] owner: Describes a user that the incident is assigned to
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'IncidentSeverity']] severity: The severity of the incident
        :param pulumi.Input[Union[str, 'IncidentStatus']] status: The status of the incident
        :param pulumi.Input[str] title: The title of the incident
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IncidentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Incident resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param IncidentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IncidentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 classification: Optional[pulumi.Input[Union[str, 'IncidentClassification']]] = None,
                 classification_comment: Optional[pulumi.Input[str]] = None,
                 classification_reason: Optional[pulumi.Input[Union[str, 'IncidentClassificationReason']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 first_activity_time_utc: Optional[pulumi.Input[str]] = None,
                 incident_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IncidentLabelArgs']]]]] = None,
                 last_activity_time_utc: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[pulumi.InputType['IncidentOwnerInfoArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[Union[str, 'IncidentSeverity']]] = None,
                 status: Optional[pulumi.Input[Union[str, 'IncidentStatus']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IncidentArgs.__new__(IncidentArgs)

            __props__.__dict__["classification"] = classification
            __props__.__dict__["classification_comment"] = classification_comment
            __props__.__dict__["classification_reason"] = classification_reason
            __props__.__dict__["description"] = description
            __props__.__dict__["first_activity_time_utc"] = first_activity_time_utc
            __props__.__dict__["incident_id"] = incident_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["last_activity_time_utc"] = last_activity_time_utc
            __props__.__dict__["owner"] = owner
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if severity is None and not opts.urn:
                raise TypeError("Missing required property 'severity'")
            __props__.__dict__["severity"] = severity
            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["additional_data"] = None
            __props__.__dict__["created_time_utc"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["incident_number"] = None
            __props__.__dict__["incident_url"] = None
            __props__.__dict__["last_modified_time_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provider_incident_id"] = None
            __props__.__dict__["provider_name"] = None
            __props__.__dict__["related_analytic_rule_ids"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["team_information"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20200101:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20210401:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20211001:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20220801:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20221101:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20230201:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20230201preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20230301preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:Incident"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:Incident")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Incident, __self__).__init__(
            'azure-native:securityinsights/v20230601preview:Incident',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Incident':
        """
        Get an existing Incident resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IncidentArgs.__new__(IncidentArgs)

        __props__.__dict__["additional_data"] = None
        __props__.__dict__["classification"] = None
        __props__.__dict__["classification_comment"] = None
        __props__.__dict__["classification_reason"] = None
        __props__.__dict__["created_time_utc"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["first_activity_time_utc"] = None
        __props__.__dict__["incident_number"] = None
        __props__.__dict__["incident_url"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["last_activity_time_utc"] = None
        __props__.__dict__["last_modified_time_utc"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["owner"] = None
        __props__.__dict__["provider_incident_id"] = None
        __props__.__dict__["provider_name"] = None
        __props__.__dict__["related_analytic_rule_ids"] = None
        __props__.__dict__["severity"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["team_information"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["type"] = None
        return Incident(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> pulumi.Output['outputs.IncidentAdditionalDataResponse']:
        """
        Additional data on the incident
        """
        return pulumi.get(self, "additional_data")

    @property
    @pulumi.getter
    def classification(self) -> pulumi.Output[Optional[str]]:
        """
        The reason the incident was closed
        """
        return pulumi.get(self, "classification")

    @property
    @pulumi.getter(name="classificationComment")
    def classification_comment(self) -> pulumi.Output[Optional[str]]:
        """
        Describes the reason the incident was closed
        """
        return pulumi.get(self, "classification_comment")

    @property
    @pulumi.getter(name="classificationReason")
    def classification_reason(self) -> pulumi.Output[Optional[str]]:
        """
        The classification reason the incident was closed with
        """
        return pulumi.get(self, "classification_reason")

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> pulumi.Output[str]:
        """
        The time the incident was created
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the incident
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="firstActivityTimeUtc")
    def first_activity_time_utc(self) -> pulumi.Output[Optional[str]]:
        """
        The time of the first activity in the incident
        """
        return pulumi.get(self, "first_activity_time_utc")

    @property
    @pulumi.getter(name="incidentNumber")
    def incident_number(self) -> pulumi.Output[int]:
        """
        A sequential number
        """
        return pulumi.get(self, "incident_number")

    @property
    @pulumi.getter(name="incidentUrl")
    def incident_url(self) -> pulumi.Output[str]:
        """
        The deep-link url to the incident in Azure portal
        """
        return pulumi.get(self, "incident_url")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence['outputs.IncidentLabelResponse']]]:
        """
        List of labels relevant to this incident
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="lastActivityTimeUtc")
    def last_activity_time_utc(self) -> pulumi.Output[Optional[str]]:
        """
        The time of the last activity in the incident
        """
        return pulumi.get(self, "last_activity_time_utc")

    @property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> pulumi.Output[str]:
        """
        The last time the incident was updated
        """
        return pulumi.get(self, "last_modified_time_utc")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[Optional['outputs.IncidentOwnerInfoResponse']]:
        """
        Describes a user that the incident is assigned to
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="providerIncidentId")
    def provider_incident_id(self) -> pulumi.Output[str]:
        """
        The incident ID assigned by the incident provider
        """
        return pulumi.get(self, "provider_incident_id")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Output[str]:
        """
        The name of the source provider that generated the incident
        """
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter(name="relatedAnalyticRuleIds")
    def related_analytic_rule_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        List of resource ids of Analytic rules related to the incident
        """
        return pulumi.get(self, "related_analytic_rule_ids")

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Output[str]:
        """
        The severity of the incident
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the incident
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="teamInformation")
    def team_information(self) -> pulumi.Output[Optional['outputs.TeamInformationResponse']]:
        """
        Describes a team for the incident
        """
        return pulumi.get(self, "team_information")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The title of the incident
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

