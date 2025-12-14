import os
from git import Repo

def clone_repo(repo_url, local_path):
    if not os.path.exists(local_path):
        Repo.clone_from(repo_url, local_path)
        print("Repository cloned successfully")
    else:
        print("Repository already exists")

def get_python_files(repo_path):
    python_files = []

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                python_files.append(full_path)

    return python_files

from git import Repo
import os

from git import Repo
import os

def write_and_commit(repo_path, file_path, new_code, branch_name):
    repo = Repo(repo_path)

    # If branch exists, switch to it; else create it
    if branch_name in repo.heads:
        repo.git.checkout(branch_name)
    else:
        repo.git.checkout("-b", branch_name)

    # Write refactored code
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_code)

    # Convert to repo-relative path
    relative_path = os.path.relpath(file_path, repo_path)

    # Commit only if there are changes
    if repo.is_dirty():
        repo.git.add(relative_path)
        repo.git.commit("-m", "AI refactor: simplify nested if logic")
        print("✅ Changes committed on branch:", branch_name)
    else:
        print("ℹ️ No changes to commit")


def push_branch(repo_path, branch_name):
    repo = Repo(repo_path)
    origin = repo.remote(name="origin")
    origin.push(branch_name)
    print("⬆️ Branch pushed to GitHub:", branch_name)
