from aiogram import Router, Bot, types
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from magic_filter import F

import time
from datetime import datetime
import requests
import asyncio

from tgbot.services.del_message import delete_message

from tgbot.keyboards.inlineBtn import CastomCallback
# CastomCallback.filter(F.action == "") // callback_query: types.CallbackQuery, callback_data: SellersCallbackFactory, state: FSMContext

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

base = psycopg2.connect(
    dbname=config.db.database,
    user=config.db.user,
    password=config.db.password,
    host=config.db.host,
)
cur = base.cursor()


@admin_router.message(Text('admin'))
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
