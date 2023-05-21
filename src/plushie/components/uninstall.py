""""""

from msgspec.json import decode

from base64 import b64decode
from platform import system
from requests import Session

from .utils.constants.package import PATH
from ..structs.package import Package
from ..structs.executable import Executable
from ..github.api.client import Client


def select(executable: Executable) -> None:
    """"""

    def handle(executable_name: str | None) -> None:
        """"""

        assert executable_name
        return executable_name

    system_name = system()

    linux_executable_name = executable.linux
    darwin_executable_name = executable.darwin
    windows_executable_name = executable.windows

    executables = {
        "Linux": handle(linux_executable_name),
        "Darwin": handle(darwin_executable_name),
        "Windows": handle(windows_executable_name),
    }

    return executables[system_name]


def handle(owner: str, repo: str) -> None:
    """"""

    session = Session()
    client = Client(session)

    package_file = client.contents.get(owner, repo=repo, path=PATH)
    package_file_content = b64decode(package_file.content)

    package = decode(package_file_content, type=Package)
    executable = select(package.executable)

    print(executable)
