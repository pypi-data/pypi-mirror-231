# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'LoggerType',
]


class LoggerType(str, Enum):
    """
    Logger type.
    """
    AZURE_EVENT_HUB = "azureEventHub"
    """
    Azure Event Hub as log destination.
    """
    APPLICATION_INSIGHTS = "applicationInsights"
    """
    Azure Application Insights as log destination.
    """
