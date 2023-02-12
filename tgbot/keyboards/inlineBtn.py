from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardButton, InlineKeyboardBuilder
from aiogram import Bot, types
from aiogram.filters.callback_data import CallbackData
from typing import Optional


class CastomCallback(CallbackData, prefix="fabnum"):
    # castom class for callback_data
    action: str
    order_id: Optional[int]

def example_button():
    example = InlineKeyboardBuilder()
    example.add(types.InlineKeyboardButton(
        text='confirm',
        callback_data=CastomCallback(action="end_order")
    ))
    example.add(types.InlineKeyboardButton(
        text='skip',
        callback_data='skip'
    ))
    return example
