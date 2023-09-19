# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/feature_store/features/feature_set.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from _qwak_proto.qwak.feature_store.features import feature_set_types_pb2 as qwak_dot_feature__store_dot_features_dot_feature__set__types__pb2
from _qwak_proto.qwak.feature_store.entities import entity_pb2 as qwak_dot_feature__store_dot_entities_dot_entity__pb2
from _qwak_proto.qwak.feature_store.features import feature_set_state_pb2 as qwak_dot_feature__store_dot_features_dot_feature__set__state__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-qwak/feature_store/features/feature_set.proto\x12\x1bqwak.feature.store.features\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x33qwak/feature_store/features/feature_set_types.proto\x1a(qwak/feature_store/entities/entity.proto\x1a\x33qwak/feature_store/features/feature_set_state.proto\"\xfc\x01\n\nFeatureSet\x12Q\n\x16\x66\x65\x61ture_set_definition\x18\x01 \x01(\x0b\x32\x31.qwak.feature.store.features.FeatureSetDefinition\x12\x41\n\x08metadata\x18\x02 \x01(\x0b\x32/.qwak.feature.store.features.FeatureSetMetadata\x12X\n\x1b\x64\x65ployed_models_in_use_link\x18\x03 \x03(\x0b\x32\x33.qwak.feature.store.features.DeployedModelInUseLink\"\xde\x03\n\x14\x46\x65\x61tureSetDefinition\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x01 \x01(\t\x12\x45\n\x10\x66\x65\x61ture_set_spec\x18\x02 \x01(\x0b\x32+.qwak.feature.store.features.FeatureSetSpec\x12:\n\x06status\x18\x03 \x01(\x0e\x32*.qwak.feature.store.features.FeatureStatus\x12\x63\n feature_set_last_execution_state\x18\x04 \x01(\x0e\x32\x39.qwak.feature.store.features.FeatureSetLastExecutionState\x12Q\n\x0e\x66\x65\x61ture_health\x18\x05 \x01(\x0e\x32\x39.qwak.feature.store.features.FeatureSetLastExecutionState\x12G\n\x11\x66\x65\x61ture_set_state\x18\x06 \x03(\x0b\x32,.qwak.feature.store.features.FeatureSetState\x12*\n\x1eqwak_internal_protocol_version\x18\x07 \x01(\x05\x42\x02\x18\x01\"\xe3\x02\n\x0e\x46\x65\x61tureSetSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x45\n\x08metadata\x18\x02 \x01(\x0b\x32\x33.qwak.feature.store.features.FeatureSetUserMetadata\x12\x12\n\ngit_commit\x18\x03 \x01(\t\x12=\n\x06\x65ntity\x18\x04 \x01(\x0b\x32-.qwak.feature.store.entities.EntityDefinition\x12\x45\n\x10\x66\x65\x61ture_set_type\x18\x05 \x01(\x0b\x32+.qwak.feature.store.features.FeatureSetType\x12\x36\n\x08\x66\x65\x61tures\x18\x06 \x03(\x0b\x32$.qwak.feature.store.features.Feature\x12*\n\x1eqwak_internal_protocol_version\x18\x07 \x01(\x05\x42\x02\x18\x01\"R\n\x16\x46\x65\x61tureSetUserMetadata\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\"\xa8\x01\n\x12\x46\x65\x61tureSetMetadata\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12\x34\n\x10last_modified_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10last_modified_by\x18\x04 \x01(\t\">\n\x16\x44\x65ployedModelInUseLink\x12\x10\n\x08model_id\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\"5\n\x07\x46\x65\x61ture\x12\x14\n\x0c\x66\x65\x61ture_name\x18\x01 \x01(\t\x12\x14\n\x0c\x66\x65\x61ture_type\x18\x02 \x01(\t\"\x8b\x01\n\x16\x44\x65ployedFeatureSetSpec\x12\x45\n\x10\x66\x65\x61ture_set_spec\x18\x01 \x01(\x0b\x32+.qwak.feature.store.features.FeatureSetSpec\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x02 \x01(\t\x12\x12\n\naccount_id\x18\x03 \x01(\t*\xb4\x01\n\rFeatureStatus\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05VALID\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x12\x17\n\x13REGISTRATION_FAILED\x10\x03\x12\x1c\n\x18REGISTRATION_IN_PROGRESS\x10\x04\x12\x18\n\x14\x44\x45LETION_IN_PROGRESS\x10\x05\x12\x13\n\x0f\x44\x45LETION_FAILED\x10\x06\x12\x18\n\x14\x42\x41\x43KFILL_IN_PROGRESS\x10\x07*\x92\x01\n\x19\x46\x65\x61turesetSchedulingState\x12\x1c\n\x18SCHEDULING_STATE_INVALID\x10\x00\x12\x1c\n\x18SCHEDULING_STATE_ENABLED\x10\x01\x12\x1b\n\x17SCHEDULING_STATE_PAUSED\x10\x02\x12\x1c\n\x18SCHEDULING_STATE_UNKNOWN\x10\x03\x42[\n&com.qwak.ai.feature.store.features.apiP\x01Z/qwak/featurestore/features;featurestorefeaturesb\x06proto3')

_FEATURESTATUS = DESCRIPTOR.enum_types_by_name['FeatureStatus']
FeatureStatus = enum_type_wrapper.EnumTypeWrapper(_FEATURESTATUS)
_FEATURESETSCHEDULINGSTATE = DESCRIPTOR.enum_types_by_name['FeaturesetSchedulingState']
FeaturesetSchedulingState = enum_type_wrapper.EnumTypeWrapper(_FEATURESETSCHEDULINGSTATE)
INVALID = 0
VALID = 1
DELETED = 2
REGISTRATION_FAILED = 3
REGISTRATION_IN_PROGRESS = 4
DELETION_IN_PROGRESS = 5
DELETION_FAILED = 6
BACKFILL_IN_PROGRESS = 7
SCHEDULING_STATE_INVALID = 0
SCHEDULING_STATE_ENABLED = 1
SCHEDULING_STATE_PAUSED = 2
SCHEDULING_STATE_UNKNOWN = 3


_FEATURESET = DESCRIPTOR.message_types_by_name['FeatureSet']
_FEATURESETDEFINITION = DESCRIPTOR.message_types_by_name['FeatureSetDefinition']
_FEATURESETSPEC = DESCRIPTOR.message_types_by_name['FeatureSetSpec']
_FEATURESETUSERMETADATA = DESCRIPTOR.message_types_by_name['FeatureSetUserMetadata']
_FEATURESETMETADATA = DESCRIPTOR.message_types_by_name['FeatureSetMetadata']
_DEPLOYEDMODELINUSELINK = DESCRIPTOR.message_types_by_name['DeployedModelInUseLink']
_FEATURE = DESCRIPTOR.message_types_by_name['Feature']
_DEPLOYEDFEATURESETSPEC = DESCRIPTOR.message_types_by_name['DeployedFeatureSetSpec']
FeatureSet = _reflection.GeneratedProtocolMessageType('FeatureSet', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESET,
  '__module__' : 'qwak.feature_store.features.feature_set_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.FeatureSet)
  })
