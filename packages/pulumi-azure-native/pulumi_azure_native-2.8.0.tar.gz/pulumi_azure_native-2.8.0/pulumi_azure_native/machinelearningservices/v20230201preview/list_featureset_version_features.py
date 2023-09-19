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
    'ListFeaturesetVersionFeaturesResult',
    'AwaitableListFeaturesetVersionFeaturesResult',
    'list_featureset_version_features',
    'list_featureset_version_features_output',
]

@pulumi.output_type
class ListFeaturesetVersionFeaturesResult:
    """
    A paginated list of Feature entities.
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
        The link to the next page of Feature objects. If null, there are no additional pages.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.FeatureResponse']]:
        """
        An array of objects of type Feature.
        """
        return pulumi.get(self, "value")


class AwaitableListFeaturesetVersionFeaturesResult(ListFeaturesetVersionFeaturesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListFeaturesetVersionFeaturesResult(
            next_link=self.next_link,
            value=self.value)


def list_featureset_version_features(name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     skip: Optional[str] = None,
                                     tags: Optional[str] = None,
                                     version: Optional[str] = None,
                                     workspace_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListFeaturesetVersionFeaturesResult:
    """
    A paginated list of Feature entities.


    :param str name: Featureset name. This is case-sensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str skip: Continuation token for pagination.
    :param str tags: Comma-separated list of tag names (and optionally values). Example: tag1,tag2=value2
    :param str version: Featureset Version identifier. This is case-sensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['skip'] = skip
    __args__['tags'] = tags
    __args__['version'] = version
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20230201preview:listFeaturesetVersionFeatures', __args__, opts=opts, typ=ListFeaturesetVersionFeaturesResult).value

    return AwaitableListFeaturesetVersionFeaturesResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_featureset_version_features)
def list_featureset_version_features_output(name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            skip: Optional[pulumi.Input[Optional[str]]] = None,
                                            tags: Optional[pulumi.Input[Optional[str]]] = None,
                                            version: Optional[pulumi.Input[str]] = None,
                                            workspace_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListFeaturesetVersionFeaturesResult]:
    """
    A paginated list of Feature entities.


    :param str name: Featureset name. This is case-sensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str skip: Continuation token for pagination.
    :param str tags: Comma-separated list of tag names (and optionally values). Example: tag1,tag2=value2
    :param str version: Featureset Version identifier. This is case-sensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
