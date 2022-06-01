from random import randint
import telebot
from telebot import types

bot = telebot.TeleBot('5366132013:AAGE6UIyaydlwThANfwQuy64ZgG9AReVKAM')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/help\n/button\n')

@bot.message_handler()
def help(message):
    string_icon = ('icon','иконка',)
    string_hi = ('hello','hi','привет')
    if message.text.lower() in string_hi:
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} или {message.from_user.username}')
    elif message.text == 'message':
        bot.send_message(message.chat.id, message)
    elif message.text.lower() in string_icon:
        icon = open ('Lec_5\pipPy\icon.jpg', 'rb')
        bot.send_photo(message.chat.id, icon)






@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    item = types.InlineKeyboardButton('FF', callback_data='q1')
    item2 = types.InlineKeyboardButton('F2', callback_data='q2')
    markup.add(item, item2)

    bot.send_message(message.chat.id, 'Ghbdtn', reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    if message.text == 'message':
        bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['candy'])
def candy(message):
    count = int(randint(30, 39))
    bot.send_message(
        message.chat.id, f'Игра в конфеты: на столе {count} конфеты, можно забирать от одной до трех, кто заберет последнюю выиграл.')
    while count > 0:
        bot.send_message(
            message.chat.id, f'На столе {count} конфеты, Сколько забирате?.')
        bot.add_callback_query_handler(message)
        count -= 1


bot.polling(none_stop=True)
