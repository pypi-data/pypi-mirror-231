# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/self_service/account/v0/account_membership.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from _qwak_proto.qwak.administration.v0.users import user_pb2 as qwak_dot_administration_dot_v0_dot_users_dot_user__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5qwak/self_service/account/v0/account_membership.proto\x12\x1cqwak.self_service.account.v0\x1a\'qwak/administration/v0/users/user.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"]\n\rInviteOptions\x12L\n\x0finvitation_spec\x18\x01 \x01(\x0b\x32\x33.qwak.self_service.account.v0.JoiningInvitationSpec\"\xa9\x02\n\x1cJoiningInvitationDescription\x12I\n\x08metadata\x18\x01 \x01(\x0b\x32\x37.qwak.self_service.account.v0.JoiningInvitationMetadata\x12\x41\n\x04spec\x18\x02 \x01(\x0b\x32\x33.qwak.self_service.account.v0.JoiningInvitationSpec\x12\x45\n\x06status\x18\x03 \x01(\x0b\x32\x35.qwak.self_service.account.v0.JoiningInvitationStatus\x12\x1e\n\x16num_of_account_members\x18\x04 \x01(\x05\x12\x14\n\x0c\x61\x63\x63ount_name\x18\x05 \x01(\t\"\xa6\x01\n\x19JoiningInvitationMetadata\x12\x15\n\rinvitation_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nexpired_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ninvited_by\x18\x04 \x01(\t\"\x88\x01\n\x15JoiningInvitationSpec\x12\x15\n\rinvitee_email\x18\x01 \x01(\t\x12?\n\x0c\x61\x63\x63ount_role\x18\x02 \x01(\x0e\x32).qwak.administration.user.QwakAccountRole\x12\x17\n\x0f\x65nvironment_ids\x18\x03 \x03(\t\"\x97\x01\n\x17JoiningInvitationStatus\x12G\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x39.qwak.self_service.account.v0.JoiningInvitationStatusCode\x12\x33\n\x0flast_changed_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\x81\x01\n\x1bJoiningInvitationStatusCode\x12*\n&JOINING_INVITATION_STATUS_CODE_INVALID\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\r\n\tCANCELLED\x10\x02\x12\x0c\n\x08\x44\x45\x43LINED\x10\x03\x12\x0c\n\x08\x41\x43\x43\x45PTED\x10\x04\x42\xb9\x01\n#com.qwak.ai.self_service.account.v0P\x01Z\x8f\x01github.com/qwak-ai/qwak-platform/services/core/java/user-management/user-management-api/pb/qwak/self_service/account/v0;self_service_account_v0b\x06proto3')

_JOININGINVITATIONSTATUSCODE = DESCRIPTOR.enum_types_by_name['JoiningInvitationStatusCode']
JoiningInvitationStatusCode = enum_type_wrapper.EnumTypeWrapper(_JOININGINVITATIONSTATUSCODE)
JOINING_INVITATION_STATUS_CODE_INVALID = 0
PENDING = 1
CANCELLED = 2
DECLINED = 3
ACCEPTED = 4


_INVITEOPTIONS = DESCRIPTOR.message_types_by_name['InviteOptions']
_JOININGINVITATIONDESCRIPTION = DESCRIPTOR.message_types_by_name['JoiningInvitationDescription']
_JOININGINVITATIONMETADATA = DESCRIPTOR.message_types_by_name['JoiningInvitationMetadata']
_JOININGINVITATIONSPEC = DESCRIPTOR.message_types_by_name['JoiningInvitationSpec']
_JOININGINVITATIONSTATUS = DESCRIPTOR.message_types_by_name['JoiningInvitationStatus']
InviteOptions = _reflection.GeneratedProtocolMessageType('InviteOptions', (_message.Message,), {
  'DESCRIPTOR' : _INVITEOPTIONS,
  '__module__' : 'qwak.self_service.account.v0.account_membership_pb2'
  # @@protoc_insertion_point(class_scope:qwak.self_service.account.v0.InviteOptions)
  })
_sym_db.RegisterMessage(InviteOptions)

JoiningInvitationDescription = _reflection.GeneratedProtocolMessageType('JoiningInvitationDescription', (_message.Message,), {
  'DESCRIPTOR' : _JOININGINVITATIONDESCRIPTION,
  '__module__' : 'qwak.self_service.account.v0.account_membership_pb2'
  # @@protoc_insertion_point(class_scope:qwak.self_service.account.v0.JoiningInvitationDescription)
  })
_sym_db.RegisterMessage(JoiningInvitationDescription)

JoiningInvitationMetadata = _reflection.GeneratedProtocolMessageType('JoiningInvitationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _JOININGINVITATIONMETADATA,
  '__module__' : 'qwak.self_service.account.v0.account_membership_pb2'
  # @@protoc_insertion_point(class_scope:qwak.self_service.account.v0.JoiningInvitationMetadata)
  })
_sym_db.RegisterMessage(JoiningInvitationMetadata)

JoiningInvitationSpec = _reflection.GeneratedProtocolMessageType('JoiningInvitationSpec', (_message.Message,), {
  'DESCRIPTOR' : _JOININGINVITATIONSPEC,
  '__module__' : 'qwak.self_service.account.v0.account_membership_pb2'
  # @@protoc_insertion_point(class_scope:qwak.self_service.account.v0.JoiningInvitationSpec)
  })
_sym_db.RegisterMessage(JoiningInvitationSpec)

JoiningInvitationStatus = _reflection.GeneratedProtocolMessageType('JoiningInvitationStatus', (_message.Message,), {
  'DESCRIPTOR' : _JOININGINVITATIONSTATUS,
  '__module__' : 'qwak.self_service.account.v0.account_membership_pb2'
  # @@protoc_insertion_point(class_scope:qwak.self_service.account.v0.JoiningInvitationStatus)
  })
_sym_db.RegisterMessage(JoiningInvitationStatus)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#com.qwak.ai.self_service.account.v0P\001Z\217\001github.com/qwak-ai/qwak-platform/services/core/java/user-management/user-management-api/pb/qwak/self_service/account/v0;self_service_account_v0'
  _JOININGINVITATIONSTATUSCODE._serialized_start=1019
  _JOININGINVITATIONSTATUSCODE._serialized_end=1148
  _INVITEOPTIONS._serialized_start=161
  _INVITEOPTIONS._serialized_end=254
  _JOININGINVITATIONDESCRIPTION._serialized_start=257
  _JOININGINVITATIONDESCRIPTION._serialized_end=554
  _JOININGINVITATIONMETADATA._serialized_start=557
  _JOININGINVITATIONMETADATA._serialized_end=723
  _JOININGINVITATIONSPEC._serialized_start=726
  _JOININGINVITATIONSPEC._serialized_end=862
  _JOININGINVITATIONSTATUS._serialized_start=865
  _JOININGINVITATIONSTATUS._serialized_end=1016
# @@protoc_insertion_point(module_scope)
