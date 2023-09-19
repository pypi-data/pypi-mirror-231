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
    'CustomRPActionRouteDefinitionResponse',
    'CustomRPResourceTypeRouteDefinitionResponse',
    'CustomRPValidationsResponse',
]

@pulumi.output_type
class CustomRPActionRouteDefinitionResponse(dict):
    """
    The route definition for an action implemented by the custom resource provider.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "routingType":
            suggest = "routing_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomRPActionRouteDefinitionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomRPActionRouteDefinitionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomRPActionRouteDefinitionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 endpoint: str,
                 name: str,
                 routing_type: Optional[str] = None):
        """
        The route definition for an action implemented by the custom resource provider.
        :param str endpoint: The route definition endpoint URI that the custom resource provider will proxy requests to. This can be in the form of a flat URI (e.g. 'https://testendpoint/') or can specify to route via a path (e.g. 'https://testendpoint/{requestPath}')
        :param str name: The name of the route definition. This becomes the name for the ARM extension (e.g. '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}')
        :param str routing_type: The routing types that are supported for action requests.
        """
        pulumi.set(__self__, "endpoint", endpoint)
        pulumi.set(__self__, "name", name)
        if routing_type is not None:
            pulumi.set(__self__, "routing_type", routing_type)

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        The route definition endpoint URI that the custom resource provider will proxy requests to. This can be in the form of a flat URI (e.g. 'https://testendpoint/') or can specify to route via a path (e.g. 'https://testendpoint/{requestPath}')
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the route definition. This becomes the name for the ARM extension (e.g. '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}')
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routingType")
    def routing_type(self) -> Optional[str]:
        """
        The routing types that are supported for action requests.
        """
        return pulumi.get(self, "routing_type")


@pulumi.output_type
class CustomRPResourceTypeRouteDefinitionResponse(dict):
    """
    The route definition for a resource implemented by the custom resource provider.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "routingType":
            suggest = "routing_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomRPResourceTypeRouteDefinitionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomRPResourceTypeRouteDefinitionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomRPResourceTypeRouteDefinitionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 endpoint: str,
                 name: str,
                 routing_type: Optional[str] = None):
        """
        The route definition for a resource implemented by the custom resource provider.
        :param str endpoint: The route definition endpoint URI that the custom resource provider will proxy requests to. This can be in the form of a flat URI (e.g. 'https://testendpoint/') or can specify to route via a path (e.g. 'https://testendpoint/{requestPath}')
        :param str name: The name of the route definition. This becomes the name for the ARM extension (e.g. '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}')
        :param str routing_type: The routing types that are supported for resource requests.
        """
        pulumi.set(__self__, "endpoint", endpoint)
        pulumi.set(__self__, "name", name)
        if routing_type is not None:
            pulumi.set(__self__, "routing_type", routing_type)

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        The route definition endpoint URI that the custom resource provider will proxy requests to. This can be in the form of a flat URI (e.g. 'https://testendpoint/') or can specify to route via a path (e.g. 'https://testendpoint/{requestPath}')
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the route definition. This becomes the name for the ARM extension (e.g. '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}')
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routingType")
    def routing_type(self) -> Optional[str]:
        """
        The routing types that are supported for resource requests.
        """
        return pulumi.get(self, "routing_type")


@pulumi.output_type
class CustomRPValidationsResponse(dict):
    """
    A validation to apply on custom resource provider requests.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "validationType":
            suggest = "validation_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomRPValidationsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomRPValidationsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomRPValidationsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 specification: str,
                 validation_type: Optional[str] = None):
        """
        A validation to apply on custom resource provider requests.
        :param str specification: A link to the validation specification. The specification must be hosted on raw.githubusercontent.com.
        :param str validation_type: The type of validation to run against a matching request.
        """
        pulumi.set(__self__, "specification", specification)
        if validation_type is not None:
            pulumi.set(__self__, "validation_type", validation_type)

    @property
    @pulumi.getter
    def specification(self) -> str:
        """
        A link to the validation specification. The specification must be hosted on raw.githubusercontent.com.
        """
        return pulumi.get(self, "specification")

    @property
    @pulumi.getter(name="validationType")
    def validation_type(self) -> Optional[str]:
        """
        The type of validation to run against a matching request.
        """
        return pulumi.get(self, "validation_type")


