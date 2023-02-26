from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# Bot = Bot('6144355865:AAGc-S-JW19KaT3LjWRTrCrY9iZJQZdimQY')
# bot = Dispatcher(Bot)

# CHANNELS = [
#     ["2", "-1001871464696", "https://t.me/+0RDeerjZvuY1MjIy"]
# ]
# channel = "-1001871464696"
# not_sub_message = 'необходимо подписаться на канал'
#
# async def check_sub_channels(channels, user_id):
#     for channel in channels:
#         chat_member = await Bot.get_chat_member(chat_id=channel[1], user_id=user_id)
#         if chat_member['status'] == 'left':
#             return False
#     return True
#
# def showChannels():
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     for channel in CHANNELS:
#         markup.add(types.InlineKeyboardButton(text=channel[0], url=channel[2]))
#     markup.add(types.InlineKeyboardButton(text='ПОДПИСАЛСЯ', callback_data='done'))
#     return markup