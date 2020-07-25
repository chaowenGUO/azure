https://git-scm.com/book/zh/v2

git config --global user.email "you@example.com"<br>
git config --global user.name "Your Name"<br>
git status<br>
git commit --allow-empty-message -m ''<br>
git push

 
import git, pathlib
with git.Repo(pathlib.Path(__file__).resolve().parent) as repository:
    repository.config_writer().set_value('user', 'name', 'Your Name').release()
    repository.config_writer().set_value('user', 'email', 'you@example.com').release()
    static = 'public'
    repository.git.subtree('add', '--prefix=' + static, 'https://github.com/chaowenGUO/aiohttp', 'master', '--squash')
    repository.index.move([*(str(_) for _  in pathlib.Path(static).resolve().iterdir() if _.suffix == '.html' or _.suffix == '.js' or _.suffix == '.sql'), str(pathlib.Path(static).resolve().parent)], f=True)
    repository.index.remove([static], True, r=True)
    repository.index.commit('')#git commit --allow-empty-message -m ''
    repository.remote().push()
