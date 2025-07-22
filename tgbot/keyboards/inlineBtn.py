from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardButton, InlineKeyboardBuilder
from aiogram import Bot, types
from aiogram.filters.callback_data import CallbackData
from typing import Optional


class CastomCallback(CallbackData, prefix="fabnum"):
    action: str
    order_id: Optional[int]

def example_button():
    example = InlineKeyboardBuilder()
    example.button(
        text='Принять ✅',
        callback_data=CastomCallback(action='confirm_user' ,order_id = 1)
    )
    example.add(types.InlineKeyboardButton(
        text='skip',
        callback_data='skip'
    ))
    example.adjust(1)
    return example
