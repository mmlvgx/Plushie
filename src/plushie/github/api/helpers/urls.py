""""""


def contents(owner: str, repo: str, path: str) -> str:
    """"""

    return f"/repos/{owner}/{repo}/contents/{path}"


def releases(owner: str, repo: str) -> str:
    """"""

    return f"/repos/{owner}/{repo}/releases"


def repos(owner: str, repo: str) -> str:
    """"""

    return f"/repos/{owner}/{repo}"
