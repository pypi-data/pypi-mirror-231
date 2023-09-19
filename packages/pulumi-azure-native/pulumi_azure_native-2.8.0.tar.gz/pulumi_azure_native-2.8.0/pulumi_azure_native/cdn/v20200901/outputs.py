# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'CompressionSettingsResponse',
    'HealthProbeParametersResponse',
    'HttpErrorRangeParametersResponse',
    'LoadBalancingSettingsParametersResponse',
    'ResourceReferenceResponse',
    'ResponseBasedOriginErrorDetectionParametersResponse',
    'SkuResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class CompressionSettingsResponse(dict):
    """
    settings for compression.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "contentTypesToCompress":
            suggest = "content_types_to_compress"
        elif key == "isCompressionEnabled":
            suggest = "is_compression_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CompressionSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CompressionSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CompressionSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 content_types_to_compress: Optional[Sequence[str]] = None,
                 is_compression_enabled: Optional[bool] = None):
        """
        settings for compression.
        :param Sequence[str] content_types_to_compress: List of content types on which compression applies. The value should be a valid MIME type.
        :param bool is_compression_enabled: Indicates whether content compression is enabled on AzureFrontDoor. Default value is false. If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won't be compressed on AzureFrontDoor when requested content is smaller than 1 byte or larger than 1 MB.
        """
        if content_types_to_compress is not None:
            pulumi.set(__self__, "content_types_to_compress", content_types_to_compress)
        if is_compression_enabled is not None:
            pulumi.set(__self__, "is_compression_enabled", is_compression_enabled)

    @property
    @pulumi.getter(name="contentTypesToCompress")
    def content_types_to_compress(self) -> Optional[Sequence[str]]:
        """
        List of content types on which compression applies. The value should be a valid MIME type.
        """
        return pulumi.get(self, "content_types_to_compress")

    @property
    @pulumi.getter(name="isCompressionEnabled")
    def is_compression_enabled(self) -> Optional[bool]:
        """
        Indicates whether content compression is enabled on AzureFrontDoor. Default value is false. If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won't be compressed on AzureFrontDoor when requested content is smaller than 1 byte or larger than 1 MB.
        """
        return pulumi.get(self, "is_compression_enabled")


@pulumi.output_type
class HealthProbeParametersResponse(dict):
    """
    The JSON object that contains the properties to send health probes to origin.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "probeIntervalInSeconds":
            suggest = "probe_interval_in_seconds"
        elif key == "probePath":
            suggest = "probe_path"
        elif key == "probeProtocol":
            suggest = "probe_protocol"
        elif key == "probeRequestType":
            suggest = "probe_request_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HealthProbeParametersResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HealthProbeParametersResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HealthProbeParametersResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 probe_interval_in_seconds: Optional[int] = None,
                 probe_path: Optional[str] = None,
                 probe_protocol: Optional[str] = None,
                 probe_request_type: Optional[str] = None):
        """
        The JSON object that contains the properties to send health probes to origin.
        :param int probe_interval_in_seconds: The number of seconds between health probes.Default is 240sec.
        :param str probe_path: The path relative to the origin that is used to determine the health of the origin.
        :param str probe_protocol: Protocol to use for health probe.
        :param str probe_request_type: The type of health probe request that is made.
        """
        if probe_interval_in_seconds is not None:
            pulumi.set(__self__, "probe_interval_in_seconds", probe_interval_in_seconds)
        if probe_path is not None:
            pulumi.set(__self__, "probe_path", probe_path)
        if probe_protocol is not None:
            pulumi.set(__self__, "probe_protocol", probe_protocol)
        if probe_request_type is not None:
            pulumi.set(__self__, "probe_request_type", probe_request_type)

    @property
    @pulumi.getter(name="probeIntervalInSeconds")
    def probe_interval_in_seconds(self) -> Optional[int]:
        """
        The number of seconds between health probes.Default is 240sec.
        """
        return pulumi.get(self, "probe_interval_in_seconds")

    @property
    @pulumi.getter(name="probePath")
    def probe_path(self) -> Optional[str]:
        """
        The path relative to the origin that is used to determine the health of the origin.
        """
        return pulumi.get(self, "probe_path")

    @property
    @pulumi.getter(name="probeProtocol")
    def probe_protocol(self) -> Optional[str]:
        """
        Protocol to use for health probe.
        """
        return pulumi.get(self, "probe_protocol")

    @property
    @pulumi.getter(name="probeRequestType")
    def probe_request_type(self) -> Optional[str]:
        """
        The type of health probe request that is made.
        """
        return pulumi.get(self, "probe_request_type")


@pulumi.output_type
class HttpErrorRangeParametersResponse(dict):
    """
    The JSON object that represents the range for http status codes
    """
    def __init__(__self__, *,
                 begin: Optional[int] = None,
                 end: Optional[int] = None):
        """
        The JSON object that represents the range for http status codes
        :param int begin: The inclusive start of the http status code range.
        :param int end: The inclusive end of the http status code range.
        """
        if begin is not None:
            pulumi.set(__self__, "begin", begin)
        if end is not None:
            pulumi.set(__self__, "end", end)

    @property
    @pulumi.getter
    def begin(self) -> Optional[int]:
        """
        The inclusive start of the http status code range.
        """
        return pulumi.get(self, "begin")

    @property
    @pulumi.getter
    def end(self) -> Optional[int]:
        """
        The inclusive end of the http status code range.
        """
        return pulumi.get(self, "end")


