import requests

# GitHub username and personal access token
username = 'enter your github username'
token = 'enter your git hub personal access token here'

# Repository name to be deleted
repo_name = 'new-repo'

# GitHub API endpoint for deleting a repository
url = f'https://api.github.com/repos/{username}/{repo_name}'

# Headers with authorization token
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Send DELETE request to delete the repository
response = requests.delete(url, headers=headers)

# Check the response code
if response.status_code == 204:
    print(f'Repository "{repo_name}" deleted successfully!')
else:
    print('Failed to delete repository.')
    print(f'Response code: {response.status_code}')
    print('Response content:')
    print(response.text)
