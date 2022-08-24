from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup


class exmple_state(StatesGroup):
    name = State()
    age = State()
