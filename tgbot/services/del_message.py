import asyncio
import logging

from aiogram import Bot
from aiogram import exceptions

async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    await message.delete()