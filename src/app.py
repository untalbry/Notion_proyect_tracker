# src/app.py
from service.githubService import GithubService 
from service.notionDBService import NotionDBService
def main():
    github_service = GithubService()  
    pr = github_service.get_new_pull_request(repo_owner="untalbry", repo_name="Notion_proyect_tracker")
    print(pr)
main()
