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
    'GetMongoDBResourceMongoRoleDefinitionResult',
    'AwaitableGetMongoDBResourceMongoRoleDefinitionResult',
    'get_mongo_db_resource_mongo_role_definition',
    'get_mongo_db_resource_mongo_role_definition_output',
]

@pulumi.output_type
class GetMongoDBResourceMongoRoleDefinitionResult:
    """
    An Azure Cosmos DB Mongo Role Definition.
    """
    def __init__(__self__, database_name=None, id=None, name=None, privileges=None, role_name=None, roles=None, type=None):
        if database_name and not isinstance(database_name, str):
            raise TypeError("Expected argument 'database_name' to be a str")
        pulumi.set(__self__, "database_name", database_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if privileges and not isinstance(privileges, list):
            raise TypeError("Expected argument 'privileges' to be a list")
        pulumi.set(__self__, "privileges", privileges)
        if role_name and not isinstance(role_name, str):
            raise TypeError("Expected argument 'role_name' to be a str")
        pulumi.set(__self__, "role_name", role_name)
        if roles and not isinstance(roles, list):
            raise TypeError("Expected argument 'roles' to be a list")
        pulumi.set(__self__, "roles", roles)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[str]:
        """
        The database name for which access is being granted for this Role Definition.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique resource identifier of the database account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the database account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def privileges(self) -> Optional[Sequence['outputs.PrivilegeResponse']]:
        """
        A set of privileges contained by the Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Scopes higher than Database are not enforceable as privilege.
        """
        return pulumi.get(self, "privileges")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[str]:
        """
        A user-friendly name for the Role Definition. Must be unique for the database account.
        """
        return pulumi.get(self, "role_name")

    @property
    @pulumi.getter
    def roles(self) -> Optional[Sequence['outputs.RoleResponse']]:
        """
        The set of roles inherited by this Role Definition.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetMongoDBResourceMongoRoleDefinitionResult(GetMongoDBResourceMongoRoleDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMongoDBResourceMongoRoleDefinitionResult(
            database_name=self.database_name,
            id=self.id,
            name=self.name,
            privileges=self.privileges,
            role_name=self.role_name,
            roles=self.roles,
            type=self.type)


def get_mongo_db_resource_mongo_role_definition(account_name: Optional[str] = None,
                                                mongo_role_definition_id: Optional[str] = None,
                                                resource_group_name: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMongoDBResourceMongoRoleDefinitionResult:
    """
    Retrieves the properties of an existing Azure Cosmos DB Mongo Role Definition with the given Id.


    :param str account_name: Cosmos DB database account name.
    :param str mongo_role_definition_id: The ID for the Role Definition {dbName.roleName}.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['mongoRoleDefinitionId'] = mongo_role_definition_id
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb/v20230415:getMongoDBResourceMongoRoleDefinition', __args__, opts=opts, typ=GetMongoDBResourceMongoRoleDefinitionResult).value

    return AwaitableGetMongoDBResourceMongoRoleDefinitionResult(
        database_name=pulumi.get(__ret__, 'database_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        privileges=pulumi.get(__ret__, 'privileges'),
        role_name=pulumi.get(__ret__, 'role_name'),
        roles=pulumi.get(__ret__, 'roles'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_mongo_db_resource_mongo_role_definition)
def get_mongo_db_resource_mongo_role_definition_output(account_name: Optional[pulumi.Input[str]] = None,
                                                       mongo_role_definition_id: Optional[pulumi.Input[str]] = None,
                                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMongoDBResourceMongoRoleDefinitionResult]:
    """
    Retrieves the properties of an existing Azure Cosmos DB Mongo Role Definition with the given Id.


    :param str account_name: Cosmos DB database account name.
    :param str mongo_role_definition_id: The ID for the Role Definition {dbName.roleName}.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
