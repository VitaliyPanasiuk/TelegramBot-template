import asyncio
import logging
from aiogram.types import Message


from aiogram import Bot
from aiogram import exceptions

async def delete_message(message: Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    await message.delete()