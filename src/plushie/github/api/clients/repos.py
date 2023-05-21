""""""

from msgspec.json import decode

from ..rest import Rest
from ..structs.repo import Repo
from ..helpers.urls import repos


class Repos:
    """"""

    def __init__(self, rest: Rest) -> None:
        """"""

        self.rest = rest

    def get(self, owner: str, repo: str) -> Repo:
        """"""

        endpoint = repos(owner, repo=repo)
        response = self.rest.get(endpoint)

        repo = decode(response.content, type=Repo)

        return repo
