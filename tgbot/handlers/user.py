from aiogram import Router, Bot, types
from aiogram.filters import Command, Text, StateFilter
from aiogram.types import Message,FSInputFile
from tgbot.config import load_config
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


user_router = Router()
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

base = psycopg2.connect(
    dbname=config.db.database,
    user=config.db.user,
    password=config.db.password,
    host=config.db.host,
)
cur = base.cursor()

# hanldler for commands
@user_router.message(Command("start"))
async def user_start(message: Message):
    msg = await bot.send_message(user_id, "Вітаю, звичайний користувач!")
    asyncio.create_task(delete_message(msg, 20))
    
    
# hanldler for text messages
# 1 version
@user_router.message(Text('Главное меню'))
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    
# 2 version
@user_router.message(F.text == 'Главное меню')
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

# version for some text messages
# @user_router.message(F.text.in_({'Покупка акаунтов бирж', 'Покупка кошелька Юмани'}))

@user_router.callback_query(CastomCallback.filter(F.action == "end_transaction"))
async def user_start(callback_query: types.CallbackQuery,callback_data: CastomCallback,state: FSMContext,):
    user_id = callback_query.from_user.id