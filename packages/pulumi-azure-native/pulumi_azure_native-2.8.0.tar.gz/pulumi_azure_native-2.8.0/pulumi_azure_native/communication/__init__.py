# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .communication_service import *
from .domain import *
from .email_service import *
from .get_communication_service import *
from .get_domain import *
from .get_email_service import *
from .get_sender_username import *
from .list_communication_service_keys import *
from .sender_username import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.communication.v20220701preview as __v20220701preview
    v20220701preview = __v20220701preview
    import pulumi_azure_native.communication.v20230331 as __v20230331
    v20230331 = __v20230331
    import pulumi_azure_native.communication.v20230401preview as __v20230401preview
    v20230401preview = __v20230401preview
else:
    v20220701preview = _utilities.lazy_import('pulumi_azure_native.communication.v20220701preview')
    v20230331 = _utilities.lazy_import('pulumi_azure_native.communication.v20230331')
    v20230401preview = _utilities.lazy_import('pulumi_azure_native.communication.v20230401preview')

