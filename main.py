from git import Repo,Remote,RemoteProgress
from traceback import format_exception
repo_url = 'https://github.com/Leteers/auto_git.git'


def git_push():
    try:
        repo = Repo('.')
        repo.git.add('-A')
        repo.index.commit('init')
        origin = repo.remote(name='origin')
        origin.push()
    except Exception as e :
        print(f'Some error occured while pushing the code: {e}')    

git_push()