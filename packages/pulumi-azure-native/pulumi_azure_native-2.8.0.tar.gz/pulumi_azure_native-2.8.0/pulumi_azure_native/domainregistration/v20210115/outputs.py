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
    'NameIdentifierResponse',
    'TldLegalAgreementResponse',
]

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


