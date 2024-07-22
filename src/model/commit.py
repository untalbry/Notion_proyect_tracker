class Commit:
    def __init__(self, message, sha, url):
        self.message = message
        self.sha = sha
        self.url = url
    
    def __repr__(self):
        return f"Commit(message='{self.message}', sha='{self.sha}', url='{self.url}')"
    
    def get_sha(self):
        return self.sha
    
    def get_message(self):
        return self.message

    def get_url(self):
        return self.url