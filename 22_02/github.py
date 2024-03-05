import requests

def get_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_repos(username):
    repos = get_repos(username)
    if repos is not None:
        for repo in repos:
            print(repo['name'])
    else:
        print("Произошла ошибка")
        
def test_get_repos():
    repos = get_repos('kamranahmedse')
    assert repos is not None
    assert isinstance(repos, list)
    assert len(repos) > 0
    assert all(isinstance(repo, dict) for repo in repos)
    assert all('name' in repo for repo in repos)
    repos = get_repos('&%(##Q&%)(@#)')
    assert repos is None

if __name__ == "__main__":
    username = 'kamranahmedse'
    print_repos(username)
