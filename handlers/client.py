from aiogram import types, Dispatcher
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
from creat_bot import bot, Bot
from handlers import others


CHANNELS = [
    ["2", "-1001871464696", "https://t.me/+0RDeerjZvuY1MjIy"]
]
channel = "-1001871464696"
not_sub_message = 'необходимо подписаться на канал'

async def check_sub_channels(channels, user_id):
    for channel in channels:
        chat_member = await Bot.get_chat_member(chat_id=channel[1], user_id=user_id)
        if chat_member['status'] == 'left':
            return False
    return True

def showChannels():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for channel in CHANNELS:
        markup.add(types.InlineKeyboardButton(text=channel[0], url=channel[2]))
    markup.add(types.InlineKeyboardButton(text='ПОДПИСАЛСЯ', callback_data='done'))
    return markup

# @bot.message_handler(commands=['start', 'help'])
async def start(message:types.Message):
    if await check_sub_channels(CHANNELS, message.chat.id):
        await Bot.send_message(message.from_user.id,
                         "/setNumber - установить номер телефона \r\n /pizza - меню магазина \r\n /setLocation - установить адресс  "
                         "\r\n /answer_quations - пройти опрос  ",parse_mode='html')
    else:
        await Bot.send_message(message.from_user.id, not_sub_message, reply_markup=showChannels())



@bot.callback_query_handler()
async def CallBacks(callback:types.CallbackQuery):
    if callback.data == 'done':
        await Bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        if not await check_sub_channels(CHANNELS, callback.message.chat.id):
            await Bot.send_message(callback.message.chat.id, not_sub_message, reply_markup=showChannels())
        else:
           await Bot.send_message(callback.message.chat.id, "/setNumber - установить номер телефона \r\n /pizza - меню магазина \r\n /setLocation - установить адресс  ", parse_mode='html')
    if callback.data == 'next':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Пицца 5', callback_data='pizza_1'))
        markup.add(types.InlineKeyboardButton('Пицца 6', callback_data='pizza_2'))
        markup.add(types.InlineKeyboardButton('Пицца 7', callback_data='pizza_3'))
        markup.add(types.InlineKeyboardButton('Пицца 8', callback_data='pizza_4'))
        markup.add(types.InlineKeyboardButton('>', callback_data='neexy'))
        markup.add(types.InlineKeyboardButton('<', callback_data='previe_2'))
        await Bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='2 страница',reply_markup=markup)
    elif callback.data == 'previe_2':
        await Bot.delete_message(callback.message.chat.id, message_id=callback.message.message_id)
        return await stuff(message=callback.message)
    elif callback.data == "previe":
     await Bot.send_message(callback.message.chat.id, text='такой страницы нет ')

# @bot.message_handler(commands=['add_new_advr'])
async def list_advr(message):
    file = open('headpphones.jpg','rb')

    await Bot.send_photo(message.chat.id,file)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('купить',callback_data='buy'))

    await Bot.send_message(message.chat.id,f'{file.name}',reply_markup=markup)

# @bot.message_handler(commands=['answer_quations'])
async def Quize(message):
    await Bot.send_message(message.chat.id,text="<b>1 вопрос</b>: \r\n сколько вам лет ?",parse_mode='html')

@bot.callback_query_handler()
async def callback_pizza_page_2(callback:types.CallbackQuery):
    if callback.data == 'next':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Пицца 5', callback_data='pizza_1'))
        markup.add(types.InlineKeyboardButton('Пицца 6', callback_data='pizza_2'))
        markup.add(types.InlineKeyboardButton('Пицца 7', callback_data='pizza_3'))
        markup.add(types.InlineKeyboardButton('Пицца 8', callback_data='pizza_4'))
        markup.add(types.InlineKeyboardButton('>', callback_data='neexy'))
        markup.add(types.InlineKeyboardButton('<', callback_data='previe_2'))
        await Bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='2 страница',reply_markup=markup)

    elif callback.data == 'previe_2':
        await Bot.edit_message_text(callback.message.chat.id, message_id=callback.message.message_id,text='1 страница',reply_markup=stuff)
        return await stuff(message=callback.message)
    elif callback.data == "previe":
        await Bot.send_message(callback.message.chat.id, text='такой страницы нет ')

# @bot.message_handler(commands=['pizza'])
async def stuff(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Пеперони', callback_data='pizza_1'))
    markup.add(types.InlineKeyboardButton('4 сыра', callback_data='pizza_2'))
    markup.add(types.InlineKeyboardButton('Баварская', callback_data='pizza_3'))
    markup.add(types.InlineKeyboardButton('Кола', callback_data='pizza_4'))
    markup.add(types.InlineKeyboardButton('>', callback_data='next'))
    markup.add(types.InlineKeyboardButton('<', callback_data='previe'))

    await Bot.send_message(message.chat.id, '1 страница', reply_markup=markup)


def register_message_handler(bot : Dispatcher):
    bot.register_message_handler(start,commands=['start', 'help'])
    bot.register_message_handler(stuff,commands=['pizza'])
    bot.register_message_handler(Quize,commands=['answer_quations'])
    bot.register_message_handler(list_advr,commands=['add_new_advr'])

