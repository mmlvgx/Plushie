""""""

from msgspec.json import decode

from base64 import b64decode
from requests import Session

from .utils.constants.package import path
from ..structs.package import Package
from ..github.api.client import Client


def handle(owner: str, repo: str) -> None:
    """"""

    session = Session()
    client = Client(session)

    packageFile = client.contents.get(owner, repo=repo, path=path)
    packageFileContent = b64decode(packageFile.content)

    package = decode(packageFileContent, type=Package)

    print(package.executable.linux)
    print(package.executable.macos)
    print(package.executable.windows)