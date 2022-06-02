from telegram import Update
from random import randint
import telebot
from telebot import types

bot = telebot.TeleBot('5366132013:AAGE6UIyaydlwThANfwQuy64ZgG9AReVKAM')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/help\n/button\n/ukulele')


@bot.message_handler(commands=['ukulele'])
def ukulele(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Укулеле', url='https://gb.ru'))
    bot.send_message(message.chat.id, 'Ukulele', reply_markup=markup)


@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    item = types.InlineKeyboardButton('FF', callback_data='q1')
    item2 = types.InlineKeyboardButton('F2', callback_data='q2')
    markup.add(item, item2)

    bot.send_message(message.chat.id, 'Ghbdtn', reply_markup=markup)


@bot.message_handler(commands=['RPS'])
def RPS(message):

    # bot.send_message(
    #     message.chat.id, f'Камень, ножницы, бумага?')
    markup = types.InlineKeyboardMarkup(row_width=5)
    item1 = types.InlineKeyboardButton('Камень', callback_data='q1')
    item2 = types.InlineKeyboardButton('Ножницы', callback_data='q2')
    item3 = types.InlineKeyboardButton('Бумага', callback_data='q3')
    markup.add(item1, item2, item3)
    bot.send_message(
        message.chat.id, f'Камень, ножницы, бумага?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot_choise = int(randint(1, 3))
    case =['','Камень', 'Ножницы', 'Бумагу']
    if call.message:

        if call.data == 'q1':
            human_choise = 1

        elif call.data == 'q2':
            human_choise = 2

        elif call.data == 'q3':
            human_choise= 3

    if human_choise == bot_choise:
            bot.send_message(call.message.chat.id, f'Ничья, оба выбрали {case[human_choise]}')

    elif human_choise == 1 and bot_choise == 2:
        bot.send_message(call.message.chat.id,f'Вы выбрали {case[human_choise]} а компьютер {case[bot_choise]}, вы победили')
    elif human_choise == 1 and bot_choise == 3:
        bot.send_message(call.message.chat.id,f'Вы выбрали {case[human_choise]} а компьютер {case[bot_choise]}, вы проиграли')
    elif human_choise == 2 and bot_choise == 1:
        bot.send_message(call.message.chat.id,f'Вы выбрали {case[human_choise]} а компьютер {case[bot_choise]}, вы проиграли')
    elif human_choise == 2 and bot_choise == 3:
        bot.send_message(call.message.chat.id,f'Вы выбрали {case[human_choise]} а компьютер {case[bot_choise]}, вы победили')
    elif human_choise == 3 and bot_choise == 1:
        bot.send_message(call.message.chat.id,f'Вы выбрали {case[human_choise]} а компьютер {case[bot_choise]}, вы победили')
    elif human_choise == 3 and bot_choise == 2:
        bot.send_message(call.message.chat.id,f'Вы выбрали {case[human_choise]} а компьютер {case[bot_choise]}, вы проиграли')

# @bot.message_handler(commands=['candy'])
# def candy(message):
#     count = int(randint(30, 39))

#     bot.send_message(
#         message.chat.id, f'Игра в конфеты: на столе лежат конфеты, можно забирать от одной до трех, кто заберет последнюю выиграл.')
#     markup = types.InlineKeyboardMarkup(row_width=5)
#     item1 = types.InlineKeyboardButton('Взять одну', callback_data='q1')
#     item2 = types.InlineKeyboardButton('Взять две', callback_data='q2')
#     item3 = types.InlineKeyboardButton('Взять три', callback_data='q3')
#     markup.add(item1, item2, item3)
#     bot.send_message(message.chat.id, f'На столе {count} конфеты, Сколько забирате?', reply_markup=markup)

# @bot.callback_query_handler(func=lambda call:True)
# def callback(call,count):
#     if call.message:
#         if call.data == 'q1':
#             count -= 1
#             bot.send_message(call.message.chat.id, f'На столе {count} конфеты, Сколько забирате?')
#     if call.message:
#         if call.data == 'q2':
#             count -= 2
#             bot.send_message(call.message.chat.id, f'На столе {count} конфеты, Сколько забирате?')
#     if call.message:
#             if call.data == 'q3':
#                 count -= 3
#                 bot.send_message(call.message.chat.id, f'На столе {count} конфеты, Сколько забирате?')

    # candy_put(message)

# @bot.message_handler()
# def candy_put (message):
#     if call.data == 'q1':
#         bot.send_message(message.chat.id, f'На столе конфеты,fefefe Сколько забирате?')
#     if message == 'q2':
#         bot.send_message(message.chat.id, f'На столе конфеты,fefefe Сколько забирате?')

@bot.message_handler()
def get_user_text(message):
    if message.text == 'message':
        bot.send_message(message.chat.id, message)


@bot.message_handler()
def help(message):
    string_icon = ('icon', 'иконка',)
    string_hi = ('hello', 'hi', 'привет')
    if message.text.lower() in string_hi:
        bot.send_message(
            message.chat.id, f'Привет {message.from_user.first_name} или {message.from_user.username}')
    elif message.text == 'message':
        bot.send_message(message.chat.id, message)
    elif message.text.lower() in string_icon:
        icon = open('Lec_5\pipPy\icon.jpg', 'rb')
        bot.send_photo(message.chat.id, icon)


bot.polling(none_stop=True)
