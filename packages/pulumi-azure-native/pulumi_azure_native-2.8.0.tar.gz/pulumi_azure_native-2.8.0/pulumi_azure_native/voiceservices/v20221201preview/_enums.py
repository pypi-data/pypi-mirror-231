# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'TestLinePurpose',
]


class TestLinePurpose(str, Enum):
    """
    Purpose of this test line, e.g. automated or manual testing
    """
    MANUAL = "Manual"
    AUTOMATED = "Automated"
