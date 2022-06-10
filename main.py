import logging
import requests

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InputFile

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, CallbackQuery,InlineKeyboardMarkup
from aiogram.utils import callback_data

Yer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="Shimoliy america", callback_data="Shimoliy Amerika"),
            InlineKeyboardMarkup(text="Janubiy Amerika", callback_data="Janubiy Amerika"),
            InlineKeyboardMarkup(text="Osiyo", callback_data="Osiyo")
        ],
        [
            InlineKeyboardMarkup(text="Evropa", callback_data="Europa"),
            InlineKeyboardMarkup(text="Avstralia", callback_data="Avstralia"),
            InlineKeyboardMarkup(text="Afrika", callback_data="Afrika")
        ],
    ]
)
Osiyo_k = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="Qozogʻiston", callback_data="Kazakhstan"),
            InlineKeyboardMarkup(text="Qirgʻiziston", callback_data="Kyrgyzstan"),
            InlineKeyboardMarkup(text="Tojikiston", callback_data="Tajikistan")
        ],
        [
            InlineKeyboardMarkup(text="Turkmaniston", callback_data="Turkmenistan"),
            InlineKeyboardMarkup(text="Hindiston", callback_data="India"),
            InlineKeyboardMarkup(text="Oʻzbekiston", callback_data="Uzbekistan")
        ],
        [
            InlineKeyboardMarkup(text="Xitoy", callback_data="China"),
            InlineKeyboardMarkup(text="Yaponiya", callback_data="Japan"),
            InlineKeyboardMarkup(text="Rossiya", callback_data="Russian")
        ],
        [
            InlineKeyboardMarkup(text="Orqaga",callback_data="Orqaga")
        ],
    ]
)
Yevropa_k = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="Albania", callback_data="Albania"),
            InlineKeyboardMarkup(text="Andorra", callback_data="Andorra"),
            InlineKeyboardMarkup(text="Avstriya", callback_data="Austria")
        ],
        [
            InlineKeyboardMarkup(text="Belarusiya", callback_data="Belarus"),
            InlineKeyboardMarkup(text="Belgiya", callback_data="Belgium"),
            InlineKeyboardMarkup(text="Bolgariya", callback_data="Bulgaria")
        ],
        [
            InlineKeyboardMarkup(text="Croatia", callback_data="Croatia"),
            InlineKeyboardMarkup(text="Daniya", callback_data="Dania"),
            InlineKeyboardMarkup(text="Estoniya", callback_data="Estonia")
        ],
        [
            InlineKeyboardMarkup(text="Orqaga",callback_data="Orqaga")
        ],
    ]
)
Afrika_k = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="Angola", callback_data="Angola"),
            InlineKeyboardMarkup(text="Benin", callback_data="Benin"),
            InlineKeyboardMarkup(text="Botsvana", callback_data="Botswana")
        ],
        [
            InlineKeyboardMarkup(text="Burundi", callback_data="Burundi"),
            InlineKeyboardMarkup(text="Gabon", callback_data="Gabon"),
            InlineKeyboardMarkup(text="Gambiya", callback_data="Gambia")
        ],
        [
            InlineKeyboardMarkup(text="Gana", callback_data="Ghana"),
            InlineKeyboardMarkup(text="Gvineya", callback_data="Guinea"),
            InlineKeyboardMarkup(text="Jazoir", callback_data="Algeria")
        ],
        [
            InlineKeyboardMarkup(text="Orqaga", callback_data="Orqaga")
        ],
    ]
)
Avstralia_k = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="Avstraliya", callback_data="Australia"),
        ],
        [
            InlineKeyboardMarkup(text="Orqaga", callback_data="Orqaga")
        ],

    ]
)
ShimoliyA_k = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="Kanada", callback_data="Canada"),
            InlineKeyboardMarkup(text="Meksika", callback_data="Mexico"),
            InlineKeyboardMarkup(text="Grenlandiya", callback_data="Greenland")
        ],
        [
            InlineKeyboardMarkup(text="Kuba", callback_data="Cuba"),
            InlineKeyboardMarkup(text="Gaiti", callback_data="Haiti"),
            InlineKeyboardMarkup(text="Gvadelupa", callback_data="Guadeloupe")
        ],
        [
            InlineKeyboardMarkup(text="Dominika", callback_data="Dominika"),
            InlineKeyboardMarkup(text="Martinika", callback_data="Martinique"),
            InlineKeyboardMarkup(text="Barbados ", callback_data="Barbados ")
        ],
        [
            InlineKeyboardMarkup(text="Orqaga", callback_data="Orqaga")
        ],

    ]
)
JanubiyA_k = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="Argentina", callback_data="Argentina"),
            InlineKeyboardMarkup(text="Boliviya", callback_data="Bolivia"),
            InlineKeyboardMarkup(text="Braziliya", callback_data="Brazil")
        ],
        [
            InlineKeyboardMarkup(text="Chili", callback_data="Chili"),
            InlineKeyboardMarkup(text="Ekvador", callback_data="Ecuador"),
            InlineKeyboardMarkup(text="Gayana", callback_data="Guyana")
        ],
        [
            InlineKeyboardMarkup(text="Kolumbiya", callback_data="Colombia"),
            InlineKeyboardMarkup(text="Paragvay", callback_data="Paraguay"),
            InlineKeyboardMarkup(text="Peru", callback_data="Peru")
        ],
        [
            InlineKeyboardMarkup(text="Orqaga", callback_data="Orqaga")
        ],
    ]
)



import wikipedia
wikipedia.set_lang("uz")
def send_info(message):
    try:
        return (wikipedia.summary(message))
    except:
        return ("Xatolik")


API_TOKEN = '5311914433:AAFEE-cygATHs52uLTTfhbizyF-z_poFBfQ'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom qayerga sayohat qilamiz?", reply_markup=Yer)


@dp.callback_query_handler(text="Osiyo")
async def send_Osiyo(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi davlatni tanlaysiz?", reply_markup=Osiyo_k)


@dp.callback_query_handler(text="Europa")
async def send_Yevropa(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi davlatni tanlaysiz?", reply_markup=Yevropa_k)


@dp.callback_query_handler(text="Afrika")
async def send_Afrika(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi davlatni tanlaysiz?", reply_markup=Afrika_k)


@dp.callback_query_handler(text="Avstralia")
async def send_Avstralia(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi davlatni tanlaysiz?", reply_markup=Avstralia_k)


@dp.callback_query_handler(text="Shimoliy Amerika")
async def send_ShA(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi davlatni tanlaysiz?", reply_markup=ShimoliyA_k)


@dp.callback_query_handler(text="Janubiy Amerika")
async def send_Ja(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Qaysi davlatni tanlaysiz?", reply_markup=JanubiyA_k)


@dp.callback_query_handler(text="Orqaga")
async def menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Salom qayerga sayohat qilamiz", reply_markup=Yer)


@dp.callback_query_handler()
async def malumot(call: CallbackQuery):
    res = send_info(call)
    await call.message.delete()
    await call.message.answer(res)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
