# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'DocumentProcessorPropertiesArgs',
]

@pulumi.input_type
class DocumentProcessorPropertiesArgs:
    def __init__(__self__, *,
                 spo_tenant_id: pulumi.Input[str],
                 spo_tenant_url: pulumi.Input[str]):
        """
        Document processor properties
        :param pulumi.Input[str] spo_tenant_id: The ID (GUID) of an SharePoint Online (SPO) tenant associated with this document processor resource
        :param pulumi.Input[str] spo_tenant_url: The URL of an SharePoint Online (SPO) tenant associated with this document processor resource
        """
        pulumi.set(__self__, "spo_tenant_id", spo_tenant_id)
        pulumi.set(__self__, "spo_tenant_url", spo_tenant_url)

    @property
    @pulumi.getter(name="spoTenantId")
    def spo_tenant_id(self) -> pulumi.Input[str]:
        """
        The ID (GUID) of an SharePoint Online (SPO) tenant associated with this document processor resource
        """
        return pulumi.get(self, "spo_tenant_id")

    @spo_tenant_id.setter
    def spo_tenant_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "spo_tenant_id", value)

    @property
    @pulumi.getter(name="spoTenantUrl")
    def spo_tenant_url(self) -> pulumi.Input[str]:
        """
        The URL of an SharePoint Online (SPO) tenant associated with this document processor resource
        """
        return pulumi.get(self, "spo_tenant_url")

    @spo_tenant_url.setter
    def spo_tenant_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "spo_tenant_url", value)


