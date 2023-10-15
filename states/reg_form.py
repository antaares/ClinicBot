

from aiogram.dispatcher.filters.state import State, StatesGroup





class RegForm(StatesGroup):
    language = State()
    phone = State()
    illness = State()
    diabet_type = State()
    enter_age = State()
    illness_duration = State()
    insulin_start = State()
    weight = State()
    height = State()


class Type2(StatesGroup):
    diabet_type = State()
    enter_age = State()
    illness_duration = State()
    insulin_start = State()
    weight = State()
    height = State()





class Type3(StatesGroup):
    enter_age = State()
    enter_confirmation = State()
    enter_weight = State()
    enter_height = State()
    enter_loaction = State()



class Obesity(StatesGroup):
    enter_age = State()
    enter_weight = State()
    enter_height = State()
    enter_loaction = State()



