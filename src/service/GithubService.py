import os
from dotenv import load_dotenv
import requests

from model.commit import Commit
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
            for c in commits_data:
                commit_message = c['commit']['message']
                commit_sha = c['sha']
                commit_url = f'https://github.com/{repo_owner}/{repo_name}/commit/{commit_sha}'
                commit = Commit(message=commit_message, sha=commit_sha, url=commit_url)
                commits.append(commit)
        else:
            print(f"Error {response.status_code}: {response.json().get('message', 'No se pudo obtener información del repositorio')}") 
        return commits
    def get_new_pull_request(self, repo_owner, repo_name):
        url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls?state=all&sort=updated&direction=desc&per_page=1'
        
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            pull_request_data = response.json()
            if pull_request_data:
                last_pull_request = pull_request_data[0]
                return {
                    'title': last_pull_request['title'],
                    'number': last_pull_request['number'],
                    'url': last_pull_request['html_url'],
                    'state': last_pull_request['state'],
                    'created_at': last_pull_request['created_at'],
                    'updated_at': last_pull_request['updated_at']
                }
            else:
                print("No se encontraron pull requests en el repositorio.")
        else:
            print(f"Error {response.status_code}: {response.json().get('message', 'No se pudo obtener información del repositorio')}")
        return None