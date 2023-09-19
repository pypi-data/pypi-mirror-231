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
    'ListVMHostResult',
    'AwaitableListVMHostResult',
    'list_vm_host',
    'list_vm_host_output',
]

@pulumi.output_type
class ListVMHostResult:
    """
    Response of a list operation.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        Link to the next Vm resource Id, if any.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.VMResourcesResponse']]:
        """
        Results of a list operation.
        """
        return pulumi.get(self, "value")


class AwaitableListVMHostResult(ListVMHostResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListVMHostResult(
            next_link=self.next_link,
            value=self.value)


def list_vm_host(monitor_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListVMHostResult:
    """
    Response of a list operation.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group to which the Elastic resource belongs.
    """
    __args__ = dict()
    __args__['monitorName'] = monitor_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elastic/v20230601:listVMHost', __args__, opts=opts, typ=ListVMHostResult).value

    return AwaitableListVMHostResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_vm_host)
def list_vm_host_output(monitor_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListVMHostResult]:
    """
    Response of a list operation.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group to which the Elastic resource belongs.
    """
    ...
