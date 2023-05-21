""""""

from cleo.commands.command import Command
from cleo.helpers import option


class Install(Command):
    """"""

    name = "install"
    description = "This is a Install command"

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
