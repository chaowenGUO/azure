import asyncio, pathlib, importlib
parent = pathlib.Path(__file__).resolve().parent
for _ in parent.iterdir():
    if _.is_dir() and not _.name.startswith('.'): importlib.import_module('.main', _.name)
