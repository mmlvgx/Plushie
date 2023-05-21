""""""

from msgspec import Struct


class Executable(Struct):
    """"""

    linux: str | None = None
    darwin: str | None = None
    windows: str | None = None