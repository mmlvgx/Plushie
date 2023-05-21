""""""

from cleo.commands.command import Command
from cleo.helpers import argument

from typing import Final

from ...components.commands.install import handle


class Install(Command):
    """"""

    name = "install"
    description = "This is a Install command"

    arguments = [argument("package", "This is a Package argument")]

    def handle(self) -> None:
        """"""

        package: Final[str] = self.argument("package")

        owner, repo = package.split("/")

        handle(owner, repo)
