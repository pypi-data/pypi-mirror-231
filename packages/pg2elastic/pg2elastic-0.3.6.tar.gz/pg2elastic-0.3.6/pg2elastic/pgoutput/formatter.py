from .decoder import *
from .types import OID_TYPE
from ..base import parse_value
from loguru import logger

relation_pool = {}


def map_tuple_to_dict(tuple_data: TupleData, relation):
    """Convert tuple data to an OrderedDict with keys from relation mapped in order to tuple data"""
    output = {}
    for idx, col in enumerate(tuple_data.column_data):
        columns = relation.get('columns', []) or []
        column = columns[idx]
        column_name = column.get('name', '') or ''
        column_type = column.get('type', 0) or 0
        output.update({column_name: parse_value(OID_TYPE.get(str(column_type), ''), col.col_data)})

    return output


def process_insert(message, transaction=None):
    if transaction is None:
        transaction = {}

    decoded_msg: Insert = Insert(message.payload)
    relation_id: int = decoded_msg.relation_id
    after = map_tuple_to_dict(tuple_data=decoded_msg.new_tuple, relation=relation_pool[relation_id])

    payload = {
        'op': decoded_msg.byte1,
        'id': str(message.message_id),
        'lsn': message.data_start,
        'transaction': transaction,
        'before': None,
        'after': after,
        'meta': relation_pool[relation_id]
    }

    return payload


def process_begin(message):
    begin_msg: Begin = Begin(message.payload)
    transaction = {'tx_id': begin_msg.tx_xid, 'begin_lsn': begin_msg.lsn, 'commit_ts': begin_msg.commit_ts}
    return transaction


def process_update(message, transaction=None):
    if transaction is None:
        transaction = {}

    decoded_msg: Update = Update(message.payload)
    relation_id: int = decoded_msg.relation_id

    if decoded_msg.old_tuple:
        before_raw = map_tuple_to_dict(tuple_data=decoded_msg.old_tuple, relation=relation_pool[relation_id])
        before_typed = before_raw
    else:
        before_typed = None

    after = map_tuple_to_dict(tuple_data=decoded_msg.new_tuple, relation=relation_pool[relation_id])

    payload = {
        'op': decoded_msg.byte1,
        'id': str(message.message_id),
        'lsn': message.data_start,
        'transaction': transaction,
        'before': before_typed,
        'after': after,
        'meta': relation_pool[relation_id]
    }

    return payload


def process_delete(message, transaction=None):
    if transaction is None:
        transaction = {}

    decoded_msg: Delete = Delete(message.payload)
    relation_id: int = decoded_msg.relation_id

    if decoded_msg.old_tuple:
        before_raw = map_tuple_to_dict(tuple_data=decoded_msg.old_tuple, relation=relation_pool[relation_id])
        before_typed = before_raw
    else:
        before_typed = None

    payload = {
        'op': decoded_msg.byte1,
        'id': str(message.message_id),
        'lsn': message.data_start,
        'transaction': transaction,
        'before': before_typed,
        'after': None,
        'meta': relation_pool[relation_id]
    }

    return payload


def process_truncate(message, transaction=None):
    if transaction is None:
        transaction = {}

    decoded_msg: Truncate = Truncate(message.payload)
    payloads = []
    meta = None

    for relation_id in decoded_msg.relation_ids:
        meta = relation_pool[relation_id]
        payloads.append({
            'op': decoded_msg.byte1,
            'id': str(message.message_id),
            'lsn': message.data_start,
            'transaction': transaction,
            'before': None,
            'after': None,
            'meta': meta
        })

    payload = {
        'op': decoded_msg.byte1,
        'id': str(message.message_id),
        'lsn': message.data_start,
        'transaction': transaction,
        'before': None,
        'after': None,
        'meta': meta
    }

    return payload


def process_relation(message, database):
    relation_msg: Relation = Relation(message.payload)
    relation_id = relation_msg.relation_id
    columns = []

    for column in relation_msg.columns:
        columns.append({'name': column.name, 'type': column.type_id, 'pk': bool(column.part_of_pkey)})

    relation_pool[relation_id] = {
        'database': database,
        'schema': relation_msg.namespace,
        'table': relation_msg.relation_name,
        'columns': columns,
        'relation': relation_id
    }

    payload = {
        'op': relation_msg.byte1,
        'id': str(message.message_id),
        'lsn': message.data_start,
        'transaction': None,
        'before': None,
        'after': None,
        'meta': None
    }

    return payload


def process_commit(message):
    decoded_msg: Commit = Commit(message.payload)

    payload = {
        'op': decoded_msg.byte1,
        'id': str(message.message_id),
        'lsn': message.data_start,
        'transaction': None,
        'before': None,
        'after': None,
        'meta': None
    }

    return payload


def get_message(data, database, txn=None):
    transaction = txn
    output = None

    try:
        message_type = (data.payload[:1]).decode("utf-8")

        if message_type == "R":
            output = process_relation(message=data, database=database)
        elif message_type == "B":
            transaction = process_begin(message=data)
        elif message_type == "I":
            output = process_insert(message=data, transaction=txn)
        elif message_type == "U":
            output = process_update(message=data, transaction=txn)
        elif message_type == "D":
            output = process_delete(message=data, transaction=txn)
        elif message_type == "T":
            output = process_truncate(message=data, transaction=txn)
        elif message_type == "C":
            transaction = None
            output = process_commit(message=data)

        return output, transaction
    except Exception as error:
        logger.error(f"Can't parse binary message, {error}")
        return None, None
