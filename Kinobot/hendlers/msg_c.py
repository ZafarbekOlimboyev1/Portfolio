from aiogram import Router, F
from aiogram.filters import and_f
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InputMediaVideo
from random import choice
from DATA_BASE.database import database_movie, database_user
from States.statess import RegistrState
from config import db_name
from functions.send_kino import get_id
from keyboards.keyboards import orqaga, menu, janr, menu_admin, super_admin, follow_channel, kino_menu, left_right_k, \
    movies_list_k
from functions.cheak import cheak_channels

msg_co = Router()


# -------------------------------------------------User panel functions----------------------------------------------------------------------#


# ------------------------------"Kino izlash" funksiyasi--------------------------------------------------------------------------------------#

# ___________________________________________START_____________________________________________________________________________________________#


@msg_co.message(F.text == "Kino izlash")
async def kino_menyu(msg: Message, state: FSMContext):
    if msg.text.isdigit():
        file_id = get_id(int(msg.text))
        if file_id:
            await msg.bot.send_video(chat_id=msg.chat.id, video=file_id[1], caption=file_id[3])
        else:
            await msg.answer(text="Bunday kodli kino topilmadi.")
    else:
        await msg.answer(f"Quyida 2 ta bo'lim bor:\n\n\t1. Kod bo'yicha izlash - Bu bo'limda kinoni kod orqali "
                         f"izlaysiz yani har bir kinoga kod biriktirilgan siz shu kod orqali kinoni yuklab olasiz\n\t"
                         f"2. Nom bo'yicha izlash - Bu bo'limda kinoni nomini yozasiz va bot sizga agar siz yozgan kino"
                         f" botda bo'lsa sizga bot tashlab beradi.", reply_markup=kino_menu)
        await state.set_state(RegistrState.kino)


# ---------------------------------------------Kod bo'yicha izlash-----------------------------------------------------#


@msg_co.message(and_f(F.text == "Kod bo'yicha izlash", RegistrState.kino))
async def kino(msg: Message, state: FSMContext):
    if await cheak_channels(msg.from_user.id, msg.bot):
        await msg.answer("Iltimos kanallarga obuna bo'ling", reply_markup=follow_channel())
    else:
        await msg.answer(text="Kino kodini kiriting: ", reply_markup=orqaga)
        await state.set_state(RegistrState.find_kino)


# ---------------------------------------------------------------------------------------------------------------------------------------------#

@msg_co.message(RegistrState.find_kino)
async def example(msg: Message, state: FSMContext):
    if await cheak_channels(msg.from_user.id, msg.bot):
        await msg.answer("Iltimos kanallarga obuna bo'ling", reply_markup=follow_channel())
    else:
        if msg.text == "Menu":
            db = database_user(db_name)
            user = db.get_user(msg.from_user.id)
            if user[4] == 0:
                await msg.answer("Menu", reply_markup=menu)
                await state.set_state(RegistrState.menu)
            elif user[4] == 1:
                await msg.answer(text="Menu", reply_markup=menu_admin)
                await state.clear()
            else:
                await msg.answer(text="Menu", reply_markup=super_admin)
                await state.clear()
        elif msg.text == "Orqaga":
            await msg.answer(f"Quyida 2 ta bo'lim bor:\n\n\t1. Kod bo'yicha izlash - Bu bo'limda kinoni kod orqali "
                             f"izlaysiz yani har bir kinoga kod biriktirilgan siz shu kod orqali kinoni yuklab olasiz\n\t"
                             f"2. Nom bo'yicha izlash - Bu bo'limda kinoni nomini yozasiz va bot sizga agar siz yozgan kino"
                             f" botda bo'lsa sizga bot tashlab beradi.", reply_markup=kino_menu)
            await state.set_state(RegistrState.kino)
        elif msg.text.isdigit():
            file_id = get_id(int(msg.text))
            if file_id:
                await msg.bot.send_video(chat_id=msg.chat.id, video=file_id[1], caption=file_id[3])
            else:
                await msg.answer(text="Bunday kodli kino topilmadi.")
        else:
            await msg.answer(text="Iltimos faqat codni kiriting faqat raqamlardan iborat bo'lsin!", reply_markup=orqaga)


# ___________________________________finish_____________________________________________________________________#

# ------------------------------------- Nom bo'yicha izlash ----------------------------------------------------#

