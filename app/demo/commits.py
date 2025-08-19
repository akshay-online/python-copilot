# Write a function to get the latest commits from a GitHub repository
# using the GitHub API.
# write the committer name and commit message into an excel file in one sheet

# Import required libraries for API calls, data manipulation, and date handling
import requests
import pandas as pd
from datetime import datetime

def get_latest_commits(token, repo_owner, repo_name, num_commits=5):
    # Construct the GitHub API URL for repository commits
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    # Set up authorization header with GitHub token
    headers = {"Authorization": f"token {token}"}
    # Make GET request to GitHub API
    response = requests.get(url, headers=headers)
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response to get commit data
        commits = response.json()
        # Slice the list to get only the requested number of latest commits
        latest_commits = commits[:num_commits]
        return latest_commits
    else:
        # Print error message if API request failed
        print("Error fetching commits")
        return []

def save_commits_to_excel(commits, file_name):
    # Convert commits list to pandas DataFrame for easy Excel export
    df = pd.DataFrame(commits)
    # Save DataFrame to Excel file without row indices
    df.to_excel(file_name, index=False)
    

if __name__ == "__main__":
    # Set repository details - replace with actual values
    repo_owner = "your_repo_owner"
    repo_name = "your_repo_name"
    # Number of recent commits to fetch
    num_commits = 5
    # Generate filename with current timestamp
    filename = f"latest_commits_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    # GitHub personal access token - replace with your actual token
    token = "your_github_token"  # Replace with your GitHub token

    # Fetch the latest commits from the repository
    commits = get_latest_commits(token, repo_owner, repo_name, num_commits)
    # Save the commits data to an Excel file
    save_commits_to_excel(commits, filename)
