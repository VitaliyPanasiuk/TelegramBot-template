import asyncpg
from tgbot.config import load_config

config = load_config(".env")

pool_func = None

async def create_db_pool(max_size):
    pool = await asyncpg.create_pool(
        database=config.db.database,
        user=config.db.user,
        password=config.db.password,
        host=config.db.host,
        max_size=max_size  # Установка максимального размера пула
    )
    return pool

async def get_pool_func():
    global pool_func
    if pool_func is None:
        pool_func = await create_db_pool(20)  # Пул для первой группы (например, личные сообщения)
    return pool_func

async def get_db_func():
    global pool_func
    if pool_func is None:
        pool_func = await create_db_pool(20)  # Пул для первой группы (например, личные сообщения)
    return pool_func

async def get_misc_func():
    global pool_func
    if pool_func is None:
        pool_func = await create_db_pool(20)  # Пул для первой группы (например, личные сообщения)
    return pool_func
