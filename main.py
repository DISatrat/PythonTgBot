# import telebot
# from telebot import types
# from telebot.apihelper import ApiTelegramException
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from creat_bot import bot
from handlers import client, others, admin

client.register_message_handler(bot)

executor.start_polling(dispatcher=bot,skip_updates=True)


# @bot.message_handler(commands=['comm'])
# def Iam(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
#     markup.add(types.InlineKeyboardButton('как дела? '))
#     markup.add(types.InlineKeyboardButton('мое имя '))
#     markup.add(types.InlineKeyboardButton('мое имя '))
#     markup.add(types.InlineKeyboardButton('мое имя '))
#
#     bot.send_message(message.chat.id, 'спроси меня что-то',reply_markup=markup )


# @bot.message_handler(content_types=['text'])
# def myName(message):
#     mess= message.from_user.first_name
#     mes=message.text.split('/')
#     if mes[0]!='':
#         print(mes)
#         if message.text=='мое имя':
#             bot.send_message(message.chat.id, f'прив  <b>{mess}</b>',parse_mode='html')
#         else:
#             bot.send_message(message.chat.id, 'who!?')


