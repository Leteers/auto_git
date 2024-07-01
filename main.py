from git import Repo,Remote,RemoteProgress
import random
import time

def git_push(commit_message: str):
    try:
        repo = Repo('.')
        repo.git.add('-A')
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
    except Exception as e :
        print(f'Some error occured while pushing the code: {e}')    

if __name__ == '__main__':
    while True:
        r_number = random.randrange(2,8)
        for i in range(r_number):
            with open('text.txt', 'w') as f:
                f.write(random.randrange(0,10000))
                f.write(random.randrange(0,10000))
            git_push(f'{i}/{r_number}')
            time.sleep((24*60*60)/r_number)