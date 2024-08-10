
from tgbot.config import load_config
from db import get_db_func
import asyncio

import logging
config = load_config(".env")
pool = asyncio.run(get_db_func())


async def postgre_start():
    async with pool.acquire() as connection:
        await connection.execute('''CREATE TABLE IF NOT EXISTS (
        
        )''',)