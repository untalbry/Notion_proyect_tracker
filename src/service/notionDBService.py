import os
from dotenv import load_dotenv
import requests

class NotionDBService():
    def __init__(self):
        env_path = os.path.join(os.path.dirname(__file__), '../..', 'venv', '.env')
        load_dotenv(env_path)
        self.NOTION_KEY = os.getenv('NOTION_KEY')
        self.COMMITS_DATABASE_ID = os.getenv('COMMITS_DATABASE_ID')
        
        self.CREATE_URL = "https://api.notion.com/v1/pages"
        self.headers = {
            "Authorization": f"Bearer {self.NOTION_KEY}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        
    def insert_commit_list(self, commits):
        for commit in commits:
            print(commit.get_sha(), commit.get_message())
            new_page = {
                "parent": {"database_id": self.COMMITS_DATABASE_ID},
                "properties": {
                    "SHA": {
                        "title": [
                            {
                                "text": {
                                    "content": commit.get_sha()
                                }
                            }
                        ]
                    },
                    "MESSAGE": {
                        "rich_text": [
                            {
                                "text": {
                                    "content": commit.get_message()
                                }
                            }
                        ]
                    },
                    "URL": {
                        "url": commit.get_url()
                    }
                }
            }
            response = requests.post(self.CREATE_URL, headers=self.headers, json=new_page)
            if response.status_code == 200:
                print(f"200: Commit inserted successfully")
            else:
                raise ValueError(f"Exception in inserting commit: {response.status_code}\n{response.json}")
    #TODO:
    def insert_issues_list():
        pass
    def insert_pr_list():
        pass
