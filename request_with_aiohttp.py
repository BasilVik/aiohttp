import asyncio
import aiohttp
from util import async_timed, fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} было равно {status}')

asyncio.run(main())
