from github import Github
from constants import *
import streamlit as st

def introduction():
    st.title(TITLE)
    st.write(DESCRIPTION)


def submit(title, description):
    # Replace these variables with your GitHub credentials and repository information
    github_token = "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"
    repository_name = "laragazzadelsole/Test-Survey"
    branch_name = "Second_Test"
    base_branch = "main"  # Replace with the branch you want to base the new branch on

    # Authenticate with GitHub using your personal access token
    g = Github(github_token)

    # Get the repository
    repo = g.get_repo(repository_name)

    # Create a new branch
    repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=repo.get_branch(base_branch).commit.sha)

        # Get the branch where you want to commit the new file
    branch = repo.get_branch(branch_name)

    # Create a new json file in the branch
    contents = f'{{"title": "{title}", "description": "{description}"}}'
    repo.create_file(
        path= 'config.json',
        message= 'configuration file',
        content=contents,
        branch=branch_name
    )