_sym_db.RegisterMessage(FeatureSet)

FeatureSetDefinition = _reflection.GeneratedProtocolMessageType('FeatureSetDefinition', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESETDEFINITION,
  '__module__' : 'qwak.feature_store.features.feature_set_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.FeatureSetDefinition)
  })
_sym_db.RegisterMessage(FeatureSetDefinition)

FeatureSetSpec = _reflection.GeneratedProtocolMessageType('FeatureSetSpec', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESETSPEC,
  '__module__' : 'qwak.feature_store.features.feature_set_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.FeatureSetSpec)
  })
_sym_db.RegisterMessage(FeatureSetSpec)

FeatureSetUserMetadata = _reflection.GeneratedProtocolMessageType('FeatureSetUserMetadata', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESETUSERMETADATA,
  '__module__' : 'qwak.feature_store.features.feature_set_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.FeatureSetUserMetadata)
  })
_sym_db.RegisterMessage(FeatureSetUserMetadata)

FeatureSetMetadata = _reflection.GeneratedProtocolMessageType('FeatureSetMetadata', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESETMETADATA,
  '__module__' : 'qwak.feature_store.features.feature_set_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.FeatureSetMetadata)
  })
_sym_db.RegisterMessage(FeatureSetMetadata)

DeployedModelInUseLink = _reflection.GeneratedProtocolMessageType('DeployedModelInUseLink', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYEDMODELINUSELINK,
  '__module__' : 'qwak.feature_store.features.feature_set_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.DeployedModelInUseLink)
  })
_sym_db.RegisterMessage(DeployedModelInUseLink)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
  'DESCRIPTOR' : _FEATURE,
  '__module__' : 'qwak.feature_store.features.feature_set_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.Feature)
  })
_sym_db.RegisterMessage(Feature)

DeployedFeatureSetSpec = _reflection.GeneratedProtocolMessageType('DeployedFeatureSetSpec', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYEDFEATURESETSPEC,
  '__module__' : 'qwak.feature_store.features.feature_set_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.features.DeployedFeatureSetSpec)
  })
_sym_db.RegisterMessage(DeployedFeatureSetSpec)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&com.qwak.ai.feature.store.features.apiP\001Z/qwak/featurestore/features;featurestorefeatures'
  _FEATURESETDEFINITION.fields_by_name['qwak_internal_protocol_version']._options = None
  _FEATURESETDEFINITION.fields_by_name['qwak_internal_protocol_version']._serialized_options = b'\030\001'
  _FEATURESETSPEC.fields_by_name['qwak_internal_protocol_version']._options = None
  _FEATURESETSPEC.fields_by_name['qwak_internal_protocol_version']._serialized_options = b'\030\001'
  _FEATURESTATUS._serialized_start=1870
  _FEATURESTATUS._serialized_end=2050
  _FEATURESETSCHEDULINGSTATE._serialized_start=2053
  _FEATURESETSCHEDULINGSTATE._serialized_end=2199
  _FEATURESET._serialized_start=260
  _FEATURESET._serialized_end=512
  _FEATURESETDEFINITION._serialized_start=515
  _FEATURESETDEFINITION._serialized_end=993
  _FEATURESETSPEC._serialized_start=996
  _FEATURESETSPEC._serialized_end=1351
  _FEATURESETUSERMETADATA._serialized_start=1353
  _FEATURESETUSERMETADATA._serialized_end=1435
  _FEATURESETMETADATA._serialized_start=1438
  _FEATURESETMETADATA._serialized_end=1606
  _DEPLOYEDMODELINUSELINK._serialized_start=1608
  _DEPLOYEDMODELINUSELINK._serialized_end=1670
  _FEATURE._serialized_start=1672
  _FEATURE._serialized_end=1725
  _DEPLOYEDFEATURESETSPEC._serialized_start=1728
  _DEPLOYEDFEATURESETSPEC._serialized_end=1867
# @@protoc_insertion_point(module_scope)
