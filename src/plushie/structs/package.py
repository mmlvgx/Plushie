""""""

from msgspec import Struct

from .executable import Executable


class Package(Struct):
    """"""

    executable: Executable