from enum import Enum


class BlockPrefix(Enum):
    ImageDescriptor = b'\x2C'
    Extension = b'\x21'
    GraphicControlExtension = b'\xF9'
    CommentExtension = b'\xFE'
    PlainTextExtension = b'\x01'
    ApplicationExtension = b'\xFF'
    NONE = b''

    @classmethod
    def _missing_(cls, value):
        return cls.NONE
