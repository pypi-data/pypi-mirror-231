# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AppServiceCertificateResponse',
    'CertificateDetailsResponse',
    'CertificateOrderContactResponse',
]

@pulumi.output_type
class AppServiceCertificateResponse(dict):
    """
    Key Vault container for a certificate that is purchased through Azure.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "keyVaultId":
            suggest = "key_vault_id"
        elif key == "keyVaultSecretName":
            suggest = "key_vault_secret_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AppServiceCertificateResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AppServiceCertificateResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AppServiceCertificateResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 provisioning_state: str,
                 key_vault_id: Optional[str] = None,
                 key_vault_secret_name: Optional[str] = None):
        """
        Key Vault container for a certificate that is purchased through Azure.
        :param str provisioning_state: Status of the Key Vault secret.
        :param str key_vault_id: Key Vault resource Id.
        :param str key_vault_secret_name: Key Vault secret name.
        """
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if key_vault_id is not None:
            pulumi.set(__self__, "key_vault_id", key_vault_id)
        if key_vault_secret_name is not None:
            pulumi.set(__self__, "key_vault_secret_name", key_vault_secret_name)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Status of the Key Vault secret.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[str]:
        """
        Key Vault resource Id.
        """
        return pulumi.get(self, "key_vault_id")

    @property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> Optional[str]:
        """
        Key Vault secret name.
        """
        return pulumi.get(self, "key_vault_secret_name")


@pulumi.output_type
class CertificateDetailsResponse(dict):
    """
    SSL certificate details.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "notAfter":
            suggest = "not_after"
        elif key == "notBefore":
            suggest = "not_before"
        elif key == "rawData":
            suggest = "raw_data"
        elif key == "serialNumber":
            suggest = "serial_number"
        elif key == "signatureAlgorithm":
            suggest = "signature_algorithm"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CertificateDetailsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CertificateDetailsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CertificateDetailsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 issuer: str,
                 not_after: str,
                 not_before: str,
                 raw_data: str,
                 serial_number: str,
                 signature_algorithm: str,
                 subject: str,
                 thumbprint: str,
                 version: int):
        """
        SSL certificate details.
        :param str issuer: Certificate Issuer.
        :param str not_after: Date Certificate is valid to.
        :param str not_before: Date Certificate is valid from.
        :param str raw_data: Raw certificate data.
        :param str serial_number: Certificate Serial Number.
        :param str signature_algorithm: Certificate Signature algorithm.
        :param str subject: Certificate Subject.
        :param str thumbprint: Certificate Thumbprint.
        :param int version: Certificate Version.
        """
        pulumi.set(__self__, "issuer", issuer)
        pulumi.set(__self__, "not_after", not_after)
        pulumi.set(__self__, "not_before", not_before)
        pulumi.set(__self__, "raw_data", raw_data)
        pulumi.set(__self__, "serial_number", serial_number)
        pulumi.set(__self__, "signature_algorithm", signature_algorithm)
        pulumi.set(__self__, "subject", subject)
        pulumi.set(__self__, "thumbprint", thumbprint)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def issuer(self) -> str:
        """
        Certificate Issuer.
        """
        return pulumi.get(self, "issuer")

    @property
    @pulumi.getter(name="notAfter")
    def not_after(self) -> str:
        """
        Date Certificate is valid to.
        """
        return pulumi.get(self, "not_after")

    @property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> str:
        """
        Date Certificate is valid from.
        """
        return pulumi.get(self, "not_before")

    @property
    @pulumi.getter(name="rawData")
    def raw_data(self) -> str:
        """
        Raw certificate data.
        """
        return pulumi.get(self, "raw_data")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> str:
        """
        Certificate Serial Number.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter(name="signatureAlgorithm")
    def signature_algorithm(self) -> str:
        """
        Certificate Signature algorithm.
        """
        return pulumi.get(self, "signature_algorithm")

    @property
    @pulumi.getter
    def subject(self) -> str:
        """
        Certificate Subject.
        """
        return pulumi.get(self, "subject")

    @property
    @pulumi.getter
    def thumbprint(self) -> str:
        """
        Certificate Thumbprint.
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        Certificate Version.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class CertificateOrderContactResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nameFirst":
            suggest = "name_first"
        elif key == "nameLast":
            suggest = "name_last"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CertificateOrderContactResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CertificateOrderContactResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CertificateOrderContactResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 email: Optional[str] = None,
                 name_first: Optional[str] = None,
                 name_last: Optional[str] = None,
                 phone: Optional[str] = None):
        if email is not None:
            pulumi.set(__self__, "email", email)
        if name_first is not None:
            pulumi.set(__self__, "name_first", name_first)
        if name_last is not None:
            pulumi.set(__self__, "name_last", name_last)
        if phone is not None:
            pulumi.set(__self__, "phone", phone)

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="nameFirst")
    def name_first(self) -> Optional[str]:
        return pulumi.get(self, "name_first")

    @property
    @pulumi.getter(name="nameLast")
    def name_last(self) -> Optional[str]:
        return pulumi.get(self, "name_last")

    @property
    @pulumi.getter
    def phone(self) -> Optional[str]:
        return pulumi.get(self, "phone")


