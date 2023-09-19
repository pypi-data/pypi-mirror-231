# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .automation_account import *
from .certificate import *
from .connection import *
from .connection_type import *
from .credential import *
from .dsc_configuration import *
from .dsc_node_configuration import *
from .get_automation_account import *
from .get_certificate import *
from .get_connection import *
from .get_connection_type import *
from .get_credential import *
from .get_dsc_configuration import *
from .get_dsc_node_configuration import *
from .get_hybrid_runbook_worker import *
from .get_hybrid_runbook_worker_group import *
from .get_job_schedule import *
from .get_module import *
from .get_private_endpoint_connection import *
from .get_python2_package import *
from .get_python3_package import *
from .get_runbook import *
from .get_schedule import *
from .get_software_update_configuration_by_name import *
from .get_source_control import *
from .get_variable import *
from .get_watcher import *
from .get_webhook import *
from .hybrid_runbook_worker import *
from .hybrid_runbook_worker_group import *
from .job_schedule import *
from .list_key_by_automation_account import *
from .module import *
from .private_endpoint_connection import *
from .python2_package import *
from .python3_package import *
from .runbook import *
from .schedule import *
from .software_update_configuration_by_name import *
from .source_control import *
from .variable import *
from .watcher import *
from .webhook import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.automation.v20151031 as __v20151031
    v20151031 = __v20151031
    import pulumi_azure_native.automation.v20170515preview as __v20170515preview
    v20170515preview = __v20170515preview
    import pulumi_azure_native.automation.v20190601 as __v20190601
    v20190601 = __v20190601
    import pulumi_azure_native.automation.v20200113preview as __v20200113preview
    v20200113preview = __v20200113preview
    import pulumi_azure_native.automation.v20210622 as __v20210622
    v20210622 = __v20210622
    import pulumi_azure_native.automation.v20220808 as __v20220808
    v20220808 = __v20220808
else:
    v20151031 = _utilities.lazy_import('pulumi_azure_native.automation.v20151031')
    v20170515preview = _utilities.lazy_import('pulumi_azure_native.automation.v20170515preview')
    v20190601 = _utilities.lazy_import('pulumi_azure_native.automation.v20190601')
    v20200113preview = _utilities.lazy_import('pulumi_azure_native.automation.v20200113preview')
    v20210622 = _utilities.lazy_import('pulumi_azure_native.automation.v20210622')
    v20220808 = _utilities.lazy_import('pulumi_azure_native.automation.v20220808')

