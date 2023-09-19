"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import qwak.traffic.v1.traffic_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ResetAndSetTrafficStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MULTIPLE_HTTP_TRAFFIC_FIELD_NUMBER: builtins.int
    @property
    def multiple_http_traffic(self) -> qwak.traffic.v1.traffic_pb2.MultipleHttpTraffic: ...
    def __init__(
        self,
        *,
        multiple_http_traffic: qwak.traffic.v1.traffic_pb2.MultipleHttpTraffic | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["multiple_http_traffic", b"multiple_http_traffic"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["multiple_http_traffic", b"multiple_http_traffic"]) -> None: ...

global___ResetAndSetTrafficStateRequest = ResetAndSetTrafficStateRequest

class ResetAndSetTrafficStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ResetAndSetTrafficStateResponse = ResetAndSetTrafficStateResponse

class ApplyGroupedTrafficRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MULTIPLE_HTTP_TRAFFIC_FIELD_NUMBER: builtins.int
    GROUP_ID_FIELD_NUMBER: builtins.int
    @property
    def multiple_http_traffic(self) -> qwak.traffic.v1.traffic_pb2.MultipleHttpTraffic: ...
    group_id: builtins.str
    def __init__(
        self,
        *,
        multiple_http_traffic: qwak.traffic.v1.traffic_pb2.MultipleHttpTraffic | None = ...,
        group_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["multiple_http_traffic", b"multiple_http_traffic", "traffic", b"traffic"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["group_id", b"group_id", "multiple_http_traffic", b"multiple_http_traffic", "traffic", b"traffic"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["traffic", b"traffic"]) -> typing_extensions.Literal["multiple_http_traffic"] | None: ...

global___ApplyGroupedTrafficRequest = ApplyGroupedTrafficRequest

class ApplyGroupedTrafficResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ApplyGroupedTrafficResponse = ApplyGroupedTrafficResponse

class CreateEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GROUP_ID_FIELD_NUMBER: builtins.int
    ENDPOINT_FIELD_NUMBER: builtins.int
    VARIATION_FIELD_NUMBER: builtins.int
    HTTP_REQUEST_TIMEOUT_MS_FIELD_NUMBER: builtins.int
    group_id: builtins.str
    endpoint: builtins.str
    variation: builtins.str
    http_request_timeout_ms: builtins.int
    """Http request timeout in ms"""
    def __init__(
        self,
        *,
        group_id: builtins.str = ...,
        endpoint: builtins.str = ...,
        variation: builtins.str = ...,
        http_request_timeout_ms: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["endpoint", b"endpoint", "group_id", b"group_id", "http_request_timeout_ms", b"http_request_timeout_ms", "variation", b"variation"]) -> None: ...

global___CreateEndpointRequest = CreateEndpointRequest

class CreateEndpointResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CreateEndpointResponse = CreateEndpointResponse

class DeleteEndpointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GROUP_ID_FIELD_NUMBER: builtins.int
    group_id: builtins.str
    def __init__(
        self,
        *,
        group_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["group_id", b"group_id"]) -> None: ...

global___DeleteEndpointRequest = DeleteEndpointRequest

class DeleteEndpointResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteEndpointResponse = DeleteEndpointResponse
