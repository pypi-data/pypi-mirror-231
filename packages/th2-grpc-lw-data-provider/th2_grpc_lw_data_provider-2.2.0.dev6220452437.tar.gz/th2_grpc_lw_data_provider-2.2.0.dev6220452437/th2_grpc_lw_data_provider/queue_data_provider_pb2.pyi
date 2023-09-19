"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import th2_grpc_lw_data_provider.lw_data_provider_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MessageGroupsQueueSearchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class BookGroups(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        BOOK_ID_FIELD_NUMBER: builtins.int
        GROUP_FIELD_NUMBER: builtins.int
        @property
        def book_id(self) -> th2_grpc_lw_data_provider.lw_data_provider_pb2.BookId: ...
        @property
        def group(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[th2_grpc_lw_data_provider.lw_data_provider_pb2.MessageGroupsSearchRequest.Group]: ...
        def __init__(
            self,
            *,
            book_id: th2_grpc_lw_data_provider.lw_data_provider_pb2.BookId | None = ...,
            group: collections.abc.Iterable[th2_grpc_lw_data_provider.lw_data_provider_pb2.MessageGroupsSearchRequest.Group] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["book_id", b"book_id"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["book_id", b"book_id", "group", b"group"]) -> None: ...

    START_TIMESTAMP_FIELD_NUMBER: builtins.int
    END_TIMESTAMP_FIELD_NUMBER: builtins.int
    MESSAGE_GROUP_FIELD_NUMBER: builtins.int
    SYNC_INTERVAL_FIELD_NUMBER: builtins.int
    EXTERNAL_QUEUE_FIELD_NUMBER: builtins.int
    KEEP_ALIVE_FIELD_NUMBER: builtins.int
    SEND_RAW_DIRECTLY_FIELD_NUMBER: builtins.int
    RAW_ONLY_FIELD_NUMBER: builtins.int
    @property
    def start_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def end_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def message_group(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MessageGroupsQueueSearchRequest.BookGroups]: ...
    @property
    def sync_interval(self) -> google.protobuf.duration_pb2.Duration: ...
    external_queue: builtins.str
    keep_alive: builtins.bool
    send_raw_directly: builtins.bool
    """*
    Enables sending raw batches directly to external_queue. Sends raw directly first then sends raw to pins
    """
    raw_only: builtins.bool
    """*
    If enabled the message won't be sent to codecs
    """
    def __init__(
        self,
        *,
        start_timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        end_timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        message_group: collections.abc.Iterable[global___MessageGroupsQueueSearchRequest.BookGroups] | None = ...,
        sync_interval: google.protobuf.duration_pb2.Duration | None = ...,
        external_queue: builtins.str = ...,
        keep_alive: builtins.bool = ...,
        send_raw_directly: builtins.bool = ...,
        raw_only: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end_timestamp", b"end_timestamp", "start_timestamp", b"start_timestamp", "sync_interval", b"sync_interval"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_timestamp", b"end_timestamp", "external_queue", b"external_queue", "keep_alive", b"keep_alive", "message_group", b"message_group", "raw_only", b"raw_only", "send_raw_directly", b"send_raw_directly", "start_timestamp", b"start_timestamp", "sync_interval", b"sync_interval"]) -> None: ...

global___MessageGroupsQueueSearchRequest = MessageGroupsQueueSearchRequest

@typing_extensions.final
class MessageLoadedStatistic(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class GroupStat(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        BOOK_ID_FIELD_NUMBER: builtins.int
        GROUP_FIELD_NUMBER: builtins.int
        COUNT_FIELD_NUMBER: builtins.int
        @property
        def book_id(self) -> th2_grpc_lw_data_provider.lw_data_provider_pb2.BookId: ...
        @property
        def group(self) -> th2_grpc_lw_data_provider.lw_data_provider_pb2.MessageGroupsSearchRequest.Group: ...
        count: builtins.int
        def __init__(
            self,
            *,
            book_id: th2_grpc_lw_data_provider.lw_data_provider_pb2.BookId | None = ...,
            group: th2_grpc_lw_data_provider.lw_data_provider_pb2.MessageGroupsSearchRequest.Group | None = ...,
            count: builtins.int = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["book_id", b"book_id", "group", b"group"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["book_id", b"book_id", "count", b"count", "group", b"group"]) -> None: ...

    STAT_FIELD_NUMBER: builtins.int
    @property
    def stat(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MessageLoadedStatistic.GroupStat]: ...
    def __init__(
        self,
        *,
        stat: collections.abc.Iterable[global___MessageLoadedStatistic.GroupStat] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["stat", b"stat"]) -> None: ...

global___MessageLoadedStatistic = MessageLoadedStatistic

@typing_extensions.final
class EventQueueSearchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class BookScopes(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        BOOK_ID_FIELD_NUMBER: builtins.int
        SCOPE_FIELD_NUMBER: builtins.int
        @property
        def book_id(self) -> th2_grpc_lw_data_provider.lw_data_provider_pb2.BookId: ...
        @property
        def scope(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[th2_grpc_lw_data_provider.lw_data_provider_pb2.EventScope]: ...
        def __init__(
            self,
            *,
            book_id: th2_grpc_lw_data_provider.lw_data_provider_pb2.BookId | None = ...,
            scope: collections.abc.Iterable[th2_grpc_lw_data_provider.lw_data_provider_pb2.EventScope] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["book_id", b"book_id"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["book_id", b"book_id", "scope", b"scope"]) -> None: ...

    START_TIMESTAMP_FIELD_NUMBER: builtins.int
    END_TIMESTAMP_FIELD_NUMBER: builtins.int
    EVENT_SCOPES_FIELD_NUMBER: builtins.int
    SYNC_INTERVAL_FIELD_NUMBER: builtins.int
    EXTERNAL_QUEUE_FIELD_NUMBER: builtins.int
    KEEP_ALIVE_FIELD_NUMBER: builtins.int
    @property
    def start_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def end_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def event_scopes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EventQueueSearchRequest.BookScopes]: ...
    @property
    def sync_interval(self) -> google.protobuf.duration_pb2.Duration: ...
    external_queue: builtins.str
    keep_alive: builtins.bool
    def __init__(
        self,
        *,
        start_timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        end_timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        event_scopes: collections.abc.Iterable[global___EventQueueSearchRequest.BookScopes] | None = ...,
        sync_interval: google.protobuf.duration_pb2.Duration | None = ...,
        external_queue: builtins.str = ...,
        keep_alive: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end_timestamp", b"end_timestamp", "start_timestamp", b"start_timestamp", "sync_interval", b"sync_interval"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_timestamp", b"end_timestamp", "event_scopes", b"event_scopes", "external_queue", b"external_queue", "keep_alive", b"keep_alive", "start_timestamp", b"start_timestamp", "sync_interval", b"sync_interval"]) -> None: ...

global___EventQueueSearchRequest = EventQueueSearchRequest

@typing_extensions.final
class EventLoadedStatistic(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ScopeStat(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        BOOK_ID_FIELD_NUMBER: builtins.int
        SCOPE_FIELD_NUMBER: builtins.int
        COUNT_FIELD_NUMBER: builtins.int
        @property
        def book_id(self) -> th2_grpc_lw_data_provider.lw_data_provider_pb2.BookId: ...
        @property
        def scope(self) -> th2_grpc_lw_data_provider.lw_data_provider_pb2.EventScope: ...
        count: builtins.int
        def __init__(
            self,
            *,
            book_id: th2_grpc_lw_data_provider.lw_data_provider_pb2.BookId | None = ...,
            scope: th2_grpc_lw_data_provider.lw_data_provider_pb2.EventScope | None = ...,
            count: builtins.int = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["book_id", b"book_id", "scope", b"scope"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["book_id", b"book_id", "count", b"count", "scope", b"scope"]) -> None: ...

    STAT_FIELD_NUMBER: builtins.int
    @property
    def stat(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EventLoadedStatistic.ScopeStat]: ...
    def __init__(
        self,
        *,
        stat: collections.abc.Iterable[global___EventLoadedStatistic.ScopeStat] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["stat", b"stat"]) -> None: ...

global___EventLoadedStatistic = EventLoadedStatistic
