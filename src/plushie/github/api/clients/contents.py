""""""

from msgspec.json import decode

from ..rest import Rest
from ..structs.content import Content
from ..helpers.urls import contents


class Contents:
    """"""

    def __init__(self, rest: Rest) -> None:
        """"""

        self.rest = rest

    def get(self, owner: str, repo: str, path: str) -> Content:
        """"""

        endpoint = contents(owner, repo=repo, path=path)
        response = self.rest.get(endpoint)

        content = decode(response.content, type=Content)

        return content