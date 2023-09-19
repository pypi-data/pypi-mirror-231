# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AuthType',
    'ClientType',
    'VNetSolutionType',
]


class AuthType(str, Enum):
    """
    The authentication type.
    """
    SYSTEM_ASSIGNED_IDENTITY = "systemAssignedIdentity"
    USER_ASSIGNED_IDENTITY = "userAssignedIdentity"
    SERVICE_PRINCIPAL_SECRET = "servicePrincipalSecret"
    SERVICE_PRINCIPAL_CERTIFICATE = "servicePrincipalCertificate"
    SECRET = "secret"


class ClientType(str, Enum):
    """
    The application client type
    """
    NONE = "none"
    DOTNET = "dotnet"
    JAVA = "java"
    PYTHON = "python"
    GO = "go"
    PHP = "php"
    RUBY = "ruby"
    DJANGO = "django"
    NODEJS = "nodejs"
    SPRING_BOOT = "springBoot"


class VNetSolutionType(str, Enum):
    """
    Type of VNet solution.
    """
    SERVICE_ENDPOINT = "serviceEndpoint"
    PRIVATE_LINK = "privateLink"
