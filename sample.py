from pydriller_tcc import Repository
from datetime import datetime

# Global configurations for all repositories.
global_configurations = {
    "since": datetime(2019, 1, 1)  # (datetime): only commits after this date will be analyzed
}

repo1 = Repository("./repositories/Brasilino", since=global_configurations['since'])
repo2 = Repository("./repositories/dialetus-service", since=global_configurations['since'])
repo3 = Repository("https://github.com/nullstack/nullstack")
repo4 = Repository("")
repositories_list = [repo3]  # [repo1, repo2]

for index_list, repository in enumerate(repositories_list):
    total_commits = 0
    for index, commit in enumerate(repository.traverse_commits()):
        total_commits += 1
        print(f"{commit=}")
        print(f"{commit.committer_date.date()=}")
        # print(f'{index=}')
        # print(f'{commit.hash}')
    print(f"Repositório {index_list + 1} - {list(repository.traverse_commits())[0].project_name}")
    print(f"{total_commits=}")
    print("----------------------------------------------", end="\n\n")
