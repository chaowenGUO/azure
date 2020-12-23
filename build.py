import asyncio, pathlib, importlib
parent = pathlib.Path(__file__).resolve().parent
for _ in parent.iterdir():
    if _.is_dir() and not _.name.startswith('.'): importlib.import_module('.main', _.name)
        
async def f():
    await asyncio.create_subprocess_exec('git', 'add', '-A')
    await asyncio.create_subprocess_exec('git', 'commit', '--allow-empty-message', '-m', '')
    await asyncio.create_subprocess_exec('git', 'push')
    
asyncio.run(f())
