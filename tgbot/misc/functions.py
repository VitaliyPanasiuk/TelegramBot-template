from aiogram import Router, Bot, types
from aiogram.types import Message, FSInputFile
from aiogram.client.bot import DefaultBotProperties
from tgbot.config import load_config
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import datetime
import asyncio

config = load_config(".env")
bot = Bot(token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode='HTML'))
