""""""

from msgspec import Struct

from .asset import Asset


class Release(Struct):
    """"""

    assets: list[Asset]
