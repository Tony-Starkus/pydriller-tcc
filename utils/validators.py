from pydriller.domain.developer import Developer


def author_is_bot(author: Developer):
    """
    This function check if the author is a bot.
    :param author: The author who bill be checked.
    :return: return True if the author is a bot, if is not a bot return False.
    """
    if "[bot]" in author.name:
        return True
    return False

