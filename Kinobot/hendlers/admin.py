from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from DATA_BASE import database
from States.admin_state import AdminState
from config import db_name
from keyboards.keyboards import orqaga, menu, menu_admin, yes_or_noo, super_admin

admin_co = Router()

#----------------------------------Super admin va Admin panel functions----------------------------------------------------------------------#


#---------------------------"Xabar yuborish" funksiyasi--------------------------------------------------------------------------------------#

#___________________________________________START_____________________________________________________________________________________________#


@admin_co.message(F.text == "Xabar yuborish")  #yangi funksiya xabar yuborish
async def input_msg(msg: Message,state: FSMContext):
    db = database.database_user(db_name)
    user = db.get_user(msg.from_user.id)
    if user[4] != 0:
        await msg.answer(text="Xabarni yuboring: ")
        await state.set_state(AdminState.send_msg)
    else:
        await msg.answer(text="Xatolik buday menu yo'q",reply_markup=menu)

#---------------------------------------------------------------------------------------------------------------------------------------------#

@admin_co.message(AdminState.send_msg)   #yangi funksiya xabar yuborish
async def send_m(msg: Message, state:FSMContext):
    db = database.database_user(db_name)
    users_id = db.get_user_id()
    if msg.text == "cancel" or msg.text == "Cancel":
        await msg.answer(text="Cancelled")
        await state.clear()
    elif msg.video:
        for i in range(len(users_id)):
            try:
                await msg.bot.send_video(chat_id=users_id[i][0],video=msg.video.file_id,caption=msg.caption)
            except:
                continue
        await state.clear()
    elif msg.photo:
        for i in range(len(users_id)):
            try:
                await msg.bot.send_photo(chat_id=users_id[i][0],photo=msg.photo[-1].file_id,caption=msg.caption)
            except:
                continue
        await state.clear()
    elif msg.document:
        for i in range(len(users_id)):
            try:
                await msg.bot.send_document(chat_id=users_id[i][0],document=msg.document.file_id,caption=msg.caption)
            except:
                continue
        await state.clear()
    elif msg.audio:
        for i in range(len(users_id)):
            try:
                await msg.bot.send_audio(chat_id=users_id[i][0],audio=msg.audio.file_id,caption=msg.caption)
            except:
                continue
        await state.clear()
    elif msg.voice:
        for i in range(len(users_id)):
            try:
                await msg.bot.send_voice(chat_id=users_id[i][0],voice=msg.voice.file_id,caption=msg.caption)
            except:
                continue
        await state.clear()
    elif msg.location:
        for i in range(len(users_id)):
            try:
                await msg.bot.send_location(chat_id=users_id[i][0],latitude=msg.location.latitude,longitude=msg.location.longitude,heading=msg.location.heading)
            except:
                continue
        await state.clear()
    elif msg.contact:
        for i in range(len(users_id)):
            try:
                await msg.bot.send_contact(chat_id=users_id[i][0],first_name=msg.contact.first_name,phone_number=msg.contact.phone_number)
            except:
                continue
        await state.clear()
    elif msg.animation:
        for i in range(len(users_id)):
            try:
                await msg.bot.send_animation(chat_id=users_id[i][0],animation=msg.animation.file_id,caption=msg.caption)
            except:
                continue
        await state.clear()
    elif msg.text:
        for i in range(len(users_id)):
            try:
                await msg.bot.send_message(chat_id=users_id[i][0],text=msg.text)
            except:
                continue
        await state.clear()
    else:
        await msg.answer(text="Xatolik")


#__________________________________________FINISH_____________________________________________________________________________________________#

#---------------------------"Yangi kino yuklash" funksiyasi-----------------------------------------------------------------------------------#

#___________________________________________START_____________________________________________________________________________________________#

@admin_co.message(F.text == "Yangi kino yuklash")
async def upload_kino(msg: Message, state: FSMContext):
    db = database.database_user(db_name)
    user = db.get_user(msg.from_user.id)
    if user[4] != 0:
        await msg.answer(text="Kino yuboring",reply_markup=orqaga)
        await state.set_state(AdminState.title)
    else:
        await msg.answer(text="Xatolik buday menu yo'q",reply_markup=menu)

#---------------------------------------------------------------------------------------------------------------------------------------------#

@admin_co.message(AdminState.title)
async def movie_id(msg: Message, state: FSMContext):
    try:
        file_id = msg.video.file_id
        await state.update_data(file_id=file_id,caption=msg.caption)
        await msg.answer(text="Qidiruv uchun nomini kiriting")
        await state.set_state(AdminState.name)
    except:
        db = database.database_user(db_name)
        user = db.get_user(msg.from_user.id)
        if msg.text == "Menu":
            if user[4] == 1 or msg.text == "Orqaga":
                await msg.answer(text="Menu",reply_markup=menu_admin)
                await state.clear()
            else:
                await msg.answer(text="Menu",reply_markup=super_admin)
                await state.clear()
        else:
            await msg.answer(text="Kino yuboring.")

#---------------------------------------------------------------------------------------------------------------------------------------------#


