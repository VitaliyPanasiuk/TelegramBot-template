from aiogram import Router, Bot, types
from aiogram.types import Message, FSInputFile
from tgbot.config import load_config
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs

from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')


# @admin_router.message(commands=["start"], state="*")
# async def admin_start(message: Message):
#     await message.reply("Вітаю, адміне!")
