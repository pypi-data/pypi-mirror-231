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
    'SubscriptionLogSettingsArgs',
]

@pulumi.input_type
class SubscriptionLogSettingsArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 category: Optional[pulumi.Input[str]] = None):
        """
        Part of Subscription diagnostic setting. Specifies the settings for a particular log.
        :param pulumi.Input[bool] enabled: a value indicating whether this log is enabled.
        :param pulumi.Input[str] category: Name of a Subscription Diagnostic Log category for a resource type this setting is applied to.
        """
        pulumi.set(__self__, "enabled", enabled)
        if category is not None:
            pulumi.set(__self__, "category", category)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        a value indicating whether this log is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        Name of a Subscription Diagnostic Log category for a resource type this setting is applied to.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)


