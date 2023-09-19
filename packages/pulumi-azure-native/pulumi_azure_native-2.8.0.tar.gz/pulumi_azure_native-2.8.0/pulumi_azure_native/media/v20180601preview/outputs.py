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
    'AkamaiAccessControlResponse',
    'AkamaiSignatureHeaderAuthenticationKeyResponse',
    'CrossSiteAccessPoliciesResponse',
    'IPAccessControlResponse',
    'IPRangeResponse',
    'LiveEventEncodingResponse',
    'LiveEventEndpointResponse',
    'LiveEventInputResponse',
    'LiveEventPreviewAccessControlResponse',
    'LiveEventPreviewResponse',
    'StreamingEndpointAccessControlResponse',
]

@pulumi.output_type
class AkamaiAccessControlResponse(dict):
    """
    Akamai access control
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "akamaiSignatureHeaderAuthenticationKeyList":
            suggest = "akamai_signature_header_authentication_key_list"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AkamaiAccessControlResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AkamaiAccessControlResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AkamaiAccessControlResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 akamai_signature_header_authentication_key_list: Optional[Sequence['outputs.AkamaiSignatureHeaderAuthenticationKeyResponse']] = None):
        """
        Akamai access control
        :param Sequence['AkamaiSignatureHeaderAuthenticationKeyResponse'] akamai_signature_header_authentication_key_list: authentication key list
        """
        if akamai_signature_header_authentication_key_list is not None:
            pulumi.set(__self__, "akamai_signature_header_authentication_key_list", akamai_signature_header_authentication_key_list)

    @property
    @pulumi.getter(name="akamaiSignatureHeaderAuthenticationKeyList")
    def akamai_signature_header_authentication_key_list(self) -> Optional[Sequence['outputs.AkamaiSignatureHeaderAuthenticationKeyResponse']]:
        """
        authentication key list
        """
        return pulumi.get(self, "akamai_signature_header_authentication_key_list")


@pulumi.output_type
class AkamaiSignatureHeaderAuthenticationKeyResponse(dict):
    """
    Akamai Signature Header authentication key.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "base64Key":
            suggest = "base64_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AkamaiSignatureHeaderAuthenticationKeyResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AkamaiSignatureHeaderAuthenticationKeyResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AkamaiSignatureHeaderAuthenticationKeyResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 base64_key: Optional[str] = None,
                 expiration: Optional[str] = None,
                 identifier: Optional[str] = None):
        """
        Akamai Signature Header authentication key.
        :param str base64_key: authentication key
        :param str expiration: The exact time the authentication key.
        :param str identifier: identifier of the key
        """
        if base64_key is not None:
            pulumi.set(__self__, "base64_key", base64_key)
        if expiration is not None:
            pulumi.set(__self__, "expiration", expiration)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)

    @property
    @pulumi.getter(name="base64Key")
    def base64_key(self) -> Optional[str]:
        """
        authentication key
        """
        return pulumi.get(self, "base64_key")

    @property
    @pulumi.getter
    def expiration(self) -> Optional[str]:
        """
        The exact time the authentication key.
        """
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter
    def identifier(self) -> Optional[str]:
        """
        identifier of the key
        """
        return pulumi.get(self, "identifier")


@pulumi.output_type
class CrossSiteAccessPoliciesResponse(dict):
    """
    The client access policy.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientAccessPolicy":
            suggest = "client_access_policy"
        elif key == "crossDomainPolicy":
            suggest = "cross_domain_policy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CrossSiteAccessPoliciesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CrossSiteAccessPoliciesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CrossSiteAccessPoliciesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_access_policy: Optional[str] = None,
                 cross_domain_policy: Optional[str] = None):
        """
        The client access policy.
        :param str client_access_policy: The content of clientaccesspolicy.xml used by Silverlight.
        :param str cross_domain_policy: The content of crossdomain.xml used by Silverlight.
        """
        if client_access_policy is not None:
            pulumi.set(__self__, "client_access_policy", client_access_policy)
        if cross_domain_policy is not None:
            pulumi.set(__self__, "cross_domain_policy", cross_domain_policy)

    @property
    @pulumi.getter(name="clientAccessPolicy")
    def client_access_policy(self) -> Optional[str]:
        """
        The content of clientaccesspolicy.xml used by Silverlight.
        """
        return pulumi.get(self, "client_access_policy")

    @property
    @pulumi.getter(name="crossDomainPolicy")
    def cross_domain_policy(self) -> Optional[str]:
        """
        The content of crossdomain.xml used by Silverlight.
        """
        return pulumi.get(self, "cross_domain_policy")


@pulumi.output_type
class IPAccessControlResponse(dict):
    """
    The IP access control.
    """
    def __init__(__self__, *,
                 allow: Optional[Sequence['outputs.IPRangeResponse']] = None):
        """
        The IP access control.
        :param Sequence['IPRangeResponse'] allow: The IP allow list.
        """
        if allow is not None:
            pulumi.set(__self__, "allow", allow)

    @property
    @pulumi.getter
    def allow(self) -> Optional[Sequence['outputs.IPRangeResponse']]:
        """
        The IP allow list.
        """
        return pulumi.get(self, "allow")


@pulumi.output_type
class IPRangeResponse(dict):
    """
    The IP address range in the CIDR scheme.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetPrefixLength":
            suggest = "subnet_prefix_length"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IPRangeResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IPRangeResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IPRangeResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 address: Optional[str] = None,
                 name: Optional[str] = None,
                 subnet_prefix_length: Optional[int] = None):
        """
        The IP address range in the CIDR scheme.
        :param str address: The IP address.
        :param str name: The friendly name for the IP address range.
        :param int subnet_prefix_length: The subnet mask prefix length (see CIDR notation).
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if subnet_prefix_length is not None:
            pulumi.set(__self__, "subnet_prefix_length", subnet_prefix_length)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        """
        The IP address.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The friendly name for the IP address range.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="subnetPrefixLength")
    def subnet_prefix_length(self) -> Optional[int]:
        """
        The subnet mask prefix length (see CIDR notation).
        """
        return pulumi.get(self, "subnet_prefix_length")


