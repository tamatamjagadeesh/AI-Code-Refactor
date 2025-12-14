import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

def create_pull_request(repo_name, branch_name, title, body):
    token = os.getenv("GITHUB_TOKEN")
    username = os.getenv("GITHUB_USERNAME")

    g = Github(token)
    repo = g.get_user(username).get_repo(repo_name)

    pr = repo.create_pull(
        title=title,
        body=body,
        head=f"{username}:{branch_name}",
        base="main"
    )

    print("🚀 Pull Request created:")
    print(pr.html_url)