@admin_co.message(AdminState.name)
async def input_key(msg: Message, state: FSMContext):
    db = database.database_user(db_name)
    user = db.get_user(msg.from_user.id)
    if msg.text == "Menu":
        if user[4] == 1:
            await msg.answer(text="Menu", reply_markup=menu_admin)
            await state.clear()
        else:
            await msg.answer(text="Menu", reply_markup=super_admin)
            await state.clear()
    elif msg.text == "Orqaga":
        await msg.answer(text="Qidiruv uchun nomini kiriting.",reply_markup=orqaga)
    else:
        await state.update_data(name=msg.text)
        await msg.answer(text="Kino nomini kiring:",reply_markup=orqaga)
        await state.set_state(AdminState.name_for_list)


# ----------------------------------------------------------------------------------------------------------------------------------#
@admin_co.message(AdminState.name_for_list)
async def name_for_list(msg: Message, state: FSMContext):
    db = database.database_user(db_name)
    user = db.get_user(msg.from_user.id)
    if msg.text == "Menu":
        if user[4] == 1:
            await msg.answer(text="Menu", reply_markup=menu_admin)
            await state.clear()
        else:
            await msg.answer(text="Menu", reply_markup=super_admin)
            await state.clear()
    elif msg.text == "Orqaga":
        await msg.answer(text="Qidiruv uchun nomini kiriting.", reply_markup=orqaga)
    else:
        await state.update_data(list_name=msg.text)
        await msg.answer(text="Kino kodini kiring:", reply_markup=orqaga)
        await state.set_state(AdminState.key)


# ----------------------------------------------------------------------------------------------------------------------------------#


@admin_co.message(AdminState.key)
async def key(msg: Message, state: FSMContext):
    dbm = database.database_movie(db_name)
    db = database.database_user(db_name)
    user = db.get_user(msg.from_user.id)
    if msg.text == "Menu":
        if user[4] == 1:
            await msg.answer(text="Menu", reply_markup=menu_admin)
            await state.clear()
        else:
            await msg.answer(text="Menu", reply_markup=super_admin)
            await state.clear()
    elif msg.text == "Orqaga":
        await state.set_state(AdminState.name)
        await msg.answer(text="Kino nomini kiriting.",reply_markup=orqaga)
    elif msg.text.isdigit():
        if not dbm.get_movie(int(msg.text)):
            data =await state.get_data()
            file_id = data.get("file_id")
            about = data.get("caption")
            name = data.get("list_name")
            keyy = int(msg.text)
            await state.update_data(keyy=keyy)
            await state.update_data(chat_idd=msg.chat.id)
            await msg.bot.send_video(chat_id=msg.chat.id, video=file_id, caption=f"Kino nomi: {about}\nKod: {keyy}\n \n\t Nomi: {name} \nSaqlansinmi",
                                     reply_markup=yes_or_noo)
            await state.set_state(AdminState.upload_movie)
        else:
            await msg.answer(text="Kino kodini kiriting. Bu kodga boshqa kino biriktirilgan")
    else:
        await msg.answer(text="Kino kodini kiriting. Faqat raqamlardan iborat bo'lsin")

#---------------------------------------------------------------------------------------------------------------------------------------------#

@admin_co.callback_query(AdminState.upload_movie)
async def upload_v(query: CallbackQuery, state: FSMContext):
    db = database.database_user(db_name)
    user = db.get_user(query.from_user.id)
    if query.data == "Ha":
        data = await state.get_data()
        file_id = data.get("file_id")
        name = data.get("name")
        list_name = data.get("list_name")
        about = data.get("caption")
        keyy = data.get("keyy")
        chat_id = data.get("chat_idd")
        dbm = database.database_movie(db_name)
        dbm.add_new_movie(file_id=file_id, key=keyy, des=about, title=name, name=list_name)
        await query.answer(text="Kino muvoffaqiyatli yuklandi.")
        await state.clear()
        if user[4] == 1:
            await query.bot.send_message(chat_id=chat_id,text="Menu",reply_markup=menu_admin)
        else:
            await query.bot.send_message(chat_id=chat_id,text="Menu",reply_markup=super_admin)
        await query.bot.delete_message(chat_id=query.from_user.id,message_id=query.message.message_id)
    else:
        if user[4] == 1:
            await state.clear()
            await query.bot.send_message(chat_id=query.message.chat.id,text="Menu", reply_markup=menu_admin)
        else:
            await state.clear()
            await query.bot.send_message(chat_id=query.message.chat.id,text="Menu", reply_markup=super_admin)
        await query.bot.delete_message(chat_id=query.from_user.id,message_id=query.message.message_id)



#__________________________________________FINISH_____________________________________________________________________________________________#

#----------------------------"Bot a'zolari soni" funksiyasi-----------------------------------------------------------------------------------#

#___________________________________________START_____________________________________________________________________________________________#


@admin_co.message(F.text == "Bot a'zolari soni")
async def son(msg: Message):
    db = database.database_user(db_name)
    user = db.get_user(msg.from_user.id)
    if user[4] != 0:
        count = db.get_all()
        count = len(count)
        await msg.answer(text=f"Bot foydalanuvchilari soni : {count}")
    else:
        await msg.answer(text="Xatolik buday menu yo'q",reply_markup=menu)
#__________________________________________FINISH_____________________________________________________________________________________________#


