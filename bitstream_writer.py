from typing import Literal

import bitstring


class BitStreamWriter:
    def __init__(self, stream: bitstring.BitStream | None = None) -> None:
        super().__init__()
        if stream:
            self._stream = stream
        else:
            self._stream = bitstring.BitStream()

    def _insert(self, bits: bitstring.Bits) -> None:
        self._stream.append(bits)

    def write_bytes(self, input_byte: bytes) -> None:
        bits = bitstring.Bits(bytes=input_byte)
        self._insert(bits)

    def write_bool(self, input_bool: bool) -> None:
        bits = bitstring.Bits(bool=input_bool)
        self._insert(bits)

    def write_unsigned_integer(self, input_num: int, length: int, unit: Literal['bits', 'bytes']) -> None:
        """

        """
        if unit == "bits":
            bits = bitstring.Bits(uint=input_num, length=length)
        elif unit == "bytes":
            bits = bitstring.Bits(uintle=input_num, length=8 * length)
        else:
            raise Exception("incorrect Unit passed, can be 'bits' or 'bytes'")
        self._insert(bits)

    def write_hex(self, input_hex: str, bytes_length: int) -> None:
        """

        """
        bits = bitstring.Bits(hex=input_hex, length=bytes_length)
        self._insert(bits)

    def skip(self, n: int, unit: Literal['bits', 'bytes']):
        """

        """
        raise NotImplemented

    def to_file(self) -> None:
        raise NotImplemented

    def __repr__(self):
        return repr(self._stream)

    def __str__(self):
        return str(self._stream)




if __name__ == '__main__':
    stream = BitStreamWriter()
    stream.write_bool(False)
    stream.write_unsigned_integer(10, 2, 'bytes')
    stream.write_hex('A3F3', 3)
    print(stream._stream.bin)
