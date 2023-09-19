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
    'GetWebAppScmAllowedResult',
    'AwaitableGetWebAppScmAllowedResult',
    'get_web_app_scm_allowed',
    'get_web_app_scm_allowed_output',
]

@pulumi.output_type
class GetWebAppScmAllowedResult:
    """
    Publishing Credentials Policies parameters.
    """
    def __init__(__self__, allow=None, id=None, kind=None, name=None, type=None):
        if allow and not isinstance(allow, bool):
            raise TypeError("Expected argument 'allow' to be a bool")
        pulumi.set(__self__, "allow", allow)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def allow(self) -> bool:
        """
        <code>true</code> to allow access to a publishing method; otherwise, <code>false</code>.
        """
        return pulumi.get(self, "allow")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetWebAppScmAllowedResult(GetWebAppScmAllowedResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAppScmAllowedResult(
            allow=self.allow,
            id=self.id,
            kind=self.kind,
            name=self.name,
            type=self.type)


def get_web_app_scm_allowed(name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAppScmAllowedResult:
    """
    Returns whether Scm basic auth is allowed on the site or not.


    :param str name: Name of the app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20210115:getWebAppScmAllowed', __args__, opts=opts, typ=GetWebAppScmAllowedResult).value

    return AwaitableGetWebAppScmAllowedResult(
        allow=pulumi.get(__ret__, 'allow'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_web_app_scm_allowed)
def get_web_app_scm_allowed_output(name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebAppScmAllowedResult]:
    """
    Returns whether Scm basic auth is allowed on the site or not.


    :param str name: Name of the app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
