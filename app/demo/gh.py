# Write a function to get the latest commits from a GitHub repository
# using the GitHub API.
# write the committer name and commit message into an excel file in one sheet

import requests
import pandas as pd
from datetime import datetime


def get_latest_commits(repo_owner, repo_name, token, num_commits=10):
    """
    Fetches the latest commits from a specified GitHub repository.
    Args:
        repo_owner (str): The owner of the repository (username or organization name).
        repo_name (str): The name of the repository.
        token (str): A personal access token for authenticating with the GitHub API.
        num_commits (int, optional): The number of commits to retrieve. Defaults to 10.
    Returns:
        list[dict] or None: A list of dictionaries containing commit data with the keys:
            - 'Committer Name': The name of the committer.
            - 'Commit Message': The commit message.
            Returns None if the request fails.
    Raises:
        None: This function handles HTTP errors internally and prints the error status code.
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"ṇ
    params = {
        "per_page": num_commits,
        "page": 1
    }
    headers = { 
        "Authorization": f"token {token}"
    }
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        commits = response.json()
        commit_data = []
        
        for commit in commits:
            committer_name = commit['commit']['committer']['name']
            commit_message = commit['commit']['message']
            commit_data.append({
                'Committer Name': committer_name,
                'Commit Message': commit_message
            })
        
        return commit_data
    else:
        print(f"Error: {response.status_code}")
        return None

def write_to_excel(commit_data, file_name=None):
    if file_name is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f'latest_commits_{timestamp}.xlsx'
    df = pd.DataFrame(commit_data)
    df.to_excel(file_name, index=False)
    print(f"Data written to {file_name}")