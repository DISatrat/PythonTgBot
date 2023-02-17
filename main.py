import telebot
from telebot import types
from telebot.apihelper import ApiTelegramException


bot = telebot.TeleBot('6144355865:AAGc-S-JW19KaT3LjWRTrCrY9iZJQZdimQY')

CHANNELS = [
    # ["1", "-1001169696508", "https://t.me/+V45TPjkSO8g4YTg6"],
    ["2", "-1001871464696", "https://t.me/+0RDeerjZvuY1MjIy"]
]
channel="-1001871464696"
not_sub_message = 'необходимо подписаться на канал'



# def check_sub_channels(channels, user_id):
#     for channel in channels:
#         chat_member=bot.get_chat_member(chat_id=channel[1],user_id=user_id)
#         if chat_member:
#             return False
#     return True




def check_sub_channels(chat_id, user_id):
    for channel in chat_id:
        try:
            response = bot.get_chat_member(chat_id=channel[1], user_id=user_id)
            if response.status == 'left':
                return False
            else:
                return True

        except ApiTelegramException as e:
            if e.result_json['description'] == 'Bad Request: chat not found':
                return False

def showChannels():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for channel in CHANNELS:
        markup.add(types.InlineKeyboardButton(text=channel[0], url=channel[2]))
    markup.add(types.InlineKeyboardButton(text='ПОДПИСАЛСЯ', callback_data='done'))
    return markup


@bot.message_handler(commands=['start', 'help'])
def start(message):
    if not check_sub_channels(CHANNELS, message.chat.id):
        bot.send_message(message.from_user.id, not_sub_message, reply_markup=showChannels())
    else:
        bot.send_message(message.from_user.id,"/setNumber - установить номер телефона \r\n /pizza - меню магазина \r\n /setLocation - установить адресс  ",parse_mode='html')



@bot.callback_query_handler(func=lambda callback: callback.data)
def CallBacks(callback):
    if callback.data == 'done':
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)

        if not check_sub_channels(CHANNELS, callback.message.chat.id):
            bot.send_message(callback.message.chat.id, not_sub_message, reply_markup=showChannels())
        else:
            bot.send_message(callback.message.chat.id, "/setNumber - установить номер телефона \r\n /pizza - меню магазина \r\n /setLocation - установить адресс  ", parse_mode='html')
    if callback.data == 'next':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Пицца 5', callback_data='pizza_1'))
        markup.add(types.InlineKeyboardButton('Пицца 6', callback_data='pizza_2'))
        markup.add(types.InlineKeyboardButton('Пицца 7', callback_data='pizza_3'))
        markup.add(types.InlineKeyboardButton('Пицца 8', callback_data='pizza_4'))
        markup.add(types.InlineKeyboardButton('>', callback_data='neexy'))
        markup.add(types.InlineKeyboardButton('<', callback_data='previe_2'))
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='2 страница',reply_markup=markup)
    elif callback.data == 'previe_2':
        bot.delete_message(callback.message.chat.id, message_id=callback.message.message_id)
        return stuff(message=callback.message)
    elif callback.data == "previe":
        bot.send_message(callback.message.chat.id, text='такой страницы нет ')

# @bot.message_handler(commands=['add_new_advr'])
# def list_advr(message):
#     file = open('headpphones.jpg','rb')
#
#     bot.send_photo(message.chat.id,file)
#
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('купить',callback_data='buy'))
#
#     bot.send_message(message.chat.id,f'{file.name}',reply_markup=markup)

# @bot.callback_query_handler(func=lambda callback : callback.data)
# def setNumber(callback):
#     if callback.data=='buy':
#         numbers=bot.send_message(callback.message.chat.id, text='введите номер телефона для доставки')
#         bot.register_next_step_handler(numbers, getNumber)


@bot.message_handler(commands=['setNumber'])
def setNumber(message):
    numbers = bot.send_message(message.chat.id, text='введите номер телефона для доставки')
    bot.register_next_step_handler(numbers, getNumber)


@bot.message_handler(commands=['setLocation'])
def setNumber(message):
    location = bot.send_message(message.chat.id, text='введите полный адресс')
    bot.register_next_step_handler(location, getLocation)


# @bot.message_handler(commands=['setFood'])
# def setNumber(message):
#     numbers = bot.send_message(message.chat.id, text='введите номер телефона для доставки')
#     bot.register_next_step_handler(numbers, getNumber)


def getNumber(numbers):
    numbers = numbers.text
    print(numbers)


def getLocation(location):
    location = location.text
    print(location)


# def getIdFood(food):
#     food=food.text
#     print(food)


# def create_user_order(numbers):
# numbers=numbers.text
# location=location.text
# food=food.text
# print(numbers)
# print(location)
# print(food)

@bot.message_handler(commands=['pizza'])
def stuff(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Пеперони', callback_data='pizza_1'))
    markup.add(types.InlineKeyboardButton('4 сыра', callback_data='pizza_2'))
    markup.add(types.InlineKeyboardButton('Баварская', callback_data='pizza_3'))
    markup.add(types.InlineKeyboardButton('Кола', callback_data='pizza_4'))
    markup.add(types.InlineKeyboardButton('>', callback_data='next'))
    markup.add(types.InlineKeyboardButton('<', callback_data='previe'))

    bot.send_message(message.chat.id, '1 страница', reply_markup=markup)


# @bot.callback_query_handler(func=lambda callback: callback.data)
# def callback_pizza_page_2(callback):
#     if callback.data == 'next':
#         markup = types.InlineKeyboardMarkup()
#         markup.add(types.InlineKeyboardButton('Пицца 5', callback_data='pizza_1'))
#         markup.add(types.InlineKeyboardButton('Пицца 6', callback_data='pizza_2'))
#         markup.add(types.InlineKeyboardButton('Пицца 7', callback_data='pizza_3'))
#         markup.add(types.InlineKeyboardButton('Пицца 8', callback_data='pizza_4'))
#         markup.add(types.InlineKeyboardButton('>', callback_data='neexy'))
#         markup.add(types.InlineKeyboardButton('<', callback_data='previe_2'))
#         bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='2 страница',reply_markup=markup)

    # elif callback.data == 'previe_2':
    #     bot.delete_message(callback.message.chat.id, message_id=callback.message.message_id)
    #     return stuff(message=callback.message)
    # elif callback.data == "previe":
    #     bot.send_message(callback.message.chat.id, text='такой страницы нет ')


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


bot.polling(none_stop=True)
