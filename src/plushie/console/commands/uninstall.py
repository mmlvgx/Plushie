""""""

from cleo.commands.command import Command
from cleo.helpers import argument

from typing import Final

from ...components.commands.uninstall import handle


class Uninstall(Command):
    """"""

    name = "uninstall"
    description = "This is a Uninstall command"

    arguments = [argument("package", "This is a Package argument")]

    def handle(self) -> None:
        """"""

        package: Final[str] = self.argument("package")

        owner, repo = package.split("/")

        handle(owner, repo)
