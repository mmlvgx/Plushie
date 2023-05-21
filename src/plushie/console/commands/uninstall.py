""""""

from cleo.helpers import argument
from cleo.commands.command import Command

from typing import Final

from ...components import uninstall


class Uninstall(Command):
    """"""

    name = "uninstall"
    description = "This is a Uninstall command"

    arguments = [argument("package", "This is a Package argument")]

    def handle(self) -> None:
        """"""

        package: Final[str] = self.argument("package")

        owner, repo = package.split("/")

        component = uninstall.Uninstall(owner, repo)
        component.handle()
