""""""

from msgspec.json import decode

from base64 import b64decode
from platform import system
from requests import Session

from .utils.constants.package import PATH
from ..structs.package import Package
from ..structs.executable import Executable
from ..github.api.client import Client
from ..github.api.structs.asset import Asset
from ..github.api.structs.release import Release


class Uninstall:
    """"""

    def __init__(self, owner: str, repo: str) -> None:
        """"""

        self.owner = owner
        self.repo = repo

        self.session = Session()
        self.client = Client(self.session)

    def get_package(self) -> Package:
        """"""

        package_file = self.client.contents.get(self.owner, repo=self.repo, path=PATH)
        package_file_content = b64decode(package_file.content)

        package = decode(package_file_content, type=Package)

        return package

    def get_executable(self, executable: Executable) -> str:
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

    def get_release(self, name: str | None = None) -> Release:
        """"""

        releases = self.client.releases.get(self.owner, self.repo)

        if name is None:
            # Last uploaded release
            release = releases[0]

        return release

    def get_asset(self, release: Release, name: str) -> Asset:
        """"""

        for asset in release:
            if asset == name:
                return asset

    def handle(self) -> None:
        """"""

        package = self.get_package()
        executable_name = self.get_executable(package.executable)

        release = self.get_release()
        asset = self.get_asset(release, executable_name)

        print(asset.name)
        print(asset.browser_download_url)