from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardButton, InlineKeyboardBuilder
from aiogram import Bot, types


def example_text_button():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="прийняти")
    )
    home_buttons.add(
        types.KeyboardButton(text="відхилити")
    )
    home_buttons.adjust(2)
    return home_buttons
