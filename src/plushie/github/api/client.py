""""""

from requests import Session

from .rest import Rest
from .clients.contents import Contents
from .clients.repos import Repos


class Client:
    """"""

    def __init__(self, session: Session) -> None:
        """"""

        self.rest = Rest(session)

        self.contents = Contents(self.rest)
        self.repos = Repos(self.rest)
