# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .disk_pool import *
from .get_disk_pool import *
from .get_iscsi_target import *
from .iscsi_target import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.storagepool.v20200315preview as __v20200315preview
    v20200315preview = __v20200315preview
    import pulumi_azure_native.storagepool.v20210801 as __v20210801
    v20210801 = __v20210801
else:
    v20200315preview = _utilities.lazy_import('pulumi_azure_native.storagepool.v20200315preview')
    v20210801 = _utilities.lazy_import('pulumi_azure_native.storagepool.v20210801')

