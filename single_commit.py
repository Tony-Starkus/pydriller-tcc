"""
Repository class params
repository: link or path to the repository
Define range of commit:
    - since (datetime)
    - from_commit (str)
    - from_tag (str)
    - to (datetime)
    - to_commit (str)
    - to_tag (str)
    - order (str)

Commit attributes (https://pydriller.readthedocs.io/en/latest/commit.html)
- project_name
- hash
- msg: message
- author
    - name
- committer_date

Commit filters
    - only_in_branch (str): only analyses commits that belong to this branch.
    - only_no_merge (bool): only analyses commits that are not merge commits.
    - only_authors (List[str]): only analyses commits that are made by these authors. The check is made on the username,
      NOT the email.
    - only_commits (List[str]): only these commits will be analyzed.
"""
from pydriller_tcc import Repository

repo1 = Repository("./repositories/pydriller")
print(f"{repo1=}")

print(f"Commit: 5")
commit_number = 5
commit = list(repo1.traverse_commits())[commit_number - 1]
print(f"Project: {commit.project_name}")
print(f'Commit number: {commit_number}')
print(f'Message: {commit.msg}')
print(f'Date: {commit.committer_date.date()}')
print(f'Number of modified files in this commit: {commit.files}')

# Number of insertions lines in the commit
print(f'Lines deletions: {commit.insertions}')

# Number of deleted lines in the commit
print(f'Lines deletions: {commit.deletions}')
