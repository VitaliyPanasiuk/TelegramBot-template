from aiogram import Router, Bot, types
from aiogram.types import Message, FSInputFile
from tgbot.config import load_config
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from db.db import get_pool_func

import datetime
import asyncio

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode="HTML")

# pool = await get_pool_func()
#     async with pool.acquire() as connection:
