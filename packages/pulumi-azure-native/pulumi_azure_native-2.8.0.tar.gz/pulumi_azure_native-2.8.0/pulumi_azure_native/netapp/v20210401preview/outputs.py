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
    'VolumeBackupsResponse',
]

@pulumi.output_type
class VolumeBackupsResponse(dict):
    """
    Volume details using the backup policy
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "backupsCount":
            suggest = "backups_count"
        elif key == "policyEnabled":
            suggest = "policy_enabled"
        elif key == "volumeName":
            suggest = "volume_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VolumeBackupsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VolumeBackupsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VolumeBackupsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 backups_count: Optional[int] = None,
                 policy_enabled: Optional[bool] = None,
                 volume_name: Optional[str] = None):
        """
        Volume details using the backup policy
        :param int backups_count: Total count of backups for volume
        :param bool policy_enabled: Policy enabled
        :param str volume_name: Volume name
        """
        if backups_count is not None:
            pulumi.set(__self__, "backups_count", backups_count)
        if policy_enabled is not None:
            pulumi.set(__self__, "policy_enabled", policy_enabled)
        if volume_name is not None:
            pulumi.set(__self__, "volume_name", volume_name)

    @property
    @pulumi.getter(name="backupsCount")
    def backups_count(self) -> Optional[int]:
        """
        Total count of backups for volume
        """
        return pulumi.get(self, "backups_count")

    @property
    @pulumi.getter(name="policyEnabled")
    def policy_enabled(self) -> Optional[bool]:
        """
        Policy enabled
        """
        return pulumi.get(self, "policy_enabled")

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[str]:
        """
        Volume name
        """
        return pulumi.get(self, "volume_name")


