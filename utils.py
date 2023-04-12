def int_to_bits(num: int) -> str:
    """
    given int, returns the bits representation of the int as string without prefix
    example: int_to_bits(11) = '1011'
    """
    # return bin(num).removeprefix('0b')
    # Convert to binary string and remove prefix "0b"
    binary_str = bin(num)[2:]

    # Pad with zeros to ensure at least 8 bits
    return '{0:0>8}'.format(binary_str)


def bits_to_int(bits: str, start: int = 0, size: int = 1) -> int:
    """
    given byte, returns the int representation of the bits from start and size amount
    example: bits_to_int('1011', 2, 2) = 3
        because, the bits from index 2 and 2 bits are '11' and is 3 in binary
    """
    end: int = start + size
    return int(bits[start:end], 2)


def bytes_to_int(block: bytes, start: int = 0, size: int = 1) -> int:
    """
    given bytes, returns the int representation of the bytes from start and size
    example: bytes_to_int(b'\n\x00\n\x00\x91\x00\x00', 2, 2) = 10
        because, the 2 bytes from index 2 are b'\n\x00\' which are 10 in little endian
    """
    end: int = start + size
    return int.from_bytes(block[start:end], "little", signed=False)


def single_byte(block: bytes, index: int) -> bytes:
    """
    given bytes array, returns a single byte at specific location
    example: single_byte(b'\n\x00\n\x00\x91\x00\x00', 2) = b'\n'
    """
    end: int = index + 1
    return block[index:end]
