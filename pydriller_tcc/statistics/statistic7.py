from pydriller import Repository
from utils.validators import author_is_bot


def main(repo: Repository) -> dict:
    """
    This function counts the active authors on Time Windows.
    An active author the the one who has at least one commit.
    :param repo: The Repository.
    :return: data: a dict where the key is autor name and the value is the total commits.
    """
    authors = []
    for commit in repo.traverse_commits():

        if not author_is_bot(commit.author):
            if commit.author.name not in authors:
                authors.append(commit.author.name)

    assert len(authors) == len(tuple(authors))

    # Sort authors name in the array
    authors.sort()
    return authors
