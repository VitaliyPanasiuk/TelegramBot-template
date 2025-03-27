import asyncpg
from tgbot.config import load_config

config = load_config(".env")

db_pool = None  # Глобальная переменная для хранения пула


async def init_db_pool(max_size):
    pool = await asyncpg.create_pool(
        database=config.db.database,
        user=config.db.user,
        password=config.db.password,
        host=config.db.host,
        max_size=max_size  # Установка максимального размера пула
    )
    return pool
    

async def get_pool_func():
    global db_pool
    if db_pool is None:
        db_pool = await init_db_pool(20)  # Пул для первой группы (например, личные сообщения)
    return db_pool