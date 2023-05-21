""""""

from msgspec.json import decode

from ..helpers.urls import releases
from ..rest import Rest
from ..structs.release import Release


class Releases:
    """"""

    def __init__(self, rest: Rest) -> None:
        """"""

        self.rest = rest

    def get(self, owner: str, repo: str) -> list[Release]:
        """"""

        endpoint = releases(owner, repo=repo)
        response = self.rest.get(endpoint)

        release = decode(response.content, type=list[Release])

        return release
