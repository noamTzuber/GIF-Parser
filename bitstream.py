from typing import Literal

import bitstring


class BitStream:
    def __init__(self, stream: bitstring.ConstBitStream) -> None:
        super().__init__()
        self._stream = stream

    def read_bytes(self, n_bytes: int) -> bytes:
        return self._stream.read(f"bytes:{n_bytes}")

    def read_decoded(self, n_bytes: int, encoding='utf-8', errors='strict') -> str:
        return self._stream.read(f"bytes:{n_bytes}").decode(encoding, errors)

    def read_bool(self) -> bool:
        return self._stream.read(f"bool")

    def read_unsigned_integer(self, n: int, unit: Literal['bits', 'bytes']) -> int:
        """
        receive a number and unit (can be 'bits' or 'bytes') and reads n times in the unit size and returns the int
        representation. if in bytes, reads in little endian
        """

        if unit == "bits":
            return self._stream.read(f"uint:{n}")
        elif unit == "bytes":
            return self._stream.read(f"uintle:{n * 8}")
        else:
            raise Exception("incorrect Unit passed, can be 'bits' or 'bytes'")

    def read_hex(self, n: int, unit: Literal['bits', 'bytes']) -> str:
        """

        """
        if unit == "bits":
            return self._stream.read(f"hex:{n}")
        elif unit == "bytes":
            return self._stream.read(f"hex:{n * 8}")
        else:
            raise Exception("incorrect Unit passed, can be 'bits' or 'bytes'")

    def skip(self, n: int, unit: Literal['bits', 'bytes']) -> None:
        """

        """
        if unit == "bits":
            self._stream.read(f"pad:{n}")
        elif unit == "bytes":
            self._stream.read(f"pad:{n * 8}")
        else:
            raise Exception("incorrect Unit passed, can be 'bits' or 'bytes'")
