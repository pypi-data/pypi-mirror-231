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

__all__ = [
    'HostNameResponse',
    'NameIdentifierResponse',
    'TldLegalAgreementResponse',
]

@pulumi.output_type
class HostNameResponse(dict):
    """
    Details of a hostname derived from a domain.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "azureResourceName":
            suggest = "azure_resource_name"
        elif key == "azureResourceType":
            suggest = "azure_resource_type"
        elif key == "customHostNameDnsRecordType":
            suggest = "custom_host_name_dns_record_type"
        elif key == "hostNameType":
            suggest = "host_name_type"
        elif key == "siteNames":
            suggest = "site_names"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostNameResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostNameResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostNameResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 azure_resource_name: Optional[str] = None,
                 azure_resource_type: Optional[str] = None,
                 custom_host_name_dns_record_type: Optional[str] = None,
                 host_name_type: Optional[str] = None,
                 name: Optional[str] = None,
                 site_names: Optional[Sequence[str]] = None):
        """
        Details of a hostname derived from a domain.
        :param str azure_resource_name: Name of the Azure resource the hostname is assigned to. If it is assigned to a Traffic Manager then it will be the Traffic Manager name otherwise it will be the app name.
        :param str azure_resource_type: Type of the Azure resource the hostname is assigned to.
        :param str custom_host_name_dns_record_type: Type of the DNS record.
        :param str host_name_type: Type of the hostname.
        :param str name: Name of the hostname.
        :param Sequence[str] site_names: List of apps the hostname is assigned to. This list will have more than one app only if the hostname is pointing to a Traffic Manager.
        """
        if azure_resource_name is not None:
            pulumi.set(__self__, "azure_resource_name", azure_resource_name)
        if azure_resource_type is not None:
            pulumi.set(__self__, "azure_resource_type", azure_resource_type)
        if custom_host_name_dns_record_type is not None:
            pulumi.set(__self__, "custom_host_name_dns_record_type", custom_host_name_dns_record_type)
        if host_name_type is not None:
            pulumi.set(__self__, "host_name_type", host_name_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if site_names is not None:
            pulumi.set(__self__, "site_names", site_names)

    @property
    @pulumi.getter(name="azureResourceName")
    def azure_resource_name(self) -> Optional[str]:
        """
        Name of the Azure resource the hostname is assigned to. If it is assigned to a Traffic Manager then it will be the Traffic Manager name otherwise it will be the app name.
        """
        return pulumi.get(self, "azure_resource_name")

    @property
    @pulumi.getter(name="azureResourceType")
    def azure_resource_type(self) -> Optional[str]:
        """
        Type of the Azure resource the hostname is assigned to.
        """
        return pulumi.get(self, "azure_resource_type")

    @property
    @pulumi.getter(name="customHostNameDnsRecordType")
    def custom_host_name_dns_record_type(self) -> Optional[str]:
        """
        Type of the DNS record.
        """
        return pulumi.get(self, "custom_host_name_dns_record_type")

    @property
    @pulumi.getter(name="hostNameType")
    def host_name_type(self) -> Optional[str]:
        """
        Type of the hostname.
        """
        return pulumi.get(self, "host_name_type")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the hostname.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="siteNames")
    def site_names(self) -> Optional[Sequence[str]]:
        """
        List of apps the hostname is assigned to. This list will have more than one app only if the hostname is pointing to a Traffic Manager.
        """
        return pulumi.get(self, "site_names")


@pulumi.output_type
class NameIdentifierResponse(dict):
    """
    Identifies an object.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        Identifies an object.
        :param str name: Name of the object.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the object.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class TldLegalAgreementResponse(dict):
    """
    Legal agreement for a top level domain.
    """
    def __init__(__self__, *,
                 agreement_key: str,
                 content: str,
                 title: str,
                 url: Optional[str] = None):
        """
        Legal agreement for a top level domain.
        :param str agreement_key: Unique identifier for the agreement.
        :param str content: Agreement details.
        :param str title: Agreement title.
        :param str url: URL where a copy of the agreement details is hosted.
        """
        pulumi.set(__self__, "agreement_key", agreement_key)
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "title", title)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="agreementKey")
    def agreement_key(self) -> str:
        """
        Unique identifier for the agreement.
        """
        return pulumi.get(self, "agreement_key")

    @property
    @pulumi.getter
    def content(self) -> str:
        """
        Agreement details.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        Agreement title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        URL where a copy of the agreement details is hosted.
        """
        return pulumi.get(self, "url")


