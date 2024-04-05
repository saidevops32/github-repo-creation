import requests
import json

# GitHub username and personal access token
username = 'enter your github username'
token = 'enter your git hub personal access token here'

# Repository information
repo_name = 'github repo creation'
repo_description = 'This is a new repository created via Python script.'
private = False  # Set to True if you want the repository to be private

# GitHub API endpoint for creating a repository
url = f'https://api.github.com/user/repos'

# JSON payload for creating the repository
payload = {
    "name": repo_name,
    "description": repo_description,
    "private": private
}

# Headers with authorization token
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Send POST request to create the repository
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check the response code
if response.status_code == 201:
    print('Repository created successfully!')
    print(f'Repository URL: https://github.com/{username}/{repo_name}')
else:
    print('Failed to create repository.')
    print(f'Response code: {response.status_code}')
    print('Response content:')
    print(response.text)