@msg_co.message(and_f(F.text == "Nom bo'yicha izlash", RegistrState.kino))
async def kino(msg: Message, state: FSMContext):
    if await cheak_channels(msg.from_user.id, msg.bot):
        await msg.answer("Iltimos kanallarga obuna bo'ling", reply_markup=follow_channel())
    else:
        if msg.text.isdigit():
            file_id = get_id(int(msg.text))
            if file_id:
                await msg.bot.send_video(chat_id=msg.chat.id, video=file_id[1], caption=file_id[3])
            else:
                await msg.answer(text="Kino nomini kiriting: ", reply_markup=orqaga)
                await state.set_state(RegistrState.kino_name)
        else:
            await msg.answer(text="Kino nomini kiriting: ", reply_markup=orqaga)
            await state.set_state(RegistrState.kino_name)


# ----------------------------------------------------------------------------------------------------------------#

@msg_co.message(RegistrState.kino_name)
async def kino_name(msg: Message, state: FSMContext):
    if await cheak_channels(msg.from_user.id, msg.bot):
        await msg.answer("Iltimos kanallarga obuna bo'ling", reply_markup=follow_channel())
    elif msg.text == "Menu":
        db = database_user(db_name)
        user = db.get_user(msg.from_user.id)
        if user[4] == 0:
            await msg.answer("Menu", reply_markup=menu)
            await state.set_state(RegistrState.menu)
        elif user[4] == 1:
            await msg.answer(text="Menu", reply_markup=menu_admin)
            await state.clear()
        else:
            await msg.answer(text="Menu", reply_markup=super_admin)
            await state.clear()
    elif msg.text == "Orqaga":
        await msg.answer(f"Quyida 2 ta bo'lim bor:\n\n\t1. Kod bo'yicha izlash - Bu bo'limda kinoni kod orqali "
                         f"izlaysiz yani har bir kinoga kod biriktirilgan siz shu kod orqali kinoni yuklab olasiz\n\t"
                         f"2. Nom bo'yicha izlash - Bu bo'limda kinoni nomini yozasiz va bot sizga agar siz yozgan kino"
                         f" botda bo'lsa sizga bot tashlab beradi.", reply_markup=kino_menu)
        await state.set_state(RegistrState.kino)
    else:
        if msg.text.isdigit():
            file_id = get_id(int(msg.text))
            if file_id:
                await msg.bot.send_video(chat_id=msg.chat.id, video=file_id[1], caption=file_id[3])
            else:
                dbm = database_movie(db_name)
                movies = dbm.get_movies(text=msg.text)
                if len(movies) == 0:
                    await msg.answer(
                        "Afsuski bunday nomdagi kino topilmadi. Bu kino nomini bot muallifga tashlab qo'ying. Yaqin orada bu kinoni botga joylaymiz.")
                    await msg.answer(text="Boshqa kino izlab ko'ring")
                elif len(movies) == 1:
                    await msg.answer_video(video=movies[0][1], caption=movies[0][3])
                else:
                    await state.update_data(movies=movies, index=0)
                    await msg.answer_video(video=movies[0][1],
                                           caption=f"<b>Natija: {len(movies)} ta kino topildi. 1-kino</b>\n\n" +
                                                   movies[0][3], reply_markup=left_right_k, parse_mode=ParseMode.HTML)
                    await state.set_state(RegistrState.kino_name)
        else:
            dbm = database_movie(db_name)
            movies = dbm.get_movies(text=msg.text)
            if len(movies) == 0:
                await msg.answer(
                    "Afsuski bunday nomdagi kino topilmadi. Bu kino nomini bot muallifga tashlab qo'ying. Yaqin orada bu kinoni botga joylaymiz.")
                await msg.answer(text="Boshqa kino izlab ko'ring")
            elif len(movies) == 1:
                await msg.answer_video(video=movies[0][1], caption=movies[0][3])
            else:
                await state.update_data(movies=movies, index=0)
                await msg.answer_video(video=movies[0][1],
                                       caption=f"<b>Natija: {len(movies)} ta kino topildi. 1-kino</b>\n\n" + movies[0][
                                           3], reply_markup=left_right_k, parse_mode=ParseMode.HTML)
                await state.set_state(RegistrState.kino_name)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


@msg_co.callback_query(RegistrState.kino_name)
async def kino(callback: CallbackQuery, state: FSMContext):
    all_data = await state.get_data()
    index = all_data.get('index')
    movies = all_data.get('movies')
    if callback.data == 'right':
        if index == len(movies) - 1:
            index = 0
        else:
            index = index + 1
        await state.update_data(index=index)

        await callback.message.edit_media(
            media=InputMediaVideo(
                media=movies[index][1],
                caption=f"<b>Natija: {len(movies)} ta kino topildi. {index + 1}-kino</b>\n\n {movies[index][3]}.",
                parse_mode=ParseMode.HTML
            ),
            reply_markup=left_right_k
        )
    else:
        if index == 0:
            index = len(movies) - 1
        else:
            index = index - 1

        await state.update_data(index=index)

        await callback.message.edit_media(
            media=InputMediaVideo(
                media=movies[index][1],
                caption=f"<b>Natija: {len(movies)} ta kino topildi. {index + 1}-kino</b>\n\n {movies[index][3]}.",
                parse_mode=ParseMode.HTML
            ),
            reply_markup=left_right_k
        )


