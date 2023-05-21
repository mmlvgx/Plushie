""""""

from requests import Session

from ..config import package_path
from ...github.api.client import Client
from ...github.api.structs.content import Content


def handle(owner: str, repo: str) -> None:
    """"""

    session = Session()
    client = Client(session)

    package: Content = client.contents.get(owner, repo, package_path)

    print(package.content)