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
    'GetDomainResult',
    'AwaitableGetDomainResult',
    'get_domain',
    'get_domain_output',
]

@pulumi.output_type
class GetDomainResult:
    """
    A class representing a Domains resource.
    """
    def __init__(__self__, data_location=None, domain_management=None, from_sender_domain=None, id=None, location=None, mail_from_sender_domain=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None, user_engagement_tracking=None, valid_sender_usernames=None, verification_records=None, verification_states=None):
        if data_location and not isinstance(data_location, str):
            raise TypeError("Expected argument 'data_location' to be a str")
        pulumi.set(__self__, "data_location", data_location)
        if domain_management and not isinstance(domain_management, str):
            raise TypeError("Expected argument 'domain_management' to be a str")
        pulumi.set(__self__, "domain_management", domain_management)
        if from_sender_domain and not isinstance(from_sender_domain, str):
            raise TypeError("Expected argument 'from_sender_domain' to be a str")
        pulumi.set(__self__, "from_sender_domain", from_sender_domain)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mail_from_sender_domain and not isinstance(mail_from_sender_domain, str):
            raise TypeError("Expected argument 'mail_from_sender_domain' to be a str")
        pulumi.set(__self__, "mail_from_sender_domain", mail_from_sender_domain)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_engagement_tracking and not isinstance(user_engagement_tracking, str):
            raise TypeError("Expected argument 'user_engagement_tracking' to be a str")
        pulumi.set(__self__, "user_engagement_tracking", user_engagement_tracking)
        if valid_sender_usernames and not isinstance(valid_sender_usernames, dict):
            raise TypeError("Expected argument 'valid_sender_usernames' to be a dict")
        pulumi.set(__self__, "valid_sender_usernames", valid_sender_usernames)
        if verification_records and not isinstance(verification_records, dict):
            raise TypeError("Expected argument 'verification_records' to be a dict")
        pulumi.set(__self__, "verification_records", verification_records)
        if verification_states and not isinstance(verification_states, dict):
            raise TypeError("Expected argument 'verification_states' to be a dict")
        pulumi.set(__self__, "verification_states", verification_states)

    @property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> str:
        """
        The location where the Domains resource data is stored at rest.
        """
        return pulumi.get(self, "data_location")

    @property
    @pulumi.getter(name="domainManagement")
    def domain_management(self) -> str:
        """
        Describes how a Domains resource is being managed.
        """
        return pulumi.get(self, "domain_management")

    @property
    @pulumi.getter(name="fromSenderDomain")
    def from_sender_domain(self) -> str:
        """
        P2 sender domain that is displayed to the email recipients [RFC 5322].
        """
        return pulumi.get(self, "from_sender_domain")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mailFromSenderDomain")
    def mail_from_sender_domain(self) -> str:
        """
        P1 sender domain that is present on the email envelope [RFC 5321].
        """
        return pulumi.get(self, "mail_from_sender_domain")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userEngagementTracking")
    def user_engagement_tracking(self) -> Optional[str]:
        """
        Describes whether user engagement tracking is enabled or disabled.
        """
        return pulumi.get(self, "user_engagement_tracking")

    @property
    @pulumi.getter(name="validSenderUsernames")
    def valid_sender_usernames(self) -> Optional[Mapping[str, str]]:
        """
        Collection of valid sender usernames. This is a key-value pair where key=username and value=display name.
        """
        return pulumi.get(self, "valid_sender_usernames")

    @property
    @pulumi.getter(name="verificationRecords")
    def verification_records(self) -> 'outputs.DomainPropertiesResponseVerificationRecords':
        """
        List of DnsRecord
        """
        return pulumi.get(self, "verification_records")

    @property
    @pulumi.getter(name="verificationStates")
    def verification_states(self) -> 'outputs.DomainPropertiesResponseVerificationStates':
        """
        List of VerificationStatusRecord
        """
        return pulumi.get(self, "verification_states")


class AwaitableGetDomainResult(GetDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainResult(
            data_location=self.data_location,
            domain_management=self.domain_management,
            from_sender_domain=self.from_sender_domain,
            id=self.id,
            location=self.location,
            mail_from_sender_domain=self.mail_from_sender_domain,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            user_engagement_tracking=self.user_engagement_tracking,
            valid_sender_usernames=self.valid_sender_usernames,
            verification_records=self.verification_records,
            verification_states=self.verification_states)


def get_domain(domain_name: Optional[str] = None,
               email_service_name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainResult:
    """
    Get the Domains resource and its properties.


    :param str domain_name: The name of the Domains resource.
    :param str email_service_name: The name of the EmailService resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['domainName'] = domain_name
    __args__['emailServiceName'] = email_service_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:communication/v20220701preview:getDomain', __args__, opts=opts, typ=GetDomainResult).value

    return AwaitableGetDomainResult(
        data_location=pulumi.get(__ret__, 'data_location'),
        domain_management=pulumi.get(__ret__, 'domain_management'),
        from_sender_domain=pulumi.get(__ret__, 'from_sender_domain'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        mail_from_sender_domain=pulumi.get(__ret__, 'mail_from_sender_domain'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        user_engagement_tracking=pulumi.get(__ret__, 'user_engagement_tracking'),
        valid_sender_usernames=pulumi.get(__ret__, 'valid_sender_usernames'),
        verification_records=pulumi.get(__ret__, 'verification_records'),
        verification_states=pulumi.get(__ret__, 'verification_states'))


@_utilities.lift_output_func(get_domain)
def get_domain_output(domain_name: Optional[pulumi.Input[str]] = None,
                      email_service_name: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainResult]:
    """
    Get the Domains resource and its properties.


    :param str domain_name: The name of the Domains resource.
    :param str email_service_name: The name of the EmailService resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