# ---------------------------------------------------------------------------------------------------------------------------------------------#


@msg_co.message(and_f(F.text == "Orqaga", RegistrState.kino))
async def kino(msg: Message, state: FSMContext):
    if await cheak_channels(msg.from_user.id, msg.bot):
        await msg.answer("Iltimos kanallarga obuna bo'ling", reply_markup=follow_channel())
    else:
        db = database_user(db_name)
        user = db.get_user(msg.from_user.id)
        if user[4] == 0:
            await msg.answer("Menu", reply_markup=menu)
            await state.set_state(RegistrState.menu)
        elif user[4] == 1:
            await msg.answer(text="Menu", reply_markup=menu_admin)
            await state.clear()
        else:
            await msg.answer(text="Menu", reply_markup=super_admin)
            await state.clear()


# __________________________________________FINISH_____________________________________________________________________________________________#

# ----------------------------------"Random kino" funksiyasi-----------------------------------------------------------------------------------#

# ___________________________________________START_____________________________________________________________________________________________#

@msg_co.message(F.text == "Random kino")
async def select_janr(msg: Message, state: FSMContext):
    if await cheak_channels(msg.from_user.id, msg.bot):
        await msg.answer("Iltimos kanallarga obuna bo'ling", reply_markup=follow_channel())
    else:
        await msg.answer(text="Kino janrini tanlang", reply_markup=janr)
        await state.set_state(RegistrState.random)


# ---------------------------------------------------------------------------------------------------------------------------------------------#

@msg_co.callback_query(RegistrState.random)
async def random_kino(msg: CallbackQuery, state: FSMContext):
    try:
        dbm = database_movie(db_name)
        file_ids = dbm.get_janr(text=msg.data)
        key = choice(file_ids)[0]
        file_id = dbm.get_movie(key)
        await msg.bot.send_video(chat_id=msg.from_user.id, video=file_id[1], caption=file_id[3])
        await msg.bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message.message_id)
        await state.clear()
    except:
        await msg.bot.send_message(chat_id=msg.from_user.id, text="Afsuski bu janrda hali hech qanday kino yo'q.")


# __________________________________________FINISH_____________________________________________________________________________________________#

# ----------------------------------"Muallif haqida" funksiyasi--------------------------------------------------------------------------------#

# ___________________________________________START_____________________________________________________________________________________________#

@msg_co.message(F.text == "ℹ️ Muallif haqida")
async def info(msg: Message):
    if await cheak_channels(msg.from_user.id, msg.bot):
        await msg.answer("Iltimos kanallarga obuna bo'ling", reply_markup=follow_channel())
    else:
        infoo = 'Bot yaratuvchisi:\n\t🐍 Python Developer:  <a href="https://t.me/un_knowndev">Zafarbek Olimboyev</a>'
        await msg.answer(text=infoo, parse_mode=ParseMode.HTML)


# __________________________________________FINISH_____________________________________________________________________________________________#

# ----------------------------------"Inglizcha Kinolar" funksiyasi-----------------------------------------------------------------------------#

# ___________________________________________START_____________________________________________________________________________________________#


@msg_co.message(F.text == "Botdagi kinolar ro'yxati")
async def kino_list(msg: Message, state: FSMContext):
    if await cheak_channels(msg.from_user.id, msg.bot):
        await msg.answer("Iltimos kanallarga obuna bo'ling", reply_markup=follow_channel())
    else:
        dbm = database_movie(db_name)
        movies = dbm.get_movies_list()
        await state.clear()
        if len(movies) == 0:
            await msg.answer(
                "Afsuski botda hech qanday kino yo'q. Yaqin orada botga kino joylaymiz.")
        elif len(movies) == 1:
            await msg.answer_video(video=movies[0][1], caption=movies[0][3])
        else:
            await state.update_data(movies=movies, interval=[0, 10])
            info = ""
            for i in range(0, 10):
                info += f"<b>{i + 1}. {movies[i][5]}</b>\n"
            await msg.answer(text=f"<b>Natija: {len(movies)} ta kino topildi. 1-10 kinolar</b>\n\n" + info,
                             reply_markup=movies_list_k([0, 10]), parse_mode=ParseMode.HTML)
            await state.set_state(RegistrState.kino_list)


# -----------------------------------------------------------------------------------------

