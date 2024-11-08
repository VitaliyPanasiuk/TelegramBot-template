import asyncpg
from tgbot.config import load_config

config = load_config(".env")

db_pool = None  # Глобальная переменная для хранения пула

async def init_db_pool():
    global db_pool
    db_pool = await asyncpg.create_pool(
        database=config.db.database,
        user=config.db.user,
        password=config.db.password,
        host=config.db.host,
        min_size=10,
        max_size=30
    )