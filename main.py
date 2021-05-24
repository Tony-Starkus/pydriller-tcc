from pydriller import Repository

repo1 = Repository("https://github.com/ishepard/pydriller")
print(f"{repo1=}")

for index, commit in enumerate(repo1.traverse_commits()):
    print(f'{index=}')
    print(f'{commit.msg}')

