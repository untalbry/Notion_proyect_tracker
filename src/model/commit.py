class Commit:
    def __init__(self, message, sha, url):
        self.message = message
        self.sha = sha
        self.url = url
    
    def __repr__(self):
        return f"Commit(message='{self.message}', sha='{self.sha}', url='{self.url}')"
