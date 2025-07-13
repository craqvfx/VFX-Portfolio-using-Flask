import requests
from flask import current_app

def get_github_repos(username, sort="updated"):
    url = f"https://api.github.com/users/{username}/repos"
    params = {
        'type': 'public',
        'sort': sort,
        'per_page': 100
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for HTTP errors first
        return response.json()
        
    except Exception as e:
        current_app.logger.error(f"GitHub API Error: {e}")
        return None

#useful info from api:
#language
#languages_url
#updated_at
#created_at
#clone_url
#watchers_count
#subscribers_count
#visibility	?