from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardButton, InlineKeyboardBuilder
from aiogram import Bot, types


def example_button():
    example = InlineKeyboardBuilder()
    example.add(types.InlineKeyboardButton(
        text='confirm',
        callback_data='confirm'
    ))
    example.add(types.InlineKeyboardButton(
        text='skip',
        callback_data='skip'
    ))
    return example
