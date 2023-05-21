""""""

from cleo.commands.command import Command
from cleo.helpers import option


class Uninstall(Command):
    """"""

    name = "uninstall"
    description = "This is a Uninstall command"

    options = [
        option("owner", short_name="o", description="This is a Owner option"),
        option("repo", short_name="r", description="This is a Repo option"),
    ]

    def handle(self) -> None:
        """"""

        owner = self.option("owner")
        repo = self.option("repo")

        print(owner)
        print(repo)
