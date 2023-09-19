# sockets.py

import json
from typing import Optional, Any, Union, Dict, Callable
import asyncio
import datetime as dt
from uuid import uuid4
from textwrap import wrap

from crypto_screening.screeners.callbacks.base import BaseCallback

__all__ = [
    "SocketCallback"
]

Connection = Union[asyncio.StreamWriter, asyncio.DatagramTransport]

class SocketCallback(BaseCallback):
    """A class to represent a socket callback."""

    BUFFER = 1024

    TCP = 'tcp'

    REGULAR_FORMAT = 'regular'
    CHUNKED_FORMAT = 'chunked'

    FORMATS = (REGULAR_FORMAT, CHUNKED_FORMAT)

    FORMAT = 'format'
    TIMESTAMP = 'timestamp'
    NAME = 'name'
    KEY = 'key'
    PROTOCOL = 'protocol'
    CHUNKS = 'chunks'
    PART = 'part'
    ID = 'id'

    CONNECTABLE = True

    def __init__(
            self,
            address: str,
            port: int,
            key: Optional[Any] = None,
            buffer: Optional[int] = None,
            delay: Optional[Union[float, dt.timedelta]] = None
    ) -> None:
        """
        Defines the class attributes.

        :param address: The address of the socket.
        :param port: The port of the socket.
        :param key: The key od the data.
        :param buffer: The buffer size.
        :param delay: The delay in handling.
        """

        super().__init__(key=key, delay=delay)

        self.address = address
        self.port = port
        self.buffer = buffer or self.BUFFER

        self._connection: Optional[Connection] = None
        self._writer: Optional[Callable[[bytes], None]] = None
    # end __init__

    # noinspection PyTypeChecker
    async def start(self) -> None:
        """Connects to the socket service."""

        _, self._connection = await asyncio.open_connection(
            host=self.address, port=self.port, limit=self.buffer
        )

        # noinspection PyUnresolvedReferences
        self._writer = (
            self._connection.write
            if hasattr(self._connection, 'write') else
            self._connection.swrite
        )
    # end start

    async def handle(
            self,
            data: Dict[str, Any],
            timestamp: float,
            key: Optional[Any] = None
    ) -> bool:
        """
        Records the data from the crypto feed into the dataset.

        :param data: The data from the exchange.
        :param timestamp: The time of the request.
        :param key: The key for the data type.

        :return: The validation value.
        """

        timestamp = float(timestamp)

        key = key or self.key

        message_id = str(uuid4())

        data = json.dumps(
            {
                self.PROTOCOL: self.TCP,
                self.KEY: key,
                self.TIMESTAMP: timestamp,
                self.DATA: data,
                self.FORMAT: self.REGULAR_FORMAT,
                self.ID: message_id
            }
        )

        if len(data) > self.buffer:
            chunks = wrap(data, self.buffer)

            for i, chunk in enumerate(chunks, start=1):
                message = json.dumps(
                    {
                        self.PROTOCOL: self.TCP,
                        self.KEY: key,
                        self.CHUNKS: len(chunks),
                        self.TIMESTAMP: timestamp,
                        self.FORMAT: self.CHUNKED_FORMAT,
                        self.DATA: chunk,
                        self.PART: i,
                        self.ID: message_id
                    }
                )

                self._writer(message.encode())
            # end for

        else:
            self._writer(data.encode())
        # end if

        return True
    # end process
# end SocketCallback