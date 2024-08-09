import telebot
from telebot import types


def start_handler(message):
    keyboard = types.InlineKeyboardMarkup()
    start_button = types.InlineKeyboardButton("Начать викторину", callback_data='quiz')
    keyboard.add(start_button)

    bot.send_message(message.chat.id, 'Привет! Добро пожаловать в викторину "Какое у вас тотемное животное?"',
                     reply_markup=keyboard)
