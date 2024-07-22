# src/app.py
from service.githubService import GithubService 
from service.notionDBService import NotionDBService
def main():
    github_service = GithubService()  
    commits = github_service.get_all_commits(repo_owner="untalbry", repo_name="Notion_proyect_tracker")
    for commit in commits:
        print(commit, end='\n\n')
    notion_bd_service = NotionDBService()
    notion_bd_service.insert_commit_list(commits=commits)

main()
