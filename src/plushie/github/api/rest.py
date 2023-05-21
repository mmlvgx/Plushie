""""""

from requests import Session, Response

from .config import scheme, domain


class Rest:
    """"""

    url = f"{scheme}://{domain}"

    def __init__(self, session: Session) -> None:
        """"""

        self.session = session

    def get(self, endpoint: str) -> Response:
        """"""

        url = self.url + endpoint

        response = self.session.get(url)

        return response
