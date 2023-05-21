""""""

from cleo.application import Application

from .utils.constants.application import name, version

from .commands.install import Install
from .commands.uninstall import Uninstall


application = Application(name, version=version)

application.add(Install())
application.add(Uninstall())


def run() -> None:
    """"""

    application.run()
