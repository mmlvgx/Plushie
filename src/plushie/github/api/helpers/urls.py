""""""


def contents(owner: str, repo: str, path: str) -> str:
    """"""

    return f"/repos/{owner}/{repo}/contents/{path}"


def repos(owner: str, repo: str) -> str:
    """"""

    return f"/repos/{owner}/{repo}"
