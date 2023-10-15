from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text

import asyncio

from keyboards.default.lang_buttons import lang_buttons, main_illness, diabet_type_button, confirm_button,\
    phone_button, remove_button, age_button

from states.reg_form import Type2, Type3, RegForm, Obesity
from loader import dp, db


# import create_pdf from testpdf.py
from testpdf import create_pdf, create_pdf_obesity






# step 1
@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    
    lang_text = "Ассалому алайкум. /  Здравствуйте.\n" \
                "Ўзингизга керакли ва қулай тилни танланг: / Выберите язык который вам нужен:"
    db.add_user(message.from_user.id, message.from_user.full_name, "uz")



    await message.answer(lang_text, reply_markup=lang_buttons)
    await RegForm.language.set()
    


# start RegForm


# step 2
@dp.message_handler(Text(equals=['Ўзб','Рус']),state=RegForm.language)
async def choose_language(message: types.Message, state: FSMContext):
    if message.text == "Рус":
        await message.answer("Рус тили вақтинчалик ишламайди.")
    
    db.add_user(message.from_user.id, message.from_user.full_name, 'uz')
    lang = message.text

    text_uz = "\"SEHAT\" клиникасида Туркия, АҚШ, Германия ва Россияда тажриба ортирган катта\
            малакага эга бариатрик жаррохлар ишлайди. Хоналар шинам, опепрация блок юқори технологиялар \
        ва уникал ускуналар билан жихозланган. Хар ойда бариатрия бўлимида 50 дан ортиқ қандли диабет \
            ва семизлик билан операциялар амалга оширилмоқда"
    




    text_ru = """В клинике «SEHAT» работают высококвалифицированные бариатрические хирурги с опытом работы \
          в Турции, США, Германии и России. Палаты уютные, операционный блок оснащен высокими технологиями \
              и уникальным оборудованием. Ежемесячно в бариатрическом отделении проводится более 50 операций \
                  при сахарном диабете и ожирении."""
    

    if lang == "Ўзб":
        language = "uz"
        text = text_uz
    else:
        language = "Рус"
        text = text_ru

    # db.update_lang(message.from_user.id, language)

    
    await message.answer(text)
    # enter phone number
    await message.answer("Телефон рақамингизни киритинг: / Введите ваш номер телефона:", reply_markup=phone_button)
    await RegForm.phone.set()


#  start Type2



@dp.message_handler(content_types=types.ContentType.CONTACT,state=RegForm.phone)
async def enter_phone(message: types.Contact, state: FSMContext):
    phone = message.contact.phone_number
    db.update_phone(message.from_user.id, phone)
    await message.answer("Раҳмат! Сизни рўйхатдан ўтказдик.\n"\
                         "<b>Сиз қайси касаллик билан мурожат этмоқдасиз?</b>",
                         reply_markup= main_illness) # attach buttons
    # await RegForm.illness.set()





@dp.message_handler(Text(equals=["Кандли диабет","Сахарный диабет"]), state="*")
async def enter_illness(message: types.Message, state: FSMContext):
    await state.update_data(user_id=message.from_user.id)
    text = "Сизда қандли диабетнинг нечанчи типи? / У вас какой тип сахарного диабета?"
    await message.answer(text,
                         reply_markup= diabet_type_button) # attach buttons
    await Type2.diabet_type.set()



@dp.message_handler(Text(equals='Тип 1'),state=Type2.diabet_type)
async def enter_diabet_type_1(message: types.Message, state: FSMContext):
    diabet_type = message.text
    # upload to state
    await state.update_data(diabet_type=diabet_type)
    # db.update_diabet_type(message.from_user.id, diabet_type)
    await message.answer("1-тип қандли диабетни операция йўли билан даволаш имкони йўқ, "\
                          "аммо бизнинг малакали эндокринолог врачларимиз Сизга ёрдам беришга тайёр. "\
                          "Эндокринолог кўригига ёзилиши учун 55-500-77-11")
    await state.finish()
    await message.answer("<b>Сиз қайси касаллик билан мурожат этмоқдасиз?</b>",
                         reply_markup= main_illness) # attach buttons
    await RegForm.illness.set()


