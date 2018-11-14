import json

from github_cursor.modules.auth_opener import AuthOpener

REQUEST_REPOS = 'https://api.github.com/users/{id}/repos'
REQUEST_COMMITS = 'https://api.github.com/repos/{id}/{repo}/commits'


class GithubCrawler(object):
    def __init__(self, cred_path, target):
        auth_opener = AuthOpener(cred_path)
        self.opener = auth_opener.get_opener()
        self.target = target
        self.repo_names = set()
        self.commit_dates = dict()

    def get_repo_names(self):
        if len(self.repo_names) != 0:
            return self.repo_names
        opener = self.opener
        request_dict = {'id': self.target}
        response = opener.open(REQUEST_REPOS.format_map(request_dict))
        response_json = json.loads(response.read())
        for repo in response_json:
            self.repo_names.add(repo['name'])
        return self.repo_names

    def get_commit_dates(self, repo_name):
        if repo_name in self.commit_dates.keys():
            return self.commit_dates[repo_name]
        opener = self.opener
        request_dict = {'id': self.target,
                        'repo': repo_name}
        response = opener.open(REQUEST_COMMITS.format_map(request_dict))
        response_json = json.loads(response.read())
        commits = list()
        for commit in response_json:
            if commit['committer'] is None:
                continue
            if commit['committer']['login'] != self.target:
                continue
            committer = commit['commit']['committer']
            commits.append((committer['date']))
        self.commit_dates[repo_name] = commits
        return self.commit_dates[repo_name]

    def get_commit_dates_all(self):
        repo_names = self.get_repo_names()
        for repo in repo_names:
            self.get_commit_dates(repo)
        return self.commit_dates
