https://git-scm.com/book/zh/v2

git config --global user.email "you@example.com"<br>
git config --global user.name "Your Name"<br>
git status<br>
git commit --allow-empty-message -m ''<br>
git push

import aiohttp, asyncio, json, os
async def f():
    async with aiohttp.ClientSession() as session:
        for _ in ('springboot', 'koa'):
            async with session.post(f'https://api.github.com/repos/chaowenGUO/{_}/dispatches', data=json.dumps({'event_type':'ping'}).encode(), auth=aiohttp.BasicAuth('chaowenGUO', os.getenv('GITHUB'))) as _: pass
       
asyncio.run(f())
