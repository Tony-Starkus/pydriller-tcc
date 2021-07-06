from pydriller import Repository
from utils.validators import author_is_bot


def main(repo: Repository) -> dict:
    """
    This function counts the total developers commits on Time Window.
    :param repo: The Repository.
    :return: data: a dict where the key is autor name and the value is the total commits.
    """
    data = {}
    for commit in repo.traverse_commits():

        if not author_is_bot(commit.author):
            if commit.author.name in data:
                data[commit.author.name] = data[commit.author.name] + 1
            else:
                data[commit.author.name] = 1

    # Sort authors name in the dict
    data = dict(sorted(data.items(), key=lambda x: x[0].lower()))
    return data
