from aiogram import Router, Bot, types
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import Command, StateFilter
from aiogram.types import Message,FSInputFile
from tgbot.config import load_config
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F

import time
from datetime import datetime
import requests
import asyncio

from tgbot.services.del_message import delete_message

from tgbot.keyboards.inlineBtn import CastomCallback
# CastomCallback.filter(F.action == "") // callback_query: types.CallbackQuery, callback_data: SellersCallbackFactory, state: FSMContext

from db.db import db_pool
from logs.logs import initlogging


user_router = Router()
config = load_config(".env")
bot = Bot(token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode='HTML'))

# async with db_pool.acquire() as connection:
db_logger, bot_logger = initlogging()

@user_router.message(Command("start"))
async def user_start(message: Message):
    user_id = message.from_user.id  
    msg = await bot.send_message(user_id, "Вітаю, звичайний користувач!")
    asyncio.create_task(delete_message(msg, 20))
    
@user_router.message(F.text == 'Главное меню')
async def user_start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

@user_router.callback_query(CastomCallback.filter(F.action == "end_transaction"))
async def user_start(callback_query: types.CallbackQuery,callback_data: CastomCallback,state: FSMContext,):
    user_id = callback_query.from_user.id
    
@user_router.callback_query(F.data == "profile")
async def user_start(callback_query: types.callback_query, state: FSMContext):
    user_id = callback_query.from_user.id  
    await callback_query.message.delete() 