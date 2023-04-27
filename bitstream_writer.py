from typing import Literal

import bitstring


class BitStreamWriter:
    def __init__(self, stream: bitstring.BitStream) -> None:
        super().__init__()
        self.stream = stream

    def write_bytes(self, input_byte: bytes) -> None:
        return self.stream.append(bitstring.Bits(bytes=input_byte))

    def write_bool(self, input_bool: bool) -> None:
        return self.stream.append(bitstring.Bits(bool=input_bool))

    def write_unsigned_integer(self, input_num: int, length: int, unit: Literal['bits', 'bytes']) -> None:
        """
        receive a number and unit (can be 'bits' or 'bytes') and reads n times in the unit size and returns the int
        representation. if in bytes, reads in little endian
        """

        if unit == "bits":
            return self.stream.append(bitstring.Bits(int=input_num, length=length))
        elif unit == "bytes":
            return self.stream.append(bitstring.Bits(int=input_num, length=8 * length))
        else:
            raise Exception("incorrect Unit passed, can be 'bits' or 'bytes'")

    def write_hex(self, input_hex: str, length: int, unit: Literal['bits', 'bytes']) -> None:
        """

        """
        if unit == "bits":
            return self.stream.append(bitstring.Bits(hex=input_hex, length=length))
        elif unit == "bytes":
            return self.stream.append(bitstring.Bits(hex=input_hex, length=8 * length))
        else:
            raise Exception("incorrect Unit passed, can be 'bits' or 'bytes'")

    def skip(self, n: int, unit: Literal['bits', 'bytes']):
        """

        """
        return NotImplemented