@dp.message_handler(Text(equals='Тип 2'),state=Type2.diabet_type)
async def enter_diabet_type_2(message: types.Message, state: FSMContext):
    diabet_type = message.text
    await state.update_data(diabet_type=diabet_type)
    # db.update_diabet_type(message.from_user.id, diabet_type)
    await message.answer("Ёшингиз неччида?", reply_markup=remove_button)
    await Type2.enter_age.set()



@dp.message_handler(state=Type2.enter_age)
async def enter_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    # db.update_age(message.from_user.id, age)
    await message.answer("Неча йил аввал касаллик бошланган?", reply_markup=remove_button)
    await Type2.illness_duration.set()


@dp.message_handler(state=Type2.illness_duration)
async def enter_duration(message: types.Message, state: FSMContext):
    duration = message.text
    await state.update_data(start_illness=duration)
    # db.update_duration(message.from_user.id, duration)
    await message.answer("Инсулин қабул қилишни бошладингизми?", reply_markup=confirm_button) # attach buttons
    await Type2.insulin_start.set()


@dp.message_handler(state=Type2.insulin_start)
async def enter_insulin_start(message: types.Message, state: FSMContext):
    insulin_start = message.text
    await state.update_data(start_insulin=insulin_start)
    # db.update_insulin_start(message.from_user.id, insulin_start)
    await message.answer("Вазнингиз канча?", reply_markup=remove_button)
    await Type2.weight.set()


@dp.message_handler(state=Type2.weight)
async def enter_weight(message: types.Message, state: FSMContext):
    weight = message.text
    await state.update_data(weight=weight)
    # db.update_weight(message.from_user.id, weight)
    await message.answer("Бўйингиз қанча?", reply_markup=remove_button)
    await Type2.height.set()


@dp.message_handler(state=Type2.height)
async def enter_height(message: types.Message, state: FSMContext):
    height = message.text
    await state.update_data(height=height)
    # db.update_height(message.from_user.id, height)
    await message.answer("Раҳмат! Сизни рўйхатдан ўтказдик.\n"\
                         "Тез орада мутахассисимиз Сиз билан боғланади, бироз кутинг.", reply_markup=main_illness)
    data = await state.get_data()
    user_id = data.get("user_id")
    diabet_type = data.get("diabet_type")
    age = data.get("age")
    duration = data.get("start_illness")
    insulin_start = data.get("start_insulin")
    weight = data.get("weight")
    height = data.get("height")

    # create pdf
    # await create_diabet_pdf(user_id, diabet_type, age, weight, height, duration, insulin_start)
    create_pdf(user_id, diabet_type, age, weight, height, duration, insulin_start)



    # await message.answer(f"{user_id} {diabet_type} {age} {duration} {insulin_start} {weight} {height}")
    # send pdf to user
    await message.answer_document(document=open(f"./files/{user_id}.pdf", 'rb'))

    # await message.answer()
    await state.finish()
    



#  start Type3
@dp.message_handler(Text(equals=['Билмайман','Не знаю']),state=Type2.diabet_type)
async def enter_diabet_type_3(message: types.Message, state: FSMContext):
    diabet_type = message.text
    await state.update_data(diabet_type=diabet_type)
    # db.update_diabet_type(message.from_user.id, diabet_type)
    await message.answer("Ёшингиз неччида?", reply_markup=age_button)
    await Type3.enter_age.set()





@dp.message_handler(state=Type3.enter_age)
async def enter_age(message: types.Message, state: FSMContext):
    age = message.text
    # upload to state
    await state.update_data(age=age)
    # db.update_age(message.from_user.id, age)
    await message.answer("Kasallik aniqlangan kundan boshlab insulinga o'tganmisiz?", reply_markup= confirm_button)
    await Type3.enter_confirmation.set()


