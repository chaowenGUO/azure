import git, pathlib, importlib
parent = pathlib.Path(__file__).resolve().parent
for _ in parent.iterdir():
    if _.is_dir() and not _.name.startswith('.'): importlib.import_module('.main', _.name)
with git.Repo(parent) as repository:
    repository.config_writer().set_value('user', 'name', 'Your Name').release()
    repository.config_writer().set_value('user', 'email', 'you@example.com').release()
    repository.git.add(A=True)
    repository.index.commit('')#git commit --allow-empty-message -m ''
    repository.remote().push()
