# src/app.py
from service.githubService import GithubService 

github_service = GithubService()  
commits = github_service.get_all_commits(repo_owner="untalbry", repo_name="Notion_proyect_tracker")
for commit in commits:
    print(commit, end='\n\n')
