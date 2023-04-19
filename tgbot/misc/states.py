from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class exmple_state(StatesGroup):
    name = State()
    age = State()
