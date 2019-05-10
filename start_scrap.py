import sys
import json

from github_cursor.modules.github_crawler import GithubCrawler

CRED_FILE = 'private/github_cred.txt'


def main(argv):
    if len(argv) < 2:
        print('Need id lists')
        sys.exit(0)
    with open(argv[1], 'r') as f:
        for target in f:
            github_crawler = GithubCrawler(CRED_FILE, target.strip())
            commits_json = github_crawler.get_commit_dates_all()
            output_path = target + '.json'
            with open(output_path, 'w') as of:
                json.dump(commits_json, of, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    sys.exit(main(sys.argv))

