# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'WebTestKind',
    'WebTestKindEnum',
]


class WebTestKind(str, Enum):
    """
    The kind of WebTest that this web test watches. Choices are ping and multistep.
    """
    PING = "ping"
    MULTISTEP = "multistep"


class WebTestKindEnum(str, Enum):
    """
    The kind of web test this is, valid choices are ping, multistep, basic, and standard.
    """
    PING = "ping"
    MULTISTEP = "multistep"
    BASIC = "basic"
    STANDARD = "standard"
