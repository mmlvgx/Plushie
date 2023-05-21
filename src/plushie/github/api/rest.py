""""""

from requests import Session, Response

from .utils.constants.rest import SCHEME, DOMAIN


class Rest:
    """"""

    url = f"{SCHEME}://{DOMAIN}"

    def __init__(self, session: Session) -> None:
        """"""

        self.session = session

    def get(self, endpoint: str) -> Response:
        """"""

        url = self.url + endpoint

        response = self.session.get(url)

        return response
