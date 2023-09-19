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
    'GetSecurityContactResult',
    'AwaitableGetSecurityContactResult',
    'get_security_contact',
    'get_security_contact_output',
]

@pulumi.output_type
class GetSecurityContactResult:
    """
    Contact details for security issues
    """
    def __init__(__self__, alert_notifications=None, alerts_to_admins=None, email=None, id=None, name=None, phone=None, type=None):
        if alert_notifications and not isinstance(alert_notifications, str):
            raise TypeError("Expected argument 'alert_notifications' to be a str")
        pulumi.set(__self__, "alert_notifications", alert_notifications)
        if alerts_to_admins and not isinstance(alerts_to_admins, str):
            raise TypeError("Expected argument 'alerts_to_admins' to be a str")
        pulumi.set(__self__, "alerts_to_admins", alerts_to_admins)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if phone and not isinstance(phone, str):
            raise TypeError("Expected argument 'phone' to be a str")
        pulumi.set(__self__, "phone", phone)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="alertNotifications")
    def alert_notifications(self) -> str:
        """
        Whether to send security alerts notifications to the security contact
        """
        return pulumi.get(self, "alert_notifications")

    @property
    @pulumi.getter(name="alertsToAdmins")
    def alerts_to_admins(self) -> str:
        """
        Whether to send security alerts notifications to subscription admins
        """
        return pulumi.get(self, "alerts_to_admins")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email of this security contact
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def phone(self) -> Optional[str]:
        """
        The phone number of this security contact
        """
        return pulumi.get(self, "phone")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetSecurityContactResult(GetSecurityContactResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityContactResult(
            alert_notifications=self.alert_notifications,
            alerts_to_admins=self.alerts_to_admins,
            email=self.email,
            id=self.id,
            name=self.name,
            phone=self.phone,
            type=self.type)


def get_security_contact(security_contact_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityContactResult:
    """
    Security contact configurations for the subscription


    :param str security_contact_name: Name of the security contact object
    """
    __args__ = dict()
    __args__['securityContactName'] = security_contact_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security/v20170801preview:getSecurityContact', __args__, opts=opts, typ=GetSecurityContactResult).value

    return AwaitableGetSecurityContactResult(
        alert_notifications=pulumi.get(__ret__, 'alert_notifications'),
        alerts_to_admins=pulumi.get(__ret__, 'alerts_to_admins'),
        email=pulumi.get(__ret__, 'email'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        phone=pulumi.get(__ret__, 'phone'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_security_contact)
def get_security_contact_output(security_contact_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityContactResult]:
    """
    Security contact configurations for the subscription


    :param str security_contact_name: Name of the security contact object
    """
    ...
