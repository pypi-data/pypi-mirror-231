# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'ConfigurationParameterArgs',
    'GuestConfigurationAssignmentPropertiesArgs',
    'GuestConfigurationNavigationArgs',
]

@pulumi.input_type
class ConfigurationParameterArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Represents a configuration parameter.
        :param pulumi.Input[str] name: Name of the configuration parameter.
        :param pulumi.Input[str] value: Value of the configuration parameter.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the configuration parameter.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Value of the configuration parameter.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class GuestConfigurationAssignmentPropertiesArgs:
    def __init__(__self__, *,
                 context: Optional[pulumi.Input[str]] = None,
                 guest_configuration: Optional[pulumi.Input['GuestConfigurationNavigationArgs']] = None):
        """
        Guest configuration assignment properties.
        :param pulumi.Input[str] context: The source which initiated the guest configuration assignment. Ex: Azure Policy
        :param pulumi.Input['GuestConfigurationNavigationArgs'] guest_configuration: The guest configuration to assign.
        """
        if context is not None:
            pulumi.set(__self__, "context", context)
        if guest_configuration is not None:
            pulumi.set(__self__, "guest_configuration", guest_configuration)

    @property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[str]]:
        """
        The source which initiated the guest configuration assignment. Ex: Azure Policy
        """
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context", value)

    @property
    @pulumi.getter(name="guestConfiguration")
    def guest_configuration(self) -> Optional[pulumi.Input['GuestConfigurationNavigationArgs']]:
        """
        The guest configuration to assign.
        """
        return pulumi.get(self, "guest_configuration")

    @guest_configuration.setter
    def guest_configuration(self, value: Optional[pulumi.Input['GuestConfigurationNavigationArgs']]):
        pulumi.set(self, "guest_configuration", value)


@pulumi.input_type
class GuestConfigurationNavigationArgs:
    def __init__(__self__, *,
                 assignment_type: Optional[pulumi.Input[Union[str, 'AssignmentType']]] = None,
                 configuration_parameter: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationParameterArgs']]]] = None,
                 configuration_protected_parameter: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationParameterArgs']]]] = None,
                 content_hash: Optional[pulumi.Input[str]] = None,
                 content_uri: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Guest configuration is an artifact that encapsulates DSC configuration and its dependencies. The artifact is a zip file containing DSC configuration (as MOF) and dependent resources and other dependencies like modules.
        :param pulumi.Input[Union[str, 'AssignmentType']] assignment_type: Specifies the assignment type and execution of the configuration. Possible values are Audit, DeployAndAutoCorrect, ApplyAndAutoCorrect and ApplyAndMonitor.
        :param pulumi.Input[Sequence[pulumi.Input['ConfigurationParameterArgs']]] configuration_parameter: The configuration parameters for the guest configuration.
        :param pulumi.Input[Sequence[pulumi.Input['ConfigurationParameterArgs']]] configuration_protected_parameter: The protected configuration parameters for the guest configuration.
        :param pulumi.Input[str] content_hash: Combined hash of the guest configuration package and configuration parameters.
        :param pulumi.Input[str] content_uri: Uri of the storage where guest configuration package is uploaded.
        :param pulumi.Input[Union[str, 'Kind']] kind: Kind of the guest configuration. For example:DSC
        :param pulumi.Input[str] name: Name of the guest configuration.
        :param pulumi.Input[str] version: Version of the guest configuration.
        """
        if assignment_type is not None:
            pulumi.set(__self__, "assignment_type", assignment_type)
        if configuration_parameter is not None:
            pulumi.set(__self__, "configuration_parameter", configuration_parameter)
        if configuration_protected_parameter is not None:
            pulumi.set(__self__, "configuration_protected_parameter", configuration_protected_parameter)
        if content_hash is not None:
            pulumi.set(__self__, "content_hash", content_hash)
        if content_uri is not None:
            pulumi.set(__self__, "content_uri", content_uri)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="assignmentType")
    def assignment_type(self) -> Optional[pulumi.Input[Union[str, 'AssignmentType']]]:
        """
        Specifies the assignment type and execution of the configuration. Possible values are Audit, DeployAndAutoCorrect, ApplyAndAutoCorrect and ApplyAndMonitor.
        """
        return pulumi.get(self, "assignment_type")

    @assignment_type.setter
    def assignment_type(self, value: Optional[pulumi.Input[Union[str, 'AssignmentType']]]):
        pulumi.set(self, "assignment_type", value)

    @property
    @pulumi.getter(name="configurationParameter")
    def configuration_parameter(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationParameterArgs']]]]:
        """
        The configuration parameters for the guest configuration.
        """
        return pulumi.get(self, "configuration_parameter")

    @configuration_parameter.setter
    def configuration_parameter(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationParameterArgs']]]]):
        pulumi.set(self, "configuration_parameter", value)

    @property
    @pulumi.getter(name="configurationProtectedParameter")
    def configuration_protected_parameter(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationParameterArgs']]]]:
        """
        The protected configuration parameters for the guest configuration.
        """
        return pulumi.get(self, "configuration_protected_parameter")

    @configuration_protected_parameter.setter
    def configuration_protected_parameter(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ConfigurationParameterArgs']]]]):
        pulumi.set(self, "configuration_protected_parameter", value)

    @property
    @pulumi.getter(name="contentHash")
    def content_hash(self) -> Optional[pulumi.Input[str]]:
        """
        Combined hash of the guest configuration package and configuration parameters.
        """
        return pulumi.get(self, "content_hash")

    @content_hash.setter
    def content_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_hash", value)

    @property
    @pulumi.getter(name="contentUri")
    def content_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Uri of the storage where guest configuration package is uploaded.
        """
        return pulumi.get(self, "content_uri")

    @content_uri.setter
    def content_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_uri", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'Kind']]]:
        """
        Kind of the guest configuration. For example:DSC
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'Kind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the guest configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Version of the guest configuration.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


