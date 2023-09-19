"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ClusterTemplate:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ClusterTemplateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ClusterTemplate.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SMALL: _ClusterTemplate.ValueType  # 0
    MEDIUM: _ClusterTemplate.ValueType  # 1
    LARGE: _ClusterTemplate.ValueType  # 2
    XLARGE: _ClusterTemplate.ValueType  # 3
    XXLARGE: _ClusterTemplate.ValueType  # 4
    XXXLARGE: _ClusterTemplate.ValueType  # 5
    NANO: _ClusterTemplate.ValueType  # 6

class ClusterTemplate(_ClusterTemplate, metaclass=_ClusterTemplateEnumTypeWrapper):
    """Templates for clusters the user may choose"""

SMALL: ClusterTemplate.ValueType  # 0
MEDIUM: ClusterTemplate.ValueType  # 1
LARGE: ClusterTemplate.ValueType  # 2
XLARGE: ClusterTemplate.ValueType  # 3
XXLARGE: ClusterTemplate.ValueType  # 4
XXXLARGE: ClusterTemplate.ValueType  # 5
NANO: ClusterTemplate.ValueType  # 6
global___ClusterTemplate = ClusterTemplate

class ExecutionSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_TEMPLATE_FIELD_NUMBER: builtins.int
    RESOURCE_CONFIGURATION_FIELD_NUMBER: builtins.int
    cluster_template: global___ClusterTemplate.ValueType
    @property
    def resource_configuration(self) -> global___ResourceConfiguration: ...
    def __init__(
        self,
        *,
        cluster_template: global___ClusterTemplate.ValueType = ...,
        resource_configuration: global___ResourceConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cluster_template", b"cluster_template", "resource_configuration", b"resource_configuration", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cluster_template", b"cluster_template", "resource_configuration", b"resource_configuration", "spec", b"spec"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["spec", b"spec"]) -> typing_extensions.Literal["cluster_template", "resource_configuration"] | None: ...

global___ExecutionSpec = ExecutionSpec

class StreamingExecutionSpec(google.protobuf.message.Message):
    """Represents the Execution Specification of a streaming FeatureSet"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ONLINE_CLUSTER_TEMPLATE_FIELD_NUMBER: builtins.int
    ONLINE_RESOURCE_CONFIGURATION_FIELD_NUMBER: builtins.int
    OFFLINE_CLUSTER_TEMPLATE_FIELD_NUMBER: builtins.int
    OFFLINE_RESOURCE_CONFIGURATION_FIELD_NUMBER: builtins.int
    online_cluster_template: global___ClusterTemplate.ValueType
    @property
    def online_resource_configuration(self) -> global___ResourceConfiguration: ...
    offline_cluster_template: global___ClusterTemplate.ValueType
    @property
    def offline_resource_configuration(self) -> global___ResourceConfiguration: ...
    def __init__(
        self,
        *,
        online_cluster_template: global___ClusterTemplate.ValueType = ...,
        online_resource_configuration: global___ResourceConfiguration | None = ...,
        offline_cluster_template: global___ClusterTemplate.ValueType = ...,
        offline_resource_configuration: global___ResourceConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["offline_cluster_template", b"offline_cluster_template", "offline_resource_configuration", b"offline_resource_configuration", "offline_resource_spec", b"offline_resource_spec", "online_cluster_template", b"online_cluster_template", "online_resource_configuration", b"online_resource_configuration", "online_resource_spec", b"online_resource_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["offline_cluster_template", b"offline_cluster_template", "offline_resource_configuration", b"offline_resource_configuration", "offline_resource_spec", b"offline_resource_spec", "online_cluster_template", b"online_cluster_template", "online_resource_configuration", b"online_resource_configuration", "online_resource_spec", b"online_resource_spec"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["offline_resource_spec", b"offline_resource_spec"]) -> typing_extensions.Literal["offline_cluster_template", "offline_resource_configuration"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["online_resource_spec", b"online_resource_spec"]) -> typing_extensions.Literal["online_cluster_template", "online_resource_configuration"] | None: ...

global___StreamingExecutionSpec = StreamingExecutionSpec

class BackfillExecutionSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_TEMPLATE_FIELD_NUMBER: builtins.int
    RESOURCE_CONFIGURATION_FIELD_NUMBER: builtins.int
    cluster_template: global___ClusterTemplate.ValueType
    @property
    def resource_configuration(self) -> global___ResourceConfiguration: ...
    def __init__(
        self,
        *,
        cluster_template: global___ClusterTemplate.ValueType = ...,
        resource_configuration: global___ResourceConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["backfill_resource_spec", b"backfill_resource_spec", "cluster_template", b"cluster_template", "resource_configuration", b"resource_configuration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["backfill_resource_spec", b"backfill_resource_spec", "cluster_template", b"cluster_template", "resource_configuration", b"resource_configuration"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["backfill_resource_spec", b"backfill_resource_spec"]) -> typing_extensions.Literal["cluster_template", "resource_configuration"] | None: ...

global___BackfillExecutionSpec = BackfillExecutionSpec

class ResourceConfiguration(google.protobuf.message.Message):
    """user-defined resource configuration, to be applied to a cluster where
    Dynamic Allocation is enabled
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DRIVER_MEMORY_FIELD_NUMBER: builtins.int
    DRIVER_CORES_FIELD_NUMBER: builtins.int
    INITIAL_EXECUTORS_FIELD_NUMBER: builtins.int
    MIN_EXECUTORS_FIELD_NUMBER: builtins.int
    MAX_EXECUTORS_FIELD_NUMBER: builtins.int
    EXECUTOR_MEMORY_FIELD_NUMBER: builtins.int
    EXECUTOR_CORES_FIELD_NUMBER: builtins.int
    driver_memory: builtins.str
    """driver memory, corresponds to "spark.driver.memory" and has the same format"""
    driver_cores: builtins.int
    """driver cores, corresponds to "spark.driver.cores" """
    initial_executors: builtins.int
    """initial executor count, corresponds to "spark.dynamicAllocation.initialExecutors" """
    min_executors: builtins.int
    """min number of executors, corresponds to "spark.dynamicAllocation.minExecutors" """
    max_executors: builtins.int
    """max number of executors, corresponds to "spark.dynamicAllocation.maxExecutors" """
    executor_memory: builtins.str
    """executor memory, corresponds to (and has the same format of) "spark.executor.memory" """
    executor_cores: builtins.int
    """executor cores, corresponds to "spark.executor.cores" """
    def __init__(
        self,
        *,
        driver_memory: builtins.str = ...,
        driver_cores: builtins.int = ...,
        initial_executors: builtins.int = ...,
        min_executors: builtins.int = ...,
        max_executors: builtins.int = ...,
        executor_memory: builtins.str = ...,
        executor_cores: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["driver_cores", b"driver_cores", "driver_memory", b"driver_memory", "executor_cores", b"executor_cores", "executor_memory", b"executor_memory", "initial_executors", b"initial_executors", "max_executors", b"max_executors", "min_executors", b"min_executors"]) -> None: ...

global___ResourceConfiguration = ResourceConfiguration
