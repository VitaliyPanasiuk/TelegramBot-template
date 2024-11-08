from aiogram import Router, Bot, types
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile
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

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())

config = load_config(".env")
bot = Bot(token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode='HTML'))




# @admin_router.message(F.text('admin'))
# async def user_start(message: types.Message, state: FSMContext):
#     user_id = message.from_user.id