@pulumi.output_type
class LoadBalancingSettingsParametersResponse(dict):
    """
    Round-Robin load balancing settings for a backend pool
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "additionalLatencyInMilliseconds":
            suggest = "additional_latency_in_milliseconds"
        elif key == "sampleSize":
            suggest = "sample_size"
        elif key == "successfulSamplesRequired":
            suggest = "successful_samples_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoadBalancingSettingsParametersResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoadBalancingSettingsParametersResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoadBalancingSettingsParametersResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 additional_latency_in_milliseconds: Optional[int] = None,
                 sample_size: Optional[int] = None,
                 successful_samples_required: Optional[int] = None):
        """
        Round-Robin load balancing settings for a backend pool
        :param int additional_latency_in_milliseconds: The additional latency in milliseconds for probes to fall into the lowest latency bucket
        :param int sample_size: The number of samples to consider for load balancing decisions
        :param int successful_samples_required: The number of samples within the sample period that must succeed
        """
        if additional_latency_in_milliseconds is not None:
            pulumi.set(__self__, "additional_latency_in_milliseconds", additional_latency_in_milliseconds)
        if sample_size is not None:
            pulumi.set(__self__, "sample_size", sample_size)
        if successful_samples_required is not None:
            pulumi.set(__self__, "successful_samples_required", successful_samples_required)

    @property
    @pulumi.getter(name="additionalLatencyInMilliseconds")
    def additional_latency_in_milliseconds(self) -> Optional[int]:
        """
        The additional latency in milliseconds for probes to fall into the lowest latency bucket
        """
        return pulumi.get(self, "additional_latency_in_milliseconds")

    @property
    @pulumi.getter(name="sampleSize")
    def sample_size(self) -> Optional[int]:
        """
        The number of samples to consider for load balancing decisions
        """
        return pulumi.get(self, "sample_size")

    @property
    @pulumi.getter(name="successfulSamplesRequired")
    def successful_samples_required(self) -> Optional[int]:
        """
        The number of samples within the sample period that must succeed
        """
        return pulumi.get(self, "successful_samples_required")


@pulumi.output_type
class ResourceReferenceResponse(dict):
    """
    Reference to another resource.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None):
        """
        Reference to another resource.
        :param str id: Resource ID.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class ResponseBasedOriginErrorDetectionParametersResponse(dict):
    """
    The JSON object that contains the properties to determine origin health using real requests/responses.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "httpErrorRanges":
            suggest = "http_error_ranges"
        elif key == "responseBasedDetectedErrorTypes":
            suggest = "response_based_detected_error_types"
        elif key == "responseBasedFailoverThresholdPercentage":
            suggest = "response_based_failover_threshold_percentage"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResponseBasedOriginErrorDetectionParametersResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResponseBasedOriginErrorDetectionParametersResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResponseBasedOriginErrorDetectionParametersResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 http_error_ranges: Optional[Sequence['outputs.HttpErrorRangeParametersResponse']] = None,
                 response_based_detected_error_types: Optional[str] = None,
                 response_based_failover_threshold_percentage: Optional[int] = None):
        """
        The JSON object that contains the properties to determine origin health using real requests/responses.
        :param Sequence['HttpErrorRangeParametersResponse'] http_error_ranges: The list of Http status code ranges that are considered as server errors for origin and it is marked as unhealthy.
        :param str response_based_detected_error_types: Type of response errors for real user requests for which origin will be deemed unhealthy
        :param int response_based_failover_threshold_percentage: The percentage of failed requests in the sample where failover should trigger.
        """
        if http_error_ranges is not None:
            pulumi.set(__self__, "http_error_ranges", http_error_ranges)
        if response_based_detected_error_types is not None:
            pulumi.set(__self__, "response_based_detected_error_types", response_based_detected_error_types)
        if response_based_failover_threshold_percentage is not None:
            pulumi.set(__self__, "response_based_failover_threshold_percentage", response_based_failover_threshold_percentage)

    @property
    @pulumi.getter(name="httpErrorRanges")
    def http_error_ranges(self) -> Optional[Sequence['outputs.HttpErrorRangeParametersResponse']]:
        """
        The list of Http status code ranges that are considered as server errors for origin and it is marked as unhealthy.
        """
        return pulumi.get(self, "http_error_ranges")

    @property
    @pulumi.getter(name="responseBasedDetectedErrorTypes")
    def response_based_detected_error_types(self) -> Optional[str]:
        """
        Type of response errors for real user requests for which origin will be deemed unhealthy
        """
        return pulumi.get(self, "response_based_detected_error_types")

    @property
    @pulumi.getter(name="responseBasedFailoverThresholdPercentage")
    def response_based_failover_threshold_percentage(self) -> Optional[int]:
        """
        The percentage of failed requests in the sample where failover should trigger.
        """
        return pulumi.get(self, "response_based_failover_threshold_percentage")


@pulumi.output_type
class SkuResponse(dict):
    """
    The pricing tier (defines a CDN provider, feature list and rate) of the CDN profile.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        The pricing tier (defines a CDN provider, feature list and rate) of the CDN profile.
        :param str name: Name of the pricing tier.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the pricing tier.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Read only system data
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Read only system data
        :param str created_at: The timestamp of resource creation (UTC)
        :param str created_by: An identifier for the identity that created the resource
        :param str created_by_type: The type of identity that created the resource
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: An identifier for the identity that last modified the resource
        :param str last_modified_by_type: The type of identity that last modified the resource
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC)
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        An identifier for the identity that created the resource
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        An identifier for the identity that last modified the resource
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource
        """
        return pulumi.get(self, "last_modified_by_type")