@pulumi.output_type
class LiveEventEncodingResponse(dict):
    """
    The Live Event encoding.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "encodingType":
            suggest = "encoding_type"
        elif key == "presetName":
            suggest = "preset_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LiveEventEncodingResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LiveEventEncodingResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LiveEventEncodingResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 encoding_type: Optional[str] = None,
                 preset_name: Optional[str] = None):
        """
        The Live Event encoding.
        :param str encoding_type: The encoding type for Live Event.
        :param str preset_name: The encoding preset name.
        """
        if encoding_type is not None:
            pulumi.set(__self__, "encoding_type", encoding_type)
        if preset_name is not None:
            pulumi.set(__self__, "preset_name", preset_name)

    @property
    @pulumi.getter(name="encodingType")
    def encoding_type(self) -> Optional[str]:
        """
        The encoding type for Live Event.
        """
        return pulumi.get(self, "encoding_type")

    @property
    @pulumi.getter(name="presetName")
    def preset_name(self) -> Optional[str]:
        """
        The encoding preset name.
        """
        return pulumi.get(self, "preset_name")


@pulumi.output_type
class LiveEventEndpointResponse(dict):
    """
    The Live Event endpoint.
    """
    def __init__(__self__, *,
                 protocol: Optional[str] = None,
                 url: Optional[str] = None):
        """
        The Live Event endpoint.
        :param str protocol: The endpoint protocol.
        :param str url: The endpoint URL.
        """
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        """
        The endpoint protocol.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        The endpoint URL.
        """
        return pulumi.get(self, "url")


@pulumi.output_type
class LiveEventInputResponse(dict):
    """
    The Live Event input.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "streamingProtocol":
            suggest = "streaming_protocol"
        elif key == "accessToken":
            suggest = "access_token"
        elif key == "keyFrameIntervalDuration":
            suggest = "key_frame_interval_duration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LiveEventInputResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LiveEventInputResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LiveEventInputResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 streaming_protocol: str,
                 access_token: Optional[str] = None,
                 endpoints: Optional[Sequence['outputs.LiveEventEndpointResponse']] = None,
                 key_frame_interval_duration: Optional[str] = None):
        """
        The Live Event input.
        :param str streaming_protocol: The streaming protocol for the Live Event.
        :param str access_token: The access token.
        :param Sequence['LiveEventEndpointResponse'] endpoints: The input endpoints for the Live Event.
        :param str key_frame_interval_duration: ISO 8601 timespan duration of the key frame interval duration.
        """
        pulumi.set(__self__, "streaming_protocol", streaming_protocol)
        if access_token is not None:
            pulumi.set(__self__, "access_token", access_token)
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if key_frame_interval_duration is not None:
            pulumi.set(__self__, "key_frame_interval_duration", key_frame_interval_duration)

    @property
    @pulumi.getter(name="streamingProtocol")
    def streaming_protocol(self) -> str:
        """
        The streaming protocol for the Live Event.
        """
        return pulumi.get(self, "streaming_protocol")

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[str]:
        """
        The access token.
        """
        return pulumi.get(self, "access_token")

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence['outputs.LiveEventEndpointResponse']]:
        """
        The input endpoints for the Live Event.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="keyFrameIntervalDuration")
    def key_frame_interval_duration(self) -> Optional[str]:
        """
        ISO 8601 timespan duration of the key frame interval duration.
        """
        return pulumi.get(self, "key_frame_interval_duration")


@pulumi.output_type
class LiveEventPreviewAccessControlResponse(dict):
    """
    The IP access control for Live Event preview.
    """
    def __init__(__self__, *,
                 ip: Optional['outputs.IPAccessControlResponse'] = None):
        """
        The IP access control for Live Event preview.
        :param 'IPAccessControlResponse' ip: The IP access control properties.
        """
        if ip is not None:
            pulumi.set(__self__, "ip", ip)

    @property
    @pulumi.getter
    def ip(self) -> Optional['outputs.IPAccessControlResponse']:
        """
        The IP access control properties.
        """
        return pulumi.get(self, "ip")


@pulumi.output_type
class LiveEventPreviewResponse(dict):
    """
    The Live Event preview.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accessControl":
            suggest = "access_control"
        elif key == "alternativeMediaId":
            suggest = "alternative_media_id"
        elif key == "previewLocator":
            suggest = "preview_locator"
        elif key == "streamingPolicyName":
            suggest = "streaming_policy_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LiveEventPreviewResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LiveEventPreviewResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LiveEventPreviewResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 access_control: Optional['outputs.LiveEventPreviewAccessControlResponse'] = None,
                 alternative_media_id: Optional[str] = None,
                 endpoints: Optional[Sequence['outputs.LiveEventEndpointResponse']] = None,
                 preview_locator: Optional[str] = None,
                 streaming_policy_name: Optional[str] = None):
        """
        The Live Event preview.
        :param 'LiveEventPreviewAccessControlResponse' access_control: The access control for LiveEvent preview.
        :param str alternative_media_id: An Alternative Media Identifier associated with the preview url.  This identifier can be used to distinguish the preview of different live events for authorization purposes in the CustomLicenseAcquisitionUrlTemplate or the CustomKeyAcquisitionUrlTemplate of the StreamingPolicy specified in the StreamingPolicyName field.
        :param Sequence['LiveEventEndpointResponse'] endpoints: The endpoints for preview.
        :param str preview_locator: The preview locator Guid.
        :param str streaming_policy_name: The name of streaming policy used for LiveEvent preview
        """
        if access_control is not None:
            pulumi.set(__self__, "access_control", access_control)
        if alternative_media_id is not None:
            pulumi.set(__self__, "alternative_media_id", alternative_media_id)
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if preview_locator is not None:
            pulumi.set(__self__, "preview_locator", preview_locator)
        if streaming_policy_name is not None:
            pulumi.set(__self__, "streaming_policy_name", streaming_policy_name)

    @property
    @pulumi.getter(name="accessControl")
    def access_control(self) -> Optional['outputs.LiveEventPreviewAccessControlResponse']:
        """
        The access control for LiveEvent preview.
        """
        return pulumi.get(self, "access_control")

    @property
    @pulumi.getter(name="alternativeMediaId")
    def alternative_media_id(self) -> Optional[str]:
        """
        An Alternative Media Identifier associated with the preview url.  This identifier can be used to distinguish the preview of different live events for authorization purposes in the CustomLicenseAcquisitionUrlTemplate or the CustomKeyAcquisitionUrlTemplate of the StreamingPolicy specified in the StreamingPolicyName field.
        """
        return pulumi.get(self, "alternative_media_id")

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence['outputs.LiveEventEndpointResponse']]:
        """
        The endpoints for preview.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="previewLocator")
    def preview_locator(self) -> Optional[str]:
        """
        The preview locator Guid.
        """
        return pulumi.get(self, "preview_locator")

    @property
    @pulumi.getter(name="streamingPolicyName")
    def streaming_policy_name(self) -> Optional[str]:
        """
        The name of streaming policy used for LiveEvent preview
        """
        return pulumi.get(self, "streaming_policy_name")


@pulumi.output_type
class StreamingEndpointAccessControlResponse(dict):
    """
    StreamingEndpoint access control definition.
    """
    def __init__(__self__, *,
                 akamai: Optional['outputs.AkamaiAccessControlResponse'] = None,
                 ip: Optional['outputs.IPAccessControlResponse'] = None):
        """
        StreamingEndpoint access control definition.
        :param 'AkamaiAccessControlResponse' akamai: The access control of Akamai
        :param 'IPAccessControlResponse' ip: The IP access control of the StreamingEndpoint.
        """
        if akamai is not None:
            pulumi.set(__self__, "akamai", akamai)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)

    @property
    @pulumi.getter
    def akamai(self) -> Optional['outputs.AkamaiAccessControlResponse']:
        """
        The access control of Akamai
        """
        return pulumi.get(self, "akamai")

    @property
    @pulumi.getter
    def ip(self) -> Optional['outputs.IPAccessControlResponse']:
        """
        The IP access control of the StreamingEndpoint.
        """
        return pulumi.get(self, "ip")


