# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EventGridDataFormat',
    'Kind',
]


class EventGridDataFormat(str, Enum):
    """
    The data format of the message. Optionally the data format can be added to each message.
    """
    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"


class Kind(str, Enum):
    """
    Kind of the endpoint for the data connection
    """
    EVENT_HUB = "EventHub"
    EVENT_GRID = "EventGrid"
    IOT_HUB = "IotHub"
