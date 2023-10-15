from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove




lang_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ўзб"),
            KeyboardButton(text="Рус")
        ]
    ],
    resize_keyboard=True
)

main_illness = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кандли диабет"),
            KeyboardButton(text="Семизлик (ортиқча вазн)")#"Кандли диабет","Сахарный диабет"
        ]
    ],
    resize_keyboard=True
)

# request_contact=True
phone_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Телефон рақамни юбориш", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

# remove keyboard
remove_button = ReplyKeyboardRemove()


diabet_type_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Тип 1"),
            KeyboardButton(text="Тип 2"),
            KeyboardButton(text="Билмайман")
        ]
    ],
    resize_keyboard=True
)

confirm_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ха"),
            KeyboardButton(text="Йўқ")
        ]
    ],
    resize_keyboard=True
)


age_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="25 ёшдан кам"),
            KeyboardButton(text="25 ва ундан юқори")
        ]
    ],
    resize_keyboard=True
)
