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
    'RuleResultsPropertiesResponse',
]

@pulumi.output_type
class RuleResultsPropertiesResponse(dict):
    """
    Rule results properties.
    """
    def __init__(__self__, *,
                 results: Optional[Sequence[Sequence[str]]] = None):
        """
        Rule results properties.
        :param Sequence[Sequence[str]] results: Expected results in the baseline.
        """
        if results is not None:
            pulumi.set(__self__, "results", results)

    @property
    @pulumi.getter
    def results(self) -> Optional[Sequence[Sequence[str]]]:
        """
        Expected results in the baseline.
        """
        return pulumi.get(self, "results")


