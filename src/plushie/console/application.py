""""""

from cleo.application import Application

from .config import application_name, application_version

from .commands.install import Install
from .commands.uninstall import Uninstall


name = application_name
version = application_version

application = Application(name, version=version)

application.add(Install())
application.add(Uninstall())


def run() -> None:
    """"""

    application.run()
