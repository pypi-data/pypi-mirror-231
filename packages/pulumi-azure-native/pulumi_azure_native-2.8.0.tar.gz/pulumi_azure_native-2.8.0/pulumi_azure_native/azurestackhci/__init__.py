# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .arc_setting import *
from .cluster import *
from .extension import *
from .gallery_image import *
from .get_arc_setting import *
from .get_cluster import *
from .get_extension import *
from .get_gallery_image import *
from .get_guest_agent import *
from .get_hybrid_identity_metadatum import *
from .get_machine_extension import *
from .get_marketplace_gallery_image import *
from .get_network_interface import *
from .get_storage_container import *
from .get_update import *
from .get_update_run import *
from .get_update_summary import *
from .get_virtual_hard_disk import *
from .get_virtual_machine import *
from .get_virtual_machine_instance import *
from .get_virtual_network import *
from .guest_agent import *
from .hybrid_identity_metadatum import *
from .machine_extension import *
from .marketplace_gallery_image import *
from .network_interface import *
from .storage_container import *
from .update import *
from .update_run import *
from .update_summary import *
from .virtual_hard_disk import *
from .virtual_machine import *
from .virtual_machine_instance import *
from .virtual_network import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.azurestackhci.v20210901preview as __v20210901preview
    v20210901preview = __v20210901preview
    import pulumi_azure_native.azurestackhci.v20220101 as __v20220101
    v20220101 = __v20220101
    import pulumi_azure_native.azurestackhci.v20220901 as __v20220901
    v20220901 = __v20220901
    import pulumi_azure_native.azurestackhci.v20221215preview as __v20221215preview
    v20221215preview = __v20221215preview
    import pulumi_azure_native.azurestackhci.v20230301 as __v20230301
    v20230301 = __v20230301
    import pulumi_azure_native.azurestackhci.v20230601 as __v20230601
    v20230601 = __v20230601
    import pulumi_azure_native.azurestackhci.v20230701preview as __v20230701preview
    v20230701preview = __v20230701preview
else:
    v20210901preview = _utilities.lazy_import('pulumi_azure_native.azurestackhci.v20210901preview')
    v20220101 = _utilities.lazy_import('pulumi_azure_native.azurestackhci.v20220101')
    v20220901 = _utilities.lazy_import('pulumi_azure_native.azurestackhci.v20220901')
    v20221215preview = _utilities.lazy_import('pulumi_azure_native.azurestackhci.v20221215preview')
    v20230301 = _utilities.lazy_import('pulumi_azure_native.azurestackhci.v20230301')
    v20230601 = _utilities.lazy_import('pulumi_azure_native.azurestackhci.v20230601')
    v20230701preview = _utilities.lazy_import('pulumi_azure_native.azurestackhci.v20230701preview')

