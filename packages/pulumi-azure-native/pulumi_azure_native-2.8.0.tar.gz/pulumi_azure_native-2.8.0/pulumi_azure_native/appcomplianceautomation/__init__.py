# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from .get_report import *
from .report import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.appcomplianceautomation.v20221116preview as __v20221116preview
    v20221116preview = __v20221116preview
else:
    v20221116preview = _utilities.lazy_import('pulumi_azure_native.appcomplianceautomation.v20221116preview')

