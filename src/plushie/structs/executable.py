""""""

from msgspec import Struct


class Executable(Struct):
    """"""

    linux: str
    macos: str
    windows: str