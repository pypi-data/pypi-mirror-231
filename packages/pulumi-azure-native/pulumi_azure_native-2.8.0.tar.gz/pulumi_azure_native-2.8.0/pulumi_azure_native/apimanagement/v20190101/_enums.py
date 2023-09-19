# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AlwaysLog',
    'HttpCorrelationProtocol',
    'IdentityProviderType',
    'SamplingType',
    'SubscriptionState',
    'Verbosity',
]


class AlwaysLog(str, Enum):
    """
    Specifies for what type of messages sampling settings should not apply.
    """
    ALL_ERRORS = "allErrors"
    """
    Always log all erroneous request regardless of sampling settings.
    """


class HttpCorrelationProtocol(str, Enum):
    """
    Sets correlation protocol to use for Application Insights diagnostics.
    """
    NONE = "None"
    """
    Do not read and inject correlation headers.
    """
    LEGACY = "Legacy"
    """
    Inject Request-Id and Request-Context headers with request correlation data. See https://github.com/dotnet/corefx/blob/master/src/System.Diagnostics.DiagnosticSource/src/HttpCorrelationProtocol.md.
    """
    W3_C = "W3C"
    """
    Inject Trace Context headers. See https://w3c.github.io/trace-context.
    """


class IdentityProviderType(str, Enum):
    """
    Identity Provider Type identifier.
    """
    FACEBOOK = "facebook"
    """
    Facebook as Identity provider.
    """
    GOOGLE = "google"
    """
    Google as Identity provider.
    """
    MICROSOFT = "microsoft"
    """
    Microsoft Live as Identity provider.
    """
    TWITTER = "twitter"
    """
    Twitter as Identity provider.
    """
    AAD = "aad"
    """
    Azure Active Directory as Identity provider.
    """
    AAD_B2_C = "aadB2C"
    """
    Azure Active Directory B2C as Identity provider.
    """


class SamplingType(str, Enum):
    """
    Sampling type.
    """
    FIXED = "fixed"
    """
    Fixed-rate sampling.
    """


class SubscriptionState(str, Enum):
    """
    Initial subscription state. If no value is specified, subscription is created with Submitted state. Possible states are * active – the subscription is active, * suspended – the subscription is blocked, and the subscriber cannot call any APIs of the product, * submitted – the subscription request has been made by the developer, but has not yet been approved or rejected, * rejected – the subscription request has been denied by an administrator, * cancelled – the subscription has been cancelled by the developer or administrator, * expired – the subscription reached its expiration date and was deactivated.
    """
    SUSPENDED = "suspended"
    ACTIVE = "active"
    EXPIRED = "expired"
    SUBMITTED = "submitted"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class Verbosity(str, Enum):
    """
    The verbosity level applied to traces emitted by trace policies.
    """
    VERBOSE = "verbose"
    """
    All the traces emitted by trace policies will be sent to the logger attached to this diagnostic instance.
    """
    INFORMATION = "information"
    """
    Traces with 'severity' set to 'information' and 'error' will be sent to the logger attached to this diagnostic instance.
    """
    ERROR = "error"
    """
    Only traces with 'severity' set to 'error' will be sent to the logger attached to this diagnostic instance.
    """
