# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/debug/debug.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/debug/debug.proto',
  package='debug',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17proto/debug/debug.proto\x12\x05\x64\x65\x62ug\"7\n\x0c\x44\x65\x62ugMessage\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\x05\x12\r\n\x05\x65xtra\x18\x03 \x01(\t')
)




_DEBUGMESSAGE = _descriptor.Descriptor(
  name='DebugMessage',
  full_name='debug.DebugMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='debug.DebugMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='debug.DebugMessage.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra', full_name='debug.DebugMessage.extra', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['DebugMessage'] = _DEBUGMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DebugMessage = _reflection.GeneratedProtocolMessageType('DebugMessage', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGMESSAGE,
  '__module__' : 'proto.debug.debug_pb2'
  # @@protoc_insertion_point(class_scope:debug.DebugMessage)
  })
_sym_db.RegisterMessage(DebugMessage)


# @@protoc_insertion_point(module_scope)
