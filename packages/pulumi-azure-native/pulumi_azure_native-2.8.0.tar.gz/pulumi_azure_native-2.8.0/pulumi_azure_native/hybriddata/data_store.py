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

__all__ = ['DataStoreArgs', 'DataStore']

@pulumi.input_type
class DataStoreArgs:
    def __init__(__self__, *,
                 data_manager_name: pulumi.Input[str],
                 data_store_type_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 state: pulumi.Input['State'],
                 customer_secrets: Optional[pulumi.Input[Sequence[pulumi.Input['CustomerSecretArgs']]]] = None,
                 data_store_name: Optional[pulumi.Input[str]] = None,
                 extended_properties: Optional[Any] = None,
                 repository_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataStore resource.
        :param pulumi.Input[str] data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        :param pulumi.Input[str] data_store_type_id: The arm id of the data store type.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name
        :param pulumi.Input['State'] state: State of the data source.
        :param pulumi.Input[Sequence[pulumi.Input['CustomerSecretArgs']]] customer_secrets: List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys.
        :param pulumi.Input[str] data_store_name: The data store/repository name to be created or updated.
        :param Any extended_properties: A generic json used differently by each data source type.
        :param pulumi.Input[str] repository_id: Arm Id for the manager resource to which the data source is associated. This is optional.
        """
        pulumi.set(__self__, "data_manager_name", data_manager_name)
        pulumi.set(__self__, "data_store_type_id", data_store_type_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "state", state)
        if customer_secrets is not None:
            pulumi.set(__self__, "customer_secrets", customer_secrets)
        if data_store_name is not None:
            pulumi.set(__self__, "data_store_name", data_store_name)
        if extended_properties is not None:
            pulumi.set(__self__, "extended_properties", extended_properties)
        if repository_id is not None:
            pulumi.set(__self__, "repository_id", repository_id)

    @property
    @pulumi.getter(name="dataManagerName")
    def data_manager_name(self) -> pulumi.Input[str]:
        """
        The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        """
        return pulumi.get(self, "data_manager_name")

    @data_manager_name.setter
    def data_manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_manager_name", value)

    @property
    @pulumi.getter(name="dataStoreTypeId")
    def data_store_type_id(self) -> pulumi.Input[str]:
        """
        The arm id of the data store type.
        """
        return pulumi.get(self, "data_store_type_id")

    @data_store_type_id.setter
    def data_store_type_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_store_type_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The Resource Group Name
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def state(self) -> pulumi.Input['State']:
        """
        State of the data source.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: pulumi.Input['State']):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="customerSecrets")
    def customer_secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomerSecretArgs']]]]:
        """
        List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys.
        """
        return pulumi.get(self, "customer_secrets")

    @customer_secrets.setter
    def customer_secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomerSecretArgs']]]]):
        pulumi.set(self, "customer_secrets", value)

    @property
    @pulumi.getter(name="dataStoreName")
    def data_store_name(self) -> Optional[pulumi.Input[str]]:
        """
        The data store/repository name to be created or updated.
        """
        return pulumi.get(self, "data_store_name")

    @data_store_name.setter
    def data_store_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_store_name", value)

    @property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[Any]:
        """
        A generic json used differently by each data source type.
        """
        return pulumi.get(self, "extended_properties")

    @extended_properties.setter
    def extended_properties(self, value: Optional[Any]):
        pulumi.set(self, "extended_properties", value)

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> Optional[pulumi.Input[str]]:
        """
        Arm Id for the manager resource to which the data source is associated. This is optional.
        """
        return pulumi.get(self, "repository_id")

    @repository_id.setter
    def repository_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_id", value)


class DataStore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_secrets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomerSecretArgs']]]]] = None,
                 data_manager_name: Optional[pulumi.Input[str]] = None,
                 data_store_name: Optional[pulumi.Input[str]] = None,
                 data_store_type_id: Optional[pulumi.Input[str]] = None,
                 extended_properties: Optional[Any] = None,
                 repository_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['State']] = None,
                 __props__=None):
        """
        Data store.
        Azure REST API version: 2019-06-01. Prior API version in Azure Native 1.x: 2019-06-01

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomerSecretArgs']]]] customer_secrets: List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys.
        :param pulumi.Input[str] data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        :param pulumi.Input[str] data_store_name: The data store/repository name to be created or updated.
        :param pulumi.Input[str] data_store_type_id: The arm id of the data store type.
        :param Any extended_properties: A generic json used differently by each data source type.
        :param pulumi.Input[str] repository_id: Arm Id for the manager resource to which the data source is associated. This is optional.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name
        :param pulumi.Input['State'] state: State of the data source.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataStoreArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Data store.
        Azure REST API version: 2019-06-01. Prior API version in Azure Native 1.x: 2019-06-01

        :param str resource_name: The name of the resource.
        :param DataStoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataStoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_secrets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomerSecretArgs']]]]] = None,
                 data_manager_name: Optional[pulumi.Input[str]] = None,
                 data_store_name: Optional[pulumi.Input[str]] = None,
                 data_store_type_id: Optional[pulumi.Input[str]] = None,
                 extended_properties: Optional[Any] = None,
                 repository_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['State']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataStoreArgs.__new__(DataStoreArgs)

            __props__.__dict__["customer_secrets"] = customer_secrets
            if data_manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_manager_name'")
            __props__.__dict__["data_manager_name"] = data_manager_name
            __props__.__dict__["data_store_name"] = data_store_name
            if data_store_type_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_store_type_id'")
            __props__.__dict__["data_store_type_id"] = data_store_type_id
            __props__.__dict__["extended_properties"] = extended_properties
            __props__.__dict__["repository_id"] = repository_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if state is None and not opts.urn:
                raise TypeError("Missing required property 'state'")
            __props__.__dict__["state"] = state
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hybriddata/v20160601:DataStore"), pulumi.Alias(type_="azure-native:hybriddata/v20190601:DataStore")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DataStore, __self__).__init__(
            'azure-native:hybriddata:DataStore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataStore':
        """
        Get an existing DataStore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataStoreArgs.__new__(DataStoreArgs)

        __props__.__dict__["customer_secrets"] = None
        __props__.__dict__["data_store_type_id"] = None
        __props__.__dict__["extended_properties"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["repository_id"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["type"] = None
        return DataStore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customerSecrets")
    def customer_secrets(self) -> pulumi.Output[Optional[Sequence['outputs.CustomerSecretResponse']]]:
        """
        List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys.
        """
        return pulumi.get(self, "customer_secrets")

    @property
    @pulumi.getter(name="dataStoreTypeId")
    def data_store_type_id(self) -> pulumi.Output[str]:
        """
        The arm id of the data store type.
        """
        return pulumi.get(self, "data_store_type_id")

    @property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> pulumi.Output[Optional[Any]]:
        """
        A generic json used differently by each data source type.
        """
        return pulumi.get(self, "extended_properties")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Output[Optional[str]]:
        """
        Arm Id for the manager resource to which the data source is associated. This is optional.
        """
        return pulumi.get(self, "repository_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the data source.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the object.
        """
        return pulumi.get(self, "type")