@dp.message_handler(Text(equals=['Ха','Да']),state=Type3.enter_confirmation)
async def enter_confirmation(message: types.Message, state: FSMContext):
    confirmation = message.text
    await state.update_data(confirmation=confirmation)
    text = "Bu jarayondagi диабетни операция йўли билан даволаш имкони йўқ, "\
                          "аммо бизнинг малакали эндокринолог врачларимиз Сизга ёрдам беришга тайёр. "\
                          "Эндокринолог кўригига ёзилиши учун 55-500-77-11"
    await message.answer(text, reply_markup=main_illness)
    await state.finish()



# no choice
@dp.message_handler(Text(equals=["йоқ","нет"]),state=Type3.enter_confirmation)
async def enter_confirmation(message: types.Message, state: FSMContext):
    await message.answer("Вазнингиз канча?", reply_markup=remove_button)
    await Type3.enter_weight.set()


@dp.message_handler(state=Type3.enter_weight)
async def enter_weight(message: types.Message, state: FSMContext):
    weight = message.text
    await state.update_data(weight=weight)
    # db.update_weight(message.from_user.id, weight)
    await message.answer("Бўйингиз қанча?", reply_markup=remove_button)
    await Type3.enter_height.set()


@dp.message_handler(state=Type3.enter_height)
async def enter_height(message: types.Message, state: FSMContext):
    height = message.text
    await state.update_data(height=height)
    # db.update_height(message.from_user.id, height)
    await message.answer("Qayerdansiz?", reply_markup=remove_button)
    await Type3.enter_loaction.set()

@dp.message_handler(state=Type3.enter_loaction)
async def enter_loaction(message: types.Message, state: FSMContext):
    # send all state datas to user
    data = await state.get_data()
    diabet_type = data['diabet_type']
    age = data['age']
    weight = data['weight']
    height = data['height']
    start_insulin = data['confirmation']
    location = message.text

    create_pdf(message.from_user.id, diabet_type, age, weight, height, location, start_insulin)
    await message.answer_document(document=open(f"./files/{message.from_user.id}.pdf", 'rb'))

    await message.answer("Раҳмат! Сизни рўйхатдан ўтказдик.\n "\
                        "Тез орада мутахассисимиз Сиз билан боғланади, бироз кутинг.", reply_markup=main_illness)
    await state.finish()








@dp.message_handler(Text(equals=["Семизлик (ортиқча вазн)","Ожирение (лишний вес)"]), state="*")
async def enter_illness(message: types.Message, state: FSMContext):
    await message.answer("Ёшингиз неччида?", reply_markup=remove_button)
    await Obesity.enter_age.set()

@dp.message_handler(state=Obesity.enter_age)
async def enter_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    # db.update_age(message.from_user.id, age)
    await message.answer("Вазнингиз канча?", reply_markup=remove_button)
    await Obesity.enter_weight.set()

@dp.message_handler(state=Obesity.enter_weight)
async def enter_weight(message: types.Message, state: FSMContext):
    weight = message.text
    await state.update_data(weight=weight)
    # db.update_weight(message.from_user.id, weight)
    await message.answer("Бўйингиз қанча?", reply_markup=remove_button)
    await Obesity.enter_height.set()


@dp.message_handler(state=Obesity.enter_height)
async def enter_height(message: types.Message, state: FSMContext):
    height = message.text
    await state.update_data(height=height)
    # db.update_height(message.from_user.id, height)
    await message.answer("Manzilni kiriting?", reply_markup=remove_button)
    await Obesity.enter_loaction.set()


@dp.message_handler(state=Obesity.enter_loaction)
async def enter_loaction(message: types.Message, state: FSMContext):
    # send all state datas to user
    data = await state.get_data()
    age = data['age']
    weight = data['weight']
    height = data['height']
    location = message.text

    create_pdf_obesity(message.from_user.id, age, weight, height, location)
    await message.answer_document(document=open(f"./files/{message.from_user.id}.pdf", 'rb'))
    await message.answer("Раҳмат! Сизни рўйхатдан ўтказдик.\n"\
                         "Тез орада мутахассисимиз Сиз билан боғланади, бироз кутинг.", reply_markup=main_illness)
    await state.finish()
