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

__all__ = [
    'ListGlobalUserEnvironmentsResult',
    'AwaitableListGlobalUserEnvironmentsResult',
    'list_global_user_environments',
    'list_global_user_environments_output',
]

@pulumi.output_type
class ListGlobalUserEnvironmentsResult:
    """
    Represents the list of environments owned by a user
    """
    def __init__(__self__, environments=None):
        if environments and not isinstance(environments, list):
            raise TypeError("Expected argument 'environments' to be a list")
        pulumi.set(__self__, "environments", environments)

    @property
    @pulumi.getter
    def environments(self) -> Optional[Sequence['outputs.EnvironmentDetailsResponse']]:
        """
        List of all the environments
        """
        return pulumi.get(self, "environments")


class AwaitableListGlobalUserEnvironmentsResult(ListGlobalUserEnvironmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListGlobalUserEnvironmentsResult(
            environments=self.environments)


def list_global_user_environments(lab_id: Optional[str] = None,
                                  user_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListGlobalUserEnvironmentsResult:
    """
    List Environments for the user


    :param str lab_id: The resource Id of the lab
    :param str user_name: The name of the user.
    """
    __args__ = dict()
    __args__['labId'] = lab_id
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:labservices/v20181015:listGlobalUserEnvironments', __args__, opts=opts, typ=ListGlobalUserEnvironmentsResult).value

    return AwaitableListGlobalUserEnvironmentsResult(
        environments=pulumi.get(__ret__, 'environments'))


@_utilities.lift_output_func(list_global_user_environments)
def list_global_user_environments_output(lab_id: Optional[pulumi.Input[Optional[str]]] = None,
                                         user_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListGlobalUserEnvironmentsResult]:
    """
    List Environments for the user


    :param str lab_id: The resource Id of the lab
    :param str user_name: The name of the user.
    """
    ...
