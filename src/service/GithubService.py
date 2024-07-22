import os
from dotenv import load_dotenv
import requests
class GithubService():
    def __init__(self):
        env_path = os.path.join(os.path.dirname(__file__), '../..', 'venv', '.env')
        load_dotenv(env_path)
        self.token = os.getenv('TOKEN')
        if not self.token:
            raise ValueError("El token no se encontró en el archivo .env\nAsegurate que el nombre sea 'TOKEN' y que sea correcto el mismo")
        # SET: Headers to connect with Github API 
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
    # GET: List of commits with data: Message, sha, URL
    def get_all_commits(self, repo_owner, repo_name):
        commits = []
        url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            commits_data = response.json()
            for commit in commits_data:
                commit_message = commit['commit']['message']
                commit_sha = commit['sha']
                commit_url = f'https://github.com/{repo_owner}/{repo_name}/commit/{commit_sha}'
            
                print(f"Commit SHA: {commit_sha}")
                print(f"Mensaje: {commit_message}")
                print(f"Enlace: {commit_url}")
        else:
            print(f"Error {response.status_code}: {response.json().get('message', 'No se pudo obtener información del repositorio')}") 