@msg_co.message(RegistrState.kino_list)
async def kino_list(msg: Message, state: FSMContext):
    if msg.text == "Orqaga":
        db = database_user(db_name)
        user = db.get_user(msg.from_user.id)
        if user[4] == 0:
            await msg.answer("Menu", reply_markup=menu)
            await state.set_state(RegistrState.menu)
        elif user[4] == 1:
            await msg.answer(text="Menu", reply_markup=menu_admin)
            await state.clear()
        else:
            await msg.answer(text="Menu", reply_markup=super_admin)
            await state.clear()
    else:
        if msg.text.isdigit():
            file_id = get_id(int(msg.text))
            if file_id:
                await msg.bot.send_video(chat_id=msg.chat.id, video=file_id[1], caption=file_id[3])
            else:
                await msg.answer(text="Bunday kodli kino topilmadi.")
        else:
            await msg.answer(text="Iltimos faqat codni kiriting faqat raqamlardan iborat bo'lsin!")



# -----------------------------------------------------------------------------------


@msg_co.callback_query(RegistrState.kino_list)
async def kino_list(callback: CallbackQuery, state: FSMContext):
    all_data = await state.get_data()
    interval = all_data.get('interval')
    movies = all_data.get('movies')
    if callback.data == 'right':
        if interval[1] == len(movies) - 1 or len(movies) - len(movies) % 10 == interval[0]:
            interval = [0, 10]
        elif len(movies) - len(movies) % 10 == interval[1]:
            interval = [interval[1], len(movies)]
        else:
            interval = [interval[1], interval[1] + 10]
        await state.update_data(interval=interval)
        info = ""
        n = 1
        print(interval[0], interval[1])
        for i in range(interval[0], interval[1]):
            info += f"<b>{n}. {movies[i][5]}</b>\n"
            n += 1
        await callback.message.edit_text(text=f"<b>Natija: {len(movies)} ta kino topildi. {interval[0]+1}-{interval[1]}"
                                              f" kinolar</b>\n\n" + info, reply_markup=movies_list_k([interval[0],
                                                                                                      interval[1]]),
                                         parse_mode=ParseMode.HTML)
    elif callback.data == 'left':
        if interval[0] == 0:
            interval = [len(movies) - len(movies) % 10, len(movies)]
        elif len(movies) == interval[1]:
            interval = [interval[0] - 10, interval[0]]
        else:
            interval = [interval[0] - 10, interval[0]]

        await state.update_data(interval=interval)

        info = ""
        print(interval[0], interval[1])
        n = 1
        for i in range(interval[0], interval[1]):
            info += f"<b>{n}. {movies[i][5]}</b>\n"
            n += 1
        await callback.message.edit_text(
            text=f"<b>Natija: {len(movies)} ta kino topildi. {interval[0] + 1}-{interval[1]}"
                 f" kinolar</b>\n\n" + info, reply_markup=movies_list_k([interval[0], interval[1]]),
            parse_mode=ParseMode.HTML)
    else:
        movie = movies[int(callback.data)]
        await callback.message.answer_video(video=movie[1], caption=movie[3])


# __________________________________________FINISH_____________________________________________________________________________________________#

# ----------------------------------Xatoliklar uchun funksiya------------------------------------------------------#

# ___________________________________________START_____________________________________________________________________________________________#


@msg_co.message()
async def unknown_command(msg: Message):
    if await cheak_channels(msg.from_user.id, msg.bot):
        await msg.answer("Iltimos kanallarga obuna bo'ling", reply_markup=follow_channel())
    else:
        if msg.text.isdigit():
            file_id = get_id(int(msg.text))
            if file_id:
                await msg.bot.send_video(chat_id=msg.chat.id, video=file_id[1], caption=file_id[3])
            else:
                await msg.answer(text="Bunday kodli kino topilmadi.")
        else:
            await msg.answer(text="Iltimos faqat codni kiriting faqat raqamlardan iborat bo'lsin!")


# __________________________________________FINISH_____________________________________________________________________________________________#

# ----------------------------------Kanalga azo bo'lgam yoki bo'lmaganligini tekshiruvchi funksiya---------------------------------------------#

# ___________________________________________START_____________________________________________________________________________________________#

@msg_co.callback_query()
async def exapmle(msg: CallbackQuery, state: FSMContext):
    cheak_answer = await cheak_channels(user_id=msg.from_user.id, bot=msg.bot)
    if cheak_answer:
        await msg.answer(text="Siz kanallarga obuna bo'lmagansiz", reply_markup=follow_channel())
    else:
        await msg.bot.send_message(chat_id=msg.message.chat.id,
                                   text=f"Siz kanallarga a'zo bo'ldingiz. Endi bemalol botdan foydalanishingiz mumkin.",
                                   reply_markup=menu)
        await msg.bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message.message_id)
        await state.clear()

# __________________________________________FINISH_____________________________________________________________________________________________#
