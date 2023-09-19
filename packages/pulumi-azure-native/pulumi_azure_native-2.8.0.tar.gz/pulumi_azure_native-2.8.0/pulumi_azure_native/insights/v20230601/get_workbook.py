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
    'GetWorkbookResult',
    'AwaitableGetWorkbookResult',
    'get_workbook',
    'get_workbook_output',
]

@pulumi.output_type
class GetWorkbookResult:
    """
    A workbook definition.
    """
    def __init__(__self__, category=None, description=None, display_name=None, etag=None, id=None, identity=None, kind=None, location=None, name=None, revision=None, serialized_data=None, source_id=None, storage_uri=None, system_data=None, tags=None, time_modified=None, type=None, user_id=None, version=None):
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if revision and not isinstance(revision, str):
            raise TypeError("Expected argument 'revision' to be a str")
        pulumi.set(__self__, "revision", revision)
        if serialized_data and not isinstance(serialized_data, str):
            raise TypeError("Expected argument 'serialized_data' to be a str")
        pulumi.set(__self__, "serialized_data", serialized_data)
        if source_id and not isinstance(source_id, str):
            raise TypeError("Expected argument 'source_id' to be a str")
        pulumi.set(__self__, "source_id", source_id)
        if storage_uri and not isinstance(storage_uri, str):
            raise TypeError("Expected argument 'storage_uri' to be a str")
        pulumi.set(__self__, "storage_uri", storage_uri)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_modified and not isinstance(time_modified, str):
            raise TypeError("Expected argument 'time_modified' to be a str")
        pulumi.set(__self__, "time_modified", time_modified)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def category(self) -> str:
        """
        Workbook category, as defined by the user at creation time.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the workbook.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-defined name (display name) of the workbook.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Resource etag
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.WorkbookResourceResponseIdentity']:
        """
        Identity used for BYOS
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The kind of workbook. Only valid value is shared.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def revision(self) -> str:
        """
        The unique revision id for this workbook definition
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter(name="serializedData")
    def serialized_data(self) -> str:
        """
        Configuration of this particular workbook. Configuration data is a string containing valid JSON
        """
        return pulumi.get(self, "serialized_data")

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[str]:
        """
        ResourceId for a source resource.
        """
        return pulumi.get(self, "source_id")

    @property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> Optional[str]:
        """
        The resourceId to the storage account when bring your own storage is used
        """
        return pulumi.get(self, "storage_uri")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> str:
        """
        Date and time in UTC of the last modification that was made to this workbook definition.
        """
        return pulumi.get(self, "time_modified")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        Unique user id of the specific user that owns this workbook.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        Workbook schema version format, like 'Notebook/1.0', which should match the workbook in serializedData
        """
        return pulumi.get(self, "version")


class AwaitableGetWorkbookResult(GetWorkbookResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkbookResult(
            category=self.category,
            description=self.description,
            display_name=self.display_name,
            etag=self.etag,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            location=self.location,
            name=self.name,
            revision=self.revision,
            serialized_data=self.serialized_data,
            source_id=self.source_id,
            storage_uri=self.storage_uri,
            system_data=self.system_data,
            tags=self.tags,
            time_modified=self.time_modified,
            type=self.type,
            user_id=self.user_id,
            version=self.version)


def get_workbook(can_fetch_content: Optional[bool] = None,
                 resource_group_name: Optional[str] = None,
                 resource_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkbookResult:
    """
    Get a single workbook by its resourceName.


    :param bool can_fetch_content: Flag indicating whether or not to return the full content for each applicable workbook. If false, only return summary content for workbooks.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the workbook resource. The value must be an UUID.
    """
    __args__ = dict()
    __args__['canFetchContent'] = can_fetch_content
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20230601:getWorkbook', __args__, opts=opts, typ=GetWorkbookResult).value

    return AwaitableGetWorkbookResult(
        category=pulumi.get(__ret__, 'category'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        revision=pulumi.get(__ret__, 'revision'),
        serialized_data=pulumi.get(__ret__, 'serialized_data'),
        source_id=pulumi.get(__ret__, 'source_id'),
        storage_uri=pulumi.get(__ret__, 'storage_uri'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        time_modified=pulumi.get(__ret__, 'time_modified'),
        type=pulumi.get(__ret__, 'type'),
        user_id=pulumi.get(__ret__, 'user_id'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_workbook)
def get_workbook_output(can_fetch_content: Optional[pulumi.Input[Optional[bool]]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        resource_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkbookResult]:
    """
    Get a single workbook by its resourceName.


    :param bool can_fetch_content: Flag indicating whether or not to return the full content for each applicable workbook. If false, only return summary content for workbooks.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the workbook resource. The value must be an UUID.
    """
    ...
