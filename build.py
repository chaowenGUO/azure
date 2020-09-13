import git, pathlib, importlib
for _ in pathlib.Path(__file__).resolve().parent.iterdir():
    if _.is_dir() and not _.name.startswith('.'): importlib.import_module('.main', _)
with git.Repo(pathlib.Path(__file__).resolve().parent) as repository:
    repository.config_writer().set_value('user', 'name', 'Your Name').release()
    repository.config_writer().set_value('user', 'email', 'you@example.com').release()
    repository.git.add(A=True)
    repository.index.commit('')#git commit --allow-empty-message -m ''
    repository.remote().push()
