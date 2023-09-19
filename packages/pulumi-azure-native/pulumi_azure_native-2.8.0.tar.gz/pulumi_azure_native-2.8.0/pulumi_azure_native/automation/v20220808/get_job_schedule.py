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
    'GetJobScheduleResult',
    'AwaitableGetJobScheduleResult',
    'get_job_schedule',
    'get_job_schedule_output',
]

@pulumi.output_type
class GetJobScheduleResult:
    """
    Definition of the job schedule.
    """
    def __init__(__self__, id=None, job_schedule_id=None, name=None, parameters=None, run_on=None, runbook=None, schedule=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if job_schedule_id and not isinstance(job_schedule_id, str):
            raise TypeError("Expected argument 'job_schedule_id' to be a str")
        pulumi.set(__self__, "job_schedule_id", job_schedule_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if run_on and not isinstance(run_on, str):
            raise TypeError("Expected argument 'run_on' to be a str")
        pulumi.set(__self__, "run_on", run_on)
        if runbook and not isinstance(runbook, dict):
            raise TypeError("Expected argument 'runbook' to be a dict")
        pulumi.set(__self__, "runbook", runbook)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Gets the id of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="jobScheduleId")
    def job_schedule_id(self) -> Optional[str]:
        """
        Gets or sets the id of job schedule.
        """
        return pulumi.get(self, "job_schedule_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the name of the variable.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, str]]:
        """
        Gets or sets the parameters of the job schedule.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="runOn")
    def run_on(self) -> Optional[str]:
        """
        Gets or sets the hybrid worker group that the scheduled job should run on.
        """
        return pulumi.get(self, "run_on")

    @property
    @pulumi.getter
    def runbook(self) -> Optional['outputs.RunbookAssociationPropertyResponse']:
        """
        Gets or sets the runbook.
        """
        return pulumi.get(self, "runbook")

    @property
    @pulumi.getter
    def schedule(self) -> Optional['outputs.ScheduleAssociationPropertyResponse']:
        """
        Gets or sets the schedule.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetJobScheduleResult(GetJobScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetJobScheduleResult(
            id=self.id,
            job_schedule_id=self.job_schedule_id,
            name=self.name,
            parameters=self.parameters,
            run_on=self.run_on,
            runbook=self.runbook,
            schedule=self.schedule,
            type=self.type)


def get_job_schedule(automation_account_name: Optional[str] = None,
                     job_schedule_id: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetJobScheduleResult:
    """
    Retrieve the job schedule identified by job schedule name.


    :param str automation_account_name: The name of the automation account.
    :param str job_schedule_id: The job schedule name.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    __args__ = dict()
    __args__['automationAccountName'] = automation_account_name
    __args__['jobScheduleId'] = job_schedule_id
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:automation/v20220808:getJobSchedule', __args__, opts=opts, typ=GetJobScheduleResult).value

    return AwaitableGetJobScheduleResult(
        id=pulumi.get(__ret__, 'id'),
        job_schedule_id=pulumi.get(__ret__, 'job_schedule_id'),
        name=pulumi.get(__ret__, 'name'),
        parameters=pulumi.get(__ret__, 'parameters'),
        run_on=pulumi.get(__ret__, 'run_on'),
        runbook=pulumi.get(__ret__, 'runbook'),
        schedule=pulumi.get(__ret__, 'schedule'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_job_schedule)
def get_job_schedule_output(automation_account_name: Optional[pulumi.Input[str]] = None,
                            job_schedule_id: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetJobScheduleResult]:
    """
    Retrieve the job schedule identified by job schedule name.


    :param str automation_account_name: The name of the automation account.
    :param str job_schedule_id: The job schedule name.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    ...
