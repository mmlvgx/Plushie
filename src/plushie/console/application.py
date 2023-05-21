""""""

from cleo.application import Application

from .configuration import Configuration

from .commands.install import Install
from .commands.uninstall import Uninstall


name = Configuration.application_name
version = Configuration.application_version

application = Application(name, version=version)

application.add(Install())
application.add(Uninstall())


def run() -> None:
    """"""

    application.run()
