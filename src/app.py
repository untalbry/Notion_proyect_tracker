# src/app.py
from service.GithubService import GithubService 

repository = GithubService()  
repository.get_all_commits(repo_owner='untalbry', repo_name='PythonLeetcodeSolutions')
