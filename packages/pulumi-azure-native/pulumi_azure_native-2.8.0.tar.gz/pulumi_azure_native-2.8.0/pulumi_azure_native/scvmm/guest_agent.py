# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['GuestAgentArgs', 'GuestAgent']

@pulumi.input_type
class GuestAgentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 virtual_machine_name: pulumi.Input[str],
                 credentials: Optional[pulumi.Input['GuestCredentialArgs']] = None,
                 guest_agent_name: Optional[pulumi.Input[str]] = None,
                 http_proxy_config: Optional[pulumi.Input['HttpProxyConfigurationArgs']] = None,
                 provisioning_action: Optional[pulumi.Input[Union[str, 'ProvisioningAction']]] = None):
        """
        The set of arguments for constructing a GuestAgent resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] virtual_machine_name: Name of the vm.
        :param pulumi.Input['GuestCredentialArgs'] credentials: Username / Password Credentials to provision guest agent.
        :param pulumi.Input[str] guest_agent_name: Name of the guestAgents.
        :param pulumi.Input['HttpProxyConfigurationArgs'] http_proxy_config: HTTP Proxy configuration for the VM.
        :param pulumi.Input[Union[str, 'ProvisioningAction']] provisioning_action: Gets or sets the guest agent provisioning action.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_machine_name", virtual_machine_name)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if guest_agent_name is not None:
            pulumi.set(__self__, "guest_agent_name", guest_agent_name)
        if http_proxy_config is not None:
            pulumi.set(__self__, "http_proxy_config", http_proxy_config)
        if provisioning_action is not None:
            pulumi.set(__self__, "provisioning_action", provisioning_action)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualMachineName")
    def virtual_machine_name(self) -> pulumi.Input[str]:
        """
        Name of the vm.
        """
        return pulumi.get(self, "virtual_machine_name")

    @virtual_machine_name.setter
    def virtual_machine_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_machine_name", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['GuestCredentialArgs']]:
        """
        Username / Password Credentials to provision guest agent.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['GuestCredentialArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter(name="guestAgentName")
    def guest_agent_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the guestAgents.
        """
        return pulumi.get(self, "guest_agent_name")

    @guest_agent_name.setter
    def guest_agent_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "guest_agent_name", value)

    @property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(self) -> Optional[pulumi.Input['HttpProxyConfigurationArgs']]:
        """
        HTTP Proxy configuration for the VM.
        """
        return pulumi.get(self, "http_proxy_config")

    @http_proxy_config.setter
    def http_proxy_config(self, value: Optional[pulumi.Input['HttpProxyConfigurationArgs']]):
        pulumi.set(self, "http_proxy_config", value)

    @property
    @pulumi.getter(name="provisioningAction")
    def provisioning_action(self) -> Optional[pulumi.Input[Union[str, 'ProvisioningAction']]]:
        """
        Gets or sets the guest agent provisioning action.
        """
        return pulumi.get(self, "provisioning_action")

    @provisioning_action.setter
    def provisioning_action(self, value: Optional[pulumi.Input[Union[str, 'ProvisioningAction']]]):
        pulumi.set(self, "provisioning_action", value)


class GuestAgent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['GuestCredentialArgs']]] = None,
                 guest_agent_name: Optional[pulumi.Input[str]] = None,
                 http_proxy_config: Optional[pulumi.Input[pulumi.InputType['HttpProxyConfigurationArgs']]] = None,
                 provisioning_action: Optional[pulumi.Input[Union[str, 'ProvisioningAction']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Defines the GuestAgent.
        Azure REST API version: 2022-05-21-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GuestCredentialArgs']] credentials: Username / Password Credentials to provision guest agent.
        :param pulumi.Input[str] guest_agent_name: Name of the guestAgents.
        :param pulumi.Input[pulumi.InputType['HttpProxyConfigurationArgs']] http_proxy_config: HTTP Proxy configuration for the VM.
        :param pulumi.Input[Union[str, 'ProvisioningAction']] provisioning_action: Gets or sets the guest agent provisioning action.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] virtual_machine_name: Name of the vm.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GuestAgentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the GuestAgent.
        Azure REST API version: 2022-05-21-preview.

        :param str resource_name: The name of the resource.
        :param GuestAgentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GuestAgentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['GuestCredentialArgs']]] = None,
                 guest_agent_name: Optional[pulumi.Input[str]] = None,
                 http_proxy_config: Optional[pulumi.Input[pulumi.InputType['HttpProxyConfigurationArgs']]] = None,
                 provisioning_action: Optional[pulumi.Input[Union[str, 'ProvisioningAction']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GuestAgentArgs.__new__(GuestAgentArgs)

            __props__.__dict__["credentials"] = credentials
            __props__.__dict__["guest_agent_name"] = guest_agent_name
            __props__.__dict__["http_proxy_config"] = http_proxy_config
            __props__.__dict__["provisioning_action"] = provisioning_action
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if virtual_machine_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machine_name'")
            __props__.__dict__["virtual_machine_name"] = virtual_machine_name
            __props__.__dict__["custom_resource_name"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["uuid"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:scvmm/v20220521preview:GuestAgent"), pulumi.Alias(type_="azure-native:scvmm/v20230401preview:GuestAgent")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GuestAgent, __self__).__init__(
            'azure-native:scvmm:GuestAgent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GuestAgent':
        """
        Get an existing GuestAgent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GuestAgentArgs.__new__(GuestAgentArgs)

        __props__.__dict__["credentials"] = None
        __props__.__dict__["custom_resource_name"] = None
        __props__.__dict__["http_proxy_config"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_action"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uuid"] = None
        return GuestAgent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional['outputs.GuestCredentialResponse']]:
        """
        Username / Password Credentials to provision guest agent.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> pulumi.Output[str]:
        """
        Gets the name of the corresponding resource in Kubernetes.
        """
        return pulumi.get(self, "custom_resource_name")

    @property
    @pulumi.getter(name="httpProxyConfig")
    def http_proxy_config(self) -> pulumi.Output[Optional['outputs.HttpProxyConfigurationResponse']]:
        """
        HTTP Proxy configuration for the VM.
        """
        return pulumi.get(self, "http_proxy_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningAction")
    def provisioning_action(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the guest agent provisioning action.
        """
        return pulumi.get(self, "provisioning_action")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Gets or sets the guest agent status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        Gets or sets a unique identifier for this resource.
        """
        return pulumi.get(self, "uuid")

