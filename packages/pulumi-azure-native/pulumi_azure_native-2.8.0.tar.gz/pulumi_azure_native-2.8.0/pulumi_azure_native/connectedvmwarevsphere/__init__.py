# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .cluster import *
from .datastore import *
from .get_cluster import *
from .get_datastore import *
from .get_guest_agent import *
from .get_host import *
from .get_hybrid_identity_metadatum import *
from .get_inventory_item import *
from .get_machine_extension import *
from .get_resource_pool import *
from .get_v_center import *
from .get_virtual_machine import *
from .get_virtual_machine_instance import *
from .get_virtual_machine_template import *
from .get_virtual_network import *
from .get_vm_instance_guest_agent import *
from .guest_agent import *
from .host import *
from .hybrid_identity_metadatum import *
from .inventory_item import *
from .machine_extension import *
from .resource_pool import *
from .v_center import *
from .virtual_machine import *
from .virtual_machine_instance import *
from .virtual_machine_template import *
from .virtual_network import *
from .vm_instance_guest_agent import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.connectedvmwarevsphere.v20220110preview as __v20220110preview
    v20220110preview = __v20220110preview
    import pulumi_azure_native.connectedvmwarevsphere.v20220715preview as __v20220715preview
    v20220715preview = __v20220715preview
    import pulumi_azure_native.connectedvmwarevsphere.v20230301preview as __v20230301preview
    v20230301preview = __v20230301preview
else:
    v20220110preview = _utilities.lazy_import('pulumi_azure_native.connectedvmwarevsphere.v20220110preview')
    v20220715preview = _utilities.lazy_import('pulumi_azure_native.connectedvmwarevsphere.v20220715preview')
    v20230301preview = _utilities.lazy_import('pulumi_azure_native.connectedvmwarevsphere.v20230301preview')

