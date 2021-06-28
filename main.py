from pydriller import Repository

# Global configurations for all repositories.
global_configurations = {
    "since": ""  # (datetime): only commits after this date will be analyzed
}

repo1 = Repository("./repositories/pydriller")
repo2 = Repository("./repositories/Brasilino")
repo3 = Repository("")
repo4 = Repository("")
repositories_list = [repo1, repo2]

print(f"{repo1=}")
for index_list, repository in enumerate(repositories_list):
    for index, commit in enumerate(repository.traverse_commits()):
        print(f'{index=}')
        print(f'{commit.hash}')
    print("----------------------------------------------", end="\n\n")
