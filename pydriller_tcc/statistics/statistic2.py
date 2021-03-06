from pydriller import Repository
from utils.validators import author_is_bot


def main(repo: Repository) -> dict:
    """
    This function count the modified lines per author in the Repository.
    The count is the total number of added + deleted lines.

    :param repo: The github repository.
    :return: data: ordered dict with author name as key and the count as value.
    """
    data = {}
    for commit in repo.traverse_commits():

        if not author_is_bot(commit.author):
            if commit.author.name in data:
                data[commit.author.name] = data[commit.author.name] + commit.lines
            else:
                data[commit.author.name] = commit.lines

    # Sort authors name in the dict
    data = dict(sorted(data.items(), key=lambda x: x[0].lower()))
    return data
