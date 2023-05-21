""""""

from cleo.application import Application

from .utils.constants.application import NAME, VERSION

from .commands.install import Install
from .commands.uninstall import Uninstall


application = Application(NAME, version=VERSION)

application.add(Install())
application.add(Uninstall())


def run() -> None:
    """"""

    application.run()
