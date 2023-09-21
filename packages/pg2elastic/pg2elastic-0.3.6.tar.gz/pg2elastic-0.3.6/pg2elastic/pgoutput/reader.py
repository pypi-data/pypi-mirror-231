import time
import typing
import uuid
import psycopg2
import psycopg2.extensions
import psycopg2.extras
import pydantic

from datetime import datetime
from .formatter import get_message
from loguru import logger


class ReplicationMessage(pydantic.BaseModel):
    message_id: pydantic.UUID4
    data_start: int
    payload: bytes
    send_time: datetime
    data_size: int
    wal_end: int


class LogicalReplicationReader:
    """
    1. One process continuously extracts (ExtractRaw) raw messages
        a. Uses pyscopg2's LogicalReplicationConnection and replication expert
        b. Send raw pg-output replication messages and metadata to a pipe for another process to read from
    2. Main process extracts the raw messages from the pipe (sent in 1.b.)
        a. Decode binary pgoutput message to B, C, I, U, D or R message type
        b. Pass decoded message into transform function that produces change events with additional metadata cached in
           from previous messages and by looking up values in the source DBs catalog
    """

    def __init__(
        self,
        publication_name: str,
        slot_name: str,
        receiver,
        dsn: typing.Optional[str] = None,
        **kwargs: typing.Optional[str],
    ) -> None:
        self.receiver = receiver
        self.dsn = psycopg2.extensions.make_dsn(dsn=dsn, **kwargs)
        self.publication_name = publication_name
        self.slot_name = slot_name
        self.database = ''
        self.txn = None

        # save map of type oid to readable name
        self.setup()

    def setup(self) -> None:
        self.extractor = ExtractRaw(
            dsn=self.dsn, publication_name=self.publication_name, slot_name=self.slot_name
        )
        self.extractor.connect()
        self.extractor.run(self.process)
        self.database = self.extractor.database

    def process(self, msg: psycopg2.extras.ReplicationMessage):
        message_id = uuid.uuid4()

        try:
            message = ReplicationMessage(
                message_id=message_id,
                data_start=msg.data_start,
                payload=msg.payload,
                send_time=msg.send_time,
                data_size=msg.data_size,
                wal_end=msg.wal_end,
            )

            output, transaction = get_message(message, database=self.database, txn=self.txn)
            self.txn = transaction
            self.receiver(output)
            msg.cursor.send_feedback(flush_lsn=msg.data_start)
            logger.debug(f"Flushed message: '{str(message_id)}'")
        except Exception as e:
            logger.error(f"Failed message: '{str(message_id)}', {e}...")

    def stop(self) -> None:
        """Stop reader process and close the pipe"""
        time.sleep(0.1)
        self.extractor.close()


class ExtractRaw:
    """
    Consume logical replication messages using psycopg2's LogicalReplicationConnection. Run as a separate process
    due to using consume_stream's endless loop. Consume msg sends data into a pipe for another process to extract

    Docs:
    https://www.psycopg.org/docs/extras.html#replication-support-objects
    https://www.psycopg.org/docs/extras.html#psycopg2.extras.ReplicationCursor.consume_stream
    """

    def __init__(self, dsn: str, publication_name: str, slot_name: str) -> None:
        self.dsn = dsn
        self.publication_name = publication_name
        self.slot_name = slot_name
        self.database = ''

    def connect(self) -> None:
        self.conn = psycopg2.extras.LogicalReplicationConnection(self.dsn)
        self.cur = psycopg2.extras.ReplicationCursor(self.conn)
        self.database = self.conn.get_dsn_parameters()["dbname"]

    def close(self) -> None:
        self.cur.close()
        self.conn.close()

    def run(self, consumer) -> None:
        replication_options = {"publication_names": self.publication_name, "proto_version": "1"}
        try:
            self.cur.start_replication(slot_name=self.slot_name, decode=False, options=replication_options)
        except psycopg2.ProgrammingError:
            self.cur.create_replication_slot(self.slot_name, output_plugin="pgoutput")
            self.cur.start_replication(slot_name=self.slot_name, decode=False, options=replication_options)
        try:
            logger.info(f"Starting replication from slot: '{self.slot_name}'")
            self.cur.consume_stream(consumer)
        except Exception as err:
            logger.error(f"Error consuming stream from slot: '{self.slot_name}'. {err}")
            self.cur.close()
            self.conn.close()
