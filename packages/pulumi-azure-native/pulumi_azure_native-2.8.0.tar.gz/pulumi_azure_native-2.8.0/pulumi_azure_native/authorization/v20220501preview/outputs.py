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
    'PermissionResponse',
]

@pulumi.output_type
class PermissionResponse(dict):
    """
    Role definition permissions.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "conditionVersion":
            suggest = "condition_version"
        elif key == "dataActions":
            suggest = "data_actions"
        elif key == "notActions":
            suggest = "not_actions"
        elif key == "notDataActions":
            suggest = "not_data_actions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PermissionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PermissionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PermissionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 condition: str,
                 condition_version: str,
                 actions: Optional[Sequence[str]] = None,
                 data_actions: Optional[Sequence[str]] = None,
                 not_actions: Optional[Sequence[str]] = None,
                 not_data_actions: Optional[Sequence[str]] = None):
        """
        Role definition permissions.
        :param str condition: The conditions on the role definition. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'
        :param str condition_version: Version of the condition. Currently the only accepted value is '2.0'
        :param Sequence[str] actions: Allowed actions.
        :param Sequence[str] data_actions: Allowed Data actions.
        :param Sequence[str] not_actions: Denied actions.
        :param Sequence[str] not_data_actions: Denied Data actions.
        """
        pulumi.set(__self__, "condition", condition)
        pulumi.set(__self__, "condition_version", condition_version)
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if data_actions is not None:
            pulumi.set(__self__, "data_actions", data_actions)
        if not_actions is not None:
            pulumi.set(__self__, "not_actions", not_actions)
        if not_data_actions is not None:
            pulumi.set(__self__, "not_data_actions", not_data_actions)

    @property
    @pulumi.getter
    def condition(self) -> str:
        """
        The conditions on the role definition. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container'
        """
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter(name="conditionVersion")
    def condition_version(self) -> str:
        """
        Version of the condition. Currently the only accepted value is '2.0'
        """
        return pulumi.get(self, "condition_version")

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[str]]:
        """
        Allowed actions.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="dataActions")
    def data_actions(self) -> Optional[Sequence[str]]:
        """
        Allowed Data actions.
        """
        return pulumi.get(self, "data_actions")

    @property
    @pulumi.getter(name="notActions")
    def not_actions(self) -> Optional[Sequence[str]]:
        """
        Denied actions.
        """
        return pulumi.get(self, "not_actions")

    @property
    @pulumi.getter(name="notDataActions")
    def not_data_actions(self) -> Optional[Sequence[str]]:
        """
        Denied Data actions.
        """
        return pulumi.get(self, "not_data_actions")


