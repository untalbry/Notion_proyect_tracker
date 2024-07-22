import os
from dotenv import load_dotenv
import requests
class Repository():
    def __init__(self) -> None:
        pass
    def get_commits_info(self):
        env_path = os.path.join(os.path.dirname(__file__), '../..', 'venv', '.env')
        load_dotenv(env_path)
        token = os.getenv('TOKEN')
        repo_owner = 'untalbry'
        repo_name = 'PythonLeetcodeSolutions'
        url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'

        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            commits = response.json()
            for commit in commits:
                commit_message = commit['commit']['message']
                commit_sha = commit['sha']
                commit_url = f'https://github.com/{repo_owner}/{repo_name}/commit/{commit_sha}'
            
                print(f"Commit SHA: {commit_sha}")
                print(f"Mensaje: {commit_message}")
                print(f"Enlace: {commit_url}")
                print('-' * 40)
        else:
            print(f"Error {response.status_code}: {response.json().get('message', 'No se pudo obtener información del repositorio')}")