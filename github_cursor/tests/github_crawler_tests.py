import unittest
import urllib.request

from github_cursor.modules.github_crawler import GithubCrawler

FILENAME = 'private/github_cred.txt'
TARGET = 'munhyunsu'


class GithubCrawlerTestCase(unittest.TestCase):
    def setUp(self):
        self.github_crawler = GithubCrawler(FILENAME, TARGET)

    def tearDown(self):
        del self.github_crawler

    def test___init__(self):
        github_crawler = self.github_crawler
        self.assertEqual(urllib.request.OpenerDirector, type(github_crawler.opener))
        self.assertEqual(TARGET, github_crawler.target)
        self.assertEqual(set, type(self.github_crawler.repo_names))
        self.assertEqual(dict, type(self.github_crawler.commit_dates))

    def test_get_repo_names(self):
        github_crawler = self.github_crawler
        self.assertEqual(set, type(github_crawler.get_repo_names()))

    def test_get_commit_dates(self):
        github_crawler = self.github_crawler
        repo_names = github_crawler.get_repo_names()
        self.assertEqual(list, type(github_crawler.get_commit_dates(list(repo_names)[0])))

    def test_get_commit_dates_all(self):
        github_crawler = self.github_crawler
        self.assertEqual(dict, type(github_crawler.get_commit_dates_all()))
