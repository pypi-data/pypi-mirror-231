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
    'ListRunLogSasUrlResult',
    'AwaitableListRunLogSasUrlResult',
    'list_run_log_sas_url',
    'list_run_log_sas_url_output',
]

@pulumi.output_type
class ListRunLogSasUrlResult:
    """
    The result of get log link operation.
    """
    def __init__(__self__, log_link=None):
        if log_link and not isinstance(log_link, str):
            raise TypeError("Expected argument 'log_link' to be a str")
        pulumi.set(__self__, "log_link", log_link)

    @property
    @pulumi.getter(name="logLink")
    def log_link(self) -> Optional[str]:
        """
        The link to logs for a run on a azure container registry.
        """
        return pulumi.get(self, "log_link")


class AwaitableListRunLogSasUrlResult(ListRunLogSasUrlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListRunLogSasUrlResult(
            log_link=self.log_link)


def list_run_log_sas_url(registry_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         run_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListRunLogSasUrlResult:
    """
    Gets a link to download the run logs.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    :param str run_id: The run ID.
    """
    __args__ = dict()
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['runId'] = run_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20180901:listRunLogSasUrl', __args__, opts=opts, typ=ListRunLogSasUrlResult).value

    return AwaitableListRunLogSasUrlResult(
        log_link=pulumi.get(__ret__, 'log_link'))


@_utilities.lift_output_func(list_run_log_sas_url)
def list_run_log_sas_url_output(registry_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                run_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListRunLogSasUrlResult]:
    """
    Gets a link to download the run logs.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    :param str run_id: The run ID.
    """
    ...
