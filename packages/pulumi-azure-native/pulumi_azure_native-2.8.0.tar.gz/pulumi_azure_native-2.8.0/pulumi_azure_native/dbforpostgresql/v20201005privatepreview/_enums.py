# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CitusVersion',
    'CreateMode',
    'PostgreSQLVersion',
    'ServerEdition',
    'ServerRole',
]


class CitusVersion(str, Enum):
    """
    The Citus version of server group.
    """
    CITUS_VERSION_8_3 = "8.3"
    CITUS_VERSION_9_0 = "9.0"
    CITUS_VERSION_9_1 = "9.1"
    CITUS_VERSION_9_2 = "9.2"
    CITUS_VERSION_9_3 = "9.3"
    CITUS_VERSION_9_4 = "9.4"
    CITUS_VERSION_9_5 = "9.5"


class CreateMode(str, Enum):
    """
    The mode to create a new server group.
    """
    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    READ_REPLICA = "ReadReplica"


class PostgreSQLVersion(str, Enum):
    """
    The PostgreSQL version of server group.
    """
    POSTGRE_SQL_VERSION_11 = "11"
    POSTGRE_SQL_VERSION_12 = "12"


class ServerEdition(str, Enum):
    """
    The edition of a server (default: GeneralPurpose).
    """
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"


class ServerRole(str, Enum):
    """
    The role of servers in the server role group.
    """
    COORDINATOR = "Coordinator"
    WORKER = "Worker"
