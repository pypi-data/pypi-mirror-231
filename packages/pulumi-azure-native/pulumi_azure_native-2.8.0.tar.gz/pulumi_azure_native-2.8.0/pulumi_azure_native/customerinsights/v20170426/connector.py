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

__all__ = ['ConnectorArgs', 'Connector']

@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *,
                 connector_properties: pulumi.Input[Mapping[str, Any]],
                 connector_type: pulumi.Input[Union[str, 'ConnectorTypes']],
                 hub_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 connector_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_internal: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Connector resource.
        :param pulumi.Input[Mapping[str, Any]] connector_properties: The connector properties.
        :param pulumi.Input[Union[str, 'ConnectorTypes']] connector_type: Type of connector.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] connector_name: Name of the connector.
        :param pulumi.Input[str] description: Description of the connector.
        :param pulumi.Input[str] display_name: Display name of the connector.
        :param pulumi.Input[bool] is_internal: If this is an internal connector.
        """
        pulumi.set(__self__, "connector_properties", connector_properties)
        pulumi.set(__self__, "connector_type", connector_type)
        pulumi.set(__self__, "hub_name", hub_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if connector_name is not None:
            pulumi.set(__self__, "connector_name", connector_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if is_internal is not None:
            pulumi.set(__self__, "is_internal", is_internal)

    @property
    @pulumi.getter(name="connectorProperties")
    def connector_properties(self) -> pulumi.Input[Mapping[str, Any]]:
        """
        The connector properties.
        """
        return pulumi.get(self, "connector_properties")

    @connector_properties.setter
    def connector_properties(self, value: pulumi.Input[Mapping[str, Any]]):
        pulumi.set(self, "connector_properties", value)

    @property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Input[Union[str, 'ConnectorTypes']]:
        """
        Type of connector.
        """
        return pulumi.get(self, "connector_type")

    @connector_type.setter
    def connector_type(self, value: pulumi.Input[Union[str, 'ConnectorTypes']]):
        pulumi.set(self, "connector_type", value)

    @property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[str]:
        """
        The name of the hub.
        """
        return pulumi.get(self, "hub_name")

    @hub_name.setter
    def hub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "hub_name", value)

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
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the connector.
        """
        return pulumi.get(self, "connector_name")

    @connector_name.setter
    def connector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the connector.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the connector.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="isInternal")
    def is_internal(self) -> Optional[pulumi.Input[bool]]:
        """
        If this is an internal connector.
        """
        return pulumi.get(self, "is_internal")

    @is_internal.setter
    def is_internal(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_internal", value)


class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 connector_properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 connector_type: Optional[pulumi.Input[Union[str, 'ConnectorTypes']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 is_internal: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The connector resource format.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connector_name: Name of the connector.
        :param pulumi.Input[Mapping[str, Any]] connector_properties: The connector properties.
        :param pulumi.Input[Union[str, 'ConnectorTypes']] connector_type: Type of connector.
        :param pulumi.Input[str] description: Description of the connector.
        :param pulumi.Input[str] display_name: Display name of the connector.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[bool] is_internal: If this is an internal connector.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The connector resource format.

        :param str resource_name: The name of the resource.
        :param ConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 connector_properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 connector_type: Optional[pulumi.Input[Union[str, 'ConnectorTypes']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 is_internal: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectorArgs.__new__(ConnectorArgs)

            __props__.__dict__["connector_name"] = connector_name
            if connector_properties is None and not opts.urn:
                raise TypeError("Missing required property 'connector_properties'")
            __props__.__dict__["connector_properties"] = connector_properties
            if connector_type is None and not opts.urn:
                raise TypeError("Missing required property 'connector_type'")
            __props__.__dict__["connector_type"] = connector_type
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'hub_name'")
            __props__.__dict__["hub_name"] = hub_name
            __props__.__dict__["is_internal"] = is_internal
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["connector_id"] = None
            __props__.__dict__["created"] = None
            __props__.__dict__["last_modified"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:customerinsights:Connector"), pulumi.Alias(type_="azure-native:customerinsights/v20170101:Connector")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Connector, __self__).__init__(
            'azure-native:customerinsights/v20170426:Connector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Connector':
        """
        Get an existing Connector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectorArgs.__new__(ConnectorArgs)

        __props__.__dict__["connector_id"] = None
        __props__.__dict__["connector_name"] = None
        __props__.__dict__["connector_properties"] = None
        __props__.__dict__["connector_type"] = None
        __props__.__dict__["created"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["is_internal"] = None
        __props__.__dict__["last_modified"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return Connector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> pulumi.Output[int]:
        """
        ID of the connector.
        """
        return pulumi.get(self, "connector_id")

    @property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the connector.
        """
        return pulumi.get(self, "connector_name")

    @property
    @pulumi.getter(name="connectorProperties")
    def connector_properties(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        The connector properties.
        """
        return pulumi.get(self, "connector_properties")

    @property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Output[str]:
        """
        Type of connector.
        """
        return pulumi.get(self, "connector_type")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        The created time.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the connector.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name of the connector.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="isInternal")
    def is_internal(self) -> pulumi.Output[Optional[bool]]:
        """
        If this is an internal connector.
        """
        return pulumi.get(self, "is_internal")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        """
        The last modified time.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of connector.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